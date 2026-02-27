import json
from pathlib import Path
from django.conf import settings

class ConfigGenerator:
    """
    Generates JSON configuration files for questions.
    Updated to use JSON for compatibility with Autograder_plus Ingestor.
    """
    # Define base directory for assignment data
    # Ideally should be configurable, defaulting to 'assignments_data' in project root
    BASE_DIR = Path(settings.BASE_DIR) / "assignments_data"

    @classmethod
    def get_config_dir(cls, question):
        """
        Get directory for a question's config based on creator and slug.
        Structure: assignments_data/{username}/{slug}/
        """
        if hasattr(question, 'created_by') and question.created_by:
            username = question.created_by.username
        else:
            username = "default_user"
            
        return cls.BASE_DIR / username / question.slug

    @classmethod
    def get_config_path(cls, question):
        return cls.get_config_dir(question) / "config.json"

    @classmethod
    def generate_question_config(cls, question):
        """
        Generates a config.json file for a given Question instance.
        """
        config_dir = cls.get_config_dir(question)
        config_dir.mkdir(parents=True, exist_ok=True)
        
        config_path = config_dir / "config.json"
        
        # Extract config details from the JSONField
        # Default to 'solution' if not specified (though frontend sends it)
        entry_point = question.config.get('entry_point', 'solution')
        timeout = question.config.get('timeout', 2.0)
        memory = question.config.get('memory', 128)
        
        # Prepare data structure for JSON
        # Autograder_plus expects: language, test_cases, execution_mode etc.
        data = {
            'title': question.title,
            'slug': question.slug,
            'language': 'python', # Defaulting to python for now, should be dynamic if multi-lang supported
            'execution_mode': {
                'type': 'program' if not entry_point or entry_point == 'solution' else 'function',
                'entry_point': entry_point
            },
            'limits': {
                'timeout_seconds': timeout,
                'memory_limit_mb': memory
            },
            'test_cases': question.test_cases
        }
        
        # Write to file
        with open(config_path, 'w') as f:
            json.dump(data, f, indent=4)
            
        # Write starter code boilerplate if none exists
        if not question.starter_code:
            if data['execution_mode']['type'] == 'function':
                # Create a boilerplate python function based on the entry_point name
                boilerplate = (
                    f"# Write your solution below\n"
                    f"# The function '{entry_point}' will be called with the test case inputs.\n"
                    f"def {entry_point}():\n"
                    f"    pass\n"
                )
            else:
                boilerplate = "# Write your solution below\n"
            
            question.starter_code = boilerplate
            question.save(update_fields=['starter_code'])
            
        return str(config_path)
