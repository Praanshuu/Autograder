import os
import django
import sys

# Change to the backend directory first so that relative paths and module resolution work properly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')

django.setup()

from submissions.services import execute_code

code = """
def fizzbuzz(n):
lis = []
for i in range n:
  pass
"""

test_cases = [
    {"input": "5", "expected_output": "[1, 2, 'Fizz', 4, 'Buzz']"}
]

config = {"entry_point": "fizzbuzz", "execution_mode": {"type": "function"}, "input_types": ["int"]}

res = execute_code(code, 'python', test_cases, config)
print("FINAL RESULT =", res)
