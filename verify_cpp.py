
import sys
import os
sys.path.append(os.getcwd())
try:
    from backend.code_executor.python_runner import CodeExecutor
    
    runner = CodeExecutor()
    code = "#include <iostream>\\nusing namespace std;\\nint main() { cout << \"Hello GCC\"; return 0; }"
    inputs = [""]
    # We need to ensure PATH contains gcc
    os.environ['PATH'] += r";C:\msys64\mingw64\bin"
    
    results = runner.execute('cpp', code, inputs)
    print("Execution Result:", results)

except Exception as e:
    print(f"Error: {e}")
