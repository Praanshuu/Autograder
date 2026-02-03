from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models
from datetime import timedelta
import random

from classes.models import Class, Module, Enrollment
from assignments.models import Assignment, Question, AssignmentQuestion, ContentItem
from submissions.models import SubmissionAttempt, TestResult, AssignmentProgress, GradebookEntry
from gamification.models import (
    PracticeQuestion, UserPoints, Achievement, UserAchievement, 
    PracticeSubmission, PracticeProgress, StudentAnalytics
)

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate database with comprehensive sample data for testing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before populating',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            self.clear_data()

        self.stdout.write('Creating sample data...')
        
        # Create users
        users = self.create_users()
        
        # Create classes and modules
        classes = self.create_classes(users)
        
        # Create questions and assignments
        questions = self.create_questions(users)
        assignments = self.create_assignments(classes, questions, users)
        
        # Create practice questions
        practice_questions = self.create_practice_questions(users)
        
        # Create achievements
        achievements = self.create_achievements()
        
        # Create submissions and progress
        self.create_submissions_and_progress(users, assignments, practice_questions)
        
        # Create user points and achievements
        self.create_user_points_and_achievements(users, achievements)
        
        # Create analytics data
        self.create_analytics_data(users)

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data')
        )

    def clear_data(self):
        """Clear existing data"""
        models_to_clear = [
            TestResult, SubmissionAttempt, AssignmentProgress, GradebookEntry,
            PracticeSubmission, PracticeProgress, UserAchievement,
            AssignmentQuestion, Assignment, Question, ContentItem,
            PracticeQuestion, Achievement, UserPoints, StudentAnalytics,
            Enrollment, Module, Class
        ]
        
        for model in models_to_clear:
            try:
                model.objects.all().delete()
                self.stdout.write(f'Cleared {model.__name__}')
            except Exception as e:
                self.stdout.write(f'Warning: Could not clear {model.__name__}: {e}')

    def create_users(self):
        """Create sample users"""
        users = {}
        
        # Create admin
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin.set_password('admin123')
            admin.save()
        users['admin'] = admin

        # Create teachers
        teacher_data = [
            ('prof_smith', 'John', 'Smith', 'john.smith@university.edu'),
            ('prof_johnson', 'Sarah', 'Johnson', 'sarah.johnson@university.edu'),
        ]
        
        for username, first_name, last_name, email in teacher_data:
            teacher, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'role': 'teacher'
                }
            )
            if created:
                teacher.set_password('teacher123')
                teacher.save()
            users[username] = teacher

        # Create students
        student_data = [
            ('alice_codes', 'Alice', 'Johnson', 'alice.johnson@student.edu'),
            ('bob_dev', 'Bob', 'Smith', 'bob.smith@student.edu'),
            ('charlie_py', 'Charlie', 'Brown', 'charlie.brown@student.edu'),
            ('diana_js', 'Diana', 'Wilson', 'diana.wilson@student.edu'),
            ('eve_algo', 'Eve', 'Davis', 'eve.davis@student.edu'),
            ('frank_code', 'Frank', 'Miller', 'frank.miller@student.edu'),
            ('grace_dev', 'Grace', 'Taylor', 'grace.taylor@student.edu'),
            ('henry_py', 'Henry', 'Anderson', 'henry.anderson@student.edu'),
        ]
        
        for username, first_name, last_name, email in student_data:
            student, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'role': 'student'
                }
            )
            if created:
                student.set_password('student123')
                student.save()
            users[username] = student

        return users

    def create_classes(self, users):
        """Create sample classes"""
        classes = []
        
        class_data = [
            ('CS 101', 'Introduction to Programming', 'prof_smith'),
            ('CS 201', 'Data Structures and Algorithms', 'prof_johnson'),
            ('CS 301', 'Advanced Programming', 'prof_smith'),
        ]
        
        for name, section, teacher_username in class_data:
            teacher = users[teacher_username]
            class_obj = Class.objects.create(
                name=name,
                section=section,
                owner=teacher
            )
            
            # Create modules for each class
            module_names = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
            for i, module_name in enumerate(module_names):
                Module.objects.create(
                    class_obj=class_obj,
                    title=module_name,
                    order_index=i
                )
            
            # Enroll students
            student_usernames = ['alice_codes', 'bob_dev', 'charlie_py', 'diana_js', 
                               'eve_algo', 'frank_code', 'grace_dev', 'henry_py']
            for student_username in student_usernames:
                if student_username in users:
                    Enrollment.objects.create(
                        class_obj=class_obj,
                        user=users[student_username],
                        role='student'
                    )
            
            classes.append(class_obj)
        
        return classes

    def create_questions(self, users):
        """Create sample questions"""
        questions = []
        
        question_data = [
            {
                'title': 'Hello World',
                'slug': 'hello-world',
                'description': 'Write a program that prints "Hello, World!" to the console.',
                'starter_code': 'print("Hello, World!")',
                'test_cases': [
                    {'input': '', 'expected_output': 'Hello, World!'}
                ]
            },
            {
                'title': 'Sum Two Numbers',
                'slug': 'sum-two-numbers',
                'description': 'Write a function that takes two numbers and returns their sum.',
                'starter_code': 'def add_numbers(a, b):\n    # Your code here\n    pass',
                'test_cases': [
                    {'input': '5 3', 'expected_output': '8'},
                    {'input': '10 -2', 'expected_output': '8'},
                    {'input': '0 0', 'expected_output': '0'}
                ]
            },
            {
                'title': 'Factorial Calculator',
                'slug': 'factorial-calculator',
                'description': 'Write a function that calculates the factorial of a number.',
                'starter_code': 'def factorial(n):\n    # Your code here\n    pass',
                'test_cases': [
                    {'input': '5', 'expected_output': '120'},
                    {'input': '0', 'expected_output': '1'},
                    {'input': '3', 'expected_output': '6'}
                ]
            },
            {
                'title': 'Fibonacci Sequence',
                'slug': 'fibonacci-sequence',
                'description': 'Write a function that returns the nth Fibonacci number.',
                'starter_code': 'def fibonacci(n):\n    # Your code here\n    pass',
                'test_cases': [
                    {'input': '0', 'expected_output': '0'},
                    {'input': '1', 'expected_output': '1'},
                    {'input': '5', 'expected_output': '5'},
                    {'input': '10', 'expected_output': '55'}
                ]
            }
        ]
        
        for data in question_data:
            question, created = Question.objects.get_or_create(
                slug=data['slug'],
                defaults={
                    'title': data['title'],
                    'description': data['description'],
                    'starter_code': data['starter_code'],
                    'test_cases': data['test_cases'],
                    'created_by': users['prof_smith']
                }
            )
            questions.append(question)
        
        return questions

    def create_assignments(self, classes, questions, users):
        """Create sample assignments"""
        assignments = []
        
        for class_obj in classes:
            module = class_obj.modules.first()
            
            # Create assignment
            assignment = Assignment.objects.create(
                module=module,
                type='assignment',
                title=f'{class_obj.name} - Basic Programming',
                description='Practice basic programming concepts',
                mode='practice',
                difficulty='Easy',
                points_total=100,
                due_date=timezone.now() + timedelta(days=7),
                is_published=True
            )
            
            # Add questions to assignment
            for i, question in enumerate(questions[:2]):  # Add first 2 questions
                AssignmentQuestion.objects.create(
                    assignment=assignment,
                    question=question,
                    order=i,
                    custom_points=50
                )
            
            assignments.append(assignment)
        
        return assignments

    def create_practice_questions(self, users):
        """Create sample practice questions"""
        practice_questions = []
        
        practice_data = [
            {
                'title': 'Array Sum',
                'description': 'Calculate the sum of all elements in an array.',
                'difficulty': 'easy',
                'category': 'Arrays',
                'point_value': 100,
                'test_cases': [
                    {'input': '[1, 2, 3, 4, 5]', 'expected_output': '15'},
                    {'input': '[]', 'expected_output': '0'},
                    {'input': '[10]', 'expected_output': '10'}
                ]
            },
            {
                'title': 'String Reversal',
                'description': 'Reverse a given string.',
                'difficulty': 'easy',
                'category': 'Strings',
                'point_value': 100,
                'test_cases': [
                    {'input': 'hello', 'expected_output': 'olleh'},
                    {'input': 'world', 'expected_output': 'dlrow'},
                    {'input': 'a', 'expected_output': 'a'}
                ]
            },
            {
                'title': 'Binary Search',
                'description': 'Implement binary search algorithm.',
                'difficulty': 'medium',
                'category': 'Algorithms',
                'point_value': 150,
                'test_cases': [
                    {'input': '[1,2,3,4,5] 3', 'expected_output': '2'},
                    {'input': '[1,2,3,4,5] 6', 'expected_output': '-1'},
                    {'input': '[1] 1', 'expected_output': '0'}
                ]
            },
            {
                'title': 'Tree Traversal',
                'description': 'Implement in-order tree traversal.',
                'difficulty': 'hard',
                'category': 'Data Structures',
                'point_value': 200,
                'test_cases': [
                    {'input': '[1,null,2,3]', 'expected_output': '[1,3,2]'},
                    {'input': '[]', 'expected_output': '[]'},
                    {'input': '[1]', 'expected_output': '[1]'}
                ]
            }
        ]
        
        for data in practice_data:
            pq, created = PracticeQuestion.objects.get_or_create(
                title=data['title'],
                defaults={
                    'description': data['description'],
                    'difficulty': data['difficulty'],
                    'category': data['category'],
                    'point_value': data['point_value'],
                    'test_cases': data['test_cases'],
                    'created_by': users['prof_smith']
                }
            )
            practice_questions.append(pq)
        
        return practice_questions

    def create_achievements(self):
        """Create sample achievements"""
        achievements = []
        
        achievement_data = [
            {
                'name': 'First Steps',
                'description': 'Complete your first practice question',
                'icon': '🎯',
                'badge_type': 'first_completion',
                'rarity': 'common',
                'criteria': {'type': 'first_practice_completion'}
            },
            {
                'name': 'Speed Demon',
                'description': 'Solve a problem in under 5 minutes',
                'icon': '⚡',
                'badge_type': 'speed',
                'rarity': 'uncommon',
                'criteria': {'type': 'speed_completion', 'time_limit': 300}
            },
            {
                'name': 'Perfect Score',
                'description': 'Get 100% on an assignment',
                'icon': '⭐',
                'badge_type': 'perfect_score',
                'rarity': 'rare',
                'criteria': {'type': 'perfect_assignment_score'}
            },
            {
                'name': 'Streak Master',
                'description': 'Maintain a 7-day coding streak',
                'icon': '🔥',
                'badge_type': 'streak',
                'rarity': 'rare',
                'criteria': {'type': 'daily_streak', 'days': 7}
            }
        ]
        
        for data in achievement_data:
            achievement, created = Achievement.objects.get_or_create(
                name=data['name'],
                defaults={
                    'description': data['description'],
                    'icon': data['icon'],
                    'badge_type': data['badge_type'],
                    'rarity': data['rarity'],
                    'criteria': data['criteria']
                }
            )
            achievements.append(achievement)
        
        return achievements

    def create_submissions_and_progress(self, users, assignments, practice_questions):
        """Create sample submissions and progress"""
        student_users = [u for u in users.values() if u.role == 'student']
        
        # Create assignment submissions
        for assignment in assignments:
            for student in student_users[:5]:  # First 5 students
                for aq in assignment.assignmentquestion_set.all():
                    # Create progress
                    progress = AssignmentProgress.objects.create(
                        student=student,
                        assignment_question=aq,
                        current_code='print("Hello, World!")',
                        time_spent=random.randint(300, 1800),  # 5-30 minutes
                        started_at=timezone.now() - timedelta(days=random.randint(1, 7))
                    )
                    
                    # Create submission
                    attempt = SubmissionAttempt.objects.create(
                        student=student,
                        assignment_question=aq,
                        attempt_number=1,
                        status='success' if random.random() > 0.2 else 'fail',
                        source_code='print("Hello, World!")',
                        created_at=timezone.now() - timedelta(days=random.randint(0, 5))
                    )
                    
                    # Create test results
                    for i, test_case in enumerate(aq.question.test_cases):
                        TestResult.objects.create(
                            attempt=attempt,
                            test_case_id=str(i),
                            status='pass' if attempt.status == 'success' else 'fail',
                            score=1.0 if attempt.status == 'success' else 0.0,
                            actual_output=test_case.get('expected_output', '') if attempt.status == 'success' else 'Wrong output'
                        )
                
                # Create gradebook entry
                GradebookEntry.objects.create(
                    student=student,
                    content_item=assignment,
                    final_score=random.randint(70, 100),
                    points_earned=random.randint(50, 100),
                    status='graded'
                )
        
        # Create practice submissions
        for pq in practice_questions:
            for student in student_users:
                if random.random() > 0.3:  # 70% chance student attempted
                    # Create progress
                    is_completed = random.random() > 0.4
                    first_attempt = timezone.now() - timedelta(days=random.randint(1, 30))
                    completed_at = timezone.now() - timedelta(days=random.randint(0, 15)) if is_completed else None
                    
                    progress, created = PracticeProgress.objects.get_or_create(
                        student=student,
                        practice_question=pq,
                        defaults={
                            'is_completed': is_completed,
                            'attempts_count': random.randint(1, 3),
                            'best_score': random.randint(60, 100),
                            'time_spent': random.randint(600, 3600),  # 10-60 minutes
                            'first_attempt_at': first_attempt,
                            'completed_at': completed_at
                        }
                    )
                    
                    # Create submission
                    PracticeSubmission.objects.create(
                        student=student,
                        practice_question=pq,
                        source_code='# Sample solution',
                        language='python',
                        status='success' if progress.is_completed else 'fail',
                        points_earned=pq.point_value if progress.is_completed else 0,
                        attempt_number=progress.attempts_count,
                        submitted_at=progress.first_attempt_at
                    )

    def create_user_points_and_achievements(self, users, achievements):
        """Create user points and achievements"""
        student_users = [u for u in users.values() if u.role == 'student']
        
        for student in student_users:
            # Calculate points based on submissions
            practice_points = PracticeSubmission.objects.filter(
                student=student, status='success'
            ).aggregate(total=models.Sum('points_earned'))['total'] or 0
            
            assignment_points = random.randint(200, 800)  # Mock assignment points
            
            UserPoints.objects.get_or_create(
                user=student,
                defaults={
                    'total_points': practice_points + assignment_points,
                    'practice_points': practice_points,
                    'assignment_points': assignment_points
                }
            )
            
            # Award some achievements randomly
            for achievement in achievements:
                if random.random() > 0.6:  # 40% chance of having each achievement
                    UserAchievement.objects.get_or_create(
                        user=student,
                        achievement=achievement,
                        defaults={
                            'earned_at': timezone.now() - timedelta(days=random.randint(1, 30))
                        }
                    )

    def create_analytics_data(self, users):
        """Create analytics data for students"""
        student_users = [u for u in users.values() if u.role == 'student']
        
        for student in student_users:
            completed_practice = PracticeProgress.objects.filter(
                student=student, is_completed=True
            ).count()
            
            completed_assignments = GradebookEntry.objects.filter(
                student=student
            ).count()
            
            avg_score = GradebookEntry.objects.filter(
                student=student
            ).aggregate(avg=models.Avg('final_score'))['avg'] or 0
            
            total_time = PracticeProgress.objects.filter(
                student=student
            ).aggregate(total=models.Sum('time_spent'))['total'] or 0
            
            StudentAnalytics.objects.get_or_create(
                student=student,
                defaults={
                    'total_practice_completed': completed_practice,
                    'total_assignments_completed': completed_assignments,
                    'average_score': avg_score,
                    'current_streak': random.randint(0, 10),
                    'longest_streak': random.randint(5, 20),
                    'total_time_spent': total_time // 60,  # Convert to minutes
                    'last_activity': timezone.now() - timedelta(days=random.randint(0, 3)),
                    'concept_mastery': {
                        'Arrays': random.randint(60, 95),
                        'Loops': random.randint(60, 95),
                        'Functions': random.randint(60, 95),
                        'Recursion': random.randint(40, 85),
                        'Data Structures': random.randint(50, 90),
                        'Algorithms': random.randint(45, 88)
                    }
                }
            )