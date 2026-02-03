"""
Tests for analytics API endpoints.

This module tests the comprehensive analytics API functionality including:
- Student dashboard analytics
- Class overview analytics (for teachers)
- Performance trends and concept mastery
- Time analysis and comparison data
- Analytics refresh and export functionality
"""

import json
from datetime import datetime, timedelta
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status

from ..models import (
    StudentAnalytics, PracticeQuestion, PracticeSubmission, 
    PracticeProgress, UserPoints
)
from ..analytics_aggregator import analytics_aggregator

User = get_user_model()


class AnalyticsAPITestCase(TestCase):
    """Test case for analytics API endpoints"""
    
    def setUp(self):
        """Set up test data"""
        # Create test users
        self.student = User.objects.create_user(
            username='teststudent',
            email='student@test.com',
            password='testpass123',
            role='student',
            first_name='Test',
            last_name='Student'
        )
        
        self.teacher = User.objects.create_user(
            username='testteacher',
            email='teacher@test.com',
            password='testpass123',
            role='teacher',
            first_name='Test',
            last_name='Teacher'
        )
        
        # Create API clients
        self.student_client = APIClient()
        self.teacher_client = APIClient()
        self.student_client.force_authenticate(user=self.student)
        self.teacher_client.force_authenticate(user=self.teacher)
        
        # Create test practice questions
        self.practice_question1 = PracticeQuestion.objects.create(
            title='Test Question 1',
            description='Test description',
            difficulty='easy',
            category='arrays',
            test_cases=[
                {'input': '1', 'expected_output': '1'},
                {'input': '2', 'expected_output': '2'}
            ],
            point_value=10,
            created_by=self.teacher,
            is_active=True
        )
        
        self.practice_question2 = PracticeQuestion.objects.create(
            title='Test Question 2',
            description='Test description 2',
            difficulty='medium',
            category='strings',
            test_cases=[
                {'input': 'hello', 'expected_output': 'hello'},
                {'input': 'world', 'expected_output': 'world'}
            ],
            point_value=20,
            created_by=self.teacher,
            is_active=True
        )
        
        # Create test submissions and progress
        self.create_test_submissions()
        
        # Create user points
        UserPoints.objects.get_or_create(
            user=self.student,
            defaults={
                'total_points': 50,
                'practice_points': 50,
                'assignment_points': 0
            }
        )
    
    def create_test_submissions(self):
        """Create test submissions and progress data"""
        # Create successful submission for question 1
        submission1 = PracticeSubmission.objects.create(
            student=self.student,
            practice_question=self.practice_question1,
            source_code='print("test")',
            language='python',
            status='success',
            test_results=[
                {'test_case_id': 0, 'passed': True},
                {'test_case_id': 1, 'passed': True}
            ],
            points_earned=10,
            attempt_number=1,
            execution_time_ms=100,
            submitted_at=timezone.now() - timedelta(days=2)
        )
        
        # Create progress for question 1
        progress1, _ = PracticeProgress.objects.get_or_create(
            student=self.student,
            practice_question=self.practice_question1,
            defaults={
                'is_completed': True,
                'attempts_count': 1,
                'best_score': 100.0,
                'time_spent': 300,  # 5 minutes in seconds
                'completed_at': timezone.now() - timedelta(days=2)
            }
        )
        
        # Create submission for question 2 (in progress)
        submission2 = PracticeSubmission.objects.create(
            student=self.student,
            practice_question=self.practice_question2,
            source_code='print("test2")',
            language='python',
            status='fail',
            test_results=[
                {'test_case_id': 0, 'passed': True},
                {'test_case_id': 1, 'passed': False}
            ],
            points_earned=0,
            attempt_number=1,
            execution_time_ms=150,
            submitted_at=timezone.now() - timedelta(days=1)
        )
        
        # Create progress for question 2
        progress2, _ = PracticeProgress.objects.get_or_create(
            student=self.student,
            practice_question=self.practice_question2,
            defaults={
                'is_completed': False,
                'attempts_count': 1,
                'best_score': 50.0,
                'time_spent': 600,  # 10 minutes in seconds
            }
        )
    
    def test_student_dashboard_analytics(self):
        """Test student dashboard analytics endpoint"""
        url = reverse('analytics-student-dashboard')
        response = self.student_client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        
        self.assertTrue(data['success'])
        self.assertIn('data', data)
        
        # Check analytics data structure
        analytics_data = data['data']
        self.assertIn('analytics', analytics_data)
        self.assertIn('points', analytics_data)
        self.assertIn('recent_activity', analytics_data)
        self.assertIn('performance_trend', analytics_data)
        
        # Verify analytics content
        analytics = analytics_data['analytics']
        self.assertGreaterEqual(analytics['total_practice_completed'], 1)
        self.assertGreaterEqual(analytics['average_score'], 0)
        self.assertGreaterEqual(analytics['total_time_spent'], 0)
    
    def test_class_overview_analytics_teacher_access(self):
        """Test class overview analytics with teacher access"""
        # This test would require a class model, so we'll test the permission check
        url = reverse('analytics-class-overview')
        response = self.teacher_client.get(url, {'class_id': '1'})
        
        # Should fail because class doesn't exist, but permission should be granted
        self.assertIn(response.status_code, [status.HTTP_404_NOT_FOUND, status.HTTP_501_NOT_IMPLEMENTED])
    
    def test_class_overview_analytics_student_denied(self):
        """Test class overview analytics denies student access"""
        url = reverse('analytics-class-overview')
        response = self.student_client.get(url, {'class_id': '1'})
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission denied')
    
    def test_performance_trends(self):
        """Test performance trends endpoint"""
        url = reverse('analytics-performance-trends')
        response = self.student_client.get(url, {'days': 7})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        
        self.assertTrue(data['success'])
        self.assertIn('data', data)
        
        # Check trends data structure
        trends_data = data['data']
        self.assertIn('trends', trends_data)
        self.assertIn('summary', trends_data)
        self.assertIn('date_range', trends_data)
        
        # Verify summary statistics
        summary = trends_data['summary']
        self.assertIn('total_days_analyzed', summary)
        self.assertIn('active_days', summary)
        self.assertIn('total_activities', summary)
        self.assertIn('avg_score', summary)
    
    def test_concept_mastery(self):
        """Test concept mastery endpoint"""
        url = reverse('analytics-concept-mastery')
        response = self.student_client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        
        self.assertTrue(data['success'])
        self.assertIn('data', data)
        
        # Check concept mastery data structure
        mastery_data = data['data']
        self.assertIn('concept_mastery', mastery_data)
        self.assertIn('insights', mastery_data)
        
        # Verify insights structure
        insights = mastery_data['insights']
        self.assertIn('total_concepts', insights)
        self.assertIn('mastered_concepts', insights)
        self.assertIn('struggling_concepts', insights)
        self.assertIn('average_mastery', insights)
    
    def test_streak_analysis(self):
        """Test streak analysis endpoint"""
        url = reverse('analytics-streak-analysis')
        response = self.student_client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        
        self.assertTrue(data['success'])
        self.assertIn('data', data)
        
        # Check streak analysis data structure
        streak_data = data['data']
        self.assertIn('streak_analysis', streak_data)
        self.assertIn('recent_activity_pattern', streak_data)
        
        # Verify streak analysis content
        streak_analysis = streak_data['streak_analysis']
        self.assertIn('current_streak', streak_analysis)
        self.assertIn('longest_streak', streak_analysis)
        self.assertIn('streak_status', streak_analysis)
        self.assertIn('days_until_milestone', streak_analysis)
    
    def test_time_analysis(self):
        """Test time analysis endpoint"""
        url = reverse('analytics-time-analysis')
        response = self.student_client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        
        self.assertTrue(data['success'])
        self.assertIn('data', data)
        
        # Check time analysis data structure
        time_data = data['data']
        self.assertIn('time_analysis', time_data)
        self.assertIn('last_activity', time_data)
        
        # Verify time analysis content
        time_analysis = time_data['time_analysis']
        self.assertIn('total_time_minutes', time_analysis)
        self.assertIn('total_time_hours', time_analysis)
        self.assertIn('practice_time_minutes', time_analysis)
        self.assertIn('avg_time_per_completion_minutes', time_analysis)
        self.assertIn('productivity_score', time_analysis)
        
        # Verify time calculations
        self.assertGreaterEqual(time_analysis['total_time_minutes'], 0)
        self.assertGreaterEqual(time_analysis['productivity_score'], 0)
        self.assertLessEqual(time_analysis['productivity_score'], 100)
    
    def test_comparison_data(self):
        """Test comparison data endpoint"""
        url = reverse('analytics-comparison-data')
        response = self.student_client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        
        self.assertTrue(data['success'])
        self.assertIn('data', data)
        
        # Check comparison data structure
        comparison_data = data['data']
        self.assertIn('student_metrics', comparison_data)
        self.assertIn('global_averages', comparison_data)
        self.assertIn('percentiles', comparison_data)
        self.assertIn('total_students', comparison_data)
        
        # Verify metrics structure
        student_metrics = comparison_data['student_metrics']
        self.assertIn('practice_completed', student_metrics)
        self.assertIn('average_score', student_metrics)
        self.assertIn('current_streak', student_metrics)
        
        # Verify percentiles are valid
        percentiles = comparison_data['percentiles']
        for key, value in percentiles.items():
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 100)
    
    def test_refresh_analytics(self):
        """Test analytics refresh endpoint"""
        url = reverse('analytics-refresh-analytics')
        response = self.student_client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], 'Analytics refreshed successfully')
        self.assertIn('data', data)
        
        # Verify refresh data structure
        refresh_data = data['data']
        self.assertIn('updated_at', refresh_data)
        self.assertIn('total_practice_completed', refresh_data)
        self.assertIn('average_score', refresh_data)
        self.assertIn('current_streak', refresh_data)
    
    def test_export_data(self):
        """Test analytics export endpoint"""
        url = reverse('analytics-export-data')
        response = self.student_client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        
        self.assertTrue(data['success'])
        self.assertIn('data', data)
        
        # Check export data structure
        export_data = data['data']
        self.assertIn('user_info', export_data)
        self.assertIn('analytics_summary', export_data)
        self.assertIn('detailed_submissions', export_data)
        
        # Verify user info
        user_info = export_data['user_info']
        self.assertEqual(user_info['username'], self.student.username)
        self.assertIn('export_date', user_info)
        
        # Verify detailed submissions
        submissions = export_data['detailed_submissions']
        self.assertIsInstance(submissions, list)
        if submissions:
            submission = submissions[0]
            self.assertIn('question_title', submission)
            self.assertIn('difficulty', submission)
            self.assertIn('status', submission)
            self.assertIn('points_earned', submission)
    
    def test_analytics_endpoints_require_authentication(self):
        """Test that analytics endpoints require authentication"""
        unauthenticated_client = APIClient()
        
        endpoints = [
            'analytics-student-dashboard',
            'analytics-performance-trends',
            'analytics-concept-mastery',
            'analytics-streak-analysis',
            'analytics-time-analysis',
            'analytics-comparison-data',
            'analytics-export-data'
        ]
        
        for endpoint in endpoints:
            url = reverse(endpoint)
            response = unauthenticated_client.get(url)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_analytics_with_no_data(self):
        """Test analytics endpoints with a user who has no activity"""
        # Create a new student with no activity
        new_student = User.objects.create_user(
            username='newstudent',
            email='new@test.com',
            password='testpass123',
            role='student'
        )
        
        new_client = APIClient()
        new_client.force_authenticate(user=new_student)
        
        # Test student dashboard with no data
        url = reverse('analytics-student-dashboard')
        response = new_client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        
        # Should still return valid structure with zero values
        analytics_data = data['data']
        self.assertIn('analytics', analytics_data)
        analytics = analytics_data['analytics']
        self.assertEqual(analytics['total_practice_completed'], 0)
        self.assertEqual(analytics['average_score'], 0.0)
    
    def test_performance_trends_different_time_periods(self):
        """Test performance trends with different time periods"""
        url = reverse('analytics-performance-trends')
        
        # Test different day ranges
        for days in [7, 14, 30, 60]:
            response = self.student_client.get(url, {'days': days})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
            data = response.json()
            self.assertTrue(data['success'])
            
            trends_data = data['data']
            self.assertEqual(trends_data['date_range']['days'], days)
    
    def test_analytics_aggregator_integration(self):
        """Test that analytics endpoints properly integrate with AnalyticsAggregator"""
        # Update analytics using aggregator
        analytics = analytics_aggregator.update_student_analytics(self.student)
        
        # Test that API endpoints return updated data
        url = reverse('analytics-student-dashboard')
        response = self.student_client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        
        # Verify that the data matches what the aggregator calculated
        api_analytics = data['data']['analytics']
        self.assertEqual(api_analytics['total_practice_completed'], analytics.total_practice_completed)
        self.assertEqual(api_analytics['average_score'], analytics.average_score)
        self.assertEqual(api_analytics['current_streak'], analytics.current_streak)
    
    def test_error_handling(self):
        """Test error handling in analytics endpoints"""
        # Test with invalid parameters
        url = reverse('analytics-performance-trends')
        response = self.student_client.get(url, {'days': 'invalid'})
        
        # Should handle invalid parameters gracefully
        # (Either return error or use default value)
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_400_BAD_REQUEST])
        
        if response.status_code == status.HTTP_200_OK:
            # If it handles gracefully, should return valid data
            data = response.json()
            self.assertTrue(data['success'])