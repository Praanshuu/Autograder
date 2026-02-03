"""
Test the integration of points system with assignment submissions.

This test verifies that points are correctly awarded when students submit
assignments and that the gradebook integration works properly.
"""

import json
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from assignments.models import Assignment, Question, AssignmentQuestion, ContentItem
from submissions.models import SubmissionAttempt, TestResult, GradebookEntry
from gamification.models import UserPoints
from gamification.points_calculator import PointsCalculator

User = get_user_model()


class PointsIntegrationTestCase(TestCase):
    """Test points integration with assignment submissions"""
    
    def setUp(self):
        """Set up test data"""
        # Create users
        self.student = User.objects.create_user(
            username='teststudent',
            email='student@test.com',
            password='testpass123',
            role='student'
        )
        
        self.teacher = User.objects.create_user(
            username='testteacher',
            email='teacher@test.com',
            password='testpass123',
            role='teacher'
        )
        
        # Create a module for the assignment
        from classes.models import Class, Module
        self.test_class = Class.objects.create(
            name='Test Class',
            section='CS101',
            owner=self.teacher
        )
        
        self.module = Module.objects.create(
            class_obj=self.test_class,
            title='Test Module'
        )
        
        # Create assignment and question
        self.assignment = Assignment.objects.create(
            module=self.module,
            type='assignment',
            title='Test Assignment',
            description='Test assignment for points integration',
            mode='practice'
        )
        
        self.question = Question.objects.create(
            title='Test Question',
            slug='test-question',
            description='Write a function that returns "Hello World"',
            test_cases=[
                {'input': '', 'output': 'Hello World'},
                {'input': '', 'output': 'Hello World'}
            ],
            created_by=self.teacher
        )
        
        self.assignment_question = AssignmentQuestion.objects.create(
            assignment=self.assignment,
            question=self.question,
            order=1
        )
        
        # Create API client
        self.client = APIClient()
        
    def test_points_awarded_on_successful_submission(self):
        """Test that points are awarded when a student successfully completes an assignment"""
        # Login as student
        self.client.force_authenticate(user=self.student)
        
        # Submit code for the assignment question
        submission_data = {
            'assignment_question_id': str(self.assignment_question.id),
            'code_content': 'def hello():\n    return "Hello World"'
        }
        
        # Mock the code execution to return successful results
        with self.mock_code_execution():
            response = self.client.post('/api/submissions/attempts/', submission_data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check that submission was created
        submission = SubmissionAttempt.objects.get(student=self.student)
        self.assertEqual(submission.status, 'success')
        
        # Check that points were awarded
        user_points = UserPoints.objects.get(user=self.student)
        self.assertGreater(user_points.assignment_points, 0)
        self.assertGreater(user_points.total_points, 0)
        
        # Check that gradebook entry was created with points
        gradebook_entry = GradebookEntry.objects.get(
            student=self.student,
            content_item_id=self.assignment.id
        )
        self.assertGreater(gradebook_entry.points_earned, 0)
        self.assertEqual(gradebook_entry.final_score, 100.0)  # All tests passed
        
    def test_partial_points_for_partial_success(self):
        """Test that partial points are awarded for partially successful submissions"""
        # Login as student
        self.client.force_authenticate(user=self.student)
        
        # Submit code that passes only one test
        submission_data = {
            'assignment_question_id': str(self.assignment_question.id),
            'code_content': 'def hello():\n    return "Wrong Answer"'
        }
        
        # Mock the code execution to return partial results
        with self.mock_code_execution(pass_count=1):
            response = self.client.post('/api/submissions/attempts/', submission_data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check that submission was created
        submission = SubmissionAttempt.objects.get(student=self.student)
        self.assertEqual(submission.status, 'fail')  # Not all tests passed
        
        # Check that partial points were awarded
        user_points = UserPoints.objects.get(user=self.student)
        self.assertGreater(user_points.assignment_points, 0)
        
        # Points should be less than full points since only partial success
        calculator = PointsCalculator()
        full_points = calculator.calculate_assignment_points(
            test_results=[{'status': 'pass', 'score': 1}, {'status': 'pass', 'score': 1}],
            attempt_number=1
        )
        partial_points = calculator.calculate_assignment_points(
            test_results=[{'status': 'pass', 'score': 1}, {'status': 'fail', 'score': 0}],
            attempt_number=1
        )
        
        self.assertLess(partial_points, full_points)
        self.assertEqual(user_points.assignment_points, partial_points)
        
    def test_first_attempt_bonus(self):
        """Test that first attempt bonus is awarded correctly"""
        calculator = PointsCalculator()
        
        # Calculate points for first attempt
        first_attempt_points = calculator.calculate_assignment_points(
            test_results=[{'status': 'pass', 'score': 1}, {'status': 'pass', 'score': 1}],
            attempt_number=1
        )
        
        # Calculate points for second attempt
        second_attempt_points = calculator.calculate_assignment_points(
            test_results=[{'status': 'pass', 'score': 1}, {'status': 'pass', 'score': 1}],
            attempt_number=2
        )
        
        # First attempt should get bonus points
        self.assertGreater(first_attempt_points, second_attempt_points)
        
    def test_gradebook_api_includes_points(self):
        """Test that gradebook API endpoints include points information"""
        # Create a gradebook entry with points
        GradebookEntry.objects.create(
            student=self.student,
            content_item_id=self.assignment.id,
            final_score=85.0,
            points_earned=150
        )
        
        # Login as student
        self.client.force_authenticate(user=self.student)
        
        # Test student summary endpoint
        response = self.client.get('/api/submissions/gradebook/student-summary/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data = response.json()
        self.assertIn('summary', data)
        self.assertIn('total_assignment_points', data['summary'])
        self.assertEqual(data['summary']['total_assignment_points'], 150)
        
    def test_assignment_progress_with_points(self):
        """Test that assignment progress endpoint includes points information"""
        # Create a submission with test results
        submission = SubmissionAttempt.objects.create(
            student=self.student,
            assignment_question=self.assignment_question,
            attempt_number=1,
            status='success',
            source_code='test code'
        )
        
        # Create test results
        TestResult.objects.create(
            attempt=submission,
            test_case_id='0',
            status='pass',
            score=1
        )
        TestResult.objects.create(
            attempt=submission,
            test_case_id='1',
            status='pass',
            score=1
        )
        
        # Login as student
        self.client.force_authenticate(user=self.student)
        
        # Test assignment progress endpoint
        response = self.client.get(
            f'/api/submissions/progress/assignment-progress-with-points/?assignment_id={self.assignment.id}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data = response.json()
        self.assertIn('total_points_earned', data)
        self.assertGreater(data['total_points_earned'], 0)
        
        # Check question-level points
        questions = data['questions']
        self.assertEqual(len(questions), 1)
        self.assertGreater(questions[0]['points_earned'], 0)
        
    def mock_code_execution(self, pass_count=2):
        """Mock code execution to return test results"""
        from unittest.mock import patch
        
        def mock_execute_code(code, language, test_cases):
            results = []
            for i, test_case in enumerate(test_cases):
                if i < pass_count:
                    results.append({
                        'status': 'pass',
                        'console_output': 'Hello World',
                        'test_case': test_case
                    })
                else:
                    results.append({
                        'status': 'fail',
                        'console_output': 'Wrong output',
                        'error_message': 'Output does not match expected',
                        'test_case': test_case
                    })
            return results
        
        return patch('submissions.services.execute_code', side_effect=mock_execute_code)
        
    def test_backward_compatibility(self):
        """Test that existing assignments continue to work without points"""
        # Create an old-style submission without points integration
        submission = SubmissionAttempt.objects.create(
            student=self.student,
            assignment_question=self.assignment_question,
            attempt_number=1,
            status='success',
            source_code='old code'
        )
        
        # Create test results
        TestResult.objects.create(
            attempt=submission,
            test_case_id='0',
            status='pass',
            score=1
        )
        
        # The system should still work and calculate points retroactively
        calculator = PointsCalculator()
        test_results = [{'status': 'pass', 'score': 1}]
        points = calculator.calculate_assignment_points(test_results, 1)
        
        self.assertGreater(points, 0)
        
        # Gradebook should handle entries without points gracefully
        gradebook_entry = GradebookEntry.objects.create(
            student=self.student,
            content_item_id=self.assignment.id,
            final_score=100.0,
            points_earned=0  # Old entry without points
        )
        
        # API should still work
        self.client.force_authenticate(user=self.student)
        response = self.client.get('/api/submissions/gradebook/student-summary/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


if __name__ == '__main__':
    import django
    from django.conf import settings
    from django.test.utils import get_runner
    
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['submissions.test_points_integration'])