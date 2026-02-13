import logging
import tempfile
import os
from pathlib import Path
from django.conf import settings
import time
import ast

logger = logging.getLogger(__name__)

def execute_code(code, language, test_cases):
    """
    Execute code against test cases using a custom implementation based on Dynamic Analyzer.
    Supports Python, C, and Java with Docker-based execution.
    """
    # Validate language support
    supported_languages = ['python', 'c', 'java']
    language = language.lower()
    
    if language not in supported_languages:
        return [{
            'status': 'error',
            'error_message': f'Unsupported language: {language}. Supported languages: {", ".join(supported_languages)}',
            'console_output': '',
            'execution_time': 0,
            'test_case': {}
        }]
    
    if not code or not code.strip():
        return [{
            'status': 'error',
            'error_message': 'Code cannot be empty',
            'console_output': '',
            'execution_time': 0,
            'test_case': {}
        }]
    
    # Create temporary file for code
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix=_get_file_extension(language), delete=False) as temp_file:
            temp_file.write(code)
            temp_file_path = temp_file.name
        
        # Use our custom executor that captures all outputs
        results = _execute_with_output_capture(temp_file_path, language, test_cases)
        return results


    except Exception as e:
        logger.error(f"Code execution failed: {e}")
        return [{
            'status': 'error',
            'error_message': f'Execution failed: {str(e)}',
            'console_output': '',
            'execution_time': 0,
            'test_case': {}
        }]
    
    finally:
        # Clean up temporary file
        try:
            if 'temp_file_path' in locals():
                os.unlink(temp_file_path)
        except Exception as e:
            logger.warning(f"Failed to clean up temporary file: {e}")

def _execute_with_output_capture(code_path, language, test_cases):
    """Execute code and capture outputs for all test cases"""
    from dynamic_analyzer import DynamicAnalyzer
    import docker
    import json
    import tarfile
    import io
    
    # For Python, try simple execution first (no Docker needed)
    if language == 'python':
        try:
            return _execute_python_simple(code_path, test_cases)
        except Exception as e:
            logger.warning(f"Simple Python execution failed: {e}")
    
    # Initialize analyzer for Docker-based execution
    analyzer = DynamicAnalyzer()
    
    if not analyzer.client:
        return [{
            'status': 'error',
            'console_output': '',
            'error_message': 'Docker unavailable',
            'execution_time': 0,
            'test_case': test_case
        } for test_case in test_cases]
    
    results = []
    
    try:
        if language == 'python':
            results = _execute_python_with_output(analyzer, code_path, test_cases)
        elif language == 'c':
            results = _execute_c_with_output(analyzer, code_path, test_cases)
        elif language == 'java':
            results = _execute_java_with_output(analyzer, code_path, test_cases)
        else:
            raise ValueError(f"Unsupported language: {language}")
            
    except Exception as e:
        logger.error(f"Execution failed for {language}: {e}")
        results = [{
            'status': 'error',
            'console_output': '',
            'error_message': str(e),
            'execution_time': 0,
            'test_case': test_case
        } for test_case in test_cases]
    
    return results

def _execute_python_with_output(analyzer, code_path, test_cases):
    """Execute Python code and capture all outputs"""
    results = []
    
    # Try to use a simpler execution method first
    try:
        return _execute_python_simple(code_path, test_cases)
    except Exception as e:
        logger.warning(f"Simple Python execution failed, falling back to analyzer: {e}")
    
    # Fallback to analyzer method
    for i, test_case in enumerate(test_cases):
        try:
            input_str = str(test_case.get('input', ''))
            expected = str(test_case.get('expected_output', '')).strip()
            
            # Run the test case
            ec, out, err, duration = analyzer._run_python_test_case(
                Path(code_path), 
                {'type': 'program'}, 
                input_str
            )
            
            if ec is None:
                status = 'timeout'
                console_output = ''
                error_message = err or 'Execution timed out'
            elif ec != 0:
                status = 'runtime_error'
                console_output = out
                error_message = err or 'Runtime error'
            else:
                # Compare outputs
                actual_norm = analyzer._normalize_output(out)
                expected_norm = analyzer._normalize_output(expected)
                
                if analyzer._compare_outputs(actual_norm, expected_norm):
                    status = 'pass'
                else:
                    status = 'fail'
                
                console_output = out
                error_message = ''
            
            results.append({
                'status': status,
                'console_output': console_output,
                'error_message': error_message,
                'execution_time': duration,
                'test_case': test_case
            })
            
        except Exception as e:
            results.append({
                'status': 'error',
                'console_output': '',
                'error_message': f'Test execution failed: {str(e)}',
                'execution_time': 0,
                'test_case': test_case
            })
    
    return results

