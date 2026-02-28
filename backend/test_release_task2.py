import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.utils import timezone
from datetime import timedelta
from assignments.models import Assignment
from gamification.models import PracticeQuestionLibrary

# Pick a published exam that has questions
exam = Assignment.objects.filter(mode='exam', is_published=True).first()
if not exam:
    print("No published exam found. Checking any exam...")
    exam = Assignment.objects.filter(mode='exam').first()
    if not exam:
        print("No exams at all! Create one via the UI first.")
        exit(0)

print(f"Using exam: '{exam.title}' (due_date: {exam.due_date}, questions_released: {exam.questions_released})")
print(f"Questions on this exam: {exam.assignmentquestion_set.count()}")

# Simulate an expired exam by backdating its due_date
original_due = exam.due_date
exam.due_date = timezone.now() - timedelta(hours=1)
exam.questions_released = False
exam.save(update_fields=['due_date', 'questions_released'])

pql_count_before = PracticeQuestionLibrary.objects.count()
print(f"\nPractice Library Count (before): {pql_count_before}")

# Run the task
from assignments.tasks import release_expired_exam_questions
result = release_expired_exam_questions()

pql_count_after = PracticeQuestionLibrary.objects.count()
print(f"\n--- Task Result ---")
print(f"Exams processed: {result['exams_processed']}")
print(f"Questions newly released: {result['questions_released']}")
print(f"Practice Library Count (after): {pql_count_after}")
print(f"Exam questions_released flag: {Assignment.objects.get(id=exam.id).questions_released}")

# Restore original due date
exam.due_date = original_due
exam.save(update_fields=['due_date'])
print(f"\nRestored exam due_date to: {original_due}")
