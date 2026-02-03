"""
Leaderboard Manager for the gamified autograder system.

This module provides the LeaderboardManager class that handles:
- Leaderboard calculation and caching
- Ranking with tie-breaking logic
- Global and class-specific leaderboards
- Real-time updates and performance optimization
"""

import logging
from typing import Dict, List, Optional, Tuple
from django.db import transaction
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import Q, Count, Sum, F

from .models import LeaderboardEntry, UserPoints, PracticeProgress, StudentAnalytics

logger = logging.getLogger(__name__)
User = get_user_model()


class LeaderboardManager:
    """
    Manager for leaderboard calculation, caching, and ranking.
    
    This class handles all leaderboard logic including:
    - Global and class-specific leaderboard calculation
    - Ranking with tie-breaking logic
    - Cached leaderboard data for performance
    - Real-time updates on user activity
    """
    
    def __init__(self):
        """Initialize the leaderboard manager"""
        self.logger = logger
    
    def update_global_leaderboard(self, force_refresh: bool = False) -> int:
        """
        Update the global leaderboard with current user data.
        
        Args:
            force_refresh: If True, recalculate all rankings regardless of cache age
            
        Returns:
            int: Number of leaderboard entries updated
        """
        try:
            with transaction.atomic():
                # Get all users with points, ordered by ranking criteria
                users_with_points = self._get_ranked_users_global()
                
                # Clear existing global leaderboard entries if force refresh
                if force_refresh:
                    LeaderboardEntry.objects.filter(
                        leaderboard_type='global',
                        class_id__isnull=True
                    ).delete()
                
                # Update or create leaderboard entries
                updated_count = 0
                for rank, user_data in enumerate(users_with_points, 1):
                    entry, created = LeaderboardEntry.objects.update_or_create(
                        user=user_data['user'],
                        leaderboard_type='global',
                        class_id=None,
                        defaults={
                            'rank': rank,
                            'total_points': user_data['total_points'],
                            'completed_problems': user_data['completed_problems']
                        }
                    )
                    updated_count += 1
                
                self.logger.info(f"Updated global leaderboard with {updated_count} entries")
                return updated_count
                
        except Exception as e:
            self.logger.error(f"Error updating global leaderboard: {e}", exc_info=True)
            return 0
    
    def update_class_leaderboard(self, class_id: str, force_refresh: bool = False) -> int:
        """
        Update the leaderboard for a specific class.
        
        Args:
            class_id: UUID of the class to update leaderboard for
            force_refresh: If True, recalculate all rankings regardless of cache age
            
        Returns:
            int: Number of leaderboard entries updated
        """
        try:
            with transaction.atomic():
                # Get class users with points, ordered by ranking criteria
                users_with_points = self._get_ranked_users_class(class_id)
                
                # Clear existing class leaderboard entries if force refresh
                if force_refresh:
                    LeaderboardEntry.objects.filter(
                        leaderboard_type='class',
                        class_id=class_id
                    ).delete()
                
                # Update or create leaderboard entries
                updated_count = 0
                for rank, user_data in enumerate(users_with_points, 1):
                    entry, created = LeaderboardEntry.objects.update_or_create(
                        user=user_data['user'],
                        leaderboard_type='class',
                        class_id=class_id,
                        defaults={
                            'rank': rank,
                            'total_points': user_data['total_points'],
                            'completed_problems': user_data['completed_problems']
                        }
                    )
                    updated_count += 1
                
                self.logger.info(f"Updated class {class_id} leaderboard with {updated_count} entries")
                return updated_count
                
        except Exception as e:
            self.logger.error(f"Error updating class {class_id} leaderboard: {e}", exc_info=True)
            return 0
    
    def _get_ranked_users_global(self) -> List[Dict]:
        """
        Get all users ranked by leaderboard criteria for global leaderboard.
        
        Ranking criteria (in order of priority):
        1. Total points (descending)
        2. Number of completed problems (descending)
        3. Most recent activity (descending)
        4. Username (ascending) - final tie-breaker
        
        Returns:
            List[Dict]: List of user data dictionaries with ranking info
        """
        # Get users with their points and completed problems count
        users_query = User.objects.filter(
            role='student',
            points__isnull=False
        ).select_related('points', 'analytics').annotate(
            completed_problems=Count(
                'practice_progress',
                filter=Q(practice_progress__is_completed=True)
            )
        ).order_by(
            '-points__total_points',  # Primary: Total points descending
            '-completed_problems',    # Secondary: Completed problems descending
            '-analytics__last_activity',  # Tertiary: Most recent activity
            'username'               # Final tie-breaker: Username ascending
        )
        
        ranked_users = []
        for user in users_query:
            user_data = {
                'user': user,
                'total_points': user.points.total_points,
                'completed_problems': getattr(user, 'completed_problems', 0),
                'last_activity': user.analytics.last_activity if hasattr(user, 'analytics') and user.analytics else None
            }
            ranked_users.append(user_data)
        
        return ranked_users
    
    def _get_ranked_users_class(self, class_id: str) -> List[Dict]:
        """
        Get class users ranked by leaderboard criteria for class-specific leaderboard.
        
        Args:
            class_id: UUID of the class
            
        Returns:
            List[Dict]: List of user data dictionaries with ranking info
        """
        # Import here to avoid circular imports
        from classes.models import Class, Enrollment
        
        try:
            # Get class instance
            class_obj = Class.objects.get(id=class_id)
            
            # Get class students through enrollment with their points and completed problems count
            users_query = User.objects.filter(
                enrollments__class_obj=class_obj,
                enrollments__role='student',
                points__isnull=False
            ).select_related('points', 'analytics').annotate(
                completed_problems=Count(
                    'practice_progress',
                    filter=Q(practice_progress__is_completed=True)
                )
            ).order_by(
                '-points__total_points',  # Primary: Total points descending
                '-completed_problems',    # Secondary: Completed problems descending
                '-analytics__last_activity',  # Tertiary: Most recent activity
                'username'               # Final tie-breaker: Username ascending
            )
            
            ranked_users = []
            for user in users_query:
                user_data = {
                    'user': user,
                    'total_points': user.points.total_points,
                    'completed_problems': getattr(user, 'completed_problems', 0),
                    'last_activity': user.analytics.last_activity if hasattr(user, 'analytics') and user.analytics else None
                }
                ranked_users.append(user_data)
            
            return ranked_users
            
        except Class.DoesNotExist:
            self.logger.error(f"Class {class_id} not found")
            return []
        except Exception as e:
            self.logger.error(f"Error getting ranked users for class {class_id}: {e}")
            return []
    
    def get_user_rank(self, user, leaderboard_type: str = 'global', class_id: str = None) -> Optional[int]:
        """
        Get the current rank of a user in the specified leaderboard.
        
        Args:
            user: User instance
            leaderboard_type: 'global' or 'class'
            class_id: Required if leaderboard_type is 'class'
            
        Returns:
            Optional[int]: User's current rank, or None if not found
        """
        try:
            entry = LeaderboardEntry.objects.get(
                user=user,
                leaderboard_type=leaderboard_type,
                class_id=class_id
            )
            return entry.rank
        except LeaderboardEntry.DoesNotExist:
            return None
    
    def get_leaderboard(self, leaderboard_type: str = 'global', class_id: str = None, 
                       limit: int = 50, offset: int = 0) -> List[Dict]:
        """
        Get leaderboard entries with pagination.
        
        Args:
            leaderboard_type: 'global' or 'class'
            class_id: Required if leaderboard_type is 'class'
            limit: Maximum number of entries to return
            offset: Number of entries to skip
            
        Returns:
            List[Dict]: List of leaderboard entry data
        """
        try:
            query = LeaderboardEntry.objects.filter(
                leaderboard_type=leaderboard_type
            ).select_related('user', 'user__points')
            
            if leaderboard_type == 'class' and class_id:
                query = query.filter(class_id=class_id)
            elif leaderboard_type == 'global':
                query = query.filter(class_id__isnull=True)
            
            entries = query.order_by('rank')[offset:offset + limit]
            
            leaderboard_data = []
            for entry in entries:
                entry_data = {
                    'rank': entry.rank,
                    'user': {
                        'id': entry.user.id,
                        'username': entry.user.username,
                        'first_name': entry.user.first_name,
                        'last_name': entry.user.last_name
                    },
                    'total_points': entry.total_points,
                    'completed_problems': entry.completed_problems,
                    'updated_at': entry.updated_at
                }
                leaderboard_data.append(entry_data)
            
            return leaderboard_data
            
        except Exception as e:
            self.logger.error(f"Error getting leaderboard: {e}")
            return []
    
    def get_nearby_competitors(self, user, leaderboard_type: str = 'global', 
                             class_id: str = None, range_size: int = 5) -> List[Dict]:
        """
        Get users ranked near the specified user.
        
        Args:
            user: User instance
            leaderboard_type: 'global' or 'class'
            class_id: Required if leaderboard_type is 'class'
            range_size: Number of users above and below to include
            
        Returns:
            List[Dict]: List of nearby leaderboard entries
        """
        user_rank = self.get_user_rank(user, leaderboard_type, class_id)
        if not user_rank:
            return []
        
        # Calculate range
        start_rank = max(1, user_rank - range_size)
        end_rank = user_rank + range_size
        
        try:
            query = LeaderboardEntry.objects.filter(
                leaderboard_type=leaderboard_type,
                rank__gte=start_rank,
                rank__lte=end_rank
            ).select_related('user', 'user__points')
            
            if leaderboard_type == 'class' and class_id:
                query = query.filter(class_id=class_id)
            elif leaderboard_type == 'global':
                query = query.filter(class_id__isnull=True)
            
            entries = query.order_by('rank')
            
            nearby_data = []
            for entry in entries:
                entry_data = {
                    'rank': entry.rank,
                    'user': {
                        'id': entry.user.id,
                        'username': entry.user.username,
                        'first_name': entry.user.first_name,
                        'last_name': entry.user.last_name
                    },
                    'total_points': entry.total_points,
                    'completed_problems': entry.completed_problems,
                    'is_current_user': entry.user == user,
                    'updated_at': entry.updated_at
                }
                nearby_data.append(entry_data)
            
            return nearby_data
            
        except Exception as e:
            self.logger.error(f"Error getting nearby competitors: {e}")
            return []
    
    def update_user_leaderboard_position(self, user):
        """
        Update a specific user's position in all relevant leaderboards.
        
        This method is called when a user's points or progress changes.
        
        Args:
            user: User instance whose position needs updating
        """
        try:
            # Update global leaderboard
            self._update_single_user_global(user)
            
            # Update class leaderboards for all classes the user belongs to
            self._update_single_user_classes(user)
            
        except Exception as e:
            self.logger.error(f"Error updating user {user.username} leaderboard position: {e}")
    
    def _update_single_user_global(self, user):
        """Update a single user's position in the global leaderboard"""
        try:
            # Get user's current stats
            user_points = getattr(user, 'points', None)
            if not user_points:
                return
            
            completed_problems = PracticeProgress.objects.filter(
                student=user,
                is_completed=True
            ).count()
            
            # Calculate new rank by counting users with better stats
            better_users_count = User.objects.filter(
                role='student',
                points__isnull=False
            ).annotate(
                completed_problems=Count(
                    'practice_progress',
                    filter=Q(practice_progress__is_completed=True)
                )
            ).filter(
                Q(points__total_points__gt=user_points.total_points) |
                Q(
                    points__total_points=user_points.total_points,
                    completed_problems__gt=completed_problems
                ) |
                Q(
                    points__total_points=user_points.total_points,
                    completed_problems=completed_problems,
                    analytics__last_activity__gt=F('analytics__last_activity')
                ) |
                Q(
                    points__total_points=user_points.total_points,
                    completed_problems=completed_problems,
                    analytics__last_activity=F('analytics__last_activity'),
                    username__lt=user.username
                )
            ).count()
            
            new_rank = better_users_count + 1
            
            # Update or create leaderboard entry
            LeaderboardEntry.objects.update_or_create(
                user=user,
                leaderboard_type='global',
                class_id=None,
                defaults={
                    'rank': new_rank,
                    'total_points': user_points.total_points,
                    'completed_problems': completed_problems
                }
            )
            
        except Exception as e:
            self.logger.error(f"Error updating single user global leaderboard: {e}")
    
    def _update_single_user_classes(self, user):
        """Update a single user's position in all class leaderboards they belong to"""
        try:
            # Import here to avoid circular imports
            from classes.models import Class, Enrollment
            
            # Get all classes the user belongs to as a student
            user_classes = Class.objects.filter(
                enrollments__user=user,
                enrollments__role='student'
            )
            
            for class_obj in user_classes:
                self._update_single_user_class(user, str(class_obj.id))
                
        except Exception as e:
            self.logger.error(f"Error updating single user class leaderboards: {e}")
    
    def _update_single_user_class(self, user, class_id: str):
        """Update a single user's position in a specific class leaderboard"""
        try:
            # Import here to avoid circular imports
            from classes.models import Class, Enrollment
            
            class_obj = Class.objects.get(id=class_id)
            
            # Get user's current stats
            user_points = getattr(user, 'points', None)
            if not user_points:
                return
            
            completed_problems = PracticeProgress.objects.filter(
                student=user,
                is_completed=True
            ).count()
            
            # Calculate new rank within the class
            better_users_count = User.objects.filter(
                enrollments__class_obj=class_obj,
                enrollments__role='student',
                points__isnull=False
            ).annotate(
                completed_problems=Count(
                    'practice_progress',
                    filter=Q(practice_progress__is_completed=True)
                )
            ).filter(
                Q(points__total_points__gt=user_points.total_points) |
                Q(
                    points__total_points=user_points.total_points,
                    completed_problems__gt=completed_problems
                ) |
                Q(
                    points__total_points=user_points.total_points,
                    completed_problems=completed_problems,
                    analytics__last_activity__gt=F('analytics__last_activity')
                ) |
                Q(
                    points__total_points=user_points.total_points,
                    completed_problems=completed_problems,
                    analytics__last_activity=F('analytics__last_activity'),
                    username__lt=user.username
                )
            ).count()
            
            new_rank = better_users_count + 1
            
            # Update or create leaderboard entry
            LeaderboardEntry.objects.update_or_create(
                user=user,
                leaderboard_type='class',
                class_id=class_id,
                defaults={
                    'rank': new_rank,
                    'total_points': user_points.total_points,
                    'completed_problems': completed_problems
                }
            )
            
        except Exception as e:
            self.logger.error(f"Error updating single user class leaderboard: {e}")
    
    def get_leaderboard_stats(self, leaderboard_type: str = 'global', class_id: str = None) -> Dict:
        """
        Get statistics about a leaderboard.
        
        Args:
            leaderboard_type: 'global' or 'class'
            class_id: Required if leaderboard_type is 'class'
            
        Returns:
            Dict: Leaderboard statistics
        """
        try:
            query = LeaderboardEntry.objects.filter(
                leaderboard_type=leaderboard_type
            )
            
            if leaderboard_type == 'class' and class_id:
                query = query.filter(class_id=class_id)
            elif leaderboard_type == 'global':
                query = query.filter(class_id__isnull=True)
            
            stats = query.aggregate(
                total_participants=Count('id'),
                avg_points=Sum('total_points') / Count('id') if query.count() > 0 else 0,
                max_points=query.order_by('-total_points').first().total_points if query.exists() else 0,
                total_problems_solved=Sum('completed_problems')
            )
            
            return {
                'total_participants': stats['total_participants'] or 0,
                'average_points': round(stats['avg_points'] or 0, 2),
                'max_points': stats['max_points'] or 0,
                'total_problems_solved': stats['total_problems_solved'] or 0,
                'last_updated': timezone.now()
            }
            
        except Exception as e:
            self.logger.error(f"Error getting leaderboard stats: {e}")
            return {
                'total_participants': 0,
                'average_points': 0,
                'max_points': 0,
                'total_problems_solved': 0,
                'last_updated': timezone.now()
            }