def _execute_python_simple(code_path, test_cases):
    """Simple Python execution without complex Docker setup"""
    import subprocess
    import tempfile
    import os
    
    results = []
    
    # Read the code
    with open(code_path, 'r') as f:
        code = f.read()
    
    for test_case in test_cases:
        try:
            input_str = str(test_case.get('input', ''))
            expected = str(test_case.get('expected_output', '')).strip()
            
            # Create a temporary script that includes the code and handles input
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_script:
                # Write the user's code
                temp_script.write(code)
                temp_script_path = temp_script.name
            
            try:
                # Execute the script with input
                start_time = time.time()
                process = subprocess.run(
                    ['python3', temp_script_path],
                    input=input_str,
                    capture_output=True,
                    text=True,
                    timeout=5,  # 5 second timeout
                    cwd=os.path.dirname(temp_script_path)
                )
                end_time = time.time()
                duration = int((end_time - start_time) * 1000)
                
                if process.returncode == 0:
                    actual_output = process.stdout.strip()
                    if actual_output == expected:
                        status = 'pass'
                    else:
                        status = 'fail'
                    
                    results.append({
                        'status': status,
                        'console_output': actual_output,
                        'error_message': process.stderr if status == 'fail' else '',
                        'execution_time': duration,
                        'test_case': test_case
                    })
                else:
                    results.append({
                        'status': 'runtime_error',
                        'console_output': process.stdout,
                        'error_message': process.stderr or 'Runtime error',
                        'execution_time': 0,
                        'test_case': test_case
                    })
                    
            finally:
                # Clean up temporary file
                try:
                    os.unlink(temp_script_path)
                except Exception:
                    pass
                    
        except subprocess.TimeoutExpired:
            results.append({
                'status': 'timeout',
                'console_output': '',
                'error_message': 'Execution timed out (5s)',
                'execution_time': 5000,
                'test_case': test_case
            })
        except Exception as e:
            results.append({
                'status': 'error',
                'console_output': '',
                'error_message': f'Execution failed: {str(e)}',
                'execution_time': 0,
                'test_case': test_case
            })
    
    return results

def _execute_c_with_output(analyzer, code_path, test_cases):
    """Execute C code and capture all outputs"""
    # For now, use the original dynamic analyzer for C
    # We could implement output capture here if needed
    submission_data = {
        'student_id': 'temp_execution',
        'code_path': code_path,
        'language': 'c',
        'config': {
            'language': 'c',
            'test_cases': _format_test_cases_for_analyzer(test_cases),
        },
        'analysis': {'dynamic': []}
    }
    
    result = analyzer.analyze(submission_data)
    dynamic_results = result.get('analysis', {}).get('dynamic', [])
    
    formatted_results = []
    for i, test_result in enumerate(dynamic_results):
        test_case_data = test_cases[i] if i < len(test_cases) else {}
        
        formatted_result = {
            'status': test_result.get('status', 'error'),
            'console_output': test_result.get('actual', ''),
            'error_message': test_result.get('error', ''),
            'execution_time': test_result.get('execution_time', 0),
            'test_case': test_case_data
        }
        
        formatted_results.append(formatted_result)
    
    return formatted_results

