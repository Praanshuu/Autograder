import os
import sys
import django

# Add backend directory to path so it can find 'autograder' module
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from submissions.models import SubmissionAttempt, AssignmentProgress
from django.contrib.auth import get_user_model

User = get_user_model()
print("--- Checking Users ---")
for u in User.objects.all():
    print(f"User: {u.username} (ID: {u.id}, Role: {u.role})")

print("\n--- Checking Submission Attempts ---")
attempts = SubmissionAttempt.objects.all().order_by('-created_at')
if not attempts.exists():
    print("No submission attempts found.")
else:
    for attempt in attempts[:5]:
        print(f"ID: {attempt.id}")
        print(f"Student: {attempt.student.username}")
        print(f"Question ID: {attempt.assignment_question.id}")
        print(f"Status: {attempt.status}")
        print(f"Created: {attempt.created_at}")
        # If we store code in a blob ref or text, check it.
        # The model has code_blob_ref.
        print(f"Code Blob Ref: {attempt.code_blob_ref}") 
        # Note: If code was executed, there might be TestResults
        print(f"Test Results: {attempt.test_results.count()}")
        print("-" * 20)

print("\n--- Checking Assignment Progress ---")
progress = AssignmentProgress.objects.all().order_by('-last_updated')
if not progress.exists():
    print("No progress found.")
else:
    for p in progress[:5]:
        print(f"Student: {p.student.username}")
        print(f"Question ID: {p.assignment_question.id}")
        print(f"Current Code Snippet: {p.current_code[:50]}..." if p.current_code else "No code")
        print(f"Time Spent: {p.time_spent}")
        print(f"Started At: {p.started_at}")
        print("-" * 20)
