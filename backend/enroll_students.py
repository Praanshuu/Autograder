import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autograder.settings")
django.setup()

from assignments.models import Assignment
from classes.models import Enrollment
from submissions.models import SubmissionAttempt
from django.contrib.auth import get_user_model

User = get_user_model()
ASSIGNMENT_ID = "1474b14a-7944-4486-a21e-a85420c9710c"

def enroll():
    print(f"Enrolling students for Assignment ID: {ASSIGNMENT_ID}")
    
    try:
        assignment = Assignment.objects.get(id=ASSIGNMENT_ID)
    except Assignment.DoesNotExist:
        print("Assignment not found.")
        return

    class_obj = assignment.module.class_obj
    print(f"Target Class: {class_obj.name}")

    # Get distinct students who have submissions
    student_ids = SubmissionAttempt.objects.filter(
        assignment_question__assignment_id=ASSIGNMENT_ID
    ).values_list('student_id', flat=True).distinct()
    
    print(f"Found {len(student_ids)} students with submissions.")
    
    count = 0
    for student_id in student_ids:
        # Check/Create enrollment
        user = User.objects.get(id=student_id)
        obj, created = Enrollment.objects.get_or_create(
            class_obj=class_obj,
            user=user,
            defaults={'role': 'student'}
        )
        if created:
            count += 1
            
    print(f"Enrolled {count} new students.")
    print(f"Total Enrollments: {Enrollment.objects.filter(class_obj=class_obj, role='student').count()}")

if __name__ == "__main__":
    enroll()
