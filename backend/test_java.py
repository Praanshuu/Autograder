import os
import django
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from submissions.services import execute_code

code = """
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!") // missing semicolon
    }
}
"""

test_cases = [
    {"input": "", "expected_output": "Hello, World!"}
]

res = execute_code(code, 'java', test_cases, {})
print("FINAL RESULT =", res)
