from django.db import migrations
from django.db.models import F

def populate_questions(apps, schema_editor):
    PracticeSubmission = apps.get_model('gamification', 'PracticeSubmission')
    PracticeProgress = apps.get_model('gamification', 'PracticeProgress')
    PracticeQuestionLibrary = apps.get_model('gamification', 'PracticeQuestionLibrary')

    # Efficiently update all records using F expressions since IDs are preserved
    PracticeSubmission.objects.all().update(question_id=F('practice_question_id'))
    PracticeProgress.objects.all().update(question_id=F('practice_question_id'))
    PracticeQuestionLibrary.objects.all().update(question_id=F('practice_question_id'))

def reverse_populate_questions(apps, schema_editor):
    PracticeSubmission = apps.get_model('gamification', 'PracticeSubmission')
    PracticeProgress = apps.get_model('gamification', 'PracticeProgress')
    PracticeQuestionLibrary = apps.get_model('gamification', 'PracticeQuestionLibrary')

    PracticeSubmission.objects.all().update(practice_question_id=F('question_id'))
    PracticeProgress.objects.all().update(practice_question_id=F('question_id'))
    PracticeQuestionLibrary.objects.all().update(practice_question_id=F('question_id'))


class Migration(migrations.Migration):
    dependencies = [
        ("gamification", "0004_alter_practicequestion_options_and_more"),
        ("assignments", "0005_auto_20260216_0625"), # Add dependency for Question models
    ]

    operations = [
        migrations.RunPython(populate_questions, reverse_populate_questions),
    ]
