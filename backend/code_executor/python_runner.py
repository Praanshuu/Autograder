#!/usr/bin/env python3
"""
Python-based code execution service
Similar to the Go runner but integrated with Django
Supports multiple languages with secure execution
"""

import os
import subprocess
import tempfile
import uuid
import time
import threading
from pathlib import Path
from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class CodeExecutor:
    """Secure code execution service supporting multiple languages"""
    
    def __init__(self):
        self.base_dir = Path(tempfile.gettempdir()) / "autograder_jobs"
        self.base_dir.mkdir(exist_ok=True)
        
        # Execution timeouts
        self.exec_timeout = 10  # seconds
        self.compile_timeout = 10  # seconds
        
        # Resource limits
        self.max_code_size = 10000  # characters
        self.max_inputs = 20
        
        # Supported languages
        self.supported_languages = {
            'python': self._execute_python,
            'javascript': self._execute_javascript,
            'java': self._execute_java,
            'c': self._execute_c,
            'cpp': self._execute_cpp,
        }
    
    def execute(self, language: str, code: str, inputs: List[str]) -> Dict[str, Any]:
        """
        Execute code with given inputs
        
        Args:
            language: Programming language (python, javascript, java, c, cpp)
            code: Source code to execute
            inputs: List of input strings for the program
            
        Returns:
            Dict with status, outputs, and any errors
        """
        try:
            # Validate inputs
            if not code or not code.strip():
                return {
                    'status': 'error',
                    'message': 'Code cannot be empty',
                    'outputs': []
                }
            
            if len(code) > self.max_code_size:
                return {
                    'status': 'error',
                    'message': 'Code too large',
                    'outputs': []
                }
            
            if len(inputs) > self.max_inputs:
                return {
                    'status': 'error',
                    'message': 'Too many inputs',
                    'outputs': []
                }
            
            language = language.lower()
            if language not in self.supported_languages:
                return {
                    'status': 'error',
                    'message': f'Unsupported language: {language}',
                    'outputs': []
                }
            
            # Validate code for security
            security_check = self._validate_code_security(language, code)
            if security_check:
                return {
                    'status': 'success',
                    'outputs': [security_check],
                    'message': 'Security restriction'
                }
            
            # Execute code
            executor_func = self.supported_languages[language]
            outputs = executor_func(code, inputs)
            
            return {
                'status': 'success',
                'outputs': outputs,
                'message': 'Execution completed'
            }
            
        except Exception as e:
            logger.error(f"Code execution error: {e}")
            return {
                'status': 'error',
                'message': str(e),
                'outputs': []
            }
    
    def _validate_code_security(self, language: str, code: str) -> Optional[str]:
        """Check for potentially dangerous code patterns"""
        dangerous_patterns = {
            'python': [
                'import os', 'import sys', 'import subprocess', 'import shutil',
                'import socket', 'import urllib', 'import requests', 'import http',
                'open(', '__import__', 'eval(', 'exec(', 'compile(',
                'globals()', 'locals()', 'vars()', 'dir()',
            ],
            'javascript': [
                'require(', 'import ', 'fetch(', 'XMLHttpRequest',
                'process.', 'global.', 'Buffer.', 'child_process',
            ],
            'java': [
                'import java.io', 'import java.net', 'import java.nio',
                'Runtime.', 'ProcessBuilder', 'System.exit',
                'Class.forName', 'reflection',
            ],
            'c': [
                '#include <stdlib.h>', '#include <unistd.h>', 
                'system(', 'exec(', 'fork(', 'popen(',
            ],
            'cpp': [
                '#include <cstdlib>', '#include <unistd.h>',
                'system(', 'exec(', 'fork(', 'popen(',
            ]
        }
        
        if language in dangerous_patterns:
            for pattern in dangerous_patterns[language]:
                if pattern in code:
                    return f"Use of '{pattern}' is not allowed for security reasons"
        
        return None
  
    #sandbox
    def _create_job_directory(self) -> Path:
        """Create a unique directory for this execution job"""
        job_id = str(uuid.uuid4())
        job_dir = self.base_dir / job_id
        job_dir.mkdir(exist_ok=True)
        return job_dir
    
    def _cleanup_job_directory(self, job_dir: Path):
        """Clean up job directory after execution"""
        try:
            import shutil
            shutil.rmtree(job_dir, ignore_errors=True)
        except Exception as e:
            logger.warning(f"Failed to cleanup job directory {job_dir}: {e}")
    
    def _execute_python(self, code: str, inputs: List[str]) -> List[str]:
        """Execute Python code"""
        job_dir = self._create_job_directory()
        
        try:
            # Write code to file
            code_file = job_dir / "program.py"
            code_file.write_text(code, encoding='utf-8')
            
            outputs = []
            
            # Execute for each input
            for input_data in inputs:
                try:
                    # Run Python with timeout
                    process = subprocess.Popen(
                        ['python3', str(code_file)],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        cwd=job_dir
                    )
                    
                    stdout, stderr = process.communicate(
                        input=input_data, 
                        timeout=self.exec_timeout
                    )
                    
                    if process.returncode == 0:
                        outputs.append(stdout.strip())
                    else:
                        error_msg = stderr.strip() if stderr.strip() else f"Process exited with code {process.returncode}"
                        outputs.append(f"Error: {error_msg}")
                        
                except subprocess.TimeoutExpired:
                    process.kill()
                    outputs.append("Error: Code execution timed out")
                except Exception as e:
                    outputs.append(f"Error: {str(e)}")
            
            return outputs
            
        finally:
            self._cleanup_job_directory(job_dir)
    
    def _execute_javascript(self, code: str, inputs: List[str]) -> List[str]:
        """Execute JavaScript code"""
        job_dir = self._create_job_directory()
        
        try:
            outputs = []
            
            for input_data in inputs:
                # Wrap code to handle input
                wrapped_code = f"""
const readline = require('readline');
const rl = readline.createInterface({{
    input: process.stdin,
    output: process.stdout
}});

let inputLines = `{input_data}`.split('\\n');
let currentLine = 0;

// Mock input function
function input() {{
    return inputLines[currentLine++] || '';
}}

// Your code here
{code}

rl.close();
"""
                
                code_file = job_dir / "program.js"
                code_file.write_text(wrapped_code, encoding='utf-8')
                
                try:
                    process = subprocess.Popen(
                        ['node', str(code_file)],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        cwd=job_dir
                    )
                    
                    stdout, stderr = process.communicate(
                        input=input_data,
                        timeout=self.exec_timeout
                    )
                    
                    if process.returncode == 0:
                        outputs.append(stdout.strip())
                    else:
                        error_msg = stderr.strip() if stderr.strip() else f"Process exited with code {process.returncode}"
                        outputs.append(f"Error: {error_msg}")
                        
                except subprocess.TimeoutExpired:
                    process.kill()
                    outputs.append("Error: Code execution timed out")
                except Exception as e:
                    outputs.append(f"Error: {str(e)}")
            
            return outputs
            
        finally:
            self._cleanup_job_directory(job_dir)
    
    def _execute_java(self, code: str, inputs: List[str]) -> List[str]:
        """Execute Java code"""
        job_dir = self._create_job_directory()
        
        try:
            # Extract class name from code
            class_name = self._extract_java_class_name(code)
            if not class_name:
                return ["Error: Could not find public class in Java code"]
            
            # Write code to file
            code_file = job_dir / f"{class_name}.java"
            code_file.write_text(code, encoding='utf-8')
            
            # Compile Java code
            try:
                compile_process = subprocess.run(
                    ['javac', str(code_file)],
                    capture_output=True,
                    text=True,
                    timeout=self.compile_timeout,
                    cwd=job_dir
                )
                
                if compile_process.returncode != 0:
                    error_msg = compile_process.stderr.strip()
                    return [f"Compilation Error: {error_msg}"]
                    
            except subprocess.TimeoutExpired:
                return ["Error: Compilation timed out"]
            except Exception as e:
                return [f"Compilation Error: {str(e)}"]
            
            # Execute compiled code
            outputs = []
            for input_data in inputs:
                try:
                    process = subprocess.Popen(
                        ['java', '-cp', str(job_dir), class_name],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        cwd=job_dir
                    )
                    
                    stdout, stderr = process.communicate(
                        input=input_data,
                        timeout=self.exec_timeout
                    )
                    
                    if process.returncode == 0:
                        outputs.append(stdout.strip())
                    else:
                        error_msg = stderr.strip() if stderr.strip() else f"Process exited with code {process.returncode}"
                        outputs.append(f"Error: {error_msg}")
                        
                except subprocess.TimeoutExpired:
                    process.kill()
                    outputs.append("Error: Code execution timed out")
                except Exception as e:
                    outputs.append(f"Error: {str(e)}")
            
            return outputs
            
        finally:
            self._cleanup_job_directory(job_dir)
    
    def _execute_c(self, code: str, inputs: List[str]) -> List[str]:
        """Execute C code"""
        return self._execute_c_cpp(code, inputs, 'gcc', 'c')
    
    def _execute_cpp(self, code: str, inputs: List[str]) -> List[str]:
        """Execute C++ code"""
        return self._execute_c_cpp(code, inputs, 'g++', 'cpp')
    
    def _execute_c_cpp(self, code: str, inputs: List[str], compiler: str, extension: str) -> List[str]:
        """Execute C/C++ code"""
        job_dir = self._create_job_directory()
        
        try:
            # Write code to file
            code_file = job_dir / f"program.{extension}"
            executable = job_dir / "program"
            
            code_file.write_text(code, encoding='utf-8')
            
            # Compile code
            try:
                compile_process = subprocess.run(
                    [compiler, '-Wall', str(code_file), '-o', str(executable)],
                    capture_output=True,
                    text=True,
                    timeout=self.compile_timeout,
                    cwd=job_dir
                )
                
                if compile_process.returncode != 0:
                    error_msg = compile_process.stderr.strip()
                    return [f"Compilation Error: {error_msg}"]
                    
            except subprocess.TimeoutExpired:
                return ["Error: Compilation timed out"]
            except Exception as e:
                return [f"Compilation Error: {str(e)}"]
            
            # Execute compiled code
            outputs = []
            for input_data in inputs:
                try:
                    process = subprocess.Popen(
                        [str(executable)],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        cwd=job_dir
                    )
                    
                    stdout, stderr = process.communicate(
                        input=input_data,
                        timeout=self.exec_timeout
                    )
                    
                    if process.returncode == 0:
                        outputs.append(stdout.strip())
                    else:
                        error_msg = stderr.strip() if stderr.strip() else f"Process exited with code {process.returncode}"
                        outputs.append(f"Error: {error_msg}")
                        
                except subprocess.TimeoutExpired:
                    process.kill()
                    outputs.append("Error: Code execution timed out")
                except Exception as e:
                    outputs.append(f"Error: {str(e)}")
            
            return outputs
            
        finally:
            self._cleanup_job_directory(job_dir)
    
    def _extract_java_class_name(self, code: str) -> Optional[str]:
        """Extract the public class name from Java code"""
        import re
        
        # Look for public class declaration
        pattern = r'public\s+class\s+(\w+)'
        match = re.search(pattern, code)
        
        if match:
            return match.group(1)
        
        # Fallback: look for any class declaration
        pattern = r'class\s+(\w+)'
        match = re.search(pattern, code)
        
        if match:
            return match.group(1)
        
        return None


# Global executor instance
_executor = None

def get_code_executor():
    """Get or create the global code executor instance"""
    global _executor
    if _executor is None:
        _executor = CodeExecutor()
    return _executor