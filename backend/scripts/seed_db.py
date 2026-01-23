import os
import sys
import django
from datetime import timedelta
from django.utils import timezone

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from classes.models import Class, Module
from assignments.models import Assignment, Question, AssignmentQuestion, ContentItem

User = get_user_model()

def run():
    print("Seeding database...")
    
    # 1. Create Users
    admin, _ = User.objects.get_or_create(username='admin', defaults={'email': 'admin@example.com', 'role': 'admin'})
    admin.set_password('admin')
    admin.is_staff = True
    admin.is_superuser = True
    admin.save()
    
    teacher, _ = User.objects.get_or_create(username='teacher', defaults={'email': 'teacher@example.com', 'role': 'teacher'})
    teacher.set_password('teacher')
    teacher.save()
    
    student, _ = User.objects.get_or_create(username='student', defaults={'email': 'student@example.com', 'role': 'student'})
    student.set_password('student')
    student.save()
    
    print(f"Users created: admin, teacher, student")
    
    # 2. Create Class
    demo_class, created = Class.objects.get_or_create(
        name='CS101: Intro to Python',
        defaults={
            'section': 'Fall 2024',
            'owner': teacher,
            'settings': {'theme': 'dark'}
        }
    )
    if created:
        print(f"Class created: {demo_class}")
    
    # 3. Create Module
    module, created = Module.objects.get_or_create(
        title='Week 1: Basics',
        class_obj=demo_class,
        defaults={'order_index': 0}
    )
    
    # 4. Create Question
    question, created = Question.objects.get_or_create(
        slug='sum-of-two',
        defaults={
            'title': 'Sum of Two Numbers',
            'description': 'Write a function that returns the sum of a and b.',
            'created_by': teacher,
            'test_cases': [
                {'input': '1\n2', 'output': '3', 'points': 5, 'hidden': False},
                {'input': '10\n20', 'output': '30', 'points': 5, 'hidden': True}
            ]
        }
    )
    
    # 5. Create Assignment
    assignment, created = Assignment.objects.get_or_create(
        title='Homework 1',
        module=module, # ContentItem field
        defaults={
            'description': 'Solve the basic problems.',
            'type': 'assignment',
            'due_date': timezone.now() + timedelta(days=7),
            'is_published': True,
            'mode': 'practice',
            'points_total': 100
        }
    )
    
    # Add Question to Assignment
    if created:
        AssignmentQuestion.objects.create(
            assignment=assignment,
            question=question,
            order=0,
            custom_points=10
        )
        print(f"Assignment created: {assignment} with question {question}")

if __name__ == '__main__':
    run()
