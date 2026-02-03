"""
Tests for ClassAnalyticsService - comprehensive class analytics and reporting.

This module tests:
- Comprehensive class analytics calculation
- Struggling student identification
- Problem-specific analytics
- Report generation (CSV and JSON)
- Engagement metrics and insights
"""

import json
import uuid
from datetime import datetime, timedelta
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from unittest.mock import patch, MagicMock

from ..class_analytics_service import ClassAnalyticsService, class_analytics_service
from ..models import (
    StudentAnalytics, PracticeSubmission, PracticeProgress, 
    PracticeQuestion, UserPoints
)

User = get_user_model()


class ClassAnalyticsServiceTest(TestCase):
    """Test cases for ClassAnalyticsService functionality."""
    
    def setUp(self):
        """Set up test data."""
        # Create test users
        self.teacher = User.objects.create_user(
            username='teacher1',
            email='teacher@test.com',
            password='testpass123',
            role='teacher',
            first_name='Test',
            last_name='Teacher'
        )
        
        self.students = []
        for i in range(5):
            student = User.objects.create_user(
                username=f'student{i+1}',
                email=f'student{i+1}@test.com',
                password='testpass123',
                role='student',
                first_name=f'Student',
                last_name=f'{i+1}'
            )
            self.students.append(student)
        
        # Create mock class object
        self.mock_class = MagicMock()
        self.mock_class.id = uuid.uuid4()
        self.mock_class.name = 'Test Class'
        
        # Create practice questions
        self.practice_questions = []
        categories = ['loops', 'conditionals', 'functions']
        difficulties = ['easy', 'medium', 'hard']
        
        for i in range(6):
            question = PracticeQuestion.objects.create(
                title=f'Practice Question {i+1}',
                description=f'Test question {i+1}',
                category=categories[i % 3],
                difficulty=difficulties[i % 3],
                point_value=10 * (i % 3 + 1),
                test_cases=[{'input': 'test', 'expected_output': 'test'}],
                created_by=self.teacher
            )
            self.practice_questions.append(question)
        
        # Create analytics service
        self.service = ClassAnalyticsService()
    
    def _create_student_analytics(self, student, **kwargs):
        """Helper to create student analytics with defaults."""
        defaults = {
            'total_practice_completed': 5,
            'total_assignments_completed': 3,
            'average_score': 75.0,
            'current_streak': 3,
            'longest_streak': 5,
            'total_time_spent': 120,
            'last_activity': timezone.now(),
            'performance_trend': [],
            'concept_mastery': {'loops': 80.0, 'conditionals': 70.0}
        }
        defaults.update(kwargs)
        
        return StudentAnalytics.objects.create(
            student=student,
            **defaults
        )
    
    def _create_practice_progress(self, student, question, **kwargs):
        """Helper to create practice progress."""
        defaults = {
            'attempts_count': 2,
            'best_score': 100.0,
            'is_completed': True,
            'time_spent': 300,
            'completed_at': timezone.now()
        }
        defaults.update(kwargs)
        
        return PracticeProgress.objects.create(
            student=student,
            practice_question=question,
            **defaults
        )
    
    @patch('classes.models.Enrollment')
    def test_comprehensive_class_analytics_with_students(self, mock_enrollment):
        """Test comprehensive class analytics calculation with students."""
        # Mock enrollment to return our test students
        mock_enrollment.objects.filter.return_value.select_related.return_value = [
            MagicMock(user=student) for student in self.students
        ]
        
        # Create analytics for students with varying performance
        analytics_data = [
            {'average_score': 90.0, 'current_streak': 7, 'total_practice_completed': 10},
            {'average_score': 75.0, 'current_streak': 3, 'total_practice_completed': 6},
            {'average_score': 45.0, 'current_streak': 0, 'total_practice_completed': 2},  # Struggling
            {'average_score': 85.0, 'current_streak': 5, 'total_practice_completed': 8},
            {'average_score': 30.0, 'current_streak': 0, 'total_practice_completed': 1},  # Struggling
        ]
        
        for i, student in enumerate(self.students):
            self._create_student_analytics(student, **analytics_data[i])
        
        # Create some practice progress
        for i, student in enumerate(self.students[:3]):
            for j, question in enumerate(self.practice_questions[:2]):
                completed = i < 2  # First two students complete questions
                self._create_practice_progress(
                    student, question, 
                    is_completed=completed,
                    attempts_count=j + 1
                )
        
        # Get comprehensive analytics
        result = self.service.get_comprehensive_class_analytics(self.mock_class)
        
        # Verify structure
        self.assertIn('class_info', result)
        self.assertIn('performance_metrics', result)
        self.assertIn('struggling_students', result)
        self.assertIn('engagement_metrics', result)
        self.assertIn('problem_analytics', result)
        self.assertIn('time_analytics', result)
        self.assertIn('progress_distribution', result)
        
        # Verify class info
        class_info = result['class_info']
        self.assertEqual(class_info['total_students'], 5)
        self.assertEqual(class_info['class_name'], 'Test Class')
        
        # Verify performance metrics
        performance = result['performance_metrics']
        self.assertIn('averages', performance)
        self.assertIn('score_distribution', performance)
        self.assertIn('top_performers', performance)
        
        # Check averages calculation
        averages = performance['averages']
        expected_avg_score = (90 + 75 + 45 + 85 + 30) / 5  # 65.0
        self.assertEqual(averages['average_score'], expected_avg_score)
        
        # Verify struggling students identification
        struggling = result['struggling_students']
        self.assertEqual(len(struggling), 2)  # Two students with low scores
        
        # Check that struggling students have correct indicators
        struggling_scores = [s['average_score'] for s in struggling]
        self.assertIn(45.0, struggling_scores)
        self.assertIn(30.0, struggling_scores)
        
        # Verify problem analytics
        problem_analytics = result['problem_analytics']
        self.assertIn('problem_statistics', problem_analytics)
        self.assertIn('category_performance', problem_analytics)
    
    @patch('classes.models.Enrollment')
    def test_empty_class_analytics(self, mock_enrollment):
        """Test analytics for empty class."""
        # Mock empty enrollment
        mock_enrollment.objects.filter.return_value.select_related.return_value = []
        
        result = self.service.get_comprehensive_class_analytics(self.mock_class)
        
        # Verify empty class structure
        self.assertEqual(result['class_info']['total_students'], 0)
        self.assertEqual(result['class_info']['active_students'], 0)
        self.assertEqual(result['class_info']['class_name'], 'Empty Class')
        self.assertEqual(result['struggling_students'], [])
        self.assertEqual(result['performance_metrics'], {})
    
    @patch('classes.models.Enrollment')
    def test_struggling_student_identification(self, mock_enrollment):
        """Test sophisticated struggling student identification."""
        # Mock enrollment
        mock_enrollment.objects.filter.return_value.select_related.return_value = [
            MagicMock(user=student) for student in self.students[:3]
        ]
        
        # Create students with different struggle patterns
        old_date = timezone.now() - timedelta(days=10)
        
        # Student 1: Low score
        self._create_student_analytics(
            self.students[0], 
            average_score=40.0,
            total_practice_completed=5,
            last_activity=timezone.now()
        )
        
        # Student 2: Low completion + inactive
        self._create_student_analytics(
            self.students[1], 
            average_score=70.0,
            total_practice_completed=1,
            last_activity=old_date
        )
        
        # Student 3: No analytics (completely inactive)
        # Don't create analytics for this student
        
        result = self.service.get_comprehensive_class_analytics(self.mock_class)
        struggling = result['struggling_students']
        
        # Should identify all 3 as struggling
        self.assertEqual(len(struggling), 3)
        
        # Check struggle indicators
        indicators_found = set()
        for student in struggling:
            indicators_found.update(student['struggle_indicators'])
        
        expected_indicators = {'low_score', 'low_completion', 'inactive', 'no_activity', 'no_streak'}
        self.assertTrue(indicators_found.intersection(expected_indicators))
        
        # Check recommendations are provided
        for student in struggling:
            self.assertIn('recommendations', student)
            self.assertIsInstance(student['recommendations'], list)
            self.assertGreater(len(student['recommendations']), 0)
    
    @patch('classes.models.Enrollment')
    def test_engagement_metrics_calculation(self, mock_enrollment):
        """Test engagement metrics calculation."""
        # Mock enrollment
        mock_enrollment.objects.filter.return_value.select_related.return_value = [
            MagicMock(user=student) for student in self.students[:3]
        ]
        
        # Create analytics with different activity patterns
        now = timezone.now()
        
        # Recent activity (last 24h)
        self._create_student_analytics(
            self.students[0], 
            last_activity=now - timedelta(hours=12)
        )
        
        # Week old activity
        self._create_student_analytics(
            self.students[1], 
            last_activity=now - timedelta(days=5)
        )
        
        # Old activity (month old)
        self._create_student_analytics(
            self.students[2], 
            last_activity=now - timedelta(days=20)
        )
        
        result = self.service.get_comprehensive_class_analytics(self.mock_class)
        engagement = result['engagement_metrics']
        
        # Verify engagement structure
        self.assertIn('activity_periods', engagement)
        self.assertIn('submission_metrics', engagement)
        self.assertIn('overall_engagement_score', engagement)
        
        # Check activity periods
        periods = engagement['activity_periods']
        self.assertIn('last_24h', periods)
        self.assertIn('last_week', periods)
        self.assertIn('last_month', periods)
        
        # Verify engagement rates
        self.assertEqual(periods['last_24h']['active_students'], 1)
        self.assertEqual(periods['last_week']['active_students'], 2)
        self.assertEqual(periods['last_month']['active_students'], 3)
        
        # Check engagement score is calculated
        self.assertIsInstance(engagement['overall_engagement_score'], float)
        self.assertGreaterEqual(engagement['overall_engagement_score'], 0)
        self.assertLessEqual(engagement['overall_engagement_score'], 100)
    
    @patch('classes.models.Enrollment')
    def test_problem_performance_analysis(self, mock_enrollment):
        """Test problem-specific performance analysis."""
        # Mock enrollment
        mock_enrollment.objects.filter.return_value.select_related.return_value = [
            MagicMock(user=student) for student in self.students[:2]
        ]
        
        # Create analytics
        for student in self.students[:2]:
            self._create_student_analytics(student)
        
        # Create progress with different completion rates
        # Question 1: High completion rate
        for student in self.students[:2]:
            self._create_practice_progress(
                student, self.practice_questions[0],
                is_completed=True, attempts_count=1
            )
        
        # Question 2: Low completion rate (only 1 student completes)
        self._create_practice_progress(
            self.students[0], self.practice_questions[1],
            is_completed=True, attempts_count=3
        )
        self._create_practice_progress(
            self.students[1], self.practice_questions[1],
            is_completed=False, attempts_count=5
        )
        
        result = self.service.get_comprehensive_class_analytics(self.mock_class)
        problem_analytics = result['problem_analytics']
        
        # Verify structure
        self.assertIn('problem_statistics', problem_analytics)
        self.assertIn('category_performance', problem_analytics)
        self.assertIn('most_difficult_problems', problem_analytics)
        self.assertIn('easiest_problems', problem_analytics)
        
        # Check problem statistics
        stats = problem_analytics['problem_statistics']
        self.assertGreater(len(stats), 0)
        
        # Verify completion rates are calculated
        for stat in stats:
            self.assertIn('completion_rate', stat['stats'])
            self.assertIn('avg_attempts_to_complete', stat['stats'])
            self.assertIn('avg_time_minutes', stat['stats'])
    
    @patch('classes.models.Enrollment')
    def test_csv_report_generation(self, mock_enrollment):
        """Test CSV report generation."""
        # Mock enrollment
        mock_enrollment.objects.filter.return_value.select_related.return_value = [
            MagicMock(user=student) for student in self.students[:2]
        ]
        
        # Create test data
        for student in self.students[:2]:
            self._create_student_analytics(student)
        
        # Generate CSV report
        response = self.service.generate_class_report(self.mock_class, 'csv')
        
        # Verify response
        self.assertEqual(response['Content-Type'], 'text/csv')
        self.assertIn('attachment', response['Content-Disposition'])
        
        # Check content contains expected sections
        content = response.content.decode('utf-8')
        self.assertIn('Class Analytics Report', content)
        self.assertIn('Class Performance Metrics', content)
        self.assertIn('Struggling Students', content)
        self.assertIn('Problem Performance', content)
    
    @patch('classes.models.Enrollment')
    def test_json_report_generation(self, mock_enrollment):
        """Test JSON report generation."""
        # Mock enrollment
        mock_enrollment.objects.filter.return_value.select_related.return_value = [
            MagicMock(user=student) for student in self.students[:2]
        ]
        
        # Create test data
        for student in self.students[:2]:
            self._create_student_analytics(student)
        
        # Generate JSON report
        response = self.service.generate_class_report(self.mock_class, 'json')
        
        # Verify response
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertIn('attachment', response['Content-Disposition'])
        
        # Parse and verify JSON content
        content = json.loads(response.content.decode('utf-8'))
        self.assertIn('metadata', content)
        self.assertIn('analytics', content)
        
        # Check metadata
        metadata = content['metadata']
        self.assertEqual(metadata['report_type'], 'class_analytics')
        self.assertIn('generated_at', metadata)
        self.assertEqual(metadata['class_id'], str(self.mock_class.id))
    
    def test_invalid_report_format(self):
        """Test error handling for invalid report format."""
        with self.assertRaises(ValueError):
            self.service.generate_class_report(self.mock_class, 'xml')
    
    @patch('classes.models.Enrollment')
    def test_progress_distribution_calculation(self, mock_enrollment):
        """Test progress distribution calculation."""
        # Mock enrollment
        mock_enrollment.objects.filter.return_value.select_related.return_value = [
            MagicMock(user=student) for student in self.students
        ]
        
        # Create students with different progress levels
        progress_levels = [
            {'total_practice_completed': 1, 'total_assignments_completed': 0},  # Beginner
            {'total_practice_completed': 5, 'total_assignments_completed': 2},  # Intermediate
            {'total_practice_completed': 12, 'total_assignments_completed': 8},  # Advanced
            {'total_practice_completed': 0, 'total_assignments_completed': 1},  # Beginner
            # Student 5 has no analytics (inactive)
        ]
        
        for i, student in enumerate(self.students[:4]):
            self._create_student_analytics(student, **progress_levels[i])
        
        result = self.service.get_comprehensive_class_analytics(self.mock_class)
        distribution = result['progress_distribution']
        
        # Verify distribution
        self.assertEqual(distribution['beginners'], 2)  # 0-2 completed
        self.assertEqual(distribution['intermediate'], 1)  # 3-9 completed
        self.assertEqual(distribution['advanced'], 1)  # 10+ completed
        self.assertEqual(distribution['inactive'], 1)  # No analytics
    
    def test_global_service_instance(self):
        """Test that global service instance is available."""
        self.assertIsInstance(class_analytics_service, ClassAnalyticsService)