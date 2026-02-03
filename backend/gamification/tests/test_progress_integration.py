"""
Integration tests for practice progress tracking with submission system.
Tests the complete workflow from practice question creation to progress tracking.
"""

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from ..models import (
    PracticeQuestion, 
    PracticeProgress, 
    PracticeSubmission,
    UserPoints
)

User = get_user_model()


class PracticeProgressIntegrationTestCase(TestCase):
    """Integration test case for practice progress tracking with submissions"""
    
    def setUp(self):
        """Set up test data"""
        # Create users
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
        
        # Create practice question
        self.practice_question = PracticeQuestion.objects.create(
            title='Array Reversal',
            description='Reverse an array in place',
            difficulty='easy',
            category='Arrays',
            test_cases=[
                {'input': '[1,2,3,4,5]', 'expected_output': '[5,4,3,2,1]'},
                {'input': '[10,20]', 'expected_output': '[20,10]'}
            ],
            point_value=100,
            created_by=self.teacher
        )
        
        # Create API client
        self.client = APIClient()
    
    def test_complete_practice_workflow_with_progress_tracking(self):
        """Test complete workflow: start session -> submit -> track progress -> view statistics"""
        self.client.force_authenticate(user=self.student)
        
        # Step 1: Start practice session
        start_url = reverse('practice-progress-start-session')
        start_response = self.client.post(start_url, {
            'practice_question_id': str(self.practice_question.id)
        })
        
        self.assertEqual(start_response.status_code, status.HTTP_200_OK)
        self.assertTrue(start_response.data['success'])
        
        # Verify progress record was created
        progress = PracticeProgress.objects.get(
            student=self.student,
            practice_question=self.practice_question
        )
        self.assertFalse(progress.is_completed)
        self.assertEqual(progress.attempts_count, 0)
        
        # Step 2: Update time spent (simulate working on the problem)
        time_url = reverse('practice-progress-update-time')
        time_response = self.client.post(time_url, {
            'practice_question_id': str(self.practice_question.id),
            'time_spent': 600  # 10 minutes
        })
        
        self.assertEqual(time_response.status_code, status.HTTP_200_OK)
        self.assertTrue(time_response.data['success'])
        
        # Verify time was updated
        progress.refresh_from_db()
        self.assertEqual(progress.time_spent, 600)
        
        # Step 3: Simulate failed submission (manually create since code execution isn't available)
        failed_submission = PracticeSubmission.objects.create(
            student=self.student,
            practice_question=self.practice_question,
            source_code='def reverse_array(arr): return arr',  # Incorrect implementation
            language='python',
            status='fail',
            test_results=[
                {
                    'test_case_id': 0,
                    'input': '[1,2,3,4,5]',
                    'expected_output': '[5,4,3,2,1]',
                    'actual_output': '[1,2,3,4,5]',
                    'status': 'fail',
                    'passed': False
                }
            ],
            points_earned=0,
            attempt_number=1
        )
        
        # Manually update progress for failed attempt
        progress.attempts_count = 1
        progress.best_score = 0.0
        progress.save()
        
        # Step 4: Simulate successful submission
        successful_submission = PracticeSubmission.objects.create(
            student=self.student,
            practice_question=self.practice_question,
            source_code='def reverse_array(arr): return arr[::-1]',  # Correct implementation
            language='python',
            status='success',
            test_results=[
                {
                    'test_case_id': 0,
                    'input': '[1,2,3,4,5]',
                    'expected_output': '[5,4,3,2,1]',
                    'actual_output': '[5,4,3,2,1]',
                    'status': 'pass',
                    'passed': True
                },
                {
                    'test_case_id': 1,
                    'input': '[10,20]',
                    'expected_output': '[20,10]',
                    'actual_output': '[20,10]',
                    'status': 'pass',
                    'passed': True
                }
            ],
            points_earned=100,
            attempt_number=2
        )
        
        # Manually update progress for successful completion
        progress.attempts_count = 2
        progress.best_score = 100.0
        progress.is_completed = True
        progress.completed_at = timezone.now()
        progress.save()
        
        # Manually create user points
        UserPoints.objects.create(
            user=self.student,
            practice_points=100,
            total_points=100
        )
        
        # Step 5: View progress summary
        summary_url = reverse('practice-progress-summary')
        summary_response = self.client.get(summary_url)
        
        self.assertEqual(summary_response.status_code, status.HTTP_200_OK)
        self.assertTrue(summary_response.data['success'])
        
        summary_data = summary_response.data['data']['overall']
        self.assertEqual(summary_data['total_attempted'], 1)
        self.assertEqual(summary_data['total_completed'], 1)
        self.assertEqual(summary_data['completion_rate'], 100.0)
        self.assertEqual(summary_data['total_time_spent'], 600)
        
        # Step 6: View dashboard statistics
        dashboard_url = reverse('practice-progress-dashboard-stats')
        dashboard_response = self.client.get(dashboard_url)
        
        self.assertEqual(dashboard_response.status_code, status.HTTP_200_OK)
        self.assertTrue(dashboard_response.data['success'])
        
        dashboard_data = dashboard_response.data['data']
        overview = dashboard_data['overview']
        self.assertEqual(overview['total_completed'], 1)
        self.assertEqual(overview['completion_rate'], 100.0)
        
        # Check points data
        points = dashboard_data['points']
        self.assertEqual(points['practice_points'], 100)
        
        # Check performance by difficulty
        difficulty_stats = dashboard_data['performance_by_difficulty']
        self.assertIn('easy', difficulty_stats)
        self.assertEqual(difficulty_stats['easy']['completed'], 1)
    
    def test_teacher_class_overview_integration(self):
        """Test teacher's ability to view class progress overview"""
        # Create progress for the student
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.practice_question,
            is_completed=True,
            attempts_count=2,
            best_score=100.0,
            time_spent=600,
            completed_at=timezone.now()
        )
        
        # Create a submission
        PracticeSubmission.objects.create(
            student=self.student,
            practice_question=self.practice_question,
            source_code='def reverse_array(arr): return arr[::-1]',
            status='success',
            points_earned=100,
            attempt_number=2
        )
        
        self.client.force_authenticate(user=self.teacher)
        
        # View class overview
        overview_url = reverse('practice-progress-class-overview')
        overview_response = self.client.get(overview_url)
        
        self.assertEqual(overview_response.status_code, status.HTTP_200_OK)
        self.assertTrue(overview_response.data['success'])
        
        data = overview_response.data['data']
        
        # Check class summary
        class_summary = data['class_summary']
        self.assertEqual(class_summary['total_students'], 1)
        self.assertEqual(class_summary['active_students'], 1)
        self.assertGreater(class_summary['average_completion_rate'], 0)
        
        # Check student performance
        student_performance = data['student_performance']
        self.assertEqual(len(student_performance), 1)
        
        student_data = student_performance[0]
        self.assertEqual(student_data['student']['username'], self.student.username)
        self.assertEqual(student_data['completed'], 1)
        self.assertEqual(student_data['completion_rate'], 100.0)
    
    def test_analytics_system_overview_integration(self):
        """Test system-wide analytics integration"""
        # Create some system data
        PracticeSubmission.objects.create(
            student=self.student,
            practice_question=self.practice_question,
            source_code='test code',
            status='success',
            points_earned=100,
            attempt_number=1
        )
        
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.practice_question,
            is_completed=True,
            attempts_count=1,
            best_score=100.0,
            time_spent=300,
            completed_at=timezone.now()
        )
        
        self.client.force_authenticate(user=self.student)
        
        # View system overview
        overview_url = reverse('practice-analytics-system-overview')
        overview_response = self.client.get(overview_url)
        
        self.assertEqual(overview_response.status_code, status.HTTP_200_OK)
        self.assertTrue(overview_response.data['success'])
        
        data = overview_response.data['data']
        
        # Check overview statistics
        overview = data['overview']
        self.assertGreaterEqual(overview['total_questions'], 1)
        self.assertGreaterEqual(overview['total_submissions'], 1)
        self.assertGreaterEqual(overview['total_completions'], 1)
        
        # Check distributions
        distributions = data['distributions']
        self.assertIn('by_difficulty', distributions)
        self.assertIn('by_category', distributions)
        
        difficulty_dist = distributions['by_difficulty']
        self.assertIn('easy', difficulty_dist)
        self.assertGreaterEqual(difficulty_dist['easy'], 1)
        
        category_dist = distributions['by_category']
        self.assertIn('Arrays', category_dist)
        self.assertGreaterEqual(category_dist['Arrays'], 1)
    
    def test_time_tracking_accuracy_integration(self):
        """Test time tracking accuracy throughout the workflow"""
        self.client.force_authenticate(user=self.student)
        
        # Start session
        start_url = reverse('practice-progress-start-session')
        self.client.post(start_url, {
            'practice_question_id': str(self.practice_question.id)
        })
        
        # Update time multiple times (simulating active work)
        time_url = reverse('practice-progress-update-time')
        
        # First update: 5 minutes
        response1 = self.client.post(time_url, {
            'practice_question_id': str(self.practice_question.id),
            'time_spent': 300
        })
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        
        # Second update: 10 minutes total
        response2 = self.client.post(time_url, {
            'practice_question_id': str(self.practice_question.id),
            'time_spent': 600
        })
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        
        # Third update: 15 minutes total
        response3 = self.client.post(time_url, {
            'practice_question_id': str(self.practice_question.id),
            'time_spent': 900
        })
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
        
        # Verify final time
        progress = PracticeProgress.objects.get(
            student=self.student,
            practice_question=self.practice_question
        )
        self.assertEqual(progress.time_spent, 900)
        
        # Simulate submission completion (without actual code execution)
        PracticeSubmission.objects.create(
            student=self.student,
            practice_question=self.practice_question,
            source_code='def reverse_array(arr): return arr[::-1]',
            language='python',
            status='success',
            points_earned=100,
            attempt_number=1
        )
        
        # Update progress to completed
        progress.is_completed = True
        progress.attempts_count = 1
        progress.best_score = 100.0
        progress.completed_at = timezone.now()
        progress.save()
        
        # Check that time is preserved after submission
        progress.refresh_from_db()
        self.assertEqual(progress.time_spent, 900)
        
        # Check summary includes correct time
        summary_url = reverse('practice-progress-summary')
        summary_response = self.client.get(summary_url)
        
        summary_data = summary_response.data['data']['overall']
        self.assertEqual(summary_data['total_time_spent'], 900)
    
    def test_filtering_and_sorting_integration(self):
        """Test filtering and sorting work correctly with real data"""
        # Create additional practice questions and progress
        medium_question = PracticeQuestion.objects.create(
            title='Binary Search',
            description='Implement binary search',
            difficulty='medium',
            category='Algorithms',
            test_cases=[{'input': '[1,2,3,4,5], 3', 'expected_output': '2'}],
            point_value=150,
            created_by=self.teacher
        )
        
        # Create progress for both questions
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.practice_question,
            is_completed=True,
            attempts_count=1,
            best_score=100.0,
            time_spent=300
        )
        
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=medium_question,
            is_completed=False,
            attempts_count=3,
            best_score=75.0,
            time_spent=900
        )
        
        self.client.force_authenticate(user=self.student)
        
        # Test completion status filter
        list_url = reverse('practice-progress-list')
        
        # Filter for completed
        completed_response = self.client.get(list_url, {'completion_status': 'completed'})
        self.assertEqual(completed_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(completed_response.data['results']), 1)
        self.assertTrue(completed_response.data['results'][0]['is_completed'])
        
        # Filter for in progress
        in_progress_response = self.client.get(list_url, {'completion_status': 'in_progress'})
        self.assertEqual(in_progress_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(in_progress_response.data['results']), 1)
        self.assertFalse(in_progress_response.data['results'][0]['is_completed'])
        
        # Test difficulty filter
        difficulty_response = self.client.get(list_url, {'difficulty': 'easy'})
        self.assertEqual(difficulty_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(difficulty_response.data['results']), 1)
        self.assertEqual(difficulty_response.data['results'][0]['practice_question_difficulty'], 'easy')
        
        # Test category filter
        category_response = self.client.get(list_url, {'category': 'Arrays'})
        self.assertEqual(category_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(category_response.data['results']), 1)
        self.assertEqual(category_response.data['results'][0]['practice_question_category'], 'Arrays')
        
        # Test ordering by best score
        ordered_response = self.client.get(list_url, {'ordering': '-best_score'})
        self.assertEqual(ordered_response.status_code, status.HTTP_200_OK)
        results = ordered_response.data['results']
        if len(results) > 1:
            self.assertGreaterEqual(results[0]['best_score'], results[1]['best_score'])