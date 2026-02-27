import os
import django
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from submissions.services import execute_code

code = """
def twoSum(nums, target):
    return 1 / 0  # ZeroDivisionError
"""

test_cases = [
    {"input": "[2,7,11,15]\n9", "expected_output": "[0,1]"}
]

config = {"execution_mode": {"type": "function", "entry_point": "twoSum"}}

res = execute_code(code, 'python', test_cases, config)
print("FINAL RESULT =", res)
