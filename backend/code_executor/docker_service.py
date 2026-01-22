"""
Docker-based code execution service
Provides secure, isolated code execution using Docker containers
Optimized for high concurrency (150+ students)
"""
import docker
import json
import time
import threading
import queue
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger(__name__)


class DockerExecutor:
    """Handles Docker-based code execution with connection pooling and concurrency optimization"""
    
    def __init__(self):
        """Initialize Docker client with connection pooling"""
        try:
            self.client = docker.from_env()
            self.image_name = getattr(settings, 'DOCKER_EXECUTOR_IMAGE', 'autograder-executor:latest')
            
            # Connection pool for high concurrency
            self.max_workers = getattr(settings, 'DOCKER_MAX_WORKERS', 20)
            self.executor_pool = ThreadPoolExecutor(max_workers=self.max_workers)
            
            # Container resource limits optimized for 150 concurrent users
            self.container_limits = {
                'mem_limit': '128m',  # Reduced from 256m for more concurrent containers
                'cpu_period': 100000,
                'cpu_quota': 30000,   # 30% of one CPU (reduced for more concurrency)
                'timeout': 8,         # Slightly increased timeout
                'tmpfs_size': '5M'    # Reduced temp space
            }
            
            # Warm up the image
            self._warm_up_image()
            
        except Exception as e:
            logger.error(f"Docker client initialization failed: {e}")
            self.client = None
            self.executor_pool = None
    
    def _warm_up_image(self):
        """Warm up Docker image to reduce first-run latency"""
        try:
            # Pull image if not exists
            try:
                self.client.images.get(self.image_name)
                logger.info(f"Docker image {self.image_name} is available")
            except docker.errors.ImageNotFound:
                logger.warning(f"Docker image {self.image_name} not found. Please build it first.")
                return False
            
            # Test run to warm up
            test_data = {'code': 'print("warmup")', 'input': ''}
            container = self.client.containers.run(
                self.image_name,
                command=['python', 'execute.py'],
                stdin_open=True,
                detach=True,
                remove=True,
                **self._get_container_config()
            )
            
            # Send test input
            container_socket = container.attach_socket(params={'stdin': 1, 'stream': 1})
            container_socket._sock.sendall(json.dumps(test_data).encode('utf-8'))
            container_socket.close()
            
            # Wait for completion
            container.wait(timeout=5)
            logger.info("Docker image warmed up successfully")
            return True
            
        except Exception as e:
            logger.warning(f"Docker warmup failed: {e}")
            return False
    
    def _get_container_config(self):
        """Get optimized container configuration"""
        return {
            'mem_limit': self.container_limits['mem_limit'],
            'cpu_period': self.container_limits['cpu_period'],
            'cpu_quota': self.container_limits['cpu_quota'],
            'network_disabled': True,
            'read_only': True,
            'tmpfs': {'/tmp': f'size={self.container_limits["tmpfs_size"]},mode=1777'},
            'security_opt': ['no-new-privileges:true'],
            'cap_drop': ['ALL'],
            'user': '1000:1000'  # Non-root user
        }
    
    def is_available(self):
        """Check if Docker is available"""
        return self.client is not None and self.executor_pool is not None
    
    def execute_code_async(self, code, test_input="", timeout=None):
        """
        Execute Python code asynchronously in Docker container
        Optimized for high concurrency
        """
        if timeout is None:
            timeout = self.container_limits['timeout']
            
        if not self.is_available():
            return {
                'success': False,
                'output': '',
                'error': 'Docker is not available. Please ensure Docker is running.',
                'execution_time': 0
            }
        
        # Submit to thread pool for concurrent execution
        future = self.executor_pool.submit(self._execute_single, code, test_input, timeout)
        return future
    
    def _execute_single(self, code, test_input, timeout):
        """Execute single code submission in Docker container"""
        try:
            # Prepare input data
            input_data = {
                'code': code,
                'input': test_input
            }
            input_json = json.dumps(input_data)
            
            start_time = time.time()
            
            # Create and run container with optimized settings
            container = self.client.containers.run(
                self.image_name,
                command=['python', 'execute.py'],
                stdin_open=True,
                detach=True,
                remove=True,
                **self._get_container_config()
            )
            
            try:
                # Send input data
                container_socket = container.attach_socket(params={'stdin': 1, 'stream': 1})
                container_socket._sock.sendall(input_json.encode('utf-8'))
                container_socket.close()
                
                # Wait for container to finish
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
                    
            except Exception as e:
                # Ensure container cleanup
                try:
                    container.kill()
                except:
                    pass
                raise e
                
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
    
    
    def execute_code(self, code, test_input="", timeout=None):
        """
        Execute Python code in Docker container (synchronous wrapper)
        """
        future = self.execute_code_async(code, test_input, timeout)
        return future.result()
    
    def execute_test_cases_concurrent(self, code, test_cases):
        """
        Execute code against multiple test cases concurrently
        Optimized for high performance with 150+ concurrent users
        """
        if not self.is_available():
            return self._fallback_error_result(len(test_cases))
        
        # Submit all test cases for concurrent execution
        futures = []
        for i, test_case in enumerate(test_cases):
            test_input = self._extract_test_input(test_case)
            future = self.execute_code_async(code, test_input)
            futures.append((i, test_case, future))
        
        # Collect results as they complete
        results = [None] * len(test_cases)
        passed_count = 0
        
        for i, test_case, future in futures:
            try:
                exec_result = future.result(timeout=self.container_limits['timeout'] + 2)
                expected_output = self._extract_expected_output(test_case)
                
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
                        'input': self._extract_test_input(test_case),
                        'expected_output': expected_output_clean
                    }
                }
                results[i] = result
                
            except Exception as e:
                logger.error(f"Test case {i} execution failed: {e}")
                results[i] = {
                    'test_case_id': i + 1,
                    'passed': False,
                    'actual_output': '',
                    'expected_output': self._extract_expected_output(test_case),
                    'error': f'Execution failed: {str(e)}',
                    'execution_time': 0,
                    'test_case': {
                        'input': self._extract_test_input(test_case),
                        'expected_output': self._extract_expected_output(test_case)
                    }
                }
        
        return {
            'results': results,
            'summary': {
                'total': len(test_cases),
                'passed': passed_count,
                'failed': len(test_cases) - passed_count,
                'all_passed': passed_count == len(test_cases)
            }
        }
    
    def _extract_test_input(self, test_case):
        """Extract input from test case object or dict"""
        if hasattr(test_case, 'input'):
            return test_case.input
        return test_case.get('input', '')
    
    def _extract_expected_output(self, test_case):
        """Extract expected output from test case object or dict"""
        if hasattr(test_case, 'expected_output'):
            return test_case.expected_output
        return test_case.get('expected_output', '')
    
    def _fallback_error_result(self, num_test_cases):
        """Return error result when Docker is not available"""
        results = []
        for i in range(num_test_cases):
            results.append({
                'test_case_id': i + 1,
                'passed': False,
                'actual_output': '',
                'expected_output': '',
                'error': 'Docker is not available',
                'execution_time': 0,
                'test_case': {'input': '', 'expected_output': ''}
            })
        
        return {
            'results': results,
            'summary': {
                'total': num_test_cases,
                'passed': 0,
                'failed': num_test_cases,
                'all_passed': False
            }
        }
    
    
    def execute_test_cases(self, code, test_cases):
        """
        Execute code against multiple test cases (backward compatibility)
        Uses concurrent execution for better performance
        """
        return self.execute_test_cases_concurrent(code, test_cases)
    
    def get_stats(self):
        """Get executor statistics for monitoring"""
        if not self.is_available():
            return {'available': False}
        
        return {
            'available': True,
            'max_workers': self.max_workers,
            'active_threads': self.executor_pool._threads,
            'container_limits': self.container_limits,
            'image_name': self.image_name
        }
    
    def shutdown(self):
        """Gracefully shutdown the executor"""
        if self.executor_pool:
            self.executor_pool.shutdown(wait=True)
            logger.info("Docker executor shutdown complete")


# Global executor instance with lazy initialization
_executor = None
_executor_lock = threading.Lock()

def get_docker_executor():
    """Get or create Docker executor instance (thread-safe)"""
    global _executor
    if _executor is None:
        with _executor_lock:
            if _executor is None:
                _executor = DockerExecutor()
    return _executor

def get_executor_stats():
    """Get executor statistics for monitoring"""
    executor = get_docker_executor()
    return executor.get_stats()
