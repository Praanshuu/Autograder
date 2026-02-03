"""
Tests for the AnalyticsAggregator and StudentAnalytics functionality.
"""

from datetime import datetime, timedelta
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from ..models import (
    StudentAnalytics, PracticeQuestion, PracticeSubmission, 
    PracticeProgress, UserPoints
)
from ..analytics_aggregator import AnalyticsAggregator

User = get_user_model()


class AnalyticsAggregatorTest(TestCase):
    """Test the AnalyticsAggregator functionality."""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.aggregator = AnalyticsAggregator()
        
        # Create test practice questions
        self.practice_question1 = PracticeQuestion.objects.create(
            title='Test Question 1',
            description='A test question',
            difficulty='easy',
            category='algorithms',
            starter_code='def solution():\n    pass',
            point_value=100,
            test_cases=[{'input': '', 'expected': 'test'}],
            created_by=self.user
        )
        
        self.practice_question2 = PracticeQuestion.objects.create(
            title='Test Question 2',
            description='Another test question',
            difficulty='medium',
            category='data-structures',
            starter_code='def solution():\n    pass',
            point_value=150,
            test_cases=[{'input': '', 'expected': 'test'}],
            created_by=self.user
        )
    
    def test_update_student_analytics_creates_new_record(self):
        """Test that updating analytics creates a new record for new students."""
        # Ensure no analytics exist initially
        self.assertFalse(StudentAnalytics.objects.filter(student=self.user).exists())
        
        # Update analytics
        analytics = self.aggregator.update_student_analytics(self.user)
        
        # Verify analytics record was created
        self.assertIsNotNone(analytics)
        self.assertEqual(analytics.student, self.user)
        self.assertEqual(analytics.total_practice_completed, 0)
        self.assertEqual(analytics.total_assignments_completed, 0)
        self.assertEqual(analytics.average_score, 0.0)
        self.assertEqual(analytics.current_streak, 0)
        self.assertEqual(analytics.longest_streak, 0)
    
    def test_calculate_practice_completed(self):
        """Test calculation of completed practice questions."""
        # Create completed practice progress
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question1,
            is_completed=True,
            attempts_count=1,
            best_score=100.0,
            completed_at=timezone.now()
        )
        
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question2,
            is_completed=True,
            attempts_count=2,
            best_score=100.0,
            completed_at=timezone.now()
        )
        
        # Test the calculation
        completed_count = self.aggregator._calculate_practice_completed(self.user)
        self.assertEqual(completed_count, 2)
    
    def test_calculate_average_score_practice_only(self):
        """Test average score calculation with only practice questions."""
        # Create practice progress with different scores
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question1,
            is_completed=True,
            best_score=100.0
        )
        
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question2,
            is_completed=True,
            best_score=100.0
        )
        
        # Test calculation (completed practice = 100%)
        avg_score = self.aggregator._calculate_average_score(self.user)
        self.assertEqual(avg_score, 100.0)
    
    def test_calculate_streaks_no_activity(self):
        """Test streak calculation with no activity."""
        current_streak, longest_streak = self.aggregator._calculate_streaks(self.user)
        self.assertEqual(current_streak, 0)
        self.assertEqual(longest_streak, 0)
    
    def test_calculate_streaks_with_activity(self):
        """Test streak calculation with consecutive daily activity."""
        today = timezone.now().date()
        yesterday = today - timedelta(days=1)
        
        # Create practice submissions for consecutive days
        PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.practice_question1,
            source_code='test',
            status='success',
            attempt_number=1,
            submitted_at=timezone.now().replace(
                year=yesterday.year,
                month=yesterday.month,
                day=yesterday.day
            )
        )
        
        PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.practice_question2,
            source_code='test',
            status='success',
            attempt_number=1,
            submitted_at=timezone.now()
        )
        
        current_streak, longest_streak = self.aggregator._calculate_streaks(self.user)
        self.assertGreaterEqual(current_streak, 1)
        self.assertGreaterEqual(longest_streak, 1)
    
    def test_calculate_total_time_spent(self):
        """Test total time calculation."""
        # Create practice progress with time spent
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question1,
            time_spent=300,  # 5 minutes in seconds
            is_completed=True
        )
        
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question2,
            time_spent=600,  # 10 minutes in seconds
            is_completed=True
        )
        
        # Test calculation (should convert seconds to minutes)
        total_time = self.aggregator._calculate_total_time_spent(self.user)
        self.assertEqual(total_time, 15)  # (300 + 600) / 60 = 15 minutes
    
    def test_get_last_activity(self):
        """Test getting last activity timestamp."""
        # Initially no activity
        last_activity = self.aggregator._get_last_activity(self.user)
        self.assertIsNone(last_activity)
        
        # Create a practice submission
        submission_time = timezone.now()
        PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.practice_question1,
            source_code='test',
            status='success',
            attempt_number=1,
            submitted_at=submission_time
        )
        
        last_activity = self.aggregator._get_last_activity(self.user)
        self.assertIsNotNone(last_activity)
        # Use assertAlmostEqual for timestamp comparison to handle microsecond differences
        self.assertAlmostEqual(
            last_activity.timestamp(), 
            submission_time.timestamp(), 
            delta=1.0  # Allow 1 second difference
        )
    
    def test_calculate_performance_trend(self):
        """Test performance trend calculation."""
        # Create submissions over multiple days
        today = timezone.now()
        yesterday = today - timedelta(days=1)
        
        PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.practice_question1,
            source_code='test',
            status='success',
            attempt_number=1,
            submitted_at=yesterday
        )
        
        PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.practice_question2,
            source_code='test',
            status='success',
            attempt_number=1,
            submitted_at=today
        )
        
        # Test trend calculation
        trend_data = self.aggregator._calculate_performance_trend(self.user, days=7)
        
        self.assertEqual(len(trend_data), 7)
        self.assertIsInstance(trend_data, list)
        
        # Check that each day has the required fields
        for day_data in trend_data:
            self.assertIn('date', day_data)
            self.assertIn('practice_completed', day_data)
            self.assertIn('assignments_completed', day_data)
            self.assertIn('total_activities', day_data)
            self.assertIn('average_score', day_data)
            self.assertIn('has_activity', day_data)
    
    def test_calculate_concept_mastery(self):
        """Test concept mastery calculation by category."""
        # Create progress in different categories
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question1,  # algorithms category
            is_completed=True
        )
        
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question2,  # data-structures category
            is_completed=False  # Not completed
        )
        
        concept_mastery = self.aggregator._calculate_concept_mastery(self.user)
        
        # Should have mastery data for both categories
        self.assertIn('algorithms', concept_mastery)
        self.assertIn('data-structures', concept_mastery)
        
        # Algorithms should be 100% (1/1 completed)
        self.assertEqual(concept_mastery['algorithms'], 100.0)
        
        # Data structures should be 0% (0/1 completed)
        self.assertEqual(concept_mastery['data-structures'], 0.0)
    
    def test_get_student_performance_summary(self):
        """Test getting comprehensive performance summary."""
        # Create some test data
        UserPoints.objects.create(
            user=self.user,
            total_points=250,
            practice_points=150,
            assignment_points=100
        )
        
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question1,
            is_completed=True,
            best_score=100.0
        )
        
        # Get performance summary
        summary = self.aggregator.get_student_performance_summary(self.user)
        
        # Verify structure
        self.assertIn('analytics', summary)
        self.assertIn('points', summary)
        self.assertIn('rank', summary)
        self.assertIn('recent_activity', summary)
        self.assertIn('performance_trend', summary)
        
        # Verify analytics data
        analytics = summary['analytics']
        self.assertEqual(analytics['total_practice_completed'], 1)
        self.assertEqual(analytics['average_score'], 100.0)
        
        # Verify points data
        points = summary['points']
        self.assertEqual(points['total_points'], 250)
        self.assertEqual(points['practice_points'], 150)
        self.assertEqual(points['assignment_points'], 100)
    
    def test_update_analytics_on_activity(self):
        """Test that analytics are updated when activity occurs."""
        # Initially no analytics
        self.assertFalse(StudentAnalytics.objects.filter(student=self.user).exists())
        
        # Trigger analytics update
        self.aggregator.update_analytics_on_activity(self.user, 'practice')
        
        # Verify analytics were created
        self.assertTrue(StudentAnalytics.objects.filter(student=self.user).exists())
        
        analytics = StudentAnalytics.objects.get(student=self.user)
        self.assertEqual(analytics.student, self.user)


