"""
Docker-based code execution service
Provides secure, isolated code execution using Docker containers
"""
import docker
import json
import time
from django.conf import settings


class DockerExecutor:
    """Handles Docker-based code execution"""
    
    def __init__(self):
        """Initialize Docker client"""
        try:
            self.client = docker.from_env()
            self.image_name = getattr(settings, 'DOCKER_EXECUTOR_IMAGE', 'autograder-executor:latest')
        except Exception as e:
            print(f"Warning: Docker client initialization failed: {e}")
            self.client = None
    
    def is_available(self):
        """Check if Docker is available"""
        return self.client is not None
    
    def execute_code(self, code, test_input="", timeout=5):
        """
        Execute Python code in Docker container
        
        Args:
            code: Python code to execute
            test_input: Input to provide to the program
            timeout: Execution timeout in seconds
            
        Returns:
            dict: Execution result with output, error, and status
        """
        if not self.is_available():
            return {
                'success': False,
                'output': '',
                'error': 'Docker is not available. Please ensure Docker is running.',
                'execution_time': 0
            }
        
        try:
            # Prepare input data
            input_data = {
                'code': code,
                'input': test_input
            }
            input_json = json.dumps(input_data)
            
            # Run container
            start_time = time.time()
            
            container = self.client.containers.run(
                self.image_name,
                command=['python', 'execute.py'],
                stdin_open=True,
                detach=True,
                remove=True,
                mem_limit='256m',
                cpu_period=100000,
                cpu_quota=50000,  # 50% of one CPU
                network_disabled=True,  # No network access
                read_only=True,  # Read-only filesystem
                tmpfs={'/tmp': 'size=10M,mode=1777'},  # Small temp space
            )
            
            # Send input and wait for result
            container_socket = container.attach_socket(params={'stdin': 1, 'stream': 1})
            container_socket._sock.sendall(input_json.encode('utf-8'))
            container_socket.close()
            
            # Wait for container to finish (with timeout)
            result = container.wait(timeout=timeout)
            execution_time = int((time.time() - start_time) * 1000)
            
            # Get output
            output = container.logs().decode('utf-8')
            
            # Parse JSON result
            try:
                result_data = json.loads(output)
                result_data['execution_time'] = execution_time
                return result_data
            except json.JSONDecodeError:
                return {
                    'success': False,
                    'output': output,
                    'error': 'Failed to parse execution result',
                    'execution_time': execution_time
                }
                
        except docker.errors.ContainerError as e:
            return {
                'success': False,
                'output': '',
                'error': f'Container error: {str(e)}',
                'execution_time': 0
            }
        except docker.errors.ImageNotFound:
            return {
                'success': False,
                'output': '',
                'error': f'Docker image not found: {self.image_name}. Please build the image first.',
                'execution_time': 0
            }
        except Exception as e:
            return {
                'success': False,
                'output': '',
                'error': f'Execution error: {str(e)}',
                'execution_time': 0
            }
    
    def execute_test_cases(self, code, test_cases):
        """
        Execute code against multiple test cases
        
        Args:
            code: Python code to execute
            test_cases: List of test case objects with input and expected_output
            
        Returns:
            dict: Results for all test cases with summary
        """
        results = []
        passed_count = 0
        
        for i, test_case in enumerate(test_cases):
            # Get test case data
            if hasattr(test_case, 'input'):
                test_input = test_case.input
                expected_output = test_case.expected_output
            else:
                test_input = test_case.get('input', '')
                expected_output = test_case.get('expected_output', '')
            
            # Execute code
            exec_result = self.execute_code(code, test_input)
            
            # Check if output matches expected
            actual_output = exec_result.get('output', '').strip()
            expected_output_clean = str(expected_output).strip()
            passed = exec_result.get('success', False) and actual_output == expected_output_clean
            
            if passed:
                passed_count += 1
            
            # Format result
            result = {
                'test_case_id': i + 1,
                'passed': passed,
                'actual_output': actual_output,
                'expected_output': expected_output_clean,
                'error': exec_result.get('error', ''),
                'execution_time': exec_result.get('execution_time', 0),
                'test_case': {
                    'input': test_input,
                    'expected_output': expected_output_clean
                }
            }
            results.append(result)
        
        return {
            'results': results,
            'summary': {
                'total': len(test_cases),
                'passed': passed_count,
                'failed': len(test_cases) - passed_count,
                'all_passed': passed_count == len(test_cases)
            }
        }


# Global executor instance
_executor = None

def get_docker_executor():
    """Get or create Docker executor instance"""
    global _executor
    if _executor is None:
        _executor = DockerExecutor()
    return _executor
