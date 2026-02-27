import os
import django
import sys
import uuid
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from submissions.services import execute_code

code = """
for i in range n: # INTENTIONAL SYNTAX ERROR
    pass
"""

test_cases = [
    {"input": "5", "expected_output": "10"}
]

res = execute_code(code, 'python', test_cases)
print("FINAL EXECUTE_CODE BACKEND RES =", res)