class StudentAnalyticsModelTest(TestCase):
    """Test the StudentAnalytics model."""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_create_student_analytics(self):
        """Test creating a StudentAnalytics record."""
        analytics = StudentAnalytics.objects.create(
            student=self.user,
            total_practice_completed=5,
            total_assignments_completed=3,
            average_score=85.5,
            current_streak=7,
            longest_streak=12,
            total_time_spent=180,
            performance_trend=[
                {'date': '2024-01-01', 'score': 80.0},
                {'date': '2024-01-02', 'score': 90.0}
            ],
            concept_mastery={
                'algorithms': 75.0,
                'data-structures': 60.0
            }
        )
        
        self.assertEqual(analytics.student, self.user)
        self.assertEqual(analytics.total_practice_completed, 5)
        self.assertEqual(analytics.total_assignments_completed, 3)
        self.assertEqual(analytics.average_score, 85.5)
        self.assertEqual(analytics.current_streak, 7)
        self.assertEqual(analytics.longest_streak, 12)
        self.assertEqual(analytics.total_time_spent, 180)
        self.assertEqual(len(analytics.performance_trend), 2)
        self.assertEqual(len(analytics.concept_mastery), 2)
    
    def test_student_analytics_str_method(self):
        """Test the string representation of StudentAnalytics."""
        analytics = StudentAnalytics.objects.create(
            student=self.user
        )
        
        expected_str = f"{self.user.username} Analytics"
        self.assertEqual(str(analytics), expected_str)
    
    def test_student_analytics_defaults(self):
        """Test that StudentAnalytics has proper default values."""
        analytics = StudentAnalytics.objects.create(
            student=self.user
        )
        
        self.assertEqual(analytics.total_practice_completed, 0)
        self.assertEqual(analytics.total_assignments_completed, 0)
        self.assertEqual(analytics.average_score, 0.0)
        self.assertEqual(analytics.current_streak, 0)
        self.assertEqual(analytics.longest_streak, 0)
        self.assertEqual(analytics.total_time_spent, 0)
        self.assertIsNone(analytics.last_activity)
        self.assertEqual(analytics.performance_trend, [])
        self.assertEqual(analytics.concept_mastery, {})
    
    def test_one_to_one_relationship(self):
        """Test that StudentAnalytics has a proper one-to-one relationship with User."""
        analytics = StudentAnalytics.objects.create(student=self.user)
        
        # Access analytics through user
        self.assertEqual(self.user.analytics, analytics)
        
        # Verify reverse relationship
        self.assertEqual(analytics.student, self.user)


