"""
Points calculation engine for the gamified autograder system.

This module provides the PointsCalculator class that handles all point calculations
for both practice questions and assignments, including bonuses and multipliers.
"""

import logging
from typing import Dict, List, Optional, Tuple
from django.db import transaction
from django.utils import timezone
from .models import UserPoints, PracticeQuestion, PracticeSubmission

logger = logging.getLogger(__name__)


class PointsCalculator:
    """
    Calculate points for various activities in the gamified autograder system.
    
    This class handles point calculations for:
    - Practice question completions with difficulty multipliers
    - Assignment submissions with proportional scoring
    - Bonus points for first attempts and speed
    - Point updates and user point tracking
    """
    
    # Difficulty multipliers for practice questions
    DIFFICULTY_MULTIPLIERS = {
        'easy': 1.0,
        'medium': 1.5,
        'hard': 2.0
    }
    
    # Base point values for different activities
    BASE_POINTS = {
        'practice_completion': 100,      # Base points for completing a practice question
        'assignment_test_case': 10,      # Points per passed test case in assignments
        'perfect_assignment': 50,        # Bonus for passing all test cases
        'first_attempt_success': 25,     # Bonus for succeeding on first attempt
        'speed_bonus': 20               # Bonus for fast completion
    }
    
    # Expected completion times by difficulty (in seconds)
    EXPECTED_TIMES = {
        'easy': 300,    # 5 minutes
        'medium': 900,  # 15 minutes
        'hard': 1800    # 30 minutes
    }
    
    def calculate_practice_points(
        self, 
        question: PracticeQuestion, 
        attempt_number: int = 1,
        execution_time_ms: Optional[int] = None,
        completion_time_seconds: Optional[int] = None
    ) -> int:
        """
        Calculate points for practice question completion.
        
        Args:
            question: The practice question that was completed
            attempt_number: Which attempt this was (1 for first attempt)
            execution_time_ms: Code execution time in milliseconds for speed bonus
            completion_time_seconds: Total time spent on question for speed bonus
            
        Returns:
            int: Total points including bonuses
        """
        # Start with base points adjusted for difficulty
        base_points = self.BASE_POINTS['practice_completion']
        difficulty_multiplier = self.DIFFICULTY_MULTIPLIERS.get(question.difficulty, 1.0)
        points = int(base_points * difficulty_multiplier)
        
        # First attempt bonus (25% of base points)
        if attempt_number == 1:
            first_attempt_bonus = int(points * 0.25)
            points += first_attempt_bonus
            logger.info(f"First attempt bonus: +{first_attempt_bonus} points")
        
        # Speed bonus based on completion time
        if completion_time_seconds is not None:
            speed_bonus = self._calculate_speed_bonus(question.difficulty, completion_time_seconds)
            points += speed_bonus
            if speed_bonus > 0:
                logger.info(f"Speed bonus: +{speed_bonus} points")
        
        # Alternative speed bonus based on execution time
        elif execution_time_ms is not None:
            exec_speed_bonus = self._calculate_execution_speed_bonus(question.difficulty, execution_time_ms)
            points += exec_speed_bonus
            if exec_speed_bonus > 0:
                logger.info(f"Execution speed bonus: +{exec_speed_bonus} points")
        
        return points
    
    def calculate_assignment_points(
        self, 
        test_results: List[Dict], 
        attempt_number: int = 1,
        assignment_question=None
    ) -> int:
        """
        Calculate points for assignment submissions based on test case results.
        
        Args:
            test_results: List of test case results with status information
            attempt_number: Which attempt this was (1 for first attempt)
            assignment_question: The assignment question for context
            
        Returns:
            int: Total points based on passed test cases and bonuses
        """
        if not test_results:
            return 0
        
        # Count passed test cases
        passed_tests = sum(1 for result in test_results if result.get('status') == 'pass')
        total_tests = len(test_results)
        
        # Base points per test case
        base_points = self.BASE_POINTS['assignment_test_case'] * passed_tests
        
        # Perfect score bonus (all test cases passed)
        if passed_tests == total_tests and total_tests > 0:
            perfect_bonus = self.BASE_POINTS['perfect_assignment']
            base_points += perfect_bonus
            logger.info(f"Perfect assignment bonus: +{perfect_bonus} points")
        
        # First attempt bonus for assignments (if they got some tests right)
        if attempt_number == 1 and passed_tests > 0:
            first_attempt_bonus = self.BASE_POINTS['first_attempt_success']
            base_points += first_attempt_bonus
            logger.info(f"First attempt bonus: +{first_attempt_bonus} points")
        
        return base_points
    
    def _calculate_speed_bonus(self, difficulty: str, completion_time_seconds: int) -> int:
        """
        Calculate speed bonus based on completion time vs expected time.
        
        Args:
            difficulty: Question difficulty level
            completion_time_seconds: Time taken to complete the question
            
        Returns:
            int: Speed bonus points (0 if no bonus earned)
        """
        expected_time = self.EXPECTED_TIMES.get(difficulty, 900)  # Default to medium
        
        # Award speed bonus if completed in less than 50% of expected time
        if completion_time_seconds < expected_time * 0.5:
            return self.BASE_POINTS['speed_bonus']
        
        return 0
    
    def _calculate_execution_speed_bonus(self, difficulty: str, execution_time_ms: int) -> int:
        """
        Calculate speed bonus based on code execution time.
        
        Args:
            difficulty: Question difficulty level
            execution_time_ms: Code execution time in milliseconds
            
        Returns:
            int: Speed bonus points (0 if no bonus earned)
        """
        # Expected execution time thresholds by difficulty (in milliseconds)
        expected_exec_times = {
            'easy': 5000,    # 5 seconds
            'medium': 10000, # 10 seconds  
            'hard': 15000    # 15 seconds
        }
        
        expected_time = expected_exec_times.get(difficulty, 10000)
        
        # Award speed bonus if executed in less than 50% of expected time
        if execution_time_ms < expected_time * 0.5:
            return self.BASE_POINTS['speed_bonus']
        
        return 0
    
    @transaction.atomic
    def update_user_points(
        self, 
        user, 
        points_to_add: int, 
        point_type: str = 'practice'
    ) -> Tuple[int, int]:
        """
        Update user's point totals atomically.
        
        Args:
            user: User instance to update points for
            points_to_add: Number of points to add
            point_type: Type of points ('practice' or 'assignment')
            
        Returns:
            Tuple[int, int]: (new_total_points, points_added)
        """
        if points_to_add <= 0:
            return 0, 0
        
        # Get or create user points record
        user_points, created = UserPoints.objects.get_or_create(
            user=user,
            defaults={
                'total_points': 0,
                'practice_points': 0,
                'assignment_points': 0
            }
        )
        
        # Store old points for real-time notification
        old_total_points = user_points.total_points
        
        # Update appropriate point category
        if point_type == 'practice':
            user_points.practice_points += points_to_add
        elif point_type == 'assignment':
            user_points.assignment_points += points_to_add
        else:
            logger.warning(f"Unknown point type: {point_type}")
            return user_points.total_points, 0
        
        # Update total points
        user_points.total_points = user_points.practice_points + user_points.assignment_points
        user_points.save()
        
        logger.info(
            f"Updated points for {user.username}: +{points_to_add} {point_type} points "
            f"(Total: {user_points.total_points})"
        )
        
        # Broadcast real-time points update
        from .realtime_service import realtime_service
        realtime_service.notify_points_update(
            user=user,
            old_points=old_total_points,
            new_points=user_points.total_points,
            source=point_type
        )
        
        # Update leaderboards (this will also broadcast leaderboard updates)
        from .models import LeaderboardManager
        LeaderboardManager.update_leaderboards_for_user(user)
        
        return user_points.total_points, points_to_add
    
    def calculate_and_award_practice_points(
        self, 
        submission: PracticeSubmission,
        completion_time_seconds: Optional[int] = None
    ) -> int:
        """
        Calculate and award points for a successful practice submission.
        
        Args:
            submission: The practice submission that succeeded
            completion_time_seconds: Total time spent on the question
            
        Returns:
            int: Points awarded
        """
        if submission.status != 'success':
            logger.warning(f"Attempted to award points for non-successful submission: {submission.id}")
            return 0
        
        # Calculate points
        points = self.calculate_practice_points(
            question=submission.practice_question,
            attempt_number=submission.attempt_number,
            execution_time_ms=submission.execution_time_ms,
            completion_time_seconds=completion_time_seconds
        )
        
        # Update submission with points earned
        submission.points_earned = points
        submission.save()
        
        # Update user points (this will also broadcast real-time updates)
        total_points, points_added = self.update_user_points(
            user=submission.student,
            points_to_add=points,
            point_type='practice'
        )
        
        # Send practice completion notification
        from .realtime_service import realtime_service
        realtime_service.notify_practice_completed(
            user=submission.student,
            question_title=submission.practice_question.title,
            points_earned=points_added,
            attempt_number=submission.attempt_number
        )
        
        return points_added
    
    def calculate_and_award_assignment_points(
        self, 
        submission_attempt,
        test_results: List[Dict]
    ) -> int:
        """
        Calculate and award points for an assignment submission.
        
        Args:
            submission_attempt: The assignment submission attempt
            test_results: List of test case results
            
        Returns:
            int: Points awarded
        """
        # Calculate points based on test results
        points = self.calculate_assignment_points(
            test_results=test_results,
            attempt_number=submission_attempt.attempt_number,
            assignment_question=submission_attempt.assignment_question
        )
        
        if points > 0:
            # Update user points
            total_points, points_added = self.update_user_points(
                user=submission_attempt.student,
                points_to_add=points,
                point_type='assignment'
            )
            
            logger.info(
                f"Awarded {points_added} assignment points to {submission_attempt.student.username} "
                f"for {submission_attempt.assignment_question}"
            )
            
            return points_added
        
        return 0
    
    def get_user_points_summary(self, user) -> Dict:
        """
        Get a summary of user's points across all categories.
        
        Args:
            user: User to get points summary for
            
        Returns:
            Dict: Points summary with totals and breakdowns
        """
        try:
            user_points = UserPoints.objects.get(user=user)
            return {
                'total_points': user_points.total_points,
                'practice_points': user_points.practice_points,
                'assignment_points': user_points.assignment_points,
                'last_updated': user_points.last_updated
            }
        except UserPoints.DoesNotExist:
            return {
                'total_points': 0,
                'practice_points': 0,
                'assignment_points': 0,
                'last_updated': None
            }
    
    def recalculate_user_points(self, user) -> Dict:
        """
        Recalculate all points for a user from scratch.
        Useful for fixing point inconsistencies.
        
        Args:
            user: User to recalculate points for
            
        Returns:
            Dict: Updated points summary
        """
        with transaction.atomic():
            # Calculate practice points from successful submissions
            practice_points = PracticeSubmission.objects.filter(
                student=user,
                status='success'
            ).aggregate(
                total=models.Sum('points_earned')
            )['total'] or 0
            
            # For assignment points, we'd need to query SubmissionAttempt
            # and recalculate based on test results - this is more complex
            # For now, we'll just update practice points
            
            user_points, created = UserPoints.objects.get_or_create(
                user=user,
                defaults={
                    'total_points': 0,
                    'practice_points': 0,
                    'assignment_points': 0
                }
            )
            
            # Update practice points
            old_practice = user_points.practice_points
            user_points.practice_points = practice_points
            user_points.total_points = user_points.practice_points + user_points.assignment_points
            user_points.save()
            
            logger.info(
                f"Recalculated points for {user.username}: "
                f"Practice {old_practice} -> {practice_points}"
            )
            
            return self.get_user_points_summary(user)


# Utility functions for point management and leaderboard updates

def get_top_users_by_points(limit: int = 10, point_type: str = 'total') -> List[Dict]:
    """
    Get top users by points for leaderboard display.
    
    Args:
        limit: Maximum number of users to return
        point_type: Type of points to rank by ('total', 'practice', 'assignment')
        
    Returns:
        List[Dict]: Top users with their point information
    """
    order_field = {
        'total': '-total_points',
        'practice': '-practice_points', 
        'assignment': '-assignment_points'
    }.get(point_type, '-total_points')
    
    top_users = UserPoints.objects.select_related('user').order_by(order_field)[:limit]
    
    return [
        {
            'user_id': up.user.id,
            'username': up.user.username,
            'first_name': up.user.first_name,
            'last_name': up.user.last_name,
            'total_points': up.total_points,
            'practice_points': up.practice_points,
            'assignment_points': up.assignment_points,
            'rank': idx + 1
        }
        for idx, up in enumerate(top_users)
    ]


def get_user_rank(user) -> Dict:
    """
    Get a user's current rank and nearby competitors.
    
    Args:
        user: User to get rank for
        
    Returns:
        Dict: User's rank information and nearby users
    """
    try:
        user_points = UserPoints.objects.get(user=user)
        
        # Count users with higher points
        higher_count = UserPoints.objects.filter(
            total_points__gt=user_points.total_points
        ).count()
        
        current_rank = higher_count + 1
        
        # Get nearby users (2 above, 2 below)
        nearby_users = UserPoints.objects.select_related('user').order_by('-total_points')[
            max(0, current_rank - 3):current_rank + 2
        ]
        
        return {
            'current_rank': current_rank,
            'total_points': user_points.total_points,
            'nearby_users': [
                {
                    'username': up.user.username,
                    'total_points': up.total_points,
                    'rank': higher_count - idx + 1 if idx < current_rank - 1 else current_rank + idx - (current_rank - 1)
                }
                for idx, up in enumerate(nearby_users)
            ]
        }
    except UserPoints.DoesNotExist:
        return {
            'current_rank': None,
            'total_points': 0,
            'nearby_users': []
        }


def update_leaderboard_cache():
    """
    Update cached leaderboard data for performance.
    This should be called periodically or after significant point changes.
    """
    from .models import LeaderboardEntry
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
    
    # Update global leaderboard
    users_with_points = UserPoints.objects.select_related('user').order_by('-total_points')
    
    # Clear existing global leaderboard entries
    LeaderboardEntry.objects.filter(leaderboard_type='global').delete()
    
    # Create new leaderboard entries
    leaderboard_entries = []
    for rank, user_points in enumerate(users_with_points, 1):
        # Count completed problems (practice + assignments)
        from .models import PracticeProgress
        practice_completed = PracticeProgress.objects.filter(
            student=user_points.user,
            is_completed=True
        ).count()
        
        # For assignments, we'd need to query successful submissions
        # This is a simplified version
        completed_problems = practice_completed
        
        leaderboard_entries.append(
            LeaderboardEntry(
                user=user_points.user,
                rank=rank,
                total_points=user_points.total_points,
                completed_problems=completed_problems,
                leaderboard_type='global'
            )
        )
    
    # Bulk create leaderboard entries
    LeaderboardEntry.objects.bulk_create(leaderboard_entries, batch_size=100)
    
    logger.info(f"Updated global leaderboard with {len(leaderboard_entries)} entries")