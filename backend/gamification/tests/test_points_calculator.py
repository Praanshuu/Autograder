"""
Unit tests for the PointsCalculator class.

Tests cover:
- Practice question point calculations with difficulty multipliers
- Assignment point calculations with proportional scoring
- Bonus point calculations for first attempts and speed
- Point awarding and user point updates
"""

from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model
from django.db import transaction
from unittest.mock import patch, MagicMock

from gamification.models import (
    UserPoints, PracticeQuestion, PracticeSubmission, PracticeProgress
)
from gamification.points_calculator import PointsCalculator
from assignments.models import AssignmentQuestion, Assignment, Question

User = get_user_model()


@override_settings(
    # Disable signals during testing to avoid interference
    GAMIFICATION_SIGNALS_ENABLED=False
)
class PointsCalculatorTestCase(TestCase):
    """Test cases for PointsCalculator functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.calculator = PointsCalculator()
        
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            role='student'
        )
        
        # Create test practice questions with different difficulties
        self.easy_question = PracticeQuestion.objects.create(
            title='Easy Test Question',
            description='An easy practice question',
            difficulty='easy',
            category='Arrays',
            test_cases=[{'input': '1', 'output': '1'}],
            point_value=100,
            created_by=self.user
        )
        
        self.medium_question = PracticeQuestion.objects.create(
            title='Medium Test Question',
            description='A medium practice question',
            difficulty='medium',
            category='Algorithms',
            test_cases=[{'input': '2', 'output': '4'}],
            point_value=150,
            created_by=self.user
        )
        
        self.hard_question = PracticeQuestion.objects.create(
            title='Hard Test Question',
            description='A hard practice question',
            difficulty='hard',
            category='Dynamic Programming',
            test_cases=[{'input': '3', 'output': '9'}],
            point_value=200,
            created_by=self.user
        )
    
    def test_difficulty_multipliers(self):
        """Test that difficulty multipliers are applied correctly"""
        # Test easy question (1.0x multiplier)
        easy_points = self.calculator.calculate_practice_points(
            question=self.easy_question,
            attempt_number=2  # Not first attempt to isolate difficulty multiplier
        )
        expected_easy = int(100 * 1.0)  # Base points * easy multiplier
        self.assertEqual(easy_points, expected_easy)
        
        # Test medium question (1.5x multiplier)
        medium_points = self.calculator.calculate_practice_points(
            question=self.medium_question,
            attempt_number=2
        )
        expected_medium = int(100 * 1.5)  # Base points * medium multiplier
        self.assertEqual(medium_points, expected_medium)
        
        # Test hard question (2.0x multiplier)
        hard_points = self.calculator.calculate_practice_points(
            question=self.hard_question,
            attempt_number=2
        )
        expected_hard = int(100 * 2.0)  # Base points * hard multiplier
        self.assertEqual(hard_points, expected_hard)
    
    def test_first_attempt_bonus(self):
        """Test that first attempt bonus is applied correctly"""
        # First attempt should get bonus
        first_attempt_points = self.calculator.calculate_practice_points(
            question=self.easy_question,
            attempt_number=1
        )
        
        # Second attempt should not get bonus
        second_attempt_points = self.calculator.calculate_practice_points(
            question=self.easy_question,
            attempt_number=2
        )
        
        # First attempt should have more points due to bonus
        self.assertGreater(first_attempt_points, second_attempt_points)
        
        # Bonus should be 25% of base points
        base_points = int(100 * 1.0)  # Easy question base points
        expected_bonus = int(base_points * 0.25)
        expected_first_attempt = base_points + expected_bonus
        
        self.assertEqual(first_attempt_points, expected_first_attempt)
    
    def test_speed_bonus_completion_time(self):
        """Test speed bonus based on completion time"""
        # Fast completion (under 50% of expected time)
        fast_completion_time = 120  # 2 minutes for easy question (expected: 5 minutes)
        fast_points = self.calculator.calculate_practice_points(
            question=self.easy_question,
            attempt_number=2,  # Not first attempt to isolate speed bonus
            completion_time_seconds=fast_completion_time
        )
        
        # Slow completion (over 50% of expected time)
        slow_completion_time = 400  # 6.67 minutes for easy question
        slow_points = self.calculator.calculate_practice_points(
            question=self.easy_question,
            attempt_number=2,
            completion_time_seconds=slow_completion_time
        )
        
        # Fast completion should get speed bonus
        self.assertGreater(fast_points, slow_points)
        self.assertEqual(fast_points - slow_points, 20)  # Speed bonus amount
    
    def test_speed_bonus_execution_time(self):
        """Test speed bonus based on execution time"""
        # Fast execution (under 50% of expected time)
        fast_execution_time = 2000  # 2 seconds for easy question (expected: 5 seconds)
        fast_points = self.calculator.calculate_practice_points(
            question=self.easy_question,
            attempt_number=2,
            execution_time_ms=fast_execution_time
        )
        
        # Slow execution (over 50% of expected time)
        slow_execution_time = 6000  # 6 seconds for easy question
        slow_points = self.calculator.calculate_practice_points(
            question=self.easy_question,
            attempt_number=2,
            execution_time_ms=slow_execution_time
        )
        
        # Fast execution should get speed bonus
        self.assertGreater(fast_points, slow_points)
        self.assertEqual(fast_points - slow_points, 20)  # Speed bonus amount
    
    def test_assignment_points_calculation(self):
        """Test assignment points calculation based on test results"""
        # All tests pass
        all_pass_results = [
            {'status': 'pass'},
            {'status': 'pass'},
            {'status': 'pass'}
        ]
        all_pass_points = self.calculator.calculate_assignment_points(
            test_results=all_pass_results,
            attempt_number=1
        )
        
        # Expected: (3 * 10) + 50 (perfect bonus) + 25 (first attempt bonus) = 105
        expected_all_pass = (3 * 10) + 50 + 25
        self.assertEqual(all_pass_points, expected_all_pass)
        
        # Partial pass
        partial_pass_results = [
            {'status': 'pass'},
            {'status': 'fail'},
            {'status': 'pass'}
        ]
        partial_pass_points = self.calculator.calculate_assignment_points(
            test_results=partial_pass_results,
            attempt_number=1
        )
        
        # Expected: (2 * 10) + 25 (first attempt bonus) = 45 (no perfect bonus)
        expected_partial_pass = (2 * 10) + 25
        self.assertEqual(partial_pass_points, expected_partial_pass)
        
        # No tests pass
        no_pass_results = [
            {'status': 'fail'},
            {'status': 'fail'},
            {'status': 'fail'}
        ]
        no_pass_points = self.calculator.calculate_assignment_points(
            test_results=no_pass_results,
            attempt_number=1
        )
        
        # Expected: 0 (no points for failed tests, no bonuses)
        self.assertEqual(no_pass_points, 0)
    
    def test_update_user_points(self):
        """Test user points updating functionality"""
        # Initial state - no points
        initial_summary = self.calculator.get_user_points_summary(self.user)
        self.assertEqual(initial_summary['total_points'], 0)
        self.assertEqual(initial_summary['practice_points'], 0)
        self.assertEqual(initial_summary['assignment_points'], 0)
        
        # Add practice points
        total_points, points_added = self.calculator.update_user_points(
            user=self.user,
            points_to_add=100,
            point_type='practice'
        )
        
        self.assertEqual(points_added, 100)
        self.assertEqual(total_points, 100)
        
        # Add assignment points
        total_points, points_added = self.calculator.update_user_points(
            user=self.user,
            points_to_add=50,
            point_type='assignment'
        )
        
        self.assertEqual(points_added, 50)
        self.assertEqual(total_points, 150)
        
        # Verify final state
        final_summary = self.calculator.get_user_points_summary(self.user)
        self.assertEqual(final_summary['total_points'], 150)
        self.assertEqual(final_summary['practice_points'], 100)
        self.assertEqual(final_summary['assignment_points'], 50)
    
    def test_calculate_and_award_practice_points(self):
        """Test complete practice points calculation and awarding"""
        # Create a successful practice submission without triggering signals
        submission = PracticeSubmission(
            student=self.user,
            practice_question=self.easy_question,
            source_code='print("test")',
            status='success',
            attempt_number=1,
            execution_time_ms=2000  # Fast execution for bonus
        )
        # Save without triggering post_save signal
        with patch('django.db.models.signals.post_save.send'):
            submission.save()
        
        # Award points manually
        points_awarded = self.calculator.calculate_and_award_practice_points(
            submission=submission,
            completion_time_seconds=120  # Fast completion for bonus
        )
        
        # Verify points were calculated correctly
        # Base (100) + First attempt bonus (25) + Speed bonus (20) = 145
        expected_points = 100 + 25 + 20
        self.assertEqual(points_awarded, expected_points)
        
        # Verify submission was updated
        submission.refresh_from_db()
        self.assertEqual(submission.points_earned, expected_points)
        
        # Verify user points were updated
        user_points = UserPoints.objects.get(user=self.user)
        self.assertEqual(user_points.total_points, expected_points)
        self.assertEqual(user_points.practice_points, expected_points)
        self.assertEqual(user_points.assignment_points, 0)
    
    def test_zero_points_handling(self):
        """Test that zero or negative points are handled correctly"""
        # Try to add zero points
        total_points, points_added = self.calculator.update_user_points(
            user=self.user,
            points_to_add=0,
            point_type='practice'
        )
        
        self.assertEqual(points_added, 0)
        self.assertEqual(total_points, 0)
        
        # Try to add negative points
        total_points, points_added = self.calculator.update_user_points(
            user=self.user,
            points_to_add=-10,
            point_type='practice'
        )
        
        self.assertEqual(points_added, 0)
        self.assertEqual(total_points, 0)
    
    def test_invalid_point_type(self):
        """Test handling of invalid point types"""
        with patch('gamification.points_calculator.logger') as mock_logger:
            total_points, points_added = self.calculator.update_user_points(
                user=self.user,
                points_to_add=100,
                point_type='invalid_type'
            )
            
            self.assertEqual(points_added, 0)
            self.assertEqual(total_points, 0)
            mock_logger.warning.assert_called_once()
    
    def test_non_successful_submission_points(self):
        """Test that points are not awarded for non-successful submissions"""
        # Create a failed practice submission
        submission = PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.easy_question,
            source_code='print("test")',
            status='fail',  # Failed submission
            attempt_number=1
        )
        
        # Try to award points
        points_awarded = self.calculator.calculate_and_award_practice_points(
            submission=submission
        )
        
        # Should not award any points
        self.assertEqual(points_awarded, 0)
        
        # Verify submission points_earned remains 0
        submission.refresh_from_db()
        self.assertEqual(submission.points_earned, 0)
    
    def test_atomic_point_updates(self):
        """Test that point updates are atomic"""
        # This test ensures that if something goes wrong during point update,
        # the database remains consistent
        
        with patch.object(UserPoints, 'save', side_effect=Exception('Database error')):
            with self.assertRaises(Exception):
                self.calculator.update_user_points(
                    user=self.user,
                    points_to_add=100,
                    point_type='practice'
                )
        
        # Verify no partial updates occurred
        self.assertFalse(UserPoints.objects.filter(user=self.user).exists())
    
    def test_get_user_points_summary_no_points(self):
        """Test getting points summary for user with no points"""
        summary = self.calculator.get_user_points_summary(self.user)
        
        expected_summary = {
            'total_points': 0,
            'practice_points': 0,
            'assignment_points': 0,
            'last_updated': None
        }
        
        self.assertEqual(summary, expected_summary)