
import sys
import os
sys.path.append(os.getcwd())
try:
    from backend.code_executor.python_runner import CodeExecutor
    
    runner = CodeExecutor()
    code = "print('Hello Sandbox')"
    inputs = [""]
    results = runner.execute('python', code, inputs)
    print("Execution Result:", results)

except Exception as e:
    print(f"Error: {e}")
