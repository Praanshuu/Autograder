"""
Tests for practice progress tracking endpoints.
Validates progress monitoring, statistics calculation, and time tracking functionality.
"""

import json
from datetime import timedelta
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


class PracticeProgressTrackingTestCase(TestCase):
    """Test case for practice progress tracking endpoints"""
    
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
        
        self.other_student = User.objects.create_user(
            username='student2',
            email='student2@test.com',
            password='testpass123',
            role='student'
        )
        
        # Create practice questions
        self.easy_question = PracticeQuestion.objects.create(
            title='Easy Array Problem',
            description='Simple array manipulation',
            difficulty='easy',
            category='Arrays',
            test_cases=[
                {'input': '[1,2,3]', 'expected_output': '[3,2,1]'}
            ],
            point_value=100,
            created_by=self.teacher
        )
        
        self.medium_question = PracticeQuestion.objects.create(
            title='Medium String Problem',
            description='String processing challenge',
            difficulty='medium',
            category='Strings',
            test_cases=[
                {'input': 'hello', 'expected_output': 'olleh'},
                {'input': 'world', 'expected_output': 'dlrow'}
            ],
            point_value=150,
            created_by=self.teacher
        )
        
        self.hard_question = PracticeQuestion.objects.create(
            title='Hard Algorithm Problem',
            description='Complex algorithmic challenge',
            difficulty='hard',
            category='Algorithms',
            test_cases=[
                {'input': '10', 'expected_output': '55'},
                {'input': '5', 'expected_output': '15'}
            ],
            point_value=200,
            created_by=self.teacher
        )
        
        # Create API client
        self.client = APIClient()
    
    def test_start_practice_session(self):
        """Test starting a practice session creates progress record"""
        self.client.force_authenticate(user=self.student)
        
        url = reverse('practice-progress-start-session')
        data = {'practice_question_id': str(self.easy_question.id)}
        
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        # Verify progress record was created
        progress = PracticeProgress.objects.get(
            student=self.student,
            practice_question=self.easy_question
        )
        self.assertIsNotNone(progress)
        self.assertEqual(progress.attempts_count, 0)
        self.assertEqual(progress.time_spent, 0)
        self.assertFalse(progress.is_completed)
    
    def test_update_time_tracking(self):
        """Test updating time spent on practice question"""
        # Create initial progress
        progress = PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.easy_question,
            attempts_count=1,
            time_spent=300  # 5 minutes
        )
        
        self.client.force_authenticate(user=self.student)
        
        url = reverse('practice-progress-update-time')
        data = {
            'practice_question_id': str(self.easy_question.id),
            'time_spent': 600  # 10 minutes
        }
        
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        # Verify time was updated
        progress.refresh_from_db()
        self.assertEqual(progress.time_spent, 600)
    
    def test_progress_summary_statistics(self):
        """Test progress summary endpoint returns correct statistics"""
        # Create progress records
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.easy_question,
            is_completed=True,
            attempts_count=2,
            best_score=100.0,
            time_spent=300,
            completed_at=timezone.now()
        )
        
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.medium_question,
            is_completed=False,
            attempts_count=3,
            best_score=75.0,
            time_spent=600
        )
        
        self.client.force_authenticate(user=self.student)
        
        url = reverse('practice-progress-summary')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        summary = response.data['data']['overall']
        self.assertEqual(summary['total_attempted'], 2)
        self.assertEqual(summary['total_completed'], 1)
        self.assertEqual(summary['completion_rate'], 50.0)
        self.assertEqual(summary['total_time_spent'], 900)
        self.assertEqual(summary['average_score'], 87.5)
    
    def test_dashboard_statistics(self):
        """Test dashboard statistics endpoint provides comprehensive data"""
        # Create progress records with different difficulties
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.easy_question,
            is_completed=True,
            attempts_count=1,
            best_score=100.0,
            time_spent=300,
            completed_at=timezone.now()
        )
        
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.medium_question,
            is_completed=True,
            attempts_count=2,
            best_score=90.0,
            time_spent=600,
            completed_at=timezone.now() - timedelta(days=2)
        )
        
        # Create user points
        UserPoints.objects.create(
            user=self.student,
            total_points=250,
            practice_points=250,
            assignment_points=0
        )
        
        self.client.force_authenticate(user=self.student)
        
        url = reverse('practice-progress-dashboard-stats')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        data = response.data['data']
        
        # Check overview statistics
        overview = data['overview']
        self.assertEqual(overview['total_attempted'], 2)
        self.assertEqual(overview['total_completed'], 2)
        self.assertEqual(overview['completion_rate'], 100.0)
        self.assertEqual(overview['average_score'], 95.0)
        
        # Check performance by difficulty
        difficulty_stats = data['performance_by_difficulty']
        self.assertIn('easy', difficulty_stats)
        self.assertIn('medium', difficulty_stats)
        self.assertEqual(difficulty_stats['easy']['completed'], 1)
        self.assertEqual(difficulty_stats['medium']['completed'], 1)
        
        # Check points data
        points = data['points']
        self.assertEqual(points['total_points'], 250)
        self.assertEqual(points['practice_points'], 250)
    
    def test_detailed_statistics_with_trends(self):
        """Test detailed statistics endpoint with time-based analysis"""
        # Create progress records over time with different questions to avoid unique constraint
        base_time = timezone.now() - timedelta(days=30)
        
        questions = [self.easy_question, self.medium_question, self.hard_question]
        
        for i in range(3):  # Reduced to 3 to use different questions
            PracticeProgress.objects.create(
                student=self.student,
                practice_question=questions[i],
                is_completed=True,
                attempts_count=i + 1,
                best_score=80.0 + (i * 5),  # Improving scores
                time_spent=300 + (i * 60),  # Increasing time
                completed_at=base_time + timedelta(days=i * 10),
                first_attempt_at=base_time + timedelta(days=i * 10)
            )
        
        self.client.force_authenticate(user=self.student)
        
        url = reverse('practice-progress-detailed-statistics')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        data = response.data['data']
        
        # Check time analysis
        self.assertIn('time_analysis', data)
        time_analysis = data['time_analysis']
        self.assertGreater(time_analysis['total_time_spent'], 0)
        self.assertGreater(time_analysis['average_time_per_question'], 0)
        
        # Check category performance
        self.assertIn('category_performance', data)
        category_performance = data['category_performance']
        self.assertGreater(len(category_performance), 0)
        
        # Check weekly trends
        self.assertIn('weekly_trends', data)
        weekly_trends = data['weekly_trends']
        self.assertEqual(len(weekly_trends), 12)  # 12 weeks of data
        
        # Check performance metrics
        self.assertIn('performance_metrics', data)
        metrics = data['performance_metrics']
        self.assertIn('efficiency_score', metrics)
        self.assertIn('consistency_score', metrics)
        self.assertIn('improvement_trend', metrics)
    
    def test_class_overview_for_teachers(self):
        """Test class overview endpoint for teachers"""
        # Create progress for multiple students
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.easy_question,
            is_completed=True,
            attempts_count=2,
            best_score=95.0,
            time_spent=300
        )
        
        PracticeProgress.objects.create(
            student=self.other_student,
            practice_question=self.easy_question,
            is_completed=False,
            attempts_count=5,
            best_score=60.0,
            time_spent=900
        )
        
        self.client.force_authenticate(user=self.teacher)
        
        url = reverse('practice-progress-class-overview')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        data = response.data['data']
        
        # Check class summary
        class_summary = data['class_summary']
        self.assertEqual(class_summary['total_students'], 2)
        self.assertEqual(class_summary['active_students'], 2)
        self.assertGreater(class_summary['average_completion_rate'], 0)
        
        # Check student performance data
        student_performance = data['student_performance']
        self.assertEqual(len(student_performance), 2)
        
        # Check struggling students identification
        struggling_students = data['struggling_students']
        self.assertIsInstance(struggling_students, list)
    
    def test_leaderboard_functionality(self):
        """Test leaderboard endpoint with ranking and filtering"""
        # Create progress for multiple students
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.easy_question,
            is_completed=True,
            attempts_count=1,
            best_score=100.0,
            time_spent=300,
            completed_at=timezone.now()
        )
        
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.medium_question,
            is_completed=True,
            attempts_count=2,
            best_score=90.0,
            time_spent=600,
            completed_at=timezone.now()
        )
        
        PracticeProgress.objects.create(
            student=self.other_student,
            practice_question=self.easy_question,
            is_completed=True,
            attempts_count=3,
            best_score=85.0,
            time_spent=450,
            completed_at=timezone.now()
        )
        
        # Create user points
        UserPoints.objects.create(
            user=self.student,
            practice_points=250,
            total_points=250
        )
        
        UserPoints.objects.create(
            user=self.other_student,
            practice_points=100,
            total_points=100
        )
        
        self.client.force_authenticate(user=self.student)
        
        url = reverse('practice-progress-leaderboard')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        data = response.data['data']
        
        # Check leaderboard structure
        leaderboard = data['leaderboard']
        self.assertGreater(len(leaderboard), 0)
        
        # Check ranking order (student should be first with more completions)
        first_place = leaderboard[0]
        self.assertEqual(first_place['completed_count'], 2)
        self.assertTrue(first_place['is_current_user'])
        
        # Check current user rank
        self.assertEqual(data['current_user_rank'], 1)
    
    def test_filtering_and_sorting_capabilities(self):
        """Test filtering and sorting functionality in progress endpoints"""
        # Create progress records with different statuses and categories
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.easy_question,
            is_completed=True,
            attempts_count=2,
            best_score=100.0,
            time_spent=300,
            completed_at=timezone.now()
        )
        
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.medium_question,
            is_completed=False,
            attempts_count=3,
            best_score=75.0,
            time_spent=600
        )
        
        self.client.force_authenticate(user=self.student)
        
        # Test completion status filter
        url = reverse('practice-progress-list')
        response = self.client.get(url, {'completion_status': 'completed'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertTrue(response.data['results'][0]['is_completed'])
        
        # Test difficulty filter
        response = self.client.get(url, {'difficulty': 'easy,medium'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        
        # Test category filter
        response = self.client.get(url, {'category': 'Arrays'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['practice_question_category'], 'Arrays')
        
        # Test ordering
        response = self.client.get(url, {'ordering': '-best_score'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        if len(results) > 1:
            self.assertGreaterEqual(results[0]['best_score'], results[1]['best_score'])
    
    def test_time_tracking_accuracy(self):
        """Test time tracking accuracy and cumulative updates"""
        # Start a practice session
        progress = PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.easy_question,
            attempts_count=0,
            time_spent=0
        )
        
        self.client.force_authenticate(user=self.student)
        
        # Update time multiple times
        url = reverse('practice-progress-update-time')
        
        # First update: 5 minutes
        response = self.client.post(url, {
            'practice_question_id': str(self.easy_question.id),
            'time_spent': 300
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Second update: 10 minutes total
        response = self.client.post(url, {
            'practice_question_id': str(self.easy_question.id),
            'time_spent': 600
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify final time
        progress.refresh_from_db()
        self.assertEqual(progress.time_spent, 600)
        
        # Verify response data
        self.assertEqual(response.data['data']['time_spent'], 600)
        self.assertIn('updated_at', response.data['data'])
    
    def test_permission_restrictions(self):
        """Test that endpoints properly restrict access based on user roles"""
        self.client.force_authenticate(user=self.student)
        
        # Students should not access class overview
        url = reverse('practice-progress-class-overview')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Teachers should not access student-specific endpoints
        self.client.force_authenticate(user=self.teacher)
        
        url = reverse('practice-progress-dashboard-stats')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        url = reverse('practice-progress-leaderboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_analytics_system_overview(self):
        """Test analytics system overview endpoint"""
        # Create some system-wide data
        PracticeSubmission.objects.create(
            student=self.student,
            practice_question=self.easy_question,
            source_code='test code',
            status='success',
            attempt_number=1,
            points_earned=100
        )
        
        self.client.force_authenticate(user=self.student)
        
        url = reverse('practice-analytics-system-overview')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        data = response.data['data']
        
        # Check overview statistics
        overview = data['overview']
        self.assertGreater(overview['total_questions'], 0)
        self.assertGreaterEqual(overview['total_submissions'], 1)
        
        # Check distributions
        distributions = data['distributions']
        self.assertIn('by_difficulty', distributions)
        self.assertIn('by_category', distributions)
        
        # Check recent activity
        recent_activity = data['recent_activity']
        self.assertIn('submissions_last_30_days', recent_activity)
        self.assertIn('completions_last_30_days', recent_activity)
    
    def test_error_handling(self):
        """Test error handling for invalid requests"""
        self.client.force_authenticate(user=self.student)
        
        # Test invalid practice question ID (non-existent UUID)
        url = reverse('practice-progress-start-session')
        import uuid
        invalid_uuid = str(uuid.uuid4())  # Valid UUID format but non-existent
        response = self.client.post(url, {'practice_question_id': invalid_uuid})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test missing required fields
        url = reverse('practice-progress-update-time')
        response = self.client.post(url, {'practice_question_id': str(self.easy_question.id)})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Test negative time values
        response = self.client.post(url, {
            'practice_question_id': str(self.easy_question.id),
            'time_spent': -100
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_data_consistency(self):
        """Test data consistency across different endpoints"""
        # Create consistent test data
        progress = PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.easy_question,
            is_completed=True,
            attempts_count=3,
            best_score=95.0,
            time_spent=450,
            completed_at=timezone.now()
        )
        
        self.client.force_authenticate(user=self.student)
        
        # Get data from summary endpoint
        summary_url = reverse('practice-progress-summary')
        summary_response = self.client.get(summary_url)
        summary_data = summary_response.data['data']['overall']
        
        # Get data from dashboard endpoint
        dashboard_url = reverse('practice-progress-dashboard-stats')
        dashboard_response = self.client.get(dashboard_url)
        dashboard_data = dashboard_response.data['data']['overview']
        
        # Verify consistency
        self.assertEqual(summary_data['total_attempted'], dashboard_data['total_attempted'])
        self.assertEqual(summary_data['total_completed'], dashboard_data['total_completed'])
        self.assertEqual(summary_data['completion_rate'], dashboard_data['completion_rate'])
        self.assertEqual(summary_data['total_time_spent'], dashboard_data['total_time_spent'])