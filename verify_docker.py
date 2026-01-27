import os
import sys
import django
import json
import time

# Setup Django environment
sys.path.append(os.path.join(os.getcwd(), 'backend'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autograder.settings")
django.setup()

from backend.code_executor.docker_service import get_docker_executor

def run_test(name, code, language, input_val, expected_output=None):
    print(f"\n--- Testing {name} ({language}) ---")
    executor = get_docker_executor()
    
    start = time.time()
    # Execute code
    # We simulate a list of test cases (though we just run one here manually)
    result = executor.execute_code(code, language, input_val)
    duration = time.time() - start
    
    print(f"Time: {duration:.4f}s")
    print(f"Success: {result['success']}")
    print(f"Output: {result['output'].strip()}")
    print(f"Error: {result['error']}")
    
    if expected_output:
        if result['output'].strip() == expected_output:
            print("✅ Result Matches Expected")
        else:
            print(f"❌ Result Mismatch. Expected: '{expected_output}'")

def main():
    executor = get_docker_executor()
    if not executor.is_available():
        print("❌ Docker Executor is NOT available! Is Docker running?")
        return

    # 1. Python Simple
    run_test("Python Hello World", "print('Hello Docker')", "python", "", "Hello Docker")

    # 2. C++ Simple
    cpp_code = """
    #include <iostream>
    using namespace std;
    int main() {
        string s;
        cin >> s;
        cout << "Hello " << s << endl;
        return 0;
    }
    """
    run_test("C++ Input/Output", cpp_code, "cpp", "World", "Hello World")
    
    # 3. Python Memory Crash (Test Limits)
    print("\n--- Testing Memory Limit (Should Fail) ---")
    mem_code = "a = 'a' * (300 * 1024 * 1024) # 300MB"
    result = executor.execute_code(mem_code, "python", "")
    print(f"Success (Should be False): {result['success']}")
    print(f"Error: {result['error']}")
    
    if "Memory limit exceeded" in result['error'] or "Runtime Error" in result['error'] or result['success'] is False:
         print("✅ Memory Limit Enforced Correctly")
    else:
         print("❌ Memory Limit Failed (Container didn't crash?)")

if __name__ == "__main__":
    main()
