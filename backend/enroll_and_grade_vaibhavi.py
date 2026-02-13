import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from classes.models import Class, Enrollment
from assignments.models import Assignment, AssignmentQuestion
from submissions.models import SubmissionAttempt

User = get_user_model()

def run():
    # 1. Get User
    try:
        student = User.objects.get(username='vaibhavi')
    except User.DoesNotExist:
        print("User 'vaibhavi' not found. Please run find_vaibhavi.py first.")
        return

    # 2. Get Class and Enroll
    class_name = 'CSL100-EE'
    try:
        cls = Class.objects.get(name=class_name)
    except Class.DoesNotExist:
        print(f"Class '{class_name}' not found.")
        return

    enrollment, created = Enrollment.objects.get_or_create(
        class_obj=cls,
        user=student,
        defaults={'role': 'student'}
    )
    if created:
        print(f"Enrolled vaibhavi in {class_name}")
    else:
        print(f"Vaibhavi already enrolled in {class_name}")

    # 3. Get Assignment
    assign_id = 'fdeed1fb-a225-43f3-995f-7d7b2521de26'
    try:
        assignment = Assignment.objects.get(id=assign_id)
    except Assignment.DoesNotExist:
        print("Assignment not found")
        return

    # 4. Create Submissions
    aqs = assignment.assignmentquestion_set.all()
    
    print("Creating submissions...")
    count = 0
    for aq in aqs:
        q = aq.question
        tags = q.tags or []
        
        # Scoring Logic for Demo
        # Strong in Strings, Recursion, Dictionaries (100%)
        # Weak in Lists, Nested Data (0% or 50%)
        # Mixed in others
        
        status = 'fail'
        
        if any(t in ['Strings & String Operations', 'Recursion', 'Dictionaries'] for t in tags):
            status = 'success'
        elif any(t in ['Python Basics & Control Flow'] for t in tags):
             # 80% chance success
             status = 'success' if random.random() > 0.2 else 'fail'
        elif any(t in ['Lists & List Operations', 'Nested Data Structures'] for t in tags):
            status = 'fail'
        else:
            status = 'success' if random.random() > 0.5 else 'fail'
            
        # Create Submission
        # Check if exists first to avoid duplicates if run multiple times
        existing = SubmissionAttempt.objects.filter(student=student, assignment_question=aq).exists()
        if not existing:
            SubmissionAttempt.objects.create(
                student=student,
                assignment_question=aq,
                status=status,
                attempt_number=1,
                manual_score=100 if status == 'success' else 0
            )
            print(f"Submitted Q: {q.title} -> {status}")
            count += 1
        else:
            # print(f"Skipping Q: {q.title} (Already submitted)")
            pass
            
    print(f"Total Submissions Created: {count}")

if __name__ == '__main__':
    run()