def _execute_java_with_output(analyzer, code_path, test_cases):
    """Execute Java code and capture all outputs"""
    # For now, use the original dynamic analyzer for Java
    # We could implement output capture here if needed
    submission_data = {
        'student_id': 'temp_execution',
        'code_path': code_path,
        'language': 'java',
        'config': {
            'language': 'java',
            'test_cases': _format_test_cases_for_analyzer(test_cases),
        },
        'analysis': {'dynamic': []}
    }
    
    result = analyzer.analyze(submission_data)
    dynamic_results = result.get('analysis', {}).get('dynamic', [])
    
    formatted_results = []
    for i, test_result in enumerate(dynamic_results):
        test_case_data = test_cases[i] if i < len(test_cases) else {}
        
        formatted_result = {
            'status': test_result.get('status', 'error'),
            'console_output': test_result.get('actual', ''),
            'error_message': test_result.get('error', ''),
            'execution_time': test_result.get('execution_time', 0),
            'test_case': test_case_data
        }
        
        formatted_results.append(formatted_result)
    
    return formatted_results

def _get_file_extension(language):
    """Get appropriate file extension for the language"""
    extensions = {
        'python': '.py',
        'c': '.c',
        'java': '.java'
    }
    return extensions.get(language, '.txt')

def _format_test_cases_for_analyzer(test_cases):
    """Format test cases for the dynamic analyzer"""
    formatted_cases = []
    
    for i, test_case in enumerate(test_cases):
        formatted_case = {
            'name': f'test_{i+1}',
            'input': test_case.get('input', ''),
            'expected_output': test_case.get('expected_output', '')
        }
        formatted_cases.append(formatted_case)
    
    return formatted_cases

def _format_docker_results(docker_result, original_test_cases):
    """Convert Docker result format to View format"""
    formatted = []
    raw_results = docker_result.get('results', [])
    
    for i, res in enumerate(raw_results):
        tc_data = original_test_cases[i] if i < len(original_test_cases) else {}
        
        status = 'pass' if res['passed'] else 'fail'
        if res.get('error'):
            status = 'error'
            
        formatted.append({
            'status': status,
            'console_output': res.get('actual_output', ''),
            'error_message': res.get('error', ''),
            'execution_time': res.get('execution_time', 0),
            'test_case': tc_data
        })
    return formatted

def analyze_code_structure(code):
    """
    Analyze Python code structure using AST.
    Returns a list of detected tags/keywords.
    """
    tags = []
    try:
        tree = ast.parse(code)
        
        # Walk the tree
        for node in ast.walk(tree):
            # Recursion Detection
            if isinstance(node, ast.FunctionDef):
                for child in ast.walk(node):
                    if isinstance(child, ast.Call):
                        if isinstance(child.func, ast.Name) and child.func.id == node.name:
                            if "recursion" not in tags: tags.append("recursion")
            
            # Nested Loops
            if isinstance(node, (ast.For, ast.While)):
                for child in node.body:
                    if isinstance(child, (ast.For, ast.While)):
                        if "nested_loops" not in tags: tags.append("nested_loops")
                        
            # List Comprehension
            if isinstance(node, ast.ListComp):
                if "list_comprehension" not in tags: tags.append("list_comprehension")
                
            # Dictionary Comprehension
            if isinstance(node, ast.DictComp):
                if "dict_comprehension" not in tags: tags.append("dict_comprehension")
                
            # Set Comprehension
            if isinstance(node, ast.SetComp):
                if "set_comprehension" not in tags: tags.append("set_comprehension")
                
            # Generators
            if isinstance(node, ast.GeneratorExp):
                if "generator" not in tags: tags.append("generator")

            # Try/Except
            if isinstance(node, ast.Try):
                if "error_handling" not in tags: tags.append("error_handling")

    except SyntaxError:
        tags.append("syntax_error")
    except Exception:
        pass
        
    return tags
