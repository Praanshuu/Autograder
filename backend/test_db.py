import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from assignments.models import Question
from gamification.models import PracticeQuestionLibrary

qs = Question.objects.all()
print("All Questions:", qs.count())
for q in qs[:5]:
    print(f"ID: {q.id}, Type: {q.question_type}, Title: {q.title}")

pqs = PracticeQuestionLibrary.objects.all()
print("\nPractice Questions:", pqs.count())
for pq in pqs[:5]:
    print(f"ID: {pq.id}, Q_ID: {pq.question.id}, Q_Type: {pq.question.question_type}")

print("\nMCQ Questions count:", Question.objects.filter(question_type='mcq').count())
print("MCQ Practice Questions count:", PracticeQuestionLibrary.objects.filter(question__question_type='mcq').count())

