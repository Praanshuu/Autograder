import logging
from celery import shared_task
from django.utils import timezone
from .models import SubmissionAttempt, TestResult
from .services import (
    execute_code, 
    update_gradebook, 
    award_assignment_points, 
    SubmissionConfigGenerator
)

logger = logging.getLogger(__name__)

@shared_task
def execute_submission_task(attempt_id, language='python'):
    """
    Background task to execute student code.
    Replaces synchronous execution in views.py.
    """
    try:
        attempt = SubmissionAttempt.objects.get(id=attempt_id)
        attempt.status = 'processing'
        attempt.save()
        
        logger.info(f"Processing submission attempt {attempt_id} for {attempt.student.username}")
        
        # execution config
        aq = attempt.assignment_question
        question = aq.question
        config = question.config or {} # Use config from question
        test_cases = question.test_cases or []
        code = attempt.source_code 

        # Execute
        results = execute_code(code, language, test_cases, config=config)
        
        # Save Results
        passed_count = 0
        test_results_data = []
        
        # Clear old results if any (though usually clean)
        attempt.test_results.all().delete()
        
        for idx, res in enumerate(results):
            status_res = res.get('status', 'fail')
            if status_res == 'pass': passed_count += 1
            
            test_result = TestResult.objects.create(
                attempt=attempt,
                test_case_id=str(idx), # Simple index based ID
                status=status_res,
                score=1 if status_res == 'pass' else 0,
                actual_output=res.get('console_output', ''),
                error_message=res.get('error_message', ''),
                execution_time_ms=res.get('execution_time', 0)
            )
            
            test_results_data.append({
                'status': status_res,
                'score': test_result.score
            })
        
        # Determine final status
        if passed_count == len(results) and len(results) > 0:
            attempt.status = 'success'
        else:
            attempt.status = 'fail'
            
        attempt.save()
        
        # Award points
        try:
            award_assignment_points(attempt, test_results_data)
        except Exception as e:
            logger.error(f"Failed to award points for {attempt_id}: {e}", exc_info=True)
        
        # Save Artifacts
        try:
            artifact_path = SubmissionConfigGenerator.save_artifacts(attempt, language)
            attempt.code_blob_ref = artifact_path
            attempt.save(update_fields=['code_blob_ref'])
        except Exception as e:
            logger.error(f"Failed to save artifacts for {attempt_id}: {e}", exc_info=True)
            
        # Update Gradebook
        try:
            update_gradebook(attempt.student, aq.assignment)
        except Exception as e:
            logger.error(f"Failed to update gradebook for {attempt_id}: {e}", exc_info=True)
        
        logger.info(f"Completed submission {attempt_id}: {attempt.status}")
        return attempt.status
        
    except SubmissionAttempt.DoesNotExist:
        logger.error(f"SubmissionAttempt {attempt_id} not found")
        return "not_found"
    except Exception as e:
        logger.error(f"Task failed for {attempt_id}: {e}", exc_info=True)
        try:
            attempt = SubmissionAttempt.objects.get(id=attempt_id)
            attempt.status = 'error'
            attempt.save()
        except:
            pass
        return "error"

