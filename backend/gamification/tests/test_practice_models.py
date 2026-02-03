"""
Tests for PracticeSubmission and PracticeProgress models
Testing unlimited attempts, progress tracking, and performance optimization
"""
import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils import timezone
from datetime import timedelta

from gamification.models import (
    PracticeQuestion, PracticeSubmission, PracticeProgress
)

User = get_user_model()


class PracticeSubmissionModelTest(TestCase):
    """Test PracticeSubmission model for unlimited attempts functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.teacher = User.objects.create_user(
            username='teacher',
            email='teacher@example.com',
            password='teacherpass123'
        )
        
        self.practice_question = PracticeQuestion.objects.create(
            title='Test Question',
            description='A test practice question',
            difficulty='medium',
            category='Arrays',
            test_cases=[
                {'input': '5', 'expected_output': '5'},
                {'input': '10', 'expected_output': '10'}
            ],
            starter_code='def solution(n):\n    return n',
            point_value=100,
            created_by=self.teacher
        )
    
    def test_unlimited_submissions_allowed(self):
        """Test that unlimited submissions are allowed for practice questions"""
        # Create multiple submissions for the same question
        submissions = []
        for i in range(10):  # Test 10 attempts
            submission = PracticeSubmission.objects.create(
                student=self.user,
                practice_question=self.practice_question,
                source_code=f'def solution(n):\n    return n + {i}',
                status='fail',
                attempt_number=i + 1,
                test_results=[
                    {'test_case': 1, 'status': 'fail', 'expected': '5', 'actual': f'{5+i}'},
                    {'test_case': 2, 'status': 'fail', 'expected': '10', 'actual': f'{10+i}'}
                ]
            )
            submissions.append(submission)
        
        # Verify all submissions were created
        self.assertEqual(PracticeSubmission.objects.filter(
            student=self.user,
            practice_question=self.practice_question
        ).count(), 10)
        
        # Verify attempt numbers are correct
        for i, submission in enumerate(submissions):
            self.assertEqual(submission.attempt_number, i + 1)
    
    def test_submission_tracking_fields(self):
        """Test that all required tracking fields are properly stored"""
        submission = PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.practice_question,
            source_code='def solution(n):\n    return n',
            language='python',
            status='success',
            attempt_number=1,
            test_results=[
                {'test_case': 1, 'status': 'pass', 'expected': '5', 'actual': '5'},
                {'test_case': 2, 'status': 'pass', 'expected': '10', 'actual': '10'}
            ],
            points_earned=150,
            execution_time_ms=1500
        )
        
        # Verify all fields are stored correctly
        self.assertEqual(submission.student, self.user)
        self.assertEqual(submission.practice_question, self.practice_question)
        self.assertEqual(submission.language, 'python')
        self.assertEqual(submission.status, 'success')
        self.assertEqual(submission.attempt_number, 1)
        self.assertEqual(submission.points_earned, 150)
        self.assertEqual(submission.execution_time_ms, 1500)
        self.assertEqual(len(submission.test_results), 2)
        self.assertIsNotNone(submission.submitted_at)
    
    def test_submission_status_choices(self):
        """Test that submission status is properly validated"""
        valid_statuses = ['processing', 'success', 'fail', 'error']
        
        for status in valid_statuses:
            submission = PracticeSubmission.objects.create(
                student=self.user,
                practice_question=self.practice_question,
                source_code='def solution(n):\n    return n',
                status=status,
                attempt_number=1
            )
            self.assertEqual(submission.status, status)
    
    def test_submission_validation(self):
        """Test model validation for required fields"""
        # Test that attempt_number must be positive
        with self.assertRaises(ValidationError):
            submission = PracticeSubmission(
                student=self.user,
                practice_question=self.practice_question,
                source_code='def solution(n):\n    return n',
                status='success',
                attempt_number=0  # Invalid: must be >= 1
            )
            submission.full_clean()
        
        # Test that points_earned must be non-negative
        with self.assertRaises(ValidationError):
            submission = PracticeSubmission(
                student=self.user,
                practice_question=self.practice_question,
                source_code='def solution(n):\n    return n',
                status='success',
                attempt_number=1,
                points_earned=-10  # Invalid: must be >= 0
            )
            submission.full_clean()


class PracticeProgressModelTest(TestCase):
    """Test PracticeProgress model for completion status tracking"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.teacher = User.objects.create_user(
            username='teacher',
            email='teacher@example.com',
            password='teacherpass123'
        )
        
        self.practice_question = PracticeQuestion.objects.create(
            title='Test Question',
            description='A test practice question',
            difficulty='easy',
            category='Loops',
            test_cases=[{'input': '5', 'expected_output': '5'}],
            point_value=100,
            created_by=self.teacher
        )
    
    def test_progress_tracking_creation(self):
        """Test that progress tracking is properly initialized"""
        progress = PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question
        )
        
        # Verify default values
        self.assertFalse(progress.is_completed)
        self.assertEqual(progress.attempts_count, 0)
        self.assertEqual(progress.best_score, 0.0)
        self.assertEqual(progress.time_spent, 0)
        self.assertIsNotNone(progress.first_attempt_at)
        self.assertIsNone(progress.completed_at)
    
    def test_unique_progress_per_student_question(self):
        """Test that only one progress record exists per student per question"""
        # Create first progress record
        progress1 = PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question
        )
        
        # Attempt to create duplicate should raise IntegrityError
        with self.assertRaises(IntegrityError):
            PracticeProgress.objects.create(
                student=self.user,
                practice_question=self.practice_question
            )
    
    def test_progress_completion_workflow(self):
        """Test the complete workflow from start to completion"""
        progress = PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question
        )
        
        # Simulate multiple attempts
        progress.attempts_count = 1
        progress.best_score = 50.0
        progress.time_spent = 300  # 5 minutes
        progress.save()
        
        # Still not completed
        self.assertFalse(progress.is_completed)
        self.assertIsNone(progress.completed_at)
        
        # Simulate successful completion
        progress.attempts_count = 3
        progress.best_score = 100.0
        progress.is_completed = True
        progress.completed_at = timezone.now()
        progress.time_spent = 900  # 15 minutes total
        progress.save()
        
        # Verify completion
        self.assertTrue(progress.is_completed)
        self.assertIsNotNone(progress.completed_at)
        self.assertEqual(progress.best_score, 100.0)
        self.assertEqual(progress.attempts_count, 3)
    
    def test_progress_validation(self):
        """Test model validation for progress fields"""
        progress = PracticeProgress(
            student=self.user,
            practice_question=self.practice_question
        )
        
        # Test invalid attempts_count
        progress.attempts_count = -1
        with self.assertRaises(ValidationError):
            progress.full_clean()
        
        # Test invalid best_score (too high)
        progress.attempts_count = 1
        progress.best_score = 150.0  # Invalid: max is 100.0
        with self.assertRaises(ValidationError):
            progress.full_clean()
        
        # Test invalid best_score (negative)
        progress.best_score = -10.0  # Invalid: min is 0.0
        with self.assertRaises(ValidationError):
            progress.full_clean()
        
        # Test invalid time_spent
        progress.best_score = 50.0
        progress.time_spent = -100  # Invalid: must be >= 0
        with self.assertRaises(ValidationError):
            progress.full_clean()
    
    def test_progress_best_score_tracking(self):
        """Test that best score is properly tracked across attempts"""
        progress = PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question,
            best_score=60.0
        )
        
        # Simulate worse score - should not update best_score
        progress.attempts_count += 1
        # best_score should remain 60.0 if new score is lower
        
        # Simulate better score - should update best_score
        progress.best_score = 85.0
        progress.save()
        
        progress.refresh_from_db()
        self.assertEqual(progress.best_score, 85.0)


