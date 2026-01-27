
import sys
import os
sys.path.append(os.getcwd())
try:
    from backend.code_executor.python_runner import CodeExecutor
    
    # Add Mingw to PATH
    mingw_path = r"C:\msys64\mingw64\bin"
    os.environ['PATH'] = mingw_path + os.pathsep + os.environ['PATH']
    
    runner = CodeExecutor()
    code = "#include <iostream>\nusing namespace std;\nint main() { cout << \"Hello GCC\"; return 0; }"
    inputs = [""]
    
    results = runner.execute('cpp', code, inputs)
    
    print("Status:", results['status'])
    print("Message:", results['message'])
    print("Outputs:", results['outputs'])

except Exception as e:
    print(f"Error: {e}")
