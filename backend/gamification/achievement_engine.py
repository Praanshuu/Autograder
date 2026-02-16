"""
Achievement Engine for automatic badge awarding in the gamified autograder system.

This module provides the AchievementEngine class that handles:
- Automatic achievement checking and awarding
- Progress tracking toward achievements
- Criteria validation for different badge types
"""

import logging
from typing import Dict, List, Optional, Tuple
from django.db import transaction
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import timedelta

from .models import (
    Achievement, UserAchievement, PracticeSubmission, PracticeProgress,
    UserPoints, StudentAnalytics
)

logger = logging.getLogger(__name__)
User = get_user_model()


class AchievementEngine:
    """
    Engine for checking and awarding achievements automatically.
    
    This class handles all achievement logic including:
    - Criteria checking for different badge types
    - Automatic badge awarding on milestone completion
    - Progress tracking for incomplete achievements
    """
    
    def __init__(self):
        """Initialize the achievement engine"""
        self.logger = logger
    
    def check_and_award_achievements(self, user, trigger_event: str = None, **context):
        """
        Check all achievements for a user and award any newly earned badges.
        
        Args:
            user: User to check achievements for
            trigger_event: Event that triggered this check (e.g., 'practice_completion')
            **context: Additional context data for achievement checking
            
        Returns:
            List[Achievement]: List of newly awarded achievements
        """
        newly_awarded = []
        
        # Get all active achievements that the user hasn't earned yet
        earned_achievement_ids = UserAchievement.objects.filter(
            user=user
        ).values_list('achievement_id', flat=True)
        
        available_achievements = Achievement.objects.filter(
            is_active=True
        ).exclude(id__in=earned_achievement_ids)
        
        for achievement in available_achievements:
            try:
                if self._check_achievement_criteria(user, achievement, trigger_event, **context):
                    awarded_achievement = self._award_achievement(user, achievement)
                    if awarded_achievement:
                        newly_awarded.append(awarded_achievement)
                        self.logger.info(
                            f"Awarded achievement '{achievement.name}' to user {user.username}"
                        )
            except Exception as e:
                self.logger.error(
                    f"Error checking achievement {achievement.name} for user {user.username}: {e}",
                    exc_info=True
                )
        
        return newly_awarded
    
    def _check_achievement_criteria(self, user, achievement: Achievement, trigger_event: str = None, **context) -> bool:
        """
        Check if a user meets the criteria for a specific achievement.
        
        Args:
            user: User to check
            achievement: Achievement to check criteria for
            trigger_event: Event that triggered this check
            **context: Additional context data
            
        Returns:
            bool: True if user meets criteria, False otherwise
        """
        criteria = achievement.criteria
        badge_type = achievement.badge_type
        
        try:
            if badge_type == 'first_completion':
                return self._check_first_completion_criteria(user, criteria, **context)
            elif badge_type == 'streak':
                return self._check_streak_criteria(user, criteria)
            elif badge_type == 'perfect_score':
                return self._check_perfect_score_criteria(user, criteria, **context)
            elif badge_type == 'speed':
                return self._check_speed_criteria(user, criteria, **context)
            elif badge_type == 'milestone':
                return self._check_milestone_criteria(user, criteria)
            else:
                self.logger.warning(f"Unknown badge type: {badge_type}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error checking criteria for {achievement.name}: {e}")
            return False
    
    def _check_first_completion_criteria(self, user, criteria: Dict, **context) -> bool:
        """Check first completion achievement criteria"""
        required_type = criteria.get('completion_type', 'any')  # 'practice', 'assignment', 'any'
        
        if required_type == 'practice':
            # Check if user has completed their first practice question
            return PracticeProgress.objects.filter(
                student=user,
                is_completed=True
            ).exists()
        elif required_type == 'assignment':
            # Check if user has completed their first assignment
            # This would need integration with assignment completion tracking
            return False  # Placeholder for assignment completion check
        else:  # 'any'
            # Check if user has completed any practice question
            return PracticeProgress.objects.filter(
                student=user,
                is_completed=True
            ).exists()
    
    def _check_streak_criteria(self, user, criteria: Dict) -> bool:
        """Check streak achievement criteria"""
        required_streak = criteria.get('streak_length', 5)
        streak_type = criteria.get('streak_type', 'daily')  # 'daily', 'consecutive'
        
        if streak_type == 'daily':
            # Check daily submission streak
            return self._check_daily_streak(user, required_streak)
        elif streak_type == 'consecutive':
            # Check consecutive successful submissions
            return self._check_consecutive_streak(user, required_streak)
        
        return False
    
    def _check_daily_streak(self, user, required_days: int) -> bool:
        """Check if user has a daily submission streak"""
        today = timezone.now().date()
        
        # Check each day going backwards
        for i in range(required_days):
            check_date = today - timedelta(days=i)
            
            # Check if user made any successful submission on this date
            has_submission = PracticeSubmission.objects.filter(
                student=user,
                status='success',
                submitted_at__date=check_date
            ).exists()
            
            if not has_submission:
                return False
        
        return True
    
    def _check_consecutive_streak(self, user, required_count: int) -> bool:
        """Check if user has consecutive successful submissions"""
        # Get recent submissions in reverse chronological order
        recent_submissions = PracticeSubmission.objects.filter(
            student=user
        ).order_by('-submitted_at')[:required_count]
        
        if len(recent_submissions) < required_count:
            return False
        
        # Check if all recent submissions were successful
        return all(sub.status == 'success' for sub in recent_submissions)
    
    def _check_perfect_score_criteria(self, user, criteria: Dict, **context) -> bool:
        """Check perfect score achievement criteria"""
        required_count = criteria.get('perfect_count', 1)
        difficulty = criteria.get('difficulty')  # Optional difficulty filter
        
        query = PracticeProgress.objects.filter(
            student=user,
            is_completed=True,
            best_score=100.0
        )
        
        if difficulty:
            # Use iexact for case-insensitive comparison since Question uses Capitalized difficulty
            query = query.filter(question__difficulty__iexact=difficulty)
        
        return query.count() >= required_count
    
    def _check_speed_criteria(self, user, criteria: Dict, **context) -> bool:
        """Check speed achievement criteria"""
        max_time = criteria.get('max_time_seconds', 300)  # 5 minutes default
        difficulty = criteria.get('difficulty')
        
        query = PracticeSubmission.objects.filter(
            student=user,
            status='success'
        )
        
        if difficulty:
            query = query.filter(question__difficulty__iexact=difficulty)
        
        # Check if user has any submission faster than max_time
        # Convert milliseconds to seconds for comparison
        fast_submissions = query.filter(
            execution_time_ms__lt=max_time * 1000
        )
        
        return fast_submissions.exists()
    
    def _check_milestone_criteria(self, user, criteria: Dict) -> bool:
        """Check milestone achievement criteria"""
        milestone_type = criteria.get('milestone_type', 'points')
        required_value = criteria.get('required_value', 100)
        
        if milestone_type == 'points':
            try:
                user_points = UserPoints.objects.get(user=user)
                return user_points.total_points >= required_value
            except UserPoints.DoesNotExist:
                return False
        
        elif milestone_type == 'practice_completed':
            completed_count = PracticeProgress.objects.filter(
                student=user,
                is_completed=True
            ).count()
            return completed_count >= required_value
        
        elif milestone_type == 'categories_mastered':
            # Count unique categories where user has completed at least one question
            mastered_categories = PracticeProgress.objects.filter(
                student=user,
                is_completed=True
            ).values_list('question__category', flat=True).distinct().count()
            return mastered_categories >= required_value
        
        return False
    
    @transaction.atomic
    def _award_achievement(self, user, achievement: Achievement) -> Optional[UserAchievement]:
        """
        Award an achievement to a user.
        
        Args:
            user: User to award achievement to
            achievement: Achievement to award
            
        Returns:
            UserAchievement: The awarded achievement record, or None if already awarded
        """
        try:
            # Double-check that user doesn't already have this achievement
            if UserAchievement.objects.filter(user=user, achievement=achievement).exists():
                return None
            
            # Create the achievement record
            user_achievement = UserAchievement.objects.create(
                user=user,
                achievement=achievement
            )
            
            self.logger.info(
                f"Successfully awarded achievement '{achievement.name}' to user {user.username}"
            )
            
            return user_achievement
            
        except Exception as e:
            self.logger.error(
                f"Error awarding achievement {achievement.name} to user {user.username}: {e}",
                exc_info=True
            )
            return None
    
    def get_achievement_progress(self, user, achievement: Achievement) -> Dict:
        """
        Get progress toward a specific achievement for a user.
        
        Args:
            user: User to check progress for
            achievement: Achievement to check progress on
            
        Returns:
            Dict: Progress information including current value, required value, and percentage
        """
        criteria = achievement.criteria
        badge_type = achievement.badge_type
        
        try:
            if badge_type == 'first_completion':
                return self._get_first_completion_progress(user, criteria)
            elif badge_type == 'streak':
                return self._get_streak_progress(user, criteria)
            elif badge_type == 'perfect_score':
                return self._get_perfect_score_progress(user, criteria)
            elif badge_type == 'speed':
                return self._get_speed_progress(user, criteria)
            elif badge_type == 'milestone':
                return self._get_milestone_progress(user, criteria)
            else:
                return {'current': 0, 'required': 1, 'percentage': 0}
                
        except Exception as e:
            self.logger.error(f"Error getting progress for {achievement.name}: {e}")
            return {'current': 0, 'required': 1, 'percentage': 0}
    
    def _get_first_completion_progress(self, user, criteria: Dict) -> Dict:
        """Get progress for first completion achievements"""
        required_type = criteria.get('completion_type', 'any')
        
        if required_type == 'practice':
            completed = PracticeProgress.objects.filter(
                student=user,
                is_completed=True
            ).exists()
        else:
            completed = PracticeProgress.objects.filter(
                student=user,
                is_completed=True
            ).exists()
        
        return {
            'current': 1 if completed else 0,
            'required': 1,
            'percentage': 100 if completed else 0
        }
    
    def _get_streak_progress(self, user, criteria: Dict) -> Dict:
        """Get progress for streak achievements"""
        required_streak = criteria.get('streak_length', 5)
        streak_type = criteria.get('streak_type', 'daily')
        
        if streak_type == 'daily':
            current_streak = self._get_current_daily_streak(user)
        else:
            current_streak = self._get_current_consecutive_streak(user)
        
        return {
            'current': current_streak,
            'required': required_streak,
            'percentage': min(100, (current_streak / required_streak) * 100)
        }
    
    def _get_current_daily_streak(self, user) -> int:
        """Get current daily submission streak"""
        today = timezone.now().date()
        streak = 0
        
        # Check each day going backwards until we find a day without submissions
        for i in range(365):  # Max check 1 year
            check_date = today - timedelta(days=i)
            
            has_submission = PracticeSubmission.objects.filter(
                student=user,
                status='success',
                submitted_at__date=check_date
            ).exists()
            
            if has_submission:
                streak += 1
            else:
                # Found a day without submissions - streak ends here
                break
        
        return streak
    
    def _get_current_consecutive_streak(self, user) -> int:
        """Get current consecutive successful submission streak"""
        submissions = PracticeSubmission.objects.filter(
            student=user
        ).order_by('-submitted_at')
        
        streak = 0
        for submission in submissions:
            if submission.status == 'success':
                streak += 1
            else:
                break
        
        return streak
    
    def _get_perfect_score_progress(self, user, criteria: Dict) -> Dict:
        """Get progress for perfect score achievements"""
        required_count = criteria.get('perfect_count', 1)
        difficulty = criteria.get('difficulty')
        
        query = PracticeProgress.objects.filter(
            student=user,
            is_completed=True,
            best_score=100.0
        )
        
        if difficulty:
            query = query.filter(question__difficulty__iexact=difficulty)
        
        current_count = query.count()
        
        return {
            'current': current_count,
            'required': required_count,
            'percentage': min(100, (current_count / required_count) * 100)
        }
    
    def _get_speed_progress(self, user, criteria: Dict) -> Dict:
        """Get progress for speed achievements"""
        max_time = criteria.get('max_time_seconds', 300)
        difficulty = criteria.get('difficulty')
        
        query = PracticeSubmission.objects.filter(
            student=user,
            status='success'
        )
        
        if difficulty:
            query = query.filter(question__difficulty__iexact=difficulty)
        
        fast_submissions = query.filter(
            execution_time_ms__lt=max_time * 1000
        ).count()
        
        return {
            'current': 1 if fast_submissions > 0 else 0,
            'required': 1,
            'percentage': 100 if fast_submissions > 0 else 0
        }
    
    def _get_milestone_progress(self, user, criteria: Dict) -> Dict:
        """Get progress for milestone achievements"""
        milestone_type = criteria.get('milestone_type', 'points')
        required_value = criteria.get('required_value', 100)
        
        if milestone_type == 'points':
            try:
                user_points = UserPoints.objects.get(user=user)
                current_value = user_points.total_points
            except UserPoints.DoesNotExist:
                current_value = 0
        
        elif milestone_type == 'practice_completed':
            current_value = PracticeProgress.objects.filter(
                student=user,
                is_completed=True
            ).count()
        
        elif milestone_type == 'categories_mastered':
            current_value = PracticeProgress.objects.filter(
                student=user,
                is_completed=True
            ).values_list('question__category', flat=True).distinct().count()
        
        else:
            current_value = 0
        
        return {
            'current': current_value,
            'required': required_value,
            'percentage': min(100, (current_value / required_value) * 100)
        }


# Utility functions for achievement management

def check_user_achievements(user, trigger_event: str = None, **context):
    """
    Convenience function to check achievements for a user.
    
    Args:
        user: User to check achievements for
        trigger_event: Event that triggered this check
        **context: Additional context data
        
    Returns:
        List[Achievement]: List of newly awarded achievements
    """
    engine = AchievementEngine()
    return engine.check_and_award_achievements(user, trigger_event, **context)


def get_user_achievement_progress(user, achievement: Achievement) -> Dict:
    """
    Convenience function to get achievement progress for a user.
    
    Args:
        user: User to check progress for
        achievement: Achievement to check progress on
        
    Returns:
        Dict: Progress information
    """
    engine = AchievementEngine()
    return engine.get_achievement_progress(user, achievement)