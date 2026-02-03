"""
Integration tests for practice submission with real code execution.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from gamification.models import (
    PracticeQuestion, 
    PracticeSubmission, 
    PracticeProgress,
    UserPoints
)

User = get_user_model()


class PracticeSubmissionIntegrationTest(TestCase):
    """Integration test for practice submission with real code execution"""
    
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
        
        # Create test practice question with simple test cases
        self.practice_question = PracticeQuestion.objects.create(
            title='Simple Echo Test',
            description='Read input and print it back',
            difficulty='easy',
            category='Basic Programming',
            test_cases=[
                {
                    'input': 'hello',
                    'expected_output': 'hello'
                },
                {
                    'input': 'world',
                    'expected_output': 'world'
                }
            ],
            starter_code='# Write your code here\n',
            point_value=100,
            created_by=self.teacher
        )
    
    def test_practice_submission_with_real_execution(self):
        """Test practice submission with real code execution service"""
        self.client.force_authenticate(user=self.student)
        
        # Submit working Python code
        response = self.client.post(
            f'/api/gamification/practice-questions/{self.practice_question.id}/submit/',
            {
                'source_code': 'print(input())',
                'language': 'python'
            },
            format='json'
        )
        
        # Check response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        # Check submission was created
        submission = PracticeSubmission.objects.get(
            student=self.student,
            practice_question=self.practice_question
        )
        
        # The submission should be processed (status should not be 'processing')
        self.assertIn(submission.status, ['success', 'fail', 'error'])
        
        # Check that test results were recorded
        self.assertIsInstance(submission.test_results, list)
        self.assertGreater(len(submission.test_results), 0)
        
        # Check progress was created
        progress = PracticeProgress.objects.get(
            student=self.student,
            practice_question=self.practice_question
        )
        self.assertEqual(progress.attempts_count, 1)
        
        # If the submission was successful, check points were awarded
        if submission.status == 'success':
            self.assertGreater(submission.points_earned, 0)
            self.assertTrue(progress.is_completed)
            
            # Check user points were updated
            user_points = UserPoints.objects.get(user=self.student)
            self.assertGreater(user_points.practice_points, 0)
            self.assertEqual(user_points.total_points, user_points.practice_points)
    
    def test_run_code_with_real_execution(self):
        """Test running code without saving submission"""
        self.client.force_authenticate(user=self.student)
        
        # Run code without saving
        response = self.client.post(
            f'/api/gamification/practice-questions/{self.practice_question.id}/run_code/',
            {
                'source_code': 'print(input())',
                'language': 'python'
            },
            format='json'
        )
        
        # Check response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        # Check response contains execution results
        self.assertIn('data', response.data)
        self.assertIn('results', response.data['data'])
        self.assertIn('summary', response.data['data'])
        
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
    
    def test_practice_progress_endpoints(self):
        """Test practice progress tracking endpoints"""
        self.client.force_authenticate(user=self.student)
        
        # Start a practice session
        response = self.client.post(
            '/api/gamification/practice-progress/start_session/',
            {
                'practice_question_id': str(self.practice_question.id)
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        # Check progress was created
        progress = PracticeProgress.objects.get(
            student=self.student,
            practice_question=self.practice_question
        )
        self.assertEqual(progress.attempts_count, 0)
        self.assertFalse(progress.is_completed)
        
        # Update time spent
        response = self.client.post(
            '/api/gamification/practice-progress/update_time/',
            {
                'practice_question_id': str(self.practice_question.id),
                'time_spent': 300  # 5 minutes
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        # Check time was updated
        progress.refresh_from_db()
        self.assertEqual(progress.time_spent, 300)
        
        # Get progress summary
        response = self.client.get('/api/gamification/practice-progress/summary/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertIn('data', response.data)
        self.assertIn('overall', response.data['data'])
        self.assertEqual(response.data['data']['overall']['total_attempted'], 1)
        self.assertEqual(response.data['data']['overall']['total_completed'], 0)