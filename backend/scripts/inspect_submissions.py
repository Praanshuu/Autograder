
import os
import django
import sys

# Add project root to path
sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from submissions.models import SubmissionAttempt
from assignments.models import Assignment

assignment_id = 'cb9b5840-c1ac-42b5-ac0c-b49ab7e0cf4e'

try:
    assignment = Assignment.objects.get(id=assignment_id)
    print(f"Assignment: {assignment.title} (Mode: {assignment.mode})")
except Assignment.DoesNotExist:
    print("Assignment not found")
    sys.exit(1)

attempts = SubmissionAttempt.objects.filter(assignment_question__assignment_id=assignment_id)
print(f"Total Attempts: {attempts.count()}")

for attempt in attempts:
    print(f"- Student: {attempt.student.username}, Status: {attempt.status}, Attempt #: {attempt.attempt_number}")

