import os
import sys
import django
from django.utils import timezone

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from classes.models import Class, Module
from assignments.models import Assignment, Question, AssignmentQuestion

def seed():
    User = get_user_model()
    
    # 1. Create Teacher
    print("Creating Teacher...")
    teacher, _ = User.objects.get_or_create(
        username='PervySage', 
        defaults={
            'email': 'jiraiya@leaf.co', 
            'role': 'teacher',
            'first_name': 'Jiraiya',
            'last_name': 'Sensei'
        }
    )
    teacher.set_password('#Dattebayo!')
    teacher.save()
    print(f"Teacher {teacher.username} ready.")

    # 2. Find Classroom
    # We pick the first classroom available, or create one if none exist.
    classroom = Class.objects.first()
    if not classroom:
        print("No classroom found. Creating 'Ninja Academy'.")
        classroom = Class.objects.create(
            name="Ninja Academy", 
            owner=teacher, 
            section="NINJA101"
        )
    else:
        print(f"Using existing classroom: {classroom.name}")

    # 3. Create Module
    print("Creating Module...")
    module, _ = Module.objects.get_or_create(
        class_obj=classroom, 
        title="Toad Sannin Training", 
        defaults={'order_index': 1}
    )

    # 4. Create Assignment
    print("Creating Assignment...")
    assignment, created = Assignment.objects.get_or_create(
        module=module,
        title="Sage Mode Mastery",
        type='assignment',
        defaults={
            'description': "Prove your worth to learn Senjutsu.",
            'is_published': True,
            'due_date': timezone.now() + timezone.timedelta(days=7),
            'mode': 'practice',
            'difficulty': 'Hard',
            'points_total': 300
        }
    )
    
    if not created:
        print("Assignment already exists. Skipping creation.")
        # We assume questions exist if assignment exists, but let's just return to avoid dups
        # Or we can check questions count
    else:
        # 5. Create Questions
        print("Creating Questions...")
        
        # Q1: Palindrome (Medium)
        q1 = Question.objects.create(
            title="Scroll Decryption",
            slug="scroll-decryption",
            description="Write a function `is_palindrome(s)` that returns `True` if the scroll text `s` reads the same forwards and backwards, `False` otherwise.",
            starter_code="def is_palindrome(s):\n    # Your code here\n    pass",
            test_cases=[
                {"input": "\"madam\"", "output": "True"},
                {"input": "\"racecar\"", "output": "True"},
                {"input": "\"ninja\"", "output": "False"}
            ],
            created_by=teacher
        )

        # Q2: Fibonacci (Harder recursion)
        q2 = Question.objects.create(
            title="Chakra Flow Steps",
            slug="chakra-steps",
            description="A ninja can jump 1 or 2 steps at a time. Write `climb_stairs(n)` to count how many distinct ways to climb `n` steps. (Hint: Fibonacci)",
            starter_code="def climb_stairs(n):\n    # Your code here\n    pass",
            test_cases=[
                {"input": "2", "output": "2"},
                {"input": "3", "output": "3"},
                {"input": "5", "output": "8"}
            ],
            created_by=teacher
        )

        # Q3: Target Sum (Logic)
        q3 = Question.objects.create(
            title="Target Lock",
            slug="target-lock",
            description="Given a list of nums and a target, return `True` if any two numbers sum to target. `has_pair_sum(nums, target)`.",
            starter_code="def has_pair_sum(nums, target):\n    # nums is a list of integers\n    pass",
            test_cases=[
                {"input": "[10, 15, 3, 7], 17", "output": "True"},
                {"input": "[1, 2, 3], 9", "output": "False"}
            ],
            created_by=teacher
        )

        # Link Questions
        AssignmentQuestion.objects.create(assignment=assignment, question=q1, order=1, custom_points=100)
        AssignmentQuestion.objects.create(assignment=assignment, question=q2, order=2, custom_points=100)
        AssignmentQuestion.objects.create(assignment=assignment, question=q3, order=3, custom_points=100)

        print("Assignment 'Sage Mode Mastery' created successfully with 3 questions!")
        
    print(f"To see it, refresh the student dashboard. Class: {classroom.name}")

if __name__ == '__main__':
    seed()
