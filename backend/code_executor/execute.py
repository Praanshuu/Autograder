#!/usr/bin/env python3
"""
Secure code execution script for Docker container
Supports Python, C, C++, Java, and JavaScript
"""
import sys
import json
import resource
import signal
import subprocess
import os
import shutil
import time

def set_limits():
    """Set CPU and memory limits for child processes"""
    # CPU time limit: 5 seconds hard limit
    resource.setrlimit(resource.RLIMIT_CPU, (5, 6))
    # Memory limit: 128 MB (Soft), 256 MB (Hard)
    resource.setrlimit(resource.RLIMIT_AS, (128 * 1024 * 1024, 256 * 1024 * 1024))
    # File size limit: 10 MB
    resource.setrlimit(resource.RLIMIT_FSIZE, (10 * 1024 * 1024, 10 * 1024 * 1024))
    # Process limit: Prevent fork bombs
    # Note: RLIMIT_NPROC is often restricted by container capability, but we set it just in case
    try:
        resource.setrlimit(resource.RLIMIT_NPROC, (20, 20))
    except (ValueError, OSError):
        pass

def compile_and_run(language, code, test_input):
    """Compile (if needed) and run code based on language"""
    
    # Setup filenames
    if language == 'python':
        filename = "program.py"
        run_cmd = ["python3", filename]
    elif language == 'c':
        filename = "program.c"
        exe = "./program"
        compile_cmd = ["gcc", "-O2", "-Wall", filename, "-o", "program"]
        run_cmd = [exe]
    elif language == 'cpp':
        filename = "program.cpp"
        exe = "./program"
        compile_cmd = ["g++", "-O2", "-Wall", filename, "-o", "program"]
        run_cmd = [exe]
    elif language == 'java':
        # Simple heuristic to find class name, default to Main
        filename = "Main.java"
        if "public class" in code:
            parts = code.split("public class")[1].strip().split()
            if parts:
                filename = f"{parts[0].split('{')[0].strip()}.java"
        
        class_name = filename.replace(".java", "")
        compile_cmd = ["javac", filename]
        run_cmd = ["java", class_name]
    elif language == 'javascript':
        filename = "program.js"
        run_cmd = ["node", filename]
    else:
        return {'success': False, 'error': f"Unsupported language: {language}", 'output': ''}

    # Write code to file
    with open(filename, "w") as f:
        f.write(code)

    # Compilation Step
    if language in ['c', 'cpp', 'java']:
        try:
            # Run compilation with strict limits
            proc = subprocess.run(
                compile_cmd,
                capture_output=True,
                text=True,
                timeout=10, # Compilation timeout
            )
            if proc.returncode != 0:
                return {
                    'success': False,
                    'error': f"Compilation Error:\n{proc.stderr}",
                    'output': ''
                }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': "Compilation timed out", 'output': ''}
        except Exception as e:
            return {'success': False, 'error': f"Compilation failed: {str(e)}", 'output': ''}

    # Execution Step
    start_time = time.time()
    try:
        # Popen allows us to pipe input and set pre-exec limits
        process = subprocess.Popen(
            run_cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            preexec_fn=set_limits # Apply resource limits to the child process
        )
        
        stdout, stderr = process.communicate(input=test_input, timeout=5) # Execution timeout
        
        return {
            'success': process.returncode == 0,
            'output': stdout,
            'error': stderr if process.returncode != 0 else '',
            'execution_time': int((time.time() - start_time) * 1000)
        }
        
    except subprocess.TimeoutExpired:
        process.kill()
        return {
            'success': False, 
            'error': "Time Limit Exceeded (5s)", 
            'output': '',
            'execution_time': 5000
        }
    except Exception as e:
        return {
            'success': False, 
            'error': f"Runtime Error: {str(e)}", 
            'output': '',
            'execution_time': int((time.time() - start_time) * 1000)
        }

if __name__ == "__main__":
    try:
        # Input expected in JSON format from stdin
        data = sys.stdin.read()
        if not data:
            print(json.dumps({'success': False, 'error': "No input data provided"}))
            sys.exit(1)
            
        input_data = json.loads(data)
        code = input_data.get('code', '')
        language = input_data.get('language', 'python').lower()
        test_input = input_data.get('input', '')
        
        result = compile_and_run(language, code, test_input)
        print(json.dumps(result))
        
    except Exception as e:
        print(json.dumps({'success': False, 'error': f"System Error: {str(e)}"}))