# Utility functions for leaderboard management

def update_global_leaderboard(force_refresh: bool = False) -> int:
    """
    Convenience function to update the global leaderboard.
    
    Args:
        force_refresh: If True, recalculate all rankings
        
    Returns:
        int: Number of entries updated
    """
    manager = LeaderboardManager()
    return manager.update_global_leaderboard(force_refresh)


def update_class_leaderboard(class_id: str, force_refresh: bool = False) -> int:
    """
    Convenience function to update a class leaderboard.
    
    Args:
        class_id: UUID of the class
        force_refresh: If True, recalculate all rankings
        
    Returns:
        int: Number of entries updated
    """
    manager = LeaderboardManager()
    return manager.update_class_leaderboard(class_id, force_refresh)


def update_user_leaderboard_position(user):
    """
    Convenience function to update a user's leaderboard position.
    
    Args:
        user: User instance
    """
    manager = LeaderboardManager()
    manager.update_user_leaderboard_position(user)


def update_user_leaderboard_position(user):
    """
    Convenience function to update a user's leaderboard position.
    
    Args:
        user: User instance
    """
    manager = LeaderboardManager()
    manager.update_user_leaderboard_position(user)


# Static methods for WebSocket consumers
class LeaderboardManagerStatic:
    """Static methods for WebSocket consumer compatibility"""
    
    @staticmethod
    def get_leaderboard_page(leaderboard_type: str = 'global', class_id: str = None, 
                           page: int = 1, page_size: int = 20) -> Dict:
        """
        Get paginated leaderboard data for WebSocket consumers.
        
        Args:
            leaderboard_type: 'global' or 'class'
            class_id: Required if leaderboard_type is 'class'
            page: Page number (1-based)
            page_size: Number of entries per page
            
        Returns:
            Dict: Paginated leaderboard data
        """
        manager = LeaderboardManager()
        offset = (page - 1) * page_size
        
        leaderboard_data = manager.get_leaderboard(
            leaderboard_type=leaderboard_type,
            class_id=class_id,
            limit=page_size,
            offset=offset
        )
        
        # Get total count for pagination
        try:
            query = LeaderboardEntry.objects.filter(
                leaderboard_type=leaderboard_type
            )
            
            if leaderboard_type == 'class' and class_id:
                query = query.filter(class_id=class_id)
            elif leaderboard_type == 'global':
                query = query.filter(class_id__isnull=True)
            
            total_count = query.count()
            total_pages = (total_count + page_size - 1) // page_size
            
        except Exception:
            total_count = len(leaderboard_data)
            total_pages = 1
        
        return {
            'entries': leaderboard_data,
            'pagination': {
                'page': page,
                'page_size': page_size,
                'total_count': total_count,
                'total_pages': total_pages,
                'has_next': page < total_pages,
                'has_previous': page > 1
            }
        }
    
    @staticmethod
    def get_user_rank(user, leaderboard_type: str = 'global', class_id: str = None) -> Dict:
        """
        Get user's rank data for WebSocket consumers.
        
        Args:
            user: User instance
            leaderboard_type: 'global' or 'class'
            class_id: Required if leaderboard_type is 'class'
            
        Returns:
            Dict: User's rank data with nearby competitors
        """
        manager = LeaderboardManager()
        
        # Get user's current rank
        user_rank = manager.get_user_rank(user, leaderboard_type, class_id)
        
        if not user_rank:
            return {
                'user_rank': None,
                'user_data': None,
                'nearby_competitors': []
            }
        
        # Get user's leaderboard entry data
        try:
            entry = LeaderboardEntry.objects.get(
                user=user,
                leaderboard_type=leaderboard_type,
                class_id=class_id
            )
            
            user_data = {
                'rank': entry.rank,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                },
                'total_points': entry.total_points,
                'completed_problems': entry.completed_problems,
                'updated_at': entry.updated_at
            }
            
        except LeaderboardEntry.DoesNotExist:
            user_data = None
        
        # Get nearby competitors
        nearby_competitors = manager.get_nearby_competitors(
            user, leaderboard_type, class_id, range_size=3
        )
        
        return {
            'user_rank': user_rank,
            'user_data': user_data,
            'nearby_competitors': nearby_competitors
        }