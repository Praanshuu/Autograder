import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from assignments.models import Question
from gamification.models import PracticeQuestionLibrary

questions = Question.objects.all()
created_count = 0
for q in questions:
    try:
        obj, created = PracticeQuestionLibrary.objects.get_or_create(
            question=q,
            defaults={
                'is_public': True,
                'tags': q.tags
            }
        )
        if created:
            created_count += 1
    except Exception as e:
        print(f"Could not add {q.id}: {e}")

print(f"Successfully linked {created_count} existing questions to the Practice Library.")