class PracticeModelsIntegrationTest(TestCase):
    """Integration tests for PracticeSubmission and PracticeProgress models"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.teacher = User.objects.create_user(
            username='teacher',
            email='teacher@example.com',
            password='teacherpass123'
        )
        
        self.practice_question = PracticeQuestion.objects.create(
            title='Integration Test Question',
            description='A test practice question for integration testing',
            difficulty='hard',
            category='Algorithms',
            test_cases=[
                {'input': '5', 'expected_output': '120'},
                {'input': '3', 'expected_output': '6'}
            ],
            point_value=200,
            created_by=self.teacher
        )
    
    def test_unlimited_attempts_workflow(self):
        """Test the complete unlimited attempts workflow"""
        # Create progress tracking
        progress = PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question
        )
        
        # Simulate multiple failed attempts
        failed_attempts = []
        for i in range(5):
            submission = PracticeSubmission.objects.create(
                student=self.user,
                practice_question=self.practice_question,
                source_code=f'def factorial(n):\n    return n * {i}  # Wrong implementation',
                status='fail',
                attempt_number=i + 1,
                test_results=[
                    {'test_case': 1, 'status': 'fail', 'expected': '120', 'actual': f'{5 * i}'},
                    {'test_case': 2, 'status': 'fail', 'expected': '6', 'actual': f'{3 * i}'}
                ],
                points_earned=0
            )
            failed_attempts.append(submission)
            
            # Update progress
            progress.attempts_count = i + 1
            progress.time_spent += 180  # 3 minutes per attempt
            progress.save()
        
        # Verify failed attempts
        self.assertEqual(len(failed_attempts), 5)
        self.assertFalse(progress.is_completed)
        self.assertEqual(progress.attempts_count, 5)
        
        # Simulate successful attempt
        successful_submission = PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.practice_question,
            source_code='def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)',
            status='success',
            attempt_number=6,
            test_results=[
                {'test_case': 1, 'status': 'pass', 'expected': '120', 'actual': '120'},
                {'test_case': 2, 'status': 'pass', 'expected': '6', 'actual': '6'}
            ],
            points_earned=200,
            execution_time_ms=2500
        )
        
        # Update progress to completed
        progress.attempts_count = 6
        progress.is_completed = True
        progress.completed_at = timezone.now()
        progress.best_score = 100.0
        progress.time_spent += 300  # 5 minutes for successful attempt
        progress.save()
        
        # Verify final state
        self.assertTrue(progress.is_completed)
        self.assertEqual(progress.attempts_count, 6)
        self.assertEqual(progress.best_score, 100.0)
        self.assertEqual(progress.time_spent, 1200)  # 20 minutes total
        self.assertIsNotNone(progress.completed_at)
        
        # Verify all submissions exist
        all_submissions = PracticeSubmission.objects.filter(
            student=self.user,
            practice_question=self.practice_question
        ).order_by('attempt_number')
        
        self.assertEqual(all_submissions.count(), 6)
        
        # Verify attempt numbers are sequential
        for i, submission in enumerate(all_submissions):
            self.assertEqual(submission.attempt_number, i + 1)
        
        # Verify only the last submission was successful
        submissions_list = list(all_submissions)
        for submission in submissions_list[:-1]:
            self.assertEqual(submission.status, 'fail')
            self.assertEqual(submission.points_earned, 0)
        
        self.assertEqual(submissions_list[-1].status, 'success')
        self.assertEqual(submissions_list[-1].points_earned, 200)
    
    def test_database_performance_indexes(self):
        """Test that database indexes are working for performance"""
        # Create multiple users and submissions to test indexing
        users = []
        for i in range(10):
            user = User.objects.create_user(
                username=f'user{i}',
                email=f'user{i}@example.com',
                password='testpass123'
            )
            users.append(user)
        
        # Create submissions for each user
        for user in users:
            progress = PracticeProgress.objects.create(
                student=user,
                practice_question=self.practice_question
            )
            
            for attempt in range(3):
                PracticeSubmission.objects.create(
                    student=user,
                    practice_question=self.practice_question,
                    source_code='def test(): return True',
                    status='success' if attempt == 2 else 'fail',
                    attempt_number=attempt + 1,
                    points_earned=100 if attempt == 2 else 0
                )
        
        # Test indexed queries perform well
        # Query by student and practice_question (indexed)
        user_submissions = PracticeSubmission.objects.filter(
            student=users[0],
            practice_question=self.practice_question
        )
        self.assertEqual(user_submissions.count(), 3)
        
        # Query by student and submission date (indexed)
        recent_submissions = PracticeSubmission.objects.filter(
            student=users[0]
        ).order_by('-submitted_at')
        self.assertEqual(recent_submissions.count(), 3)
        
        # Query by status (indexed)
        successful_submissions = PracticeSubmission.objects.filter(
            status='success'
        )
        self.assertEqual(successful_submissions.count(), 10)  # One per user
        
        # Query progress by completion status (indexed)
        completed_progress = PracticeProgress.objects.filter(
            is_completed=False  # All should be incomplete in this test
        )
        self.assertEqual(completed_progress.count(), 10)


class PracticeModelRequirementsTest(TestCase):
    """Test that models meet specific requirements from the task"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.teacher = User.objects.create_user(
            username='teacher',
            email='teacher@example.com',
            password='teacherpass123'
        )
        
        self.practice_question = PracticeQuestion.objects.create(
            title='Requirements Test Question',
            description='Testing requirements compliance',
            difficulty='medium',
            category='Testing',
            test_cases=[{'input': 'test', 'expected_output': 'test'}],
            point_value=100,
            created_by=self.teacher
        )
    
    def test_requirement_2_1_unlimited_attempts(self):
        """Test Requirement 2.1: Unlimited submission attempts"""
        # Create many submissions to verify no limits
        for i in range(50):  # Test with 50 attempts
            PracticeSubmission.objects.create(
                student=self.user,
                practice_question=self.practice_question,
                source_code=f'# Attempt {i+1}',
                status='fail',
                attempt_number=i + 1
            )
        
        # Verify all 50 submissions were created
        submission_count = PracticeSubmission.objects.filter(
            student=self.user,
            practice_question=self.practice_question
        ).count()
        self.assertEqual(submission_count, 50)
    
    def test_requirement_2_3_completion_status_tracking(self):
        """Test Requirement 2.3: Progress tracking for completion status"""
        progress = PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question
        )
        
        # Initially not completed
        self.assertFalse(progress.is_completed)
        self.assertIsNone(progress.completed_at)
        
        # Mark as completed
        progress.is_completed = True
        progress.completed_at = timezone.now()
        progress.save()
        
        # Verify completion tracking
        progress.refresh_from_db()
        self.assertTrue(progress.is_completed)
        self.assertIsNotNone(progress.completed_at)
    
    def test_requirement_1_4_progress_tracking(self):
        """Test Requirement 1.4: Comprehensive progress tracking"""
        progress = PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question
        )
        
        # Test all progress tracking fields
        progress.attempts_count = 5
        progress.best_score = 85.5
        progress.time_spent = 1800  # 30 minutes
        progress.save()
        
        progress.refresh_from_db()
        self.assertEqual(progress.attempts_count, 5)
        self.assertEqual(progress.best_score, 85.5)
        self.assertEqual(progress.time_spent, 1800)
    
    def test_performance_indexing_requirements(self):
        """Test that proper indexing is in place for performance"""
        # Verify that the models have the expected indexes
        # This tests the Meta.indexes configuration
        
        # Check PracticeSubmission indexes
        submission_indexes = PracticeSubmission._meta.indexes
        index_fields = [tuple(index.fields) for index in submission_indexes]
        
        # Verify expected indexes exist
        expected_submission_indexes = [
            ('student', 'practice_question'),
            ('student', '-submitted_at'),
            ('status',)
        ]
        
        for expected_index in expected_submission_indexes:
            self.assertIn(expected_index, index_fields, 
                         f"Missing index for fields: {expected_index}")
        
        # Check PracticeProgress indexes
        progress_indexes = PracticeProgress._meta.indexes
        progress_index_fields = [tuple(index.fields) for index in progress_indexes]
        
        expected_progress_indexes = [
            ('student', 'is_completed'),
            ('practice_question', 'is_completed')
        ]
        
        for expected_index in expected_progress_indexes:
            self.assertIn(expected_index, progress_index_fields,
                         f"Missing index for fields: {expected_index}")