import os
import django
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from submissions.services import execute_code

code = """
for i in range n:
  pass
"""

test_cases = [
    {"input": "5", "expected_output": "10"}
]

# Provide NO entry_point so it falls back to _run_python_test_case loop
config = {"execution_mode": {"type": "program"}}

res = execute_code(code, 'python', test_cases, config)
print("FINAL RESULT =", res)