class AnalyticsIntegrationTest(TestCase):
    """Integration tests for analytics with other gamification features."""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.aggregator = AnalyticsAggregator()
        
        self.practice_question = PracticeQuestion.objects.create(
            title='Integration Test Question',
            description='A test question for integration testing',
            difficulty='easy',
            category='algorithms',
            starter_code='def solution():\n    pass',
            point_value=100,
            test_cases=[{'input': '', 'expected': 'test'}],
            created_by=self.user
        )
    
    def test_analytics_update_after_practice_completion(self):
        """Test that analytics are updated after completing a practice question."""
        # Create a successful practice submission
        submission = PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.practice_question,
            source_code='def solution():\n    return "test"',
            status='success',
            attempt_number=1,
            points_earned=100
        )
        
        # Create corresponding progress (use get_or_create to avoid duplicates)
        progress, created = PracticeProgress.objects.get_or_create(
            student=self.user,
            practice_question=self.practice_question,
            defaults={
                'is_completed': True,
                'attempts_count': 1,
                'best_score': 100.0,
                'time_spent': 300,  # 5 minutes
                'completed_at': timezone.now()
            }
        )
        
        # If not created, update the existing record
        if not created:
            progress.is_completed = True
            progress.attempts_count = 1
            progress.best_score = 100.0
            progress.time_spent = 300
            progress.completed_at = timezone.now()
            progress.save()
        
        # Update analytics
        analytics = self.aggregator.update_student_analytics(self.user)
        
        # Verify analytics reflect the completion
        self.assertEqual(analytics.total_practice_completed, 1)
        self.assertEqual(analytics.average_score, 100.0)
        self.assertEqual(analytics.total_time_spent, 5)  # 300 seconds = 5 minutes
        self.assertIsNotNone(analytics.last_activity)
        
        # Verify concept mastery
        self.assertIn('algorithms', analytics.concept_mastery)
        self.assertEqual(analytics.concept_mastery['algorithms'], 100.0)
    
    def test_analytics_with_points_integration(self):
        """Test analytics integration with points system."""
        # Create user points
        UserPoints.objects.create(
            user=self.user,
            total_points=150,
            practice_points=100,
            assignment_points=50
        )
        
        # Get performance summary
        summary = self.aggregator.get_student_performance_summary(self.user)
        
        # Verify points are included in summary
        self.assertEqual(summary['points']['total_points'], 150)
        self.assertEqual(summary['points']['practice_points'], 100)
        self.assertEqual(summary['points']['assignment_points'], 50)