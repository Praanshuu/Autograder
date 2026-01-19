#!/usr/bin/env python3
"""
Secure code execution script for Docker container
Runs student code with resource limits and security restrictions
"""
import sys
import json
import resource
import signal
import traceback
from io import StringIO
import contextlib

# Set resource limits
def set_limits():
    """Set CPU and memory limits"""
    # CPU time limit: 5 seconds
    resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
    # Memory limit: 256 MB
    resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
    # File size limit: 1 MB
    resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))

def timeout_handler(signum, frame):
    """Handle timeout"""
    raise TimeoutError("Execution time limit exceeded (5 seconds)")

def execute_code(code, test_input=""):
    """
    Execute Python code with security restrictions
    
    Args:
        code: Python code to execute
        test_input: Input to provide to the program
        
    Returns:
        dict: Execution result with output, error, and status
    """
    result = {
        'success': False,
        'output': '',
        'error': '',
        'execution_time': 0
    }
    
    try:
        # Set resource limits
        set_limits()
        
        # Set timeout alarm
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(5)  # 5 second timeout
        
        # Capture stdout and stderr
        stdout_capture = StringIO()
        stderr_capture = StringIO()
        
        # Prepare stdin if test input provided
        if test_input:
            sys.stdin = StringIO(test_input)
        
        # Execute code with captured output
        with contextlib.redirect_stdout(stdout_capture), \
             contextlib.redirect_stderr(stderr_capture):
            
            # Create restricted globals (no dangerous builtins)
            safe_globals = {
                '__builtins__': {
                    'print': print,
                    'input': input,
                    'len': len,
                    'range': range,
                    'int': int,
                    'float': float,
                    'str': str,
                    'list': list,
                    'dict': dict,
                    'tuple': tuple,
                    'set': set,
                    'bool': bool,
                    'abs': abs,
                    'min': min,
                    'max': max,
                    'sum': sum,
                    'sorted': sorted,
                    'enumerate': enumerate,
                    'zip': zip,
                    'map': map,
                    'filter': filter,
                    'any': any,
                    'all': all,
                    'isinstance': isinstance,
                    'type': type,
                    'Exception': Exception,
                    'ValueError': ValueError,
                    'TypeError': TypeError,
                    'IndexError': IndexError,
                    'KeyError': KeyError,
                    'ZeroDivisionError': ZeroDivisionError,
                }
            }
            
            # Execute the code
            exec(code, safe_globals)
        
        # Cancel alarm
        signal.alarm(0)
        
        # Get output
        result['success'] = True
        result['output'] = stdout_capture.getvalue()
        result['error'] = stderr_capture.getvalue()
        
    except TimeoutError as e:
        result['error'] = str(e)
    except MemoryError:
        result['error'] = "Memory limit exceeded (256 MB)"
    except SyntaxError as e:
        result['error'] = f"Syntax Error: {str(e)}"
    except Exception as e:
        result['error'] = f"{type(e).__name__}: {str(e)}\n{traceback.format_exc()}"
    finally:
        # Reset stdin
        sys.stdin = sys.__stdin__
        # Cancel any remaining alarm
        signal.alarm(0)
    
    return result

if __name__ == "__main__":
    # Read input from stdin (JSON format)
    try:
        input_data = json.loads(sys.stdin.read())
        code = input_data.get('code', '')
        test_input = input_data.get('input', '')
        
        # Execute code
        result = execute_code(code, test_input)
        
        # Output result as JSON
        print(json.dumps(result))
        
    except Exception as e:
        error_result = {
            'success': False,
            'output': '',
            'error': f"Execution error: {str(e)}"
        }
        print(json.dumps(error_result))
