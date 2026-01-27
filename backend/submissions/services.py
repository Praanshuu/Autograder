import logging
import time
from django.conf import settings
from code_executor.docker_service import get_docker_executor
from code_executor.python_runner import get_code_executor

logger = logging.getLogger(__name__)

def execute_code(code, language, test_cases):
    """
    Execute code against test cases using the best available executor.
    Strategy:
    1. Try DockerExecutor (Preferred for isolation & scale)
    2. Fallback to CodeExecutor (Local process) if Docker is down
    """
    # 1. Try Docker Execution
    docker_executor = get_docker_executor()
    if docker_executor.is_available():
        logger.info(f"Executing {language} code using DockerExecutor")
        result = docker_executor.execute_test_cases_concurrent(code, test_cases)
        return _format_docker_results(result, test_cases)
    
    # 2. Fallback to Local Execution
    logger.warning("Docker execution unavailable. Falling back to Local CodeExecutor.")
    local_executor = get_code_executor()
    
    results = []
    # Extract inputs for batch execution
    inputs = []
    for tc in test_cases:
        inputs.append(str(tc.get('input', '')))
    
    # Execute (Local runner returns list of outputs strings)
    # Note: Local runner currently assumes inputs are strings
    execution_result = local_executor.execute(language, code, inputs)
    
    if execution_result['status'] == 'error':
        # Compilation or System Error
        return [{
            'status': 'error',
            'error_message': execution_result['message'],
            'console_output': '',
            'execution_time': 0,
            'test_case': {}
        }]
    
    # Map outputs back to test cases
    outputs = execution_result['outputs']
    for i, output in enumerate(outputs):
        test_case_data = test_cases[i]
        expected_output = str(test_case_data.get('expected_output', '')).strip()
        actual_output = str(output).strip()
        
        # Grading Logic
        passed = actual_output == expected_output
        # Handle simple error strings from runner
        error_msg = ""
        if output.startswith("Error:"):
            error_msg = output
            status = 'error'
        else:
            status = 'pass' if passed else 'fail'

        results.append({
            'status': status,
            'console_output': actual_output,
            'error_message': error_msg,
            'execution_time': 0, # Local runner doesn't track per-test time yet
            'test_case': test_case_data
        })
        
    return results

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
