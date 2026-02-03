"""
Cached Leaderboard Manager with performance optimization.

This module extends the LeaderboardManager with comprehensive caching strategies:
- Cache-first data retrieval with fallback to database
- Intelligent cache invalidation on data changes
- Background cache warming for frequently accessed data
- Performance monitoring and cache hit rate tracking
"""

import logging
from typing import Dict, List, Optional, Tuple, Any
from django.db import transaction
from django.utils import timezone
from django.contrib.auth import get_user_model

from .leaderboard_manager import LeaderboardManager
from .cache_service import cache_service
from .models import LeaderboardEntry, UserPoints, PracticeProgress

logger = logging.getLogger(__name__)
User = get_user_model()


class CachedLeaderboardManager(LeaderboardManager):
    """
    Enhanced LeaderboardManager with comprehensive caching.
    
    This class provides:
    - Cache-first data retrieval with database fallback
    - Automatic cache invalidation on updates
    - Background cache warming for performance
    - Cache hit rate monitoring and statistics
    """
    
    def __init__(self):
        super().__init__()
        self.cache_service = cache_service
        self.cache_hits = 0
        self.cache_misses = 0
    
    # ==================== CACHED LEADERBOARD OPERATIONS ====================
    
    def get_leaderboard(self, leaderboard_type: str = 'global', class_id: str = None,
                       limit: int = 50, offset: int = 0) -> List[Dict]:
        """
        Get leaderboard with caching support.
        
        Args:
            leaderboard_type: 'global' or 'class'
            class_id: Required for class leaderboards
            limit: Maximum number of entries to return
            offset: Number of entries to skip
            
        Returns:
            List[Dict]: Leaderboard entries
        """
        # Calculate page parameters for caching
        page_size = limit
        page = (offset // page_size) + 1
        
        # Try to get from cache first
        cached_data = self.cache_service.get_leaderboard(
            leaderboard_type=leaderboard_type,
            class_id=class_id,
            page=page,
            page_size=page_size
        )
        
        if cached_data and 'data' in cached_data:
            self.cache_hits += 1
            self.logger.debug(f"Cache hit for leaderboard {leaderboard_type}")
            
            # Extract entries from cached data
            if 'entries' in cached_data['data']:
                return cached_data['data']['entries']
            return cached_data['data']
        
        # Cache miss - get from database
        self.cache_misses += 1
        self.logger.debug(f"Cache miss for leaderboard {leaderboard_type}")
        
        # Get fresh data from parent class
        leaderboard_data = super().get_leaderboard(
            leaderboard_type=leaderboard_type,
            class_id=class_id,
            limit=limit,
            offset=offset
        )
        
        # Cache the result
        if leaderboard_data:
            self.cache_service.set_leaderboard(
                data={'entries': leaderboard_data},
                leaderboard_type=leaderboard_type,
                class_id=class_id,
                page=page,
                page_size=page_size
            )
        
        return leaderboard_data
    
    def get_user_rank(self, user, leaderboard_type: str = 'global',
                     class_id: str = None) -> Optional[int]:
        """
        Get user rank with caching support.
        
        Args:
            user: User instance
            leaderboard_type: 'global' or 'class'
            class_id: Required for class leaderboards
            
        Returns:
            Optional[int]: User's rank or None if not found
        """
        # Try cache first
        cached_rank_data = self.cache_service.get_user_rank(
            user_id=user.id,
            leaderboard_type=leaderboard_type,
            class_id=class_id
        )
        
        if cached_rank_data and 'data' in cached_rank_data:
            self.cache_hits += 1
            rank_data = cached_rank_data['data']
            if 'user_rank' in rank_data:
                return rank_data['user_rank']
        
        # Cache miss - get from database
        self.cache_misses += 1
        rank = super().get_user_rank(user, leaderboard_type, class_id)
        
        # Cache the result
        if rank is not None:
            rank_data = {
                'user_rank': rank,
                'user_id': user.id,
                'leaderboard_type': leaderboard_type,
                'class_id': class_id,
                'cached_at': timezone.now().isoformat()
            }
            
            self.cache_service.set_user_rank(
                user_id=user.id,
                data=rank_data,
                leaderboard_type=leaderboard_type,
                class_id=class_id
            )
        
        return rank
    
    def get_nearby_competitors(self, user, leaderboard_type: str = 'global',
                             class_id: str = None, range_size: int = 5) -> List[Dict]:
        """
        Get nearby competitors with caching support.
        
        Args:
            user: User instance
            leaderboard_type: 'global' or 'class'
            class_id: Required for class leaderboards
            range_size: Number of users above and below to include
            
        Returns:
            List[Dict]: Nearby competitor data
        """
        # Try to get user rank from cache
        cached_rank_data = self.cache_service.get_user_rank(
            user_id=user.id,
            leaderboard_type=leaderboard_type,
            class_id=class_id
        )
        
        if cached_rank_data and 'data' in cached_rank_data:
            rank_data = cached_rank_data['data']
            if 'nearby_competitors' in rank_data:
                self.cache_hits += 1
                return rank_data['nearby_competitors']
        
        # Cache miss - get from database
        self.cache_misses += 1
        nearby_data = super().get_nearby_competitors(
            user, leaderboard_type, class_id, range_size
        )
        
        # Cache the result with user rank data
        user_rank = self.get_user_rank(user, leaderboard_type, class_id)
        if user_rank is not None:
            rank_data = {
                'user_rank': user_rank,
                'nearby_competitors': nearby_data,
                'user_id': user.id,
                'leaderboard_type': leaderboard_type,
                'class_id': class_id,
                'cached_at': timezone.now().isoformat()
            }
            
            self.cache_service.set_user_rank(
                user_id=user.id,
                data=rank_data,
                leaderboard_type=leaderboard_type,
                class_id=class_id
            )
        
        return nearby_data
    
    # ==================== CACHED UPDATE OPERATIONS ====================
    
    @transaction.atomic
    def update_global_leaderboard(self, force_refresh: bool = False) -> int:
        """
        Update global leaderboard with cache invalidation.
        
        Args:
            force_refresh: If True, recalculate all rankings
            
        Returns:
            int: Number of entries updated
        """
        # Invalidate global leaderboard caches before update
        self.cache_service.invalidate_leaderboard_caches(leaderboard_type='global')
        
        # Update the leaderboard
        updated_count = super().update_global_leaderboard(force_refresh)
        
        # Warm the cache with first few pages
        if updated_count > 0:
            self._warm_leaderboard_cache('global', pages=3)
        
        self.logger.info(f"Updated global leaderboard and invalidated caches ({updated_count} entries)")
        return updated_count
    
    @transaction.atomic
    def update_class_leaderboard(self, class_id: str, force_refresh: bool = False) -> int:
        """
        Update class leaderboard with cache invalidation.
        
        Args:
            class_id: UUID of the class to update
            force_refresh: If True, recalculate all rankings
            
        Returns:
            int: Number of entries updated
        """
        # Invalidate class leaderboard caches before update
        self.cache_service.invalidate_leaderboard_caches(
            leaderboard_type='class',
            class_id=class_id
        )
        
        # Update the leaderboard
        updated_count = super().update_class_leaderboard(class_id, force_refresh)
        
        # Warm the cache with first few pages
        if updated_count > 0:
            self._warm_leaderboard_cache('class', class_id=class_id, pages=2)
        
        self.logger.info(f"Updated class {class_id} leaderboard and invalidated caches ({updated_count} entries)")
        return updated_count
    
    def update_user_leaderboard_position(self, user):
        """
        Update user's leaderboard position with cache invalidation.
        
        Args:
            user: User instance whose position needs updating
        """
        # Invalidate user-specific caches
        self.cache_service.invalidate_user_caches(user.id)
        
        # Update the position
        super().update_user_leaderboard_position(user)
        
        # Invalidate affected leaderboard caches
        self.cache_service.invalidate_leaderboard_caches(leaderboard_type='global')
        
        # Invalidate class leaderboards for user's classes
        try:
            from classes.models import Class, Enrollment
            user_classes = Class.objects.filter(
                enrollments__user=user,
                enrollments__role='student'
            )
            
            for class_obj in user_classes:
                self.cache_service.invalidate_leaderboard_caches(
                    leaderboard_type='class',
                    class_id=str(class_obj.id)
                )
        except Exception as e:
            self.logger.error(f"Error invalidating class caches for user {user.username}: {e}")
        
        self.logger.info(f"Updated leaderboard position for {user.username} and invalidated caches")
    
    # ==================== CACHE WARMING ====================
    
    def _warm_leaderboard_cache(self, leaderboard_type: str, class_id: str = None,
                               pages: int = 3) -> bool:
        """
        Warm leaderboard cache with commonly accessed pages.
        
        Args:
            leaderboard_type: Type of leaderboard to warm
            class_id: Class ID for class leaderboards
            pages: Number of pages to pre-cache
            
        Returns:
            bool: True if warming was successful
        """
        try:
            for page in range(1, pages + 1):
                offset = (page - 1) * 20
                
                # Get fresh data
                leaderboard_data = super().get_leaderboard(
                    leaderboard_type=leaderboard_type,
                    class_id=class_id,
                    limit=20,
                    offset=offset
                )
                
                # Cache the data
                if leaderboard_data:
                    self.cache_service.set_leaderboard(
                        data={'entries': leaderboard_data},
                        leaderboard_type=leaderboard_type,
                        class_id=class_id,
                        page=page,
                        page_size=20
                    )
            
            self.logger.debug(f"Warmed {pages} pages of {leaderboard_type} leaderboard cache")
            return True
            
        except Exception as e:
            self.logger.error(f"Error warming leaderboard cache: {e}")
            return False
    
    def warm_user_rank_cache(self, user_ids: List, leaderboard_type: str = 'global',
                            class_id: str = None) -> int:
        """
        Warm user rank cache for specific users.
        
        Args:
            user_ids: List of user IDs to warm cache for
            leaderboard_type: Type of leaderboard
            class_id: Class ID for class leaderboards
            
        Returns:
            int: Number of users cached
        """
        warmed_count = 0
        
        try:
            for user_id in user_ids:
                try:
                    user = User.objects.get(id=user_id)
                    
                    # Get rank and nearby competitors
                    rank = super().get_user_rank(user, leaderboard_type, class_id)
                    nearby = super().get_nearby_competitors(
                        user, leaderboard_type, class_id, range_size=3
                    )
                    
                    if rank is not None:
                        rank_data = {
                            'user_rank': rank,
                            'nearby_competitors': nearby,
                            'user_id': user.id,
                            'leaderboard_type': leaderboard_type,
                            'class_id': class_id,
                            'cached_at': timezone.now().isoformat()
                        }
                        
                        self.cache_service.set_user_rank(
                            user_id=user.id,
                            data=rank_data,
                            leaderboard_type=leaderboard_type,
                            class_id=class_id
                        )
                        
                        warmed_count += 1
                        
                except User.DoesNotExist:
                    self.logger.warning(f"User {user_id} not found for rank cache warming")
                    continue
            
            self.logger.info(f"Warmed rank cache for {warmed_count} users")
            return warmed_count
            
        except Exception as e:
            self.logger.error(f"Error warming user rank cache: {e}")
            return 0
    
    # ==================== PERFORMANCE MONITORING ====================
    
    def get_cache_performance_stats(self) -> Dict[str, Any]:
        """
        Get cache performance statistics.
        
        Returns:
            Dict: Cache hit rates and performance metrics
        """
        total_requests = self.cache_hits + self.cache_misses
        hit_rate = (self.cache_hits / total_requests * 100) if total_requests > 0 else 0
        
        return {
            'cache_hits': self.cache_hits,
            'cache_misses': self.cache_misses,
            'total_requests': total_requests,
            'hit_rate_percentage': round(hit_rate, 2),
            'cache_service_stats': self.cache_service.get_cache_stats(),
            'timestamp': timezone.now().isoformat()
        }
    
    def reset_performance_counters(self):
        """Reset cache performance counters."""
        self.cache_hits = 0
        self.cache_misses = 0
        self.logger.info("Reset cache performance counters")
    
    # ==================== BATCH OPERATIONS ====================
    
    def batch_update_leaderboards(self, class_ids: List[str] = None) -> Dict[str, int]:
        """
        Batch update multiple leaderboards efficiently.
        
        Args:
            class_ids: List of class IDs to update, or None for all classes
            
        Returns:
            Dict: Update results for each leaderboard
        """
        results = {}
        
        try:
            # Update global leaderboard
            global_count = self.update_global_leaderboard()
            results['global'] = global_count
            
            # Update class leaderboards
            if class_ids:
                target_classes = class_ids
            else:
                # Get all active classes
                try:
                    from classes.models import Class
                    target_classes = list(Class.objects.filter(
                        is_active=True
                    ).values_list('id', flat=True))
                except ImportError:
                    target_classes = []
            
            for class_id in target_classes:
                try:
                    class_count = self.update_class_leaderboard(str(class_id))
                    results[f'class_{class_id}'] = class_count
                except Exception as e:
                    self.logger.error(f"Error updating leaderboard for class {class_id}: {e}")
                    results[f'class_{class_id}'] = 0
            
            self.logger.info(f"Batch updated {len(results)} leaderboards")
            return results
            
        except Exception as e:
            self.logger.error(f"Error in batch leaderboard update: {e}")
            return {'error': str(e)}
    
    def preload_popular_data(self) -> Dict[str, bool]:
        """
        Preload commonly accessed leaderboard data into cache.
        
        Returns:
            Dict: Success status for each preload operation
        """
        results = {}
        
        try:
            # Warm global leaderboard (first 5 pages)
            results['global_leaderboard'] = self._warm_leaderboard_cache('global', pages=5)
            
            # Warm top user ranks (top 100 users)
            try:
                top_users = User.objects.filter(
                    role='student',
                    points__isnull=False
                ).order_by('-points__total_points')[:100]
                
                user_ids = [user.id for user in top_users]
                warmed_count = self.warm_user_rank_cache(user_ids, 'global')
                results['top_user_ranks'] = warmed_count > 0
                
            except Exception as e:
                self.logger.error(f"Error warming top user ranks: {e}")
                results['top_user_ranks'] = False
            
            # Warm active class leaderboards
            try:
                from classes.models import Class
                active_classes = Class.objects.filter(is_active=True)[:10]  # Top 10 active classes
                
                for class_obj in active_classes:
                    class_result = self._warm_leaderboard_cache(
                        'class', 
                        class_id=str(class_obj.id), 
                        pages=3
                    )
                    results[f'class_{class_obj.id}'] = class_result
                    
            except ImportError:
                results['class_leaderboards'] = False
            
            self.logger.info(f"Preloaded popular data: {results}")
            return results
            
        except Exception as e:
            self.logger.error(f"Error preloading popular data: {e}")
            return {'error': str(e)}


# Global cached leaderboard manager instance
cached_leaderboard_manager = CachedLeaderboardManager()


# Utility functions for easy access
def get_cached_leaderboard(leaderboard_type: str = 'global', class_id: str = None,
                          limit: int = 50, offset: int = 0) -> List[Dict]:
    """Get leaderboard data with caching."""
    return cached_leaderboard_manager.get_leaderboard(
        leaderboard_type, class_id, limit, offset
    )


def get_cached_user_rank(user, leaderboard_type: str = 'global',
                        class_id: str = None) -> Optional[int]:
    """Get user rank with caching."""
    return cached_leaderboard_manager.get_user_rank(user, leaderboard_type, class_id)


def update_leaderboards_with_cache(class_ids: List[str] = None) -> Dict[str, int]:
    """Update leaderboards with cache management."""
    return cached_leaderboard_manager.batch_update_leaderboards(class_ids)


def warm_leaderboard_caches() -> Dict[str, bool]:
    """Warm commonly accessed leaderboard caches."""
    return cached_leaderboard_manager.preload_popular_data()