from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from gamification.models import PracticeQuestion, PracticeQuestionLibrary

User = get_user_model()


class Command(BaseCommand):
    help = 'Set up sample practice questions for the gamification system'

    def handle(self, *args, **options):
        # Get or create a system user for creating practice questions
        system_user, created = User.objects.get_or_create(
            username='system',
            defaults={
                'email': 'system@example.com',
                'first_name': 'System',
                'last_name': 'User',
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True,
            }
        )

        practice_questions_data = [
            {
                'title': 'Hello World',
                'description': 'Write a function that returns "Hello, World!"',
                'difficulty': 'easy',
                'category': 'Basics',
                'point_value': 50,
                'starter_code': 'def hello_world():\n    # Your code here\n    pass',
                'test_cases': [
                    {
                        'id': 'test_1',
                        'input': '',
                        'expected_output': 'Hello, World!',
                        'is_hidden': False,
                        'points': 10
                    }
                ]
            },
            {
                'title': 'Sum Two Numbers',
                'description': 'Write a function that takes two numbers and returns their sum.',
                'difficulty': 'easy',
                'category': 'Basics',
                'point_value': 75,
                'starter_code': 'def sum_two_numbers(a, b):\n    # Your code here\n    pass',
                'test_cases': [
                    {
                        'id': 'test_1',
                        'input': '2, 3',
                        'expected_output': '5',
                        'is_hidden': False,
                        'points': 5
                    },
                    {
                        'id': 'test_2',
                        'input': '-1, 1',
                        'expected_output': '0',
                        'is_hidden': False,
                        'points': 5
                    }
                ]
            },
            {
                'title': 'Find Maximum',
                'description': 'Write a function that finds the maximum number in a list.',
                'difficulty': 'medium',
                'category': 'Arrays',
                'point_value': 100,
                'starter_code': 'def find_maximum(numbers):\n    # Your code here\n    pass',
                'test_cases': [
                    {
                        'id': 'test_1',
                        'input': '[1, 3, 2, 5, 4]',
                        'expected_output': '5',
                        'is_hidden': False,
                        'points': 5
                    },
                    {
                        'id': 'test_2',
                        'input': '[-1, -5, -2]',
                        'expected_output': '-1',
                        'is_hidden': False,
                        'points': 5
                    },
                    {
                        'id': 'test_3',
                        'input': '[10]',
                        'expected_output': '10',
                        'is_hidden': True,
                        'points': 5
                    }
                ]
            },
            {
                'title': 'Reverse String',
                'description': 'Write a function that reverses a string.',
                'difficulty': 'medium',
                'category': 'Strings',
                'point_value': 100,
                'starter_code': 'def reverse_string(s):\n    # Your code here\n    pass',
                'test_cases': [
                    {
                        'id': 'test_1',
                        'input': '"hello"',
                        'expected_output': '"olleh"',
                        'is_hidden': False,
                        'points': 5
                    },
                    {
                        'id': 'test_2',
                        'input': '"Python"',
                        'expected_output': '"nohtyP"',
                        'is_hidden': False,
                        'points': 5
                    }
                ]
            },
            {
                'title': 'Fibonacci Sequence',
                'description': 'Write a function that returns the nth Fibonacci number.',
                'difficulty': 'hard',
                'category': 'Recursion',
                'point_value': 150,
                'starter_code': 'def fibonacci(n):\n    # Your code here\n    pass',
                'test_cases': [
                    {
                        'id': 'test_1',
                        'input': '0',
                        'expected_output': '0',
                        'is_hidden': False,
                        'points': 5
                    },
                    {
                        'id': 'test_2',
                        'input': '1',
                        'expected_output': '1',
                        'is_hidden': False,
                        'points': 5
                    },
                    {
                        'id': 'test_3',
                        'input': '5',
                        'expected_output': '5',
                        'is_hidden': False,
                        'points': 5
                    },
                    {
                        'id': 'test_4',
                        'input': '10',
                        'expected_output': '55',
                        'is_hidden': True,
                        'points': 10
                    }
                ]
            },
            {
                'title': 'Binary Search',
                'description': 'Implement binary search to find an element in a sorted array.',
                'difficulty': 'hard',
                'category': 'Algorithms',
                'point_value': 200,
                'starter_code': 'def binary_search(arr, target):\n    # Your code here\n    pass',
                'test_cases': [
                    {
                        'id': 'test_1',
                        'input': '[1, 2, 3, 4, 5], 3',
                        'expected_output': '2',
                        'is_hidden': False,
                        'points': 10
                    },
                    {
                        'id': 'test_2',
                        'input': '[1, 2, 3, 4, 5], 6',
                        'expected_output': '-1',
                        'is_hidden': False,
                        'points': 10
                    },
                    {
                        'id': 'test_3',
                        'input': '[1, 3, 5, 7, 9, 11], 7',
                        'expected_output': '3',
                        'is_hidden': True,
                        'points': 15
                    }
                ]
            }
        ]

        created_count = 0
        for question_data in practice_questions_data:
            question_data['created_by'] = system_user
            
            question, created = PracticeQuestion.objects.get_or_create(
                title=question_data['title'],
                defaults=question_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created practice question: {question.title}')
                )
                
                # Add to library
                library_entry, lib_created = PracticeQuestionLibrary.objects.get_or_create(
                    question=question,
                    defaults={
                        'is_public': True,
                        'tags': [question.category.lower(), question.difficulty]
                    }
                )
                
                if lib_created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Added to library: {question.title}')
                    )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Practice question already exists: {question.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new practice questions')
        )