@shared_task
def analyze_assignment_ai_task(assignment_id):
    """
    Trigger Bulk AI Analysis for an assignment using Autograder_plus/main.py.
    Now runs PER-QUESTION to ensure correct configuration and execution.
    """
    import subprocess
    import json
    import os
    import shutil
    from pathlib import Path
    from django.conf import settings
    from assignments.models import Assignment
    
    try:
        assignment = Assignment.objects.get(id=assignment_id)
        logger.info(f"Starting Bulk AI Analysis for Assignment: {assignment.title} ({assignment_id})")

        # Define Autograder_plus paths once
        autograder_plus_root = Path(settings.BASE_DIR).parent.parent / "Autograder_plus"
        main_script = autograder_plus_root / "main.py"
        venv_python = autograder_plus_root / "newgrade" / "bin" / "python"
        
        if not venv_python.exists():
            logger.warning(f"Virtualenv python not found at {venv_python}. Trying system python.")
            venv_python = "python3"

        # Iterate over EACH question to ensure dedicated config and execution context
        for aq in assignment.assignmentquestion_set.all():
            question = aq.question
            q_slug = question.slug
            
            logger.info(f"--- Processing Question: {question.title} ({q_slug}) ---")
            
            # 1. Prepare Staging Directory for THIS Question
            # Path: media/ai_staging/<assignment_id>/<question_slug>
            staging_dir = Path(settings.MEDIA_ROOT) / "ai_staging" / str(assignment_id) / q_slug
            
            if staging_dir.exists():
                shutil.rmtree(staging_dir)
            staging_dir.mkdir(parents=True, exist_ok=True)
            
            submissions_dir = staging_dir / "submissions"
            submissions_dir.mkdir()
            
            # 2. Gather Latest Submissions for THIS Question
            attempts_to_process = SubmissionAttempt.objects.filter(
                assignment_question=aq
            ).order_by('student_id', '-created_at').distinct('student_id')
            
            if not attempts_to_process.exists():
                logger.info(f"No submissions for question {q_slug}, skipping.")
                continue
                
            logger.info(f"Staging {attempts_to_process.count()} submissions for {q_slug}...")
            
            # 3. Write Submission Files
            # Structure: submissions_dir / <student_username> / main.py
            # We rename to main.py (or matching lang) so Ingestor picks it up predictably
            
            # Detect language from first attempt or question config
            # Fallback to python
            q_config = question.config or {}
            language = q_config.get('language', 'python').lower()
            
            ext_map = {'python': '.py', 'c': '.c', 'java': '.java'}
            target_ext = ext_map.get(language, '.py')
            target_filename = "Main.java" if language == 'java' else f"main{target_ext}"
            
            for attempt in attempts_to_process:
                student_name = attempt.student.username
                student_dir = submissions_dir / student_name
                student_dir.mkdir(exist_ok=True)
                
                # Write file
                with open(student_dir / target_filename, 'w') as f:
                    f.write(attempt.source_code)
                    
            # 4. Generate FULL Config for this Question
            # The Critical Fix: Pass test_cases and execution_mode!
            
            # Construct config.json
            config_data = {
                "assignment_name": f"{assignment.title} - {question.title}",
                "language": language,
                "execution_mode": q_config.get('execution_mode', {'type': 'program'}),
                "test_cases": question.test_cases or [],
                "entry_point": q_config.get('entry_point'), # Important for batch mode/function mode
                "input_types": q_config.get('input_types'), # For batch runner structure decoding
                "points": aq.custom_points if aq.custom_points is not None else question.point_value,
                "description": question.description
            }
            
            config_path = staging_dir / "config.json"
            with open(config_path, 'w') as f:
                json.dump(config_data, f, indent=4)
                
            # 5. Run Pipeline
            output_dir = staging_dir / "reports"
            
            cmd = [
                str(venv_python),
                str(main_script),
                "grade",
                "--assignment-config", str(config_path),
                "--submissions-dir", str(submissions_dir),
                "--output-dir", str(output_dir),
                "--level", "full"
            ]
            
            logger.info(f"Running Pipeline for {q_slug}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                logger.error(f"Pipeline Failed for {q_slug}: {result.stderr}")
                continue # Skip to next question
                
            # 6. Process Results
            results_file = output_dir / "results.json"
            if not results_file.exists():
                logger.error(f"No results.json for {q_slug}")
                continue
                
            try:
                with open(results_file, 'r') as f:
                    results_data = json.load(f)
                    
                for item in results_data:
                    student_username = item.get("student_id")
                    if not student_username: continue
                    
                    # Update the specific attempt we staged
                    attempt = attempts_to_process.get(student__username=student_username)
                    if attempt:
                        analysis_data = item.get("analysis", {})
                        if item.get("error_processing"):
                            analysis_data["error"] = item.get("error_processing")
                            
                        attempt.ai_analysis_data = analysis_data
                        attempt.save(update_fields=['ai_analysis_data'])
                        logger.info(f"Updated AI data for {student_username} on {q_slug}")
                        
            except Exception as e:
                logger.error(f"Error processing results for {q_slug}: {e}")
                
            # Cleanup (optional)
            if not getattr(settings, 'DEBUG', False):
                shutil.rmtree(staging_dir)
                
        return "success"

    except Exception as e:
        logger.error(f"Bulk Analysis Task Failed: {e}", exc_info=True)
        return "failed"
