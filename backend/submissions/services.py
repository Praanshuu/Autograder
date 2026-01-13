import subprocess
import tempfile
import os
import uuid
from django.conf import settings
from .models import TestResult
from assignments.models import TestCase


def execute_code(code, language, test_cases):
    """
    Execute code against test cases
    Returns list of test results
    """
    results = []
    
    for test_case_data in test_cases:
        test_case = test_case_data.get('test_case') if isinstance(test_case_data, dict) else None
        input_data = test_case_data.get('input', '') if isinstance(test_case_data, dict) else str(test_case_data.get('input', ''))
        expected_output = test_case_data.get('expected_output', '') if isinstance(test_case_data, dict) else str(test_case_data.get('expected_output', ''))
        
        result = execute_single_test(code, language, input_data, expected_output, test_case)
        results.append(result)
    
    return results


def execute_single_test(code, language, input_data, expected_output, test_case=None):
    """Execute code for a single test case"""
    timeout = getattr(settings, 'CODE_EXECUTION_TIMEOUT', 10)
    temp_dir = tempfile.mkdtemp()
    test_id = str(uuid.uuid4())
    
    try:
        if language == 'python':
            return execute_python(code, input_data, expected_output, temp_dir, test_id, timeout, test_case)
        elif language == 'javascript':
            return execute_javascript(code, input_data, expected_output, temp_dir, test_id, timeout, test_case)
        elif language == 'java':
            return execute_java(code, input_data, expected_output, temp_dir, test_id, timeout, test_case)
        elif language in ['cpp', 'c']:
            return execute_cpp(code, input_data, expected_output, temp_dir, test_id, timeout, language, test_case)
        else:
            return {
                'status': 'error',
                'error_message': f'Unsupported language: {language}',
                'console_output': '',
                'execution_time': 0
            }
    except Exception as e:
        return {
            'status': 'error',
            'error_message': str(e),
            'console_output': '',
            'execution_time': 0
        }
    finally:
        # Cleanup
        import shutil
        try:
            shutil.rmtree(temp_dir)
        except:
            pass


def execute_python(code, input_data, expected_output, temp_dir, test_id, timeout, test_case=None):
    """Execute Python code"""
    file_path = os.path.join(temp_dir, f'{test_id}.py')
    input_file = os.path.join(temp_dir, f'{test_id}_input.txt')
    
    with open(file_path, 'w') as f:
        f.write(code)
    
    with open(input_file, 'w') as f:
        f.write(str(input_data))
    
    import time
    start_time = time.time()
    
    try:
        result = subprocess.run(
            ['python3', file_path],
            stdin=open(input_file, 'r'),
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=temp_dir
        )
        
        execution_time = int((time.time() - start_time) * 1000)
        output = result.stdout.strip()
        
        status = 'pass' if output == str(expected_output).strip() else 'fail'
        
        return {
            'status': status,
            'console_output': output,
            'error_message': result.stderr,
            'execution_time': execution_time,
            'test_case': test_case
        }
    except subprocess.TimeoutExpired:
        return {
            'status': 'timeout',
            'error_message': 'Execution timeout',
            'console_output': '',
            'execution_time': timeout * 1000,
            'test_case': test_case
        }
    except Exception as e:
        return {
            'status': 'error',
            'error_message': str(e),
            'console_output': '',
            'execution_time': 0,
            'test_case': test_case
        }


def execute_javascript(code, input_data, expected_output, temp_dir, test_id, timeout, test_case=None):
    """Execute JavaScript code"""
    file_path = os.path.join(temp_dir, f'{test_id}.js')
    input_file = os.path.join(temp_dir, f'{test_id}_input.txt')
    
    # Wrap code to read input
    wrapped_code = f"""
const fs = require('fs');
const input = fs.readFileSync('{input_file}', 'utf8').trim();
{code}
"""
    
    with open(file_path, 'w') as f:
        f.write(wrapped_code)
    
    with open(input_file, 'w') as f:
        f.write(str(input_data))
    
    import time
    start_time = time.time()
    
    try:
        result = subprocess.run(
            ['node', file_path],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=temp_dir
        )
        
        execution_time = int((time.time() - start_time) * 1000)
        output = result.stdout.strip()
        
        status = 'pass' if output == str(expected_output).strip() else 'fail'
        
        return {
            'status': status,
            'console_output': output,
            'error_message': result.stderr,
            'execution_time': execution_time,
            'test_case': test_case
        }
    except subprocess.TimeoutExpired:
        return {
            'status': 'timeout',
            'error_message': 'Execution timeout',
            'console_output': '',
            'execution_time': timeout * 1000,
            'test_case': test_case
        }
    except Exception as e:
        return {
            'status': 'error',
            'error_message': str(e),
            'console_output': '',
            'execution_time': 0,
            'test_case': test_case
        }


