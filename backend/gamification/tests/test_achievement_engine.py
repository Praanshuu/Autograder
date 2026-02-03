"""
Tests for the AchievementEngine class.

Tests cover:
- Achievement criteria checking for different badge types
- Automatic badge awarding
- Progress tracking calculations
- Integration with signals
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

from gamification.models import (
    Achievement, UserAchievement, PracticeQuestion, PracticeSubmission, 
    PracticeProgress, UserPoints
)
from gamification.achievement_engine import AchievementEngine, check_user_achievements

User = get_user_model()


class AchievementEngineTestCase(TestCase):
    """Test cases for AchievementEngine functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.engine = AchievementEngine()
        
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            role='student'
        )
        
        # Create test practice question
        self.practice_question = PracticeQuestion.objects.create(
            title='Test Question',
            description='A test practice question',
            difficulty='easy',
            category='Arrays',
            test_cases=[{'input': '1', 'output': '1'}],
            point_value=100,
            created_by=self.user
        )
        
        # Create test achievements
        self.first_completion_achievement = Achievement.objects.create(
            name='First Steps',
            description='Complete your first practice question',
            icon='🎯',
            badge_type='first_completion',
            criteria={'completion_type': 'practice'},
            rarity='common'
        )
        
        self.streak_achievement = Achievement.objects.create(
            name='Perfect Streak',
            description='Get 3 consecutive successful submissions',
            icon='✨',
            badge_type='streak',
            criteria={'streak_type': 'consecutive', 'streak_length': 3},
            rarity='uncommon'
        )
        
        self.milestone_achievement = Achievement.objects.create(
            name='Point Collector',
            description='Earn 100 points',
            icon='🏆',
            badge_type='milestone',
            criteria={'milestone_type': 'points', 'required_value': 100},
            point_threshold=100,
            rarity='common'
        )
        
        self.perfect_score_achievement = Achievement.objects.create(
            name='Perfectionist',
            description='Get perfect scores on 2 practice questions',
            icon='💯',
            badge_type='perfect_score',
            criteria={'perfect_count': 2},
            rarity='uncommon'
        )
    
    def test_first_completion_achievement(self):
        """Test first completion achievement checking"""
        # Initially, user should not have the achievement
        self.assertFalse(
            self.engine._check_achievement_criteria(
                self.user, self.first_completion_achievement
            )
        )
        
        # Create a completed practice progress
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question,
            is_completed=True,
            attempts_count=1,
            best_score=100.0
        )
        
        # Now user should meet the criteria
        self.assertTrue(
            self.engine._check_achievement_criteria(
                self.user, self.first_completion_achievement
            )
        )
    
    def test_streak_achievement_consecutive(self):
        """Test consecutive streak achievement checking"""
        # Create 3 consecutive successful submissions
        for i in range(3):
            PracticeSubmission.objects.create(
                student=self.user,
                practice_question=self.practice_question,
                source_code='test code',
                status='success',
                attempt_number=i + 1,
                submitted_at=timezone.now() - timedelta(minutes=i)
            )
        
        # User should meet the streak criteria
        self.assertTrue(
            self.engine._check_achievement_criteria(
                self.user, self.streak_achievement
            )
        )
        
        # Add a failed submission (breaks the streak)
        PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.practice_question,
            source_code='bad code',
            status='fail',
            attempt_number=4,
            submitted_at=timezone.now()
        )
        
        # User should no longer meet the criteria
        self.assertFalse(
            self.engine._check_achievement_criteria(
                self.user, self.streak_achievement
            )
        )
    
    def test_milestone_achievement_points(self):
        """Test points milestone achievement checking"""
        # Initially, user should not have enough points
        self.assertFalse(
            self.engine._check_achievement_criteria(
                self.user, self.milestone_achievement
            )
        )
        
        # Create user points with enough points
        UserPoints.objects.create(
            user=self.user,
            total_points=150,
            practice_points=150,
            assignment_points=0
        )
        
        # Now user should meet the criteria
        self.assertTrue(
            self.engine._check_achievement_criteria(
                self.user, self.milestone_achievement
            )
        )
    
    def test_perfect_score_achievement(self):
        """Test perfect score achievement checking"""
        # Create one perfect score
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question,
            is_completed=True,
            best_score=100.0,
            attempts_count=1
        )
        
        # Should not meet criteria yet (needs 2)
        self.assertFalse(
            self.engine._check_achievement_criteria(
                self.user, self.perfect_score_achievement
            )
        )
        
        # Create second practice question and perfect score
        second_question = PracticeQuestion.objects.create(
            title='Second Question',
            description='Another test question',
            difficulty='medium',
            category='Algorithms',
            test_cases=[{'input': '2', 'output': '4'}],
            point_value=150,
            created_by=self.user
        )
        
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=second_question,
            is_completed=True,
            best_score=100.0,
            attempts_count=1
        )
        
        # Now should meet criteria
        self.assertTrue(
            self.engine._check_achievement_criteria(
                self.user, self.perfect_score_achievement
            )
        )
    
    def test_award_achievement(self):
        """Test achievement awarding functionality"""
        # Award the first completion achievement
        awarded = self.engine._award_achievement(self.user, self.first_completion_achievement)
        
        self.assertIsNotNone(awarded)
        self.assertEqual(awarded.user, self.user)
        self.assertEqual(awarded.achievement, self.first_completion_achievement)
        
        # Verify it was saved to database
        self.assertTrue(
            UserAchievement.objects.filter(
                user=self.user,
                achievement=self.first_completion_achievement
            ).exists()
        )
        
        # Try to award the same achievement again (should return None)
        duplicate = self.engine._award_achievement(self.user, self.first_completion_achievement)
        self.assertIsNone(duplicate)
    
    def test_check_and_award_achievements(self):
        """Test the main achievement checking and awarding flow"""
        # Create conditions for first completion achievement
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question,
            is_completed=True,
            attempts_count=1,
            best_score=100.0
        )
        
        # Check and award achievements
        newly_awarded = self.engine.check_and_award_achievements(
            self.user, 
            trigger_event='practice_completion'
        )
        
        # Should have awarded the first completion achievement
        self.assertEqual(len(newly_awarded), 1)
        self.assertEqual(newly_awarded[0].achievement, self.first_completion_achievement)
        
        # Run again - should not award anything new
        newly_awarded_again = self.engine.check_and_award_achievements(
            self.user,
            trigger_event='practice_completion'
        )
        self.assertEqual(len(newly_awarded_again), 0)
    
    def test_get_achievement_progress_first_completion(self):
        """Test progress calculation for first completion achievements"""
        # Initially no progress
        progress = self.engine.get_achievement_progress(self.user, self.first_completion_achievement)
        self.assertEqual(progress['current'], 0)
        self.assertEqual(progress['required'], 1)
        self.assertEqual(progress['percentage'], 0)
        
        # Complete a practice question
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question,
            is_completed=True,
            attempts_count=1,
            best_score=100.0
        )
        
        # Should show completion
        progress = self.engine.get_achievement_progress(self.user, self.first_completion_achievement)
        self.assertEqual(progress['current'], 1)
        self.assertEqual(progress['required'], 1)
        self.assertEqual(progress['percentage'], 100)
    
    def test_get_achievement_progress_milestone(self):
        """Test progress calculation for milestone achievements"""
        # Initially no points
        progress = self.engine.get_achievement_progress(self.user, self.milestone_achievement)
        self.assertEqual(progress['current'], 0)
        self.assertEqual(progress['required'], 100)
        self.assertEqual(progress['percentage'], 0)
        
        # Add some points
        UserPoints.objects.create(
            user=self.user,
            total_points=50,
            practice_points=50,
            assignment_points=0
        )
        
        # Should show partial progress
        progress = self.engine.get_achievement_progress(self.user, self.milestone_achievement)
        self.assertEqual(progress['current'], 50)
        self.assertEqual(progress['required'], 100)
        self.assertEqual(progress['percentage'], 50)
    
    def test_get_achievement_progress_streak(self):
        """Test progress calculation for streak achievements"""
        # Initially no streak
        progress = self.engine.get_achievement_progress(self.user, self.streak_achievement)
        self.assertEqual(progress['current'], 0)
        self.assertEqual(progress['required'], 3)
        self.assertEqual(progress['percentage'], 0)
        
        # Create 2 consecutive successful submissions
        for i in range(2):
            PracticeSubmission.objects.create(
                student=self.user,
                practice_question=self.practice_question,
                source_code='test code',
                status='success',
                attempt_number=i + 1,
                submitted_at=timezone.now() - timedelta(minutes=i)
            )
        
        # Should show partial progress
        progress = self.engine.get_achievement_progress(self.user, self.streak_achievement)
        self.assertEqual(progress['current'], 2)
        self.assertEqual(progress['required'], 3)
        self.assertAlmostEqual(progress['percentage'], 66.67, places=1)
    
    def test_convenience_functions(self):
        """Test the convenience functions"""
        # Create conditions for achievement
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.practice_question,
            is_completed=True,
            attempts_count=1,
            best_score=100.0
        )
        
        # Test check_user_achievements function
        newly_awarded = check_user_achievements(self.user, 'test_trigger')
        self.assertEqual(len(newly_awarded), 1)
        
        # Test get_user_achievement_progress function
        from gamification.achievement_engine import get_user_achievement_progress
        progress = get_user_achievement_progress(self.user, self.milestone_achievement)
        self.assertIn('current', progress)
        self.assertIn('required', progress)
        self.assertIn('percentage', progress)
    
    def test_daily_streak_calculation(self):
        """Test daily streak calculation"""
        today = timezone.now().date()
        
        # Create submissions for the last 3 days
        for i in range(3):
            submission_date = today - timedelta(days=i)
            submission = PracticeSubmission.objects.create(
                student=self.user,
                practice_question=self.practice_question,
                source_code='test code',
                status='success',
                attempt_number=i + 1
            )
            # Update the submitted_at field after creation to override auto_now_add
            target_datetime = timezone.make_aware(
                timezone.datetime.combine(submission_date, timezone.datetime.min.time().replace(hour=12))
            )
            PracticeSubmission.objects.filter(id=submission.id).update(submitted_at=target_datetime)
        
        # Test daily streak calculation
        streak = self.engine._get_current_daily_streak(self.user)
        self.assertEqual(streak, 3)
        
        # Test with a gap (no submission yesterday)
        PracticeSubmission.objects.filter(
            submitted_at__date=today - timedelta(days=1)
        ).delete()
        
        streak_with_gap = self.engine._get_current_daily_streak(self.user)
        self.assertEqual(streak_with_gap, 1)  # Only today's submission
    
    def test_error_handling(self):
        """Test error handling in achievement engine"""
        # Create achievement with invalid criteria
        invalid_achievement = Achievement.objects.create(
            name='Invalid Achievement',
            description='Achievement with invalid criteria',
            icon='❌',
            badge_type='invalid_type',
            criteria={'invalid': 'criteria'},
            rarity='common'
        )
        
        # Should handle gracefully and return False
        result = self.engine._check_achievement_criteria(
            self.user, invalid_achievement
        )
        self.assertFalse(result)
        
        # Should not crash when getting progress for invalid achievement
        progress = self.engine.get_achievement_progress(self.user, invalid_achievement)
        self.assertEqual(progress['current'], 0)
        self.assertEqual(progress['required'], 1)
        self.assertEqual(progress['percentage'], 0)