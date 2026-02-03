"""
Real-time notification service for gamification features.

This service handles broadcasting WebSocket messages for:
- Leaderboard updates
- Achievement notifications
- Points changes
- Rank changes
"""

import json
import logging
from typing import Optional, Dict, Any, List
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)
User = get_user_model()


class RealtimeService:
    """Service for broadcasting real-time gamification updates."""
    
    def __init__(self):
        self.channel_layer = get_channel_layer()
    
    def broadcast_leaderboard_update(self, leaderboard_type: str, class_id: Optional[str] = None, data: Optional[Dict] = None):
        """
        Broadcast leaderboard update to all connected clients.
        
        Args:
            leaderboard_type: 'global' or 'class'
            class_id: Required for class leaderboards
            data: Optional leaderboard data to include
        """
        if not self.channel_layer:
            logger.warning("Channel layer not configured - skipping leaderboard broadcast")
            return
        
        # Determine group name
        if leaderboard_type == 'global':
            group_name = "leaderboard_global"
        else:
            group_name = f"leaderboard_class_{class_id}"
        
        # Prepare message
        message = {
            'type': 'leaderboard_update',
            'leaderboard_type': leaderboard_type,
            'data': data or {}
        }
        
        if class_id:
            message['class_id'] = class_id
        
        # Broadcast to group
        try:
            async_to_sync(self.channel_layer.group_send)(group_name, message)
            logger.info(f"Broadcasted leaderboard update to {group_name}")
        except Exception as e:
            logger.error(f"Failed to broadcast leaderboard update: {e}")
    
    def notify_rank_change(self, user, old_rank: int, new_rank: int, leaderboard_type: str, class_id: Optional[str] = None):
        """
        Notify a specific user about their rank change.
        
        Args:
            user: User object
            old_rank: Previous rank
            new_rank: New rank
            leaderboard_type: 'global' or 'class'
            class_id: Required for class leaderboards
        """
        if not self.channel_layer:
            logger.warning("Channel layer not configured - skipping rank change notification")
            return
        
        user_group_name = f"user_{user.id}"
        
        message = {
            'type': 'rank_change',
            'old_rank': old_rank,
            'new_rank': new_rank,
            'leaderboard_type': leaderboard_type
        }
        
        if class_id:
            message['class_id'] = class_id
        
        try:
            async_to_sync(self.channel_layer.group_send)(user_group_name, message)
            logger.info(f"Notified user {user.username} of rank change: {old_rank} -> {new_rank}")
        except Exception as e:
            logger.error(f"Failed to notify rank change: {e}")
    
    def notify_achievement_earned(self, user, achievement_data: Dict, points_earned: int = 0):
        """
        Notify a user about earning an achievement.
        
        Args:
            user: User object
            achievement_data: Achievement information
            points_earned: Points earned from the achievement
        """
        if not self.channel_layer:
            logger.warning("Channel layer not configured - skipping achievement notification")
            return
        
        user_group_name = f"user_{user.id}"
        
        message = {
            'type': 'achievement_earned',
            'achievement': achievement_data,
            'points_earned': points_earned
        }
        
        try:
            async_to_sync(self.channel_layer.group_send)(user_group_name, message)
            logger.info(f"Notified user {user.username} of achievement: {achievement_data.get('name', 'Unknown')}")
        except Exception as e:
            logger.error(f"Failed to notify achievement earned: {e}")
    
    def notify_points_update(self, user, old_points: int, new_points: int, source: str = 'unknown'):
        """
        Notify a user about points update.
        
        Args:
            user: User object
            old_points: Previous total points
            new_points: New total points
            source: Source of points (e.g., 'practice', 'assignment')
        """
        if not self.channel_layer:
            logger.warning("Channel layer not configured - skipping points notification")
            return
        
        user_group_name = f"user_{user.id}"
        points_earned = new_points - old_points
        
        message = {
            'type': 'points_update',
            'old_points': old_points,
            'new_points': new_points,
            'points_earned': points_earned,
            'source': source
        }
        
        try:
            async_to_sync(self.channel_layer.group_send)(user_group_name, message)
            logger.info(f"Notified user {user.username} of points update: {old_points} -> {new_points}")
        except Exception as e:
            logger.error(f"Failed to notify points update: {e}")
    
    def notify_practice_completed(self, user, question_title: str, points_earned: int, attempt_number: int):
        """
        Notify a user about completing a practice question.
        
        Args:
            user: User object
            question_title: Title of the completed question
            points_earned: Points earned from completion
            attempt_number: Which attempt this was
        """
        if not self.channel_layer:
            logger.warning("Channel layer not configured - skipping practice completion notification")
            return
        
        user_group_name = f"game_user_{user.id}"
        
        message = {
            'type': 'practice_completed',
            'question_title': question_title,
            'points_earned': points_earned,
            'attempt_number': attempt_number
        }
        
        try:
            async_to_sync(self.channel_layer.group_send)(user_group_name, message)
            logger.info(f"Notified user {user.username} of practice completion: {question_title}")
        except Exception as e:
            logger.error(f"Failed to notify practice completion: {e}")
    
    def notify_assignment_submitted(self, user, assignment_title: str, points_earned: int, score: Optional[float] = None):
        """
        Notify a user about assignment submission.
        
        Args:
            user: User object
            assignment_title: Title of the submitted assignment
            points_earned: Points earned from submission
            score: Optional score percentage
        """
        if not self.channel_layer:
            logger.warning("Channel layer not configured - skipping assignment submission notification")
            return
        
        user_group_name = f"game_user_{user.id}"
        
        message = {
            'type': 'assignment_submitted',
            'assignment_title': assignment_title,
            'points_earned': points_earned
        }
        
        if score is not None:
            message['score'] = score
        
        try:
            async_to_sync(self.channel_layer.group_send)(user_group_name, message)
            logger.info(f"Notified user {user.username} of assignment submission: {assignment_title}")
        except Exception as e:
            logger.error(f"Failed to notify assignment submission: {e}")
    
    def notify_streak_update(self, user, current_streak: int, streak_type: str):
        """
        Notify a user about streak update.
        
        Args:
            user: User object
            current_streak: Current streak count
            streak_type: Type of streak (e.g., 'daily', 'weekly')
        """
        if not self.channel_layer:
            logger.warning("Channel layer not configured - skipping streak notification")
            return
        
        user_group_name = f"game_user_{user.id}"
        
        message = {
            'type': 'streak_update',
            'current_streak': current_streak,
            'streak_type': streak_type
        }
        
        try:
            async_to_sync(self.channel_layer.group_send)(user_group_name, message)
            logger.info(f"Notified user {user.username} of streak update: {current_streak} {streak_type}")
        except Exception as e:
            logger.error(f"Failed to notify streak update: {e}")
    
    def broadcast_to_class(self, class_id: str, message_type: str, data: Dict[str, Any]):
        """
        Broadcast a message to all users in a specific class.
        
        Args:
            class_id: Class UUID
            message_type: Type of message
            data: Message data
        """
        if not self.channel_layer:
            logger.warning("Channel layer not configured - skipping class broadcast")
            return
        
        group_name = f"leaderboard_class_{class_id}"
        
        message = {
            'type': message_type,
            'class_id': class_id,
            **data
        }
        
        try:
            async_to_sync(self.channel_layer.group_send)(group_name, message)
            logger.info(f"Broadcasted {message_type} to class {class_id}")
        except Exception as e:
            logger.error(f"Failed to broadcast to class: {e}")


# Global instance
realtime_service = RealtimeService()