import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.utils import timezone
from assignments.models import Assignment
from gamification.models import PracticeQuestionLibrary

# Create a fake past-due exam to test against
print("--- Test Setup ---")
print(f"Total Assignments: {Assignment.objects.count()}")
print(f"Exam Assignments: {Assignment.objects.filter(mode='exam').count()}")
print(f"Practice Library Count (before): {PracticeQuestionLibrary.objects.count()}")

# Run the task directly (not via celery worker, just call the function)
from assignments.tasks import release_expired_exam_questions
result = release_expired_exam_questions()

print(f"\n--- Task Result ---")
print(f"Exams processed: {result['exams_processed']}")
print(f"Questions released: {result['questions_released']}")
print(f"Practice Library Count (after): {PracticeQuestionLibrary.objects.count()}")
