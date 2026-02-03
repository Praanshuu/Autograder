"""
Tests for practice submission endpoint functionality.
"""
import json
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch, MagicMock

from gamification.models import (
    PracticeQuestion, 
    PracticeSubmission, 
    PracticeProgress,
    UserPoints
)

User = get_user_model()


class PracticeSubmissionEndpointTest(TestCase):
    """Test practice submission endpoint functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        
        # Create test users
        self.student = User.objects.create_user(
            username='student1',
            email='student1@test.com',
            password='testpass123',
            role='student'
        )
        
        self.teacher = User.objects.create_user(
            username='teacher1',
            email='teacher1@test.com',
            password='testpass123',
            role='teacher'
        )
        
        # Create test practice question
        self.practice_question = PracticeQuestion.objects.create(
            title='Test Practice Question',
            description='A simple test question',
            difficulty='easy',
            category='Basic Programming',
            test_cases=[
                {
                    'input': '5',
                    'expected_output': '5'
                },
                {
                    'input': '10',
                    'expected_output': '10'
                }
            ],
            starter_code='# Write your code here\n',
            point_value=100,
            created_by=self.teacher
        )
    
    def test_student_can_submit_practice_question(self):
        """Test that students can submit practice questions"""
        self.client.force_authenticate(user=self.student)
        
        # Mock the code execution service
        with patch('submissions.services.execute_code') as mock_execute:
            mock_execute.return_value = [
                {
                    'status': 'pass',
                    'console_output': '5',
                    'error_message': '',
                    'execution_time': 100
                },
                {
                    'status': 'pass',
                    'console_output': '10',
                    'error_message': '',
                    'execution_time': 150
                }
            ]
            
            response = self.client.post(
                f'/api/gamification/practice-questions/{self.practice_question.id}/submit/',
                {
                    'source_code': 'print(input())',
                    'language': 'python'
                },
                format='json'
            )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        # Check submission was created
        submission = PracticeSubmission.objects.get(
            student=self.student,
            practice_question=self.practice_question
        )
        self.assertEqual(submission.status, 'success')
        self.assertEqual(submission.attempt_number, 1)
        self.assertGreater(submission.points_earned, 0)
        
        # Check progress was updated
        progress = PracticeProgress.objects.get(
            student=self.student,
            practice_question=self.practice_question
        )
        self.assertTrue(progress.is_completed)
        self.assertEqual(progress.attempts_count, 1)
        self.assertEqual(progress.best_score, 100.0)
        
        # Check points were awarded
        user_points = UserPoints.objects.get(user=self.student)
        self.assertGreater(user_points.practice_points, 0)
        self.assertEqual(user_points.total_points, user_points.practice_points)
    
    def test_unlimited_attempts_allowed(self):
        """Test that students can make unlimited attempts"""
        self.client.force_authenticate(user=self.student)
        
        # First attempt - fail
        with patch('submissions.services.execute_code') as mock_execute:
            mock_execute.return_value = [
                {
                    'status': 'fail',
                    'console_output': 'wrong',
                    'error_message': '',
                    'execution_time': 100
                },
                {
                    'status': 'pass',
                    'console_output': '10',
                    'error_message': '',
                    'execution_time': 150
                }
            ]
            
            response = self.client.post(
                f'/api/gamification/practice-questions/{self.practice_question.id}/submit/',
                {
                    'source_code': 'print("wrong")',
                    'language': 'python'
                },
                format='json'
            )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        first_submission = PracticeSubmission.objects.get(
            student=self.student,
            practice_question=self.practice_question,
            attempt_number=1
        )
        self.assertEqual(first_submission.status, 'fail')
        self.assertEqual(first_submission.points_earned, 0)
        
        # Second attempt - success
        with patch('submissions.services.execute_code') as mock_execute:
            mock_execute.return_value = [
                {
                    'status': 'pass',
                    'console_output': '5',
                    'error_message': '',
                    'execution_time': 100
                },
                {
                    'status': 'pass',
                    'console_output': '10',
                    'error_message': '',
                    'execution_time': 150
                }
            ]
            
            response = self.client.post(
                f'/api/gamification/practice-questions/{self.practice_question.id}/submit/',
                {
                    'source_code': 'print(input())',
                    'language': 'python'
                },
                format='json'
            )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        second_submission = PracticeSubmission.objects.get(
            student=self.student,
            practice_question=self.practice_question,
            attempt_number=2
        )
        self.assertEqual(second_submission.status, 'success')
        self.assertGreater(second_submission.points_earned, 0)
        
        # Check progress reflects both attempts
        progress = PracticeProgress.objects.get(
            student=self.student,
            practice_question=self.practice_question
        )
        self.assertTrue(progress.is_completed)
        self.assertEqual(progress.attempts_count, 2)
        self.assertEqual(progress.best_score, 100.0)
    
    def test_all_tests_must_pass_for_completion(self):
        """Test that ALL test cases must pass for practice completion"""
        self.client.force_authenticate(user=self.student)
        
        # Submit with partial success (1 out of 2 tests pass)
        with patch('submissions.services.execute_code') as mock_execute:
            mock_execute.return_value = [
                {
                    'status': 'pass',
                    'console_output': '5',
                    'error_message': '',
                    'execution_time': 100
                },
                {
                    'status': 'fail',
                    'console_output': 'wrong',
                    'error_message': '',
                    'execution_time': 150
                }
            ]
            
            response = self.client.post(
                f'/api/gamification/practice-questions/{self.practice_question.id}/submit/',
                {
                    'source_code': 'print("5" if input() == "5" else "wrong")',
                    'language': 'python'
                },
                format='json'
            )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check submission failed despite partial success
        submission = PracticeSubmission.objects.get(
            student=self.student,
            practice_question=self.practice_question
        )
        self.assertEqual(submission.status, 'fail')
        self.assertEqual(submission.points_earned, 0)
        
        # Check progress shows not completed
        progress = PracticeProgress.objects.get(
            student=self.student,
            practice_question=self.practice_question
        )
        self.assertFalse(progress.is_completed)
        self.assertEqual(progress.best_score, 50.0)  # 1 out of 2 tests passed
        
        # Check no points were awarded (UserPoints may not exist yet)
        try:
            user_points = UserPoints.objects.get(user=self.student)
            self.assertEqual(user_points.practice_points, 0)
        except UserPoints.DoesNotExist:
            # This is expected when no points have been awarded yet
            pass
    
    def test_teacher_cannot_submit_practice_questions(self):
        """Test that teachers cannot submit practice questions"""
        self.client.force_authenticate(user=self.teacher)
        
        response = self.client.post(
            f'/api/gamification/practice-questions/{self.practice_question.id}/submit/',
            {
                'source_code': 'print(input())',
                'language': 'python'
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(response.data['success'])
    
    def test_submission_with_empty_code_fails(self):
        """Test that submissions with empty code are rejected"""
        self.client.force_authenticate(user=self.student)
        
        response = self.client.post(
            f'/api/gamification/practice-questions/{self.practice_question.id}/submit/',
            {
                'source_code': '',
                'language': 'python'
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data['success'])
    
    def test_code_execution_error_handling(self):
        """Test proper handling of code execution errors"""
        self.client.force_authenticate(user=self.student)
        
        # Mock execution service to raise an exception
        with patch('submissions.services.execute_code') as mock_execute:
            mock_execute.side_effect = Exception("Code execution failed")
            
            response = self.client.post(
                f'/api/gamification/practice-questions/{self.practice_question.id}/submit/',
                {
                    'source_code': 'print(input())',
                    'language': 'python'
                },
                format='json'
            )
        
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertFalse(response.data['success'])
        
        # Check submission was created with error status
        submission = PracticeSubmission.objects.get(
            student=self.student,
            practice_question=self.practice_question
        )
        self.assertEqual(submission.status, 'error')
        self.assertEqual(submission.points_earned, 0)
    
    def test_run_code_without_saving_submission(self):
        """Test running code without saving a submission"""
        self.client.force_authenticate(user=self.student)
        
        with patch('submissions.services.execute_code') as mock_execute:
            mock_execute.return_value = [
                {
                    'status': 'pass',
                    'console_output': '5',
                    'error_message': '',
                    'execution_time': 100
                },
                {
                    'status': 'fail',
                    'console_output': 'wrong',
                    'error_message': '',
                    'execution_time': 150
                }
            ]
            
            response = self.client.post(
                f'/api/gamification/practice-questions/{self.practice_question.id}/run_code/',
                {
                    'source_code': 'print("5" if input() == "5" else "wrong")',
                    'language': 'python'
                },
                format='json'
            )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        # Check that no submission was created
        self.assertFalse(
            PracticeSubmission.objects.filter(
                student=self.student,
                practice_question=self.practice_question
            ).exists()
        )
        
        # Check that no progress was created
        self.assertFalse(
            PracticeProgress.objects.filter(
                student=self.student,
                practice_question=self.practice_question
            ).exists()
        )
        
        # Verify response contains test results
        self.assertIn('data', response.data)
        self.assertIn('results', response.data['data'])
        self.assertIn('summary', response.data['data'])
        self.assertEqual(len(response.data['data']['results']), 2)
        self.assertFalse(response.data['data']['summary']['all_passed'])