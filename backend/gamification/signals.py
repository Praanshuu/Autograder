"""
Django signals for automatic points awarding and gamification updates.

This module handles automatic point calculation and awarding when submissions
are processed, ensuring points are updated in real-time as students complete
practice questions and assignments.
"""

import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import transaction

from .models import PracticeSubmission, PracticeProgress
from assignments.models import Question
from .points_calculator import PointsCalculator
from submissions.models import SubmissionAttempt, TestResult

logger = logging.getLogger(__name__)


@receiver(post_save, sender=PracticeSubmission)
def handle_practice_submission_points(sender, instance, created, **kwargs):
    """
    Handle point awarding for practice question submissions.
    
    This signal is triggered when a PracticeSubmission is saved.
    If the submission is successful, it calculates and awards points.
    """
    if not created:
        return  # Only process new submissions
    
    if instance.status != 'success':
        return  # Only award points for successful submissions
    
    try:
        with transaction.atomic():
            calculator = PointsCalculator()
            
            # Get completion time from practice progress if available
            completion_time_seconds = None
            try:
                progress = PracticeProgress.objects.get(
                    student=instance.student,
                    question=instance.question
                )
                completion_time_seconds = progress.time_spent
            except PracticeProgress.DoesNotExist:
                pass
            
            # Get old points for real-time notification
            from .models import UserPoints
            old_points = 0
            try:
                user_points = UserPoints.objects.get(user=instance.student)
                old_points = user_points.total_points
            except UserPoints.DoesNotExist:
                pass
            
            # Calculate and award points
            points_awarded = calculator.calculate_and_award_practice_points(
                submission=instance,
                completion_time_seconds=completion_time_seconds
            )
            
            logger.info(
                f"Awarded {points_awarded} points to {instance.student.username} "
                f"for completing practice question: {instance.question.title}"
            )
            
            # Update practice progress to mark as completed
            progress, created = PracticeProgress.objects.get_or_create(
                student=instance.student,
                question=instance.question,
                defaults={
                    'attempts_count': instance.attempt_number,
                    'best_score': 100.0,  # Successful completion = 100%
                    'time_spent': completion_time_seconds or 0
                }
            )
            
            if not progress.is_completed:
                progress.is_completed = True
                progress.completed_at = instance.submitted_at
                progress.best_score = 100.0
                progress.save()
                
                logger.info(
                    f"Marked practice question as completed for {instance.student.username}: "
                    f"{instance.question.title}"
                )
            
            # Send real-time notifications
            from .realtime_service import realtime_service
            
            # Get new points total
            new_points = 0
            try:
                user_points = UserPoints.objects.get(user=instance.student)
                new_points = user_points.total_points
            except UserPoints.DoesNotExist:
                pass
            
            # Notify practice completion
            realtime_service.notify_practice_completed(
                user=instance.student,
                question_title=instance.question.title,
                points_earned=points_awarded,
                attempt_number=instance.attempt_number
            )
            
            # Notify points update
            if points_awarded > 0:
                realtime_service.notify_points_update(
                    user=instance.student,
                    old_points=old_points,
                    new_points=new_points,
                    source='practice'
                )
            
            # Update student analytics
            from .analytics_aggregator import analytics_aggregator
            analytics_aggregator.update_analytics_on_activity(instance.student, 'practice')
            
    except Exception as e:
        logger.error(
            f"Error processing practice submission points for {instance.id}: {e}",
            exc_info=True
        )


@receiver(post_save, sender=SubmissionAttempt)
def handle_assignment_submission_points(sender, instance, created, **kwargs):
    """
    Handle point awarding for assignment submissions.
    
    This signal is triggered when a SubmissionAttempt is saved.
    Points are awarded after the submission is complete and test results are available.
    """
    if not created:
        return  # Only process new submissions
    
    # Only process completed submissions
    if instance.status not in ['success', 'fail']:
        return
    
    # Use a slight delay to ensure test results are saved
    # In production, this should be handled with proper async processing
    from django.db import transaction
    
    def award_points():
        try:
            with transaction.atomic():
                calculator = PointsCalculator()
                
                # Get old points for real-time notification
                from .models import UserPoints
                old_points = 0
                try:
                    user_points = UserPoints.objects.get(user=instance.student)
                    old_points = user_points.total_points
                except UserPoints.DoesNotExist:
                    pass
                
                # Get test results for this submission
                test_results = []
                for test_result in instance.test_results.all():
                    test_results.append({
                        'status': test_result.status,
                        'score': test_result.score
                    })
                
                if not test_results:
                    # Test results might not be available yet, skip for now
                    # The TestResult signal will handle this case
                    return
                
                # Calculate and award points
                points_awarded = calculator.calculate_and_award_assignment_points(
                    submission_attempt=instance,
                    test_results=test_results
                )
                
                if points_awarded > 0:
                    logger.info(
                        f"Awarded {points_awarded} points to {instance.student.username} "
                        f"for assignment submission: {instance.assignment_question}"
                    )
                    
                    # Send real-time notifications
                    from .realtime_service import realtime_service
                    
                    # Get new points total
                    new_points = 0
                    try:
                        user_points = UserPoints.objects.get(user=instance.student)
                        new_points = user_points.total_points
                    except UserPoints.DoesNotExist:
                        pass
                    
                    # Calculate score percentage
                    passed_tests = sum(1 for result in test_results if result['status'] == 'pass')
                    total_tests = len(test_results)
                    score_percentage = (passed_tests / total_tests * 100) if total_tests > 0 else 0
                    
                    # Notify assignment submission
                    realtime_service.notify_assignment_submitted(
                        user=instance.student,
                        assignment_title=str(instance.assignment_question),
                        points_earned=points_awarded,
                        score=score_percentage
                    )
                    
                    # Notify points update
                    realtime_service.notify_points_update(
                        user=instance.student,
                        old_points=old_points,
                        new_points=new_points,
                        source='assignment'
                    )
                
        except Exception as e:
            logger.error(
                f"Error processing assignment submission points for {instance.id}: {e}",
                exc_info=True
            )
    
    # Execute point awarding
    award_points()


@receiver(post_save, sender=TestResult)
def handle_test_result_completion(sender, instance, created, **kwargs):
    """
    Handle point awarding when test results are complete.
    
    This ensures points are awarded after all test results are saved,
    since test results might be saved after the submission attempt.
    """
    if not created:
        return
    
    # Check if this is the last test result for the submission
    submission = instance.attempt
    expected_test_count = len(submission.assignment_question.question.test_cases or [])
    actual_test_count = submission.test_results.count()
    
    # Only award points when all test results are complete
    if actual_test_count >= expected_test_count and expected_test_count > 0:
        # All test results are now available, trigger point calculation
        try:
            with transaction.atomic():
                calculator = PointsCalculator()
                
                # Get all test results for this submission
                test_results = []
                for test_result in submission.test_results.all():
                    test_results.append({
                        'status': test_result.status,
                        'score': test_result.score
                    })
                
                # Check if points have already been awarded to avoid double-awarding
                from .models import UserPoints
                user_points_before = UserPoints.objects.filter(user=submission.student).first()
                initial_assignment_points = user_points_before.assignment_points if user_points_before else 0
                
                # Calculate and award points
                points_awarded = calculator.calculate_and_award_assignment_points(
                    submission_attempt=submission,
                    test_results=test_results
                )
                
                # Verify points were actually added (not double-awarded)
                user_points_after = UserPoints.objects.filter(user=submission.student).first()
                final_assignment_points = user_points_after.assignment_points if user_points_after else 0
                actual_points_added = final_assignment_points - initial_assignment_points
                
                if actual_points_added > 0:
                    logger.info(
                        f"Awarded {actual_points_added} points to {submission.student.username} "
                        f"after test completion for: {submission.assignment_question}"
                    )
                    
                    # Update student analytics
                    from .analytics_aggregator import analytics_aggregator
                    analytics_aggregator.update_analytics_on_activity(submission.student, 'assignment')
                
        except Exception as e:
            logger.error(
                f"Error processing test result completion points for {instance.id}: {e}",
                exc_info=True
            )


@receiver(post_save, sender=PracticeProgress)
def update_practice_progress_time(sender, instance, created, **kwargs):
    """
    Update time tracking for practice progress.
    
    This signal helps maintain accurate time tracking for speed bonuses.
    """
    if created:
        return
    
    # If the progress was just completed, ensure we have accurate timing
    if instance.is_completed and instance.completed_at:
        try:
            # Find the successful submission for this progress
            successful_submission = PracticeSubmission.objects.filter(
                student=instance.student,
                question=instance.question,
                status='success'
            ).first()
            
            if successful_submission and successful_submission.points_earned == 0:
                # Recalculate points with updated timing information
                calculator = PointsCalculator()
                points_awarded = calculator.calculate_and_award_practice_points(
                    submission=successful_submission,
                    completion_time_seconds=instance.time_spent
                )
                
                logger.info(
                    f"Recalculated points with timing for {instance.student.username}: "
                    f"{points_awarded} points"
                )
                
        except Exception as e:
            logger.error(
                f"Error updating practice progress timing for {instance.id}: {e}",
                exc_info=True
            )


# Achievement checking signals (placeholder for future implementation)
@receiver(post_save, sender=PracticeSubmission)
def check_practice_achievements(sender, instance, created, **kwargs):
    """
    Check for new achievements after practice submissions.
    
    This triggers achievement checking when students complete practice questions.
    """
    if not created or instance.status != 'success':
        return
    
    try:
        from .achievement_engine import check_user_achievements
        from .realtime_service import realtime_service
        
        # Check achievements with practice completion context
        newly_awarded = check_user_achievements(
            user=instance.student,
            trigger_event='practice_completion',
            practice_question=instance.question,
            submission=instance
        )
        
        if newly_awarded:
            logger.info(
                f"User {instance.student.username} earned {len(newly_awarded)} new achievements: "
                f"{[a.achievement.name for a in newly_awarded]}"
            )
            
            # Send real-time achievement notifications
            for user_achievement in newly_awarded:
                achievement_data = {
                    'id': str(user_achievement.achievement.id),
                    'name': user_achievement.achievement.name,
                    'description': user_achievement.achievement.description,
                    'badge_type': user_achievement.achievement.badge_type,
                    'rarity': user_achievement.achievement.rarity,
                    'earned_at': user_achievement.earned_at.isoformat()
                }
                
                realtime_service.notify_achievement_earned(
                    user=instance.student,
                    achievement_data=achievement_data,
                    points_earned=0  # Achievements don't have points_reward field
                )
            
    except Exception as e:
        logger.error(
            f"Error checking achievements for practice submission {instance.id}: {e}",
            exc_info=True
        )


@receiver(post_save, sender=SubmissionAttempt)
def check_assignment_achievements(sender, instance, created, **kwargs):
    """
    Check for new achievements after assignment submissions.
    
    This triggers achievement checking when students complete assignments.
    """
    if not created:
        return
    
    try:
        from .achievement_engine import check_user_achievements
        from .realtime_service import realtime_service
        
        # Check achievements with assignment completion context
        newly_awarded = check_user_achievements(
            user=instance.student,
            trigger_event='assignment_completion',
            assignment_question=instance.assignment_question,
            submission=instance
        )
        
        if newly_awarded:
            logger.info(
                f"User {instance.student.username} earned {len(newly_awarded)} new achievements: "
                f"{[a.achievement.name for a in newly_awarded]}"
            )
            
            # Send real-time achievement notifications
            for user_achievement in newly_awarded:
                achievement_data = {
                    'id': str(user_achievement.achievement.id),
                    'name': user_achievement.achievement.name,
                    'description': user_achievement.achievement.description,
                    'badge_type': user_achievement.achievement.badge_type,
                    'rarity': user_achievement.achievement.rarity,
                    'earned_at': user_achievement.earned_at.isoformat()
                }
                
                realtime_service.notify_achievement_earned(
                    user=instance.student,
                    achievement_data=achievement_data,
                    points_earned=0  # Achievements don't have points_reward field
                )
        
    except Exception as e:
        logger.error(
            f"Error checking achievements for assignment submission {instance.id}: {e}",
            exc_info=True
        )


# Leaderboard update signals
@receiver(post_save, sender=PracticeSubmission)
def trigger_leaderboard_update_practice(sender, instance, created, **kwargs):
    """
    Trigger leaderboard updates after practice submissions.
    
    This updates leaderboards and sends real-time notifications when students
    complete practice questions and their rankings change.
    """
    if not created or instance.status != 'success':
        return
    
    try:
        from .leaderboard_manager import LeaderboardManager
        from .realtime_service import realtime_service
        
        # Update user's leaderboard position
        manager = LeaderboardManager()
        
        # Get old rank before update
        old_global_rank = manager.get_user_rank(instance.student, 'global')
        
        # Update leaderboard positions
        manager.update_user_leaderboard_position(instance.student)
        
        # Get new rank after update
        new_global_rank = manager.get_user_rank(instance.student, 'global')
        
        # Notify rank change if it changed
        if old_global_rank and new_global_rank and old_global_rank != new_global_rank:
            realtime_service.notify_rank_change(
                user=instance.student,
                old_rank=old_global_rank,
                new_rank=new_global_rank,
                leaderboard_type='global'
            )
        
        # Broadcast global leaderboard update
        realtime_service.broadcast_leaderboard_update(
            leaderboard_type='global'
        )
        
        # Update class leaderboards for user's classes
        from classes.models import Class
        user_classes = Class.objects.filter(
            enrollments__user=instance.student,
            enrollments__role='student'
        )
        
        for class_obj in user_classes:
            old_class_rank = manager.get_user_rank(instance.student, 'class', str(class_obj.id))
            
            # Class leaderboard is updated as part of update_user_leaderboard_position
            new_class_rank = manager.get_user_rank(instance.student, 'class', str(class_obj.id))
            
            # Notify class rank change
            if old_class_rank and new_class_rank and old_class_rank != new_class_rank:
                realtime_service.notify_rank_change(
                    user=instance.student,
                    old_rank=old_class_rank,
                    new_rank=new_class_rank,
                    leaderboard_type='class',
                    class_id=str(class_obj.id)
                )
            
            # Broadcast class leaderboard update
            realtime_service.broadcast_leaderboard_update(
                leaderboard_type='class',
                class_id=str(class_obj.id)
            )
        
    except Exception as e:
        logger.error(
            f"Error updating leaderboard for practice submission {instance.id}: {e}",
            exc_info=True
        )


@receiver(post_save, sender=SubmissionAttempt)
def trigger_leaderboard_update_assignment(sender, instance, created, **kwargs):
    """
    Trigger leaderboard updates after assignment submissions.
    
    This updates leaderboards and sends real-time notifications when students
    complete assignments and their rankings change.
    """
    if not created or instance.status not in ['success', 'fail']:
        return
    
    try:
        from .leaderboard_manager import LeaderboardManager
        from .realtime_service import realtime_service
        
        # Update user's leaderboard position
        manager = LeaderboardManager()
        
        # Get old rank before update
        old_global_rank = manager.get_user_rank(instance.student, 'global')
        
        # Update leaderboard positions
        manager.update_user_leaderboard_position(instance.student)
        
        # Get new rank after update
        new_global_rank = manager.get_user_rank(instance.student, 'global')
        
        # Notify rank change if it changed
        if old_global_rank and new_global_rank and old_global_rank != new_global_rank:
            realtime_service.notify_rank_change(
                user=instance.student,
                old_rank=old_global_rank,
                new_rank=new_global_rank,
                leaderboard_type='global'
            )
        
        # Broadcast global leaderboard update
        realtime_service.broadcast_leaderboard_update(
            leaderboard_type='global'
        )
        
        # Update class leaderboards for assignment's class
        if hasattr(instance.assignment_question, 'assignment') and hasattr(instance.assignment_question.assignment, 'class_obj'):
            class_obj = instance.assignment_question.assignment.class_obj
            old_class_rank = manager.get_user_rank(instance.student, 'class', str(class_obj.id))
            
            # Class leaderboard is updated as part of update_user_leaderboard_position
            new_class_rank = manager.get_user_rank(instance.student, 'class', str(class_obj.id))
            
            # Notify class rank change
            if old_class_rank and new_class_rank and old_class_rank != new_class_rank:
                realtime_service.notify_rank_change(
                    user=instance.student,
                    old_rank=old_class_rank,
                    new_rank=new_class_rank,
                    leaderboard_type='class',
                    class_id=str(class_obj.id)
                )
            
            # Broadcast class leaderboard update
            realtime_service.broadcast_leaderboard_update(
                leaderboard_type='class',
                class_id=str(class_obj.id)
            )
        
    except Exception as e:
        logger.error(
            f"Error updating leaderboard for assignment submission {instance.id}: {e}",
            exc_info=True
        )


@receiver(post_save, sender=Question)
def create_default_config(sender, instance, created, **kwargs):
    """
    Ensure every Question has a default configuration.
    This signal runs after a Question is saved.
    """
    if created or not instance.config:
        default_config = {
            "time_limit": 2.0,      # seconds
            "memory_limit": 256,    # MB
            "difficulty": instance.difficulty,
            "allow_imports": []
        }
        
        # Only update if config is empty or doesn't exist
        if not instance.config:
            instance.config = default_config
            instance.save(update_fields=['config'])