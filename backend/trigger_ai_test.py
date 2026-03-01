import os
import django
import sys

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from assignments.models import Assignment
from submissions.models import AIAnalysisTask, SubmissionAttempt
from submissions.tasks import analyze_assignment_ai_task

# Find an assignment that has submissions
assignments_with_subs = SubmissionAttempt.objects.values_list('assignment_question__assignment_id', flat=True).distinct()
if assignments_with_subs:
    a_id = assignments_with_subs[0]
    assignment = Assignment.objects.filter(id=a_id).first()
    
    if assignment:
        print(f"Triggering AI Analysis for Assignment: {assignment.title}")
        
        # Create the task record
        ai_task = AIAnalysisTask.objects.create(
            assignment=assignment,
            status='pending',
            total_batches=assignment.assignmentquestion_set.count()
        )
        
        # Dispatch the celery task
        analyze_assignment_ai_task.delay(str(assignment.id), str(ai_task.id))
        print("AI Analysis dispatched. You can check the Celery logs or wait a minute for it to appear.")
    else:
        print("No valid assignment found.")
else:
    print("No assignments with submissions found to trigger AI Analysis.")