def execute_java(code, input_data, expected_output, temp_dir, test_id, timeout, test_case=None):
    """Execute Java code"""
    class_name = f'Solution_{test_id.replace("-", "")}'
    file_path = os.path.join(temp_dir, f'{class_name}.java')
    input_file = os.path.join(temp_dir, f'{test_id}_input.txt')
    
    # Ensure class name matches
    modified_code = code.replace('public class Solution', f'public class {class_name}')
    if 'public class' not in modified_code:
        modified_code = f'public class {class_name} {{\n{code}\n}}'
    
    with open(file_path, 'w') as f:
        f.write(modified_code)
    
    with open(input_file, 'w') as f:
        f.write(str(input_data))
    
    import time
    start_time = time.time()
    
    try:
        # Compile
        compile_result = subprocess.run(
            ['javac', file_path],
            capture_output=True,
            text=True,
            timeout=5,
            cwd=temp_dir
        )
        
        if compile_result.returncode != 0:
            return {
                'status': 'error',
                'error_message': compile_result.stderr,
                'console_output': '',
                'execution_time': 0,
                'test_case': test_case
            }
        
        # Execute
        result = subprocess.run(
            ['java', '-cp', temp_dir, class_name],
            stdin=open(input_file, 'r'),
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=temp_dir
        )
        
        execution_time = int((time.time() - start_time) * 1000)
        output = result.stdout.strip()
        
        status = 'pass' if output == str(expected_output).strip() else 'fail'
        
        return {
            'status': status,
            'console_output': output,
            'error_message': result.stderr,
            'execution_time': execution_time,
            'test_case': test_case
        }
    except subprocess.TimeoutExpired:
        return {
            'status': 'timeout',
            'error_message': 'Execution timeout',
            'console_output': '',
            'execution_time': timeout * 1000,
            'test_case': test_case
        }
    except Exception as e:
        return {
            'status': 'error',
            'error_message': str(e),
            'console_output': '',
            'execution_time': 0,
            'test_case': test_case
        }


def execute_cpp(code, input_data, expected_output, temp_dir, test_id, timeout, language, test_case=None):
    """Execute C/C++ code"""
    ext = 'cpp' if language == 'cpp' else 'c'
    compiler = 'g++' if language == 'cpp' else 'gcc'
    file_path = os.path.join(temp_dir, f'{test_id}.{ext}')
    executable = os.path.join(temp_dir, f'{test_id}_exec')
    input_file = os.path.join(temp_dir, f'{test_id}_input.txt')
    
    with open(file_path, 'w') as f:
        f.write(code)
    
    with open(input_file, 'w') as f:
        f.write(str(input_data))
    
    import time
    start_time = time.time()
    
    try:
        # Compile
        compile_result = subprocess.run(
            [compiler, file_path, '-o', executable],
            capture_output=True,
            text=True,
            timeout=5,
            cwd=temp_dir
        )
        
        if compile_result.returncode != 0:
            return {
                'status': 'error',
                'error_message': compile_result.stderr,
                'console_output': '',
                'execution_time': 0,
                'test_case': test_case
            }
        
        # Execute
        result = subprocess.run(
            [executable],
            stdin=open(input_file, 'r'),
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=temp_dir
        )
        
        execution_time = int((time.time() - start_time) * 1000)
        output = result.stdout.strip()
        
        status = 'pass' if output == str(expected_output).strip() else 'fail'
        
        return {
            'status': status,
            'console_output': output,
            'error_message': result.stderr,
            'execution_time': execution_time,
            'test_case': test_case
        }
    except subprocess.TimeoutExpired:
        return {
            'status': 'timeout',
            'error_message': 'Execution timeout',
            'console_output': '',
            'execution_time': timeout * 1000,
            'test_case': test_case
        }
    except Exception as e:
        return {
            'status': 'error',
            'error_message': str(e),
            'console_output': '',
            'execution_time': 0,
            'test_case': test_case
        }
