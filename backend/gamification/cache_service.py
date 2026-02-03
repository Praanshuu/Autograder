"""
Caching service for gamification analytics and leaderboards.

This module provides comprehensive caching strategies for:
- Leaderboard data (global and class-specific)
- Student analytics and performance data
- Achievement progress and badge collections
- Real-time update coordination with cache invalidation
"""

import json
import logging
from typing import Dict, List, Optional, Any, Union
from datetime import datetime, timedelta
from django.core.cache import cache
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)
User = get_user_model()


class CacheService:
    """
    Centralized caching service for gamification features.
    
    Provides:
    - Hierarchical cache key management
    - Automatic cache invalidation strategies
    - Performance-optimized data retrieval
    - Cache warming and preloading
    """
    
    # Cache key prefixes
    LEADERBOARD_PREFIX = "leaderboard"
    ANALYTICS_PREFIX = "analytics"
    ACHIEVEMENTS_PREFIX = "achievements"
    USER_STATS_PREFIX = "user_stats"
    CLASS_STATS_PREFIX = "class_stats"
    
    # Cache timeouts (in seconds)
    LEADERBOARD_TIMEOUT = 300      # 5 minutes
    ANALYTICS_TIMEOUT = 600        # 10 minutes
    USER_STATS_TIMEOUT = 900       # 15 minutes
    CLASS_STATS_TIMEOUT = 1800     # 30 minutes
    ACHIEVEMENTS_TIMEOUT = 3600    # 1 hour
    
    def __init__(self):
        self.logger = logger
    
    # ==================== CACHE KEY MANAGEMENT ====================
    
    def _make_key(self, *parts: str) -> str:
        """Create a standardized cache key from parts."""
        return ":".join(str(part) for part in parts if part is not None)
    
    def _get_leaderboard_key(self, leaderboard_type: str, class_id: str = None, 
                           page: int = 1, page_size: int = 20) -> str:
        """Generate cache key for leaderboard data."""
        if leaderboard_type == 'class' and class_id:
            return self._make_key(self.LEADERBOARD_PREFIX, leaderboard_type, 
                                class_id, f"p{page}", f"s{page_size}")
        return self._make_key(self.LEADERBOARD_PREFIX, leaderboard_type, 
                            f"p{page}", f"s{page_size}")
    
    def _get_user_rank_key(self, user_id: Union[str, int], leaderboard_type: str, 
                          class_id: str = None) -> str:
        """Generate cache key for user rank data."""
        if leaderboard_type == 'class' and class_id:
            return self._make_key(self.LEADERBOARD_PREFIX, "user_rank", 
                                user_id, leaderboard_type, class_id)
        return self._make_key(self.LEADERBOARD_PREFIX, "user_rank", 
                            user_id, leaderboard_type)
    
    def _get_analytics_key(self, user_id: Union[str, int], data_type: str = "summary") -> str:
        """Generate cache key for user analytics data."""
        return self._make_key(self.ANALYTICS_PREFIX, user_id, data_type)
    
    def _get_class_analytics_key(self, class_id: str, data_type: str = "summary") -> str:
        """Generate cache key for class analytics data."""
        return self._make_key(self.CLASS_STATS_PREFIX, class_id, data_type)
    
    def _get_achievements_key(self, user_id: Union[str, int], data_type: str = "earned") -> str:
        """Generate cache key for user achievements data."""
        return self._make_key(self.ACHIEVEMENTS_PREFIX, user_id, data_type)
    
    # ==================== LEADERBOARD CACHING ====================
    
    def get_leaderboard(self, leaderboard_type: str = 'global', class_id: str = None,
                       page: int = 1, page_size: int = 20) -> Optional[Dict]:
        """
        Get cached leaderboard data.
        
        Args:
            leaderboard_type: 'global' or 'class'
            class_id: Required for class leaderboards
            page: Page number
            page_size: Number of entries per page
            
        Returns:
            Dict: Cached leaderboard data or None if not cached
        """
        cache_key = self._get_leaderboard_key(leaderboard_type, class_id, page, page_size)
        
        try:
            cached_data = cache.get(cache_key)
            if cached_data:
                self.logger.debug(f"Cache hit for leaderboard: {cache_key}")
                return json.loads(cached_data) if isinstance(cached_data, str) else cached_data
            
            self.logger.debug(f"Cache miss for leaderboard: {cache_key}")
            return None
            
        except Exception as e:
            self.logger.error(f"Error retrieving cached leaderboard {cache_key}: {e}")
            return None
    
    def set_leaderboard(self, data: Dict, leaderboard_type: str = 'global', 
                       class_id: str = None, page: int = 1, page_size: int = 20) -> bool:
        """
        Cache leaderboard data.
        
        Args:
            data: Leaderboard data to cache
            leaderboard_type: 'global' or 'class'
            class_id: Required for class leaderboards
            page: Page number
            page_size: Number of entries per page
            
        Returns:
            bool: True if successfully cached
        """
        cache_key = self._get_leaderboard_key(leaderboard_type, class_id, page, page_size)
        
        try:
            # Add cache metadata
            cache_data = {
                'data': data,
                'cached_at': timezone.now().isoformat(),
                'leaderboard_type': leaderboard_type,
                'class_id': class_id,
                'page': page,
                'page_size': page_size
            }
            
            success = cache.set(cache_key, cache_data, timeout=self.LEADERBOARD_TIMEOUT)
            
            if success:
                self.logger.debug(f"Cached leaderboard: {cache_key}")
            else:
                self.logger.warning(f"Failed to cache leaderboard: {cache_key}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error caching leaderboard {cache_key}: {e}")
            return False
    
    def get_user_rank(self, user_id: Union[str, int], leaderboard_type: str = 'global',
                     class_id: str = None) -> Optional[Dict]:
        """Get cached user rank data."""
        cache_key = self._get_user_rank_key(user_id, leaderboard_type, class_id)
        
        try:
            cached_data = cache.get(cache_key)
            if cached_data:
                self.logger.debug(f"Cache hit for user rank: {cache_key}")
                return json.loads(cached_data) if isinstance(cached_data, str) else cached_data
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error retrieving cached user rank {cache_key}: {e}")
            return None
    
    def set_user_rank(self, user_id: Union[str, int], data: Dict, 
                     leaderboard_type: str = 'global', class_id: str = None) -> bool:
        """Cache user rank data."""
        cache_key = self._get_user_rank_key(user_id, leaderboard_type, class_id)
        
        try:
            cache_data = {
                'data': data,
                'cached_at': timezone.now().isoformat(),
                'user_id': str(user_id),
                'leaderboard_type': leaderboard_type,
                'class_id': class_id
            }
            
            success = cache.set(cache_key, cache_data, timeout=self.LEADERBOARD_TIMEOUT)
            
            if success:
                self.logger.debug(f"Cached user rank: {cache_key}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error caching user rank {cache_key}: {e}")
            return False
    
    # ==================== ANALYTICS CACHING ====================
    
    def get_user_analytics(self, user_id: Union[str, int], 
                          data_type: str = "summary") -> Optional[Dict]:
        """Get cached user analytics data."""
        cache_key = self._get_analytics_key(user_id, data_type)
        
        try:
            cached_data = cache.get(cache_key)
            if cached_data:
                self.logger.debug(f"Cache hit for user analytics: {cache_key}")
                return json.loads(cached_data) if isinstance(cached_data, str) else cached_data
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error retrieving cached analytics {cache_key}: {e}")
            return None
    
    def set_user_analytics(self, user_id: Union[str, int], data: Dict,
                          data_type: str = "summary") -> bool:
        """Cache user analytics data."""
        cache_key = self._get_analytics_key(user_id, data_type)
        
        try:
            cache_data = {
                'data': data,
                'cached_at': timezone.now().isoformat(),
                'user_id': str(user_id),
                'data_type': data_type
            }
            
            success = cache.set(cache_key, cache_data, timeout=self.ANALYTICS_TIMEOUT)
            
            if success:
                self.logger.debug(f"Cached user analytics: {cache_key}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error caching analytics {cache_key}: {e}")
            return False
    
    def get_class_analytics(self, class_id: str, data_type: str = "summary") -> Optional[Dict]:
        """Get cached class analytics data."""
        cache_key = self._get_class_analytics_key(class_id, data_type)
        
        try:
            cached_data = cache.get(cache_key)
            if cached_data:
                self.logger.debug(f"Cache hit for class analytics: {cache_key}")
                return json.loads(cached_data) if isinstance(cached_data, str) else cached_data
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error retrieving cached class analytics {cache_key}: {e}")
            return None
    
    def set_class_analytics(self, class_id: str, data: Dict,
                           data_type: str = "summary") -> bool:
        """Cache class analytics data."""
        cache_key = self._get_class_analytics_key(class_id, data_type)
        
        try:
            cache_data = {
                'data': data,
                'cached_at': timezone.now().isoformat(),
                'class_id': class_id,
                'data_type': data_type
            }
            
            success = cache.set(cache_key, cache_data, timeout=self.CLASS_STATS_TIMEOUT)
            
            if success:
                self.logger.debug(f"Cached class analytics: {cache_key}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error caching class analytics {cache_key}: {e}")
            return False
    
    # ==================== ACHIEVEMENTS CACHING ====================
    
    def get_user_achievements(self, user_id: Union[str, int],
                             data_type: str = "earned") -> Optional[Dict]:
        """Get cached user achievements data."""
        cache_key = self._get_achievements_key(user_id, data_type)
        
        try:
            cached_data = cache.get(cache_key)
            if cached_data:
                self.logger.debug(f"Cache hit for user achievements: {cache_key}")
                return json.loads(cached_data) if isinstance(cached_data, str) else cached_data
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error retrieving cached achievements {cache_key}: {e}")
            return None
    
    def set_user_achievements(self, user_id: Union[str, int], data: Dict,
                             data_type: str = "earned") -> bool:
        """Cache user achievements data."""
        cache_key = self._get_achievements_key(user_id, data_type)
        
        try:
            cache_data = {
                'data': data,
                'cached_at': timezone.now().isoformat(),
                'user_id': str(user_id),
                'data_type': data_type
            }
            
            success = cache.set(cache_key, cache_data, timeout=self.ACHIEVEMENTS_TIMEOUT)
            
            if success:
                self.logger.debug(f"Cached user achievements: {cache_key}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error caching achievements {cache_key}: {e}")
            return False
    
    # ==================== CACHE INVALIDATION ====================
    
    def invalidate_user_caches(self, user_id: Union[str, int]) -> bool:
        """
        Invalidate all caches related to a specific user.
        
        Args:
            user_id: User ID to invalidate caches for
            
        Returns:
            bool: True if invalidation was successful
        """
        try:
            patterns_to_delete = [
                f"{self.ANALYTICS_PREFIX}:{user_id}:*",
                f"{self.ACHIEVEMENTS_PREFIX}:{user_id}:*",
                f"{self.LEADERBOARD_PREFIX}:user_rank:{user_id}:*",
                f"{self.USER_STATS_PREFIX}:{user_id}:*"
            ]
            
            deleted_count = 0
            for pattern in patterns_to_delete:
                keys = cache.keys(pattern)
                if keys:
                    cache.delete_many(keys)
                    deleted_count += len(keys)
            
            self.logger.info(f"Invalidated {deleted_count} cache entries for user {user_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error invalidating user caches for {user_id}: {e}")
            return False
    
    def invalidate_leaderboard_caches(self, leaderboard_type: str = None,
                                    class_id: str = None) -> bool:
        """
        Invalidate leaderboard caches.
        
        Args:
            leaderboard_type: Specific type to invalidate, or None for all
            class_id: Specific class to invalidate, or None for all
            
        Returns:
            bool: True if invalidation was successful
        """
        try:
            if leaderboard_type and class_id:
                # Invalidate specific class leaderboard
                pattern = f"{self.LEADERBOARD_PREFIX}:{leaderboard_type}:{class_id}:*"
            elif leaderboard_type:
                # Invalidate specific leaderboard type
                pattern = f"{self.LEADERBOARD_PREFIX}:{leaderboard_type}:*"
            else:
                # Invalidate all leaderboards
                pattern = f"{self.LEADERBOARD_PREFIX}:*"
            
            keys = cache.keys(pattern)
            if keys:
                cache.delete_many(keys)
                self.logger.info(f"Invalidated {len(keys)} leaderboard cache entries")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error invalidating leaderboard caches: {e}")
            return False
    
    def invalidate_class_caches(self, class_id: str) -> bool:
        """
        Invalidate all caches related to a specific class.
        
        Args:
            class_id: Class ID to invalidate caches for
            
        Returns:
            bool: True if invalidation was successful
        """
        try:
            patterns_to_delete = [
                f"{self.CLASS_STATS_PREFIX}:{class_id}:*",
                f"{self.LEADERBOARD_PREFIX}:class:{class_id}:*"
            ]
            
            deleted_count = 0
            for pattern in patterns_to_delete:
                keys = cache.keys(pattern)
                if keys:
                    cache.delete_many(keys)
                    deleted_count += len(keys)
            
            self.logger.info(f"Invalidated {deleted_count} cache entries for class {class_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error invalidating class caches for {class_id}: {e}")
            return False
    
    def invalidate_all_analytics_caches(self) -> bool:
        """Invalidate all analytics-related caches."""
        try:
            patterns_to_delete = [
                f"{self.ANALYTICS_PREFIX}:*",
                f"{self.CLASS_STATS_PREFIX}:*",
                f"{self.USER_STATS_PREFIX}:*"
            ]
            
            deleted_count = 0
            for pattern in patterns_to_delete:
                keys = cache.keys(pattern)
                if keys:
                    cache.delete_many(keys)
                    deleted_count += len(keys)
            
            self.logger.info(f"Invalidated {deleted_count} analytics cache entries")
            return True
            
        except Exception as e:
            self.logger.error(f"Error invalidating analytics caches: {e}")
            return False
    
    # ==================== CACHE WARMING ====================
    
    def warm_leaderboard_cache(self, leaderboard_type: str = 'global',
                              class_id: str = None, pages: int = 5) -> bool:
        """
        Pre-warm leaderboard cache with commonly accessed pages.
        
        Args:
            leaderboard_type: Type of leaderboard to warm
            class_id: Class ID for class leaderboards
            pages: Number of pages to pre-cache
            
        Returns:
            bool: True if warming was successful
        """
        try:
            from .leaderboard_manager import LeaderboardManager
            
            manager = LeaderboardManager()
            
            for page in range(1, pages + 1):
                # Get fresh data
                leaderboard_data = manager.get_leaderboard(
                    leaderboard_type=leaderboard_type,
                    class_id=class_id,
                    limit=20,
                    offset=(page - 1) * 20
                )
                
                # Cache the data
                if leaderboard_data:
                    self.set_leaderboard(
                        data={'entries': leaderboard_data},
                        leaderboard_type=leaderboard_type,
                        class_id=class_id,
                        page=page,
                        page_size=20
                    )
            
            self.logger.info(f"Warmed {pages} pages of {leaderboard_type} leaderboard cache")
            return True
            
        except Exception as e:
            self.logger.error(f"Error warming leaderboard cache: {e}")
            return False
    
    def warm_user_analytics_cache(self, user_ids: List[Union[str, int]]) -> bool:
        """
        Pre-warm analytics cache for specific users.
        
        Args:
            user_ids: List of user IDs to warm cache for
            
        Returns:
            bool: True if warming was successful
        """
        try:
            from .analytics_aggregator import analytics_aggregator
            
            warmed_count = 0
            for user_id in user_ids:
                try:
                    user = User.objects.get(id=user_id)
                    analytics_data = analytics_aggregator.get_student_performance_summary(user)
                    
                    if analytics_data:
                        self.set_user_analytics(user_id, analytics_data)
                        warmed_count += 1
                        
                except User.DoesNotExist:
                    self.logger.warning(f"User {user_id} not found for cache warming")
                    continue
            
            self.logger.info(f"Warmed analytics cache for {warmed_count} users")
            return True
            
        except Exception as e:
            self.logger.error(f"Error warming user analytics cache: {e}")
            return False
    
    # ==================== CACHE STATISTICS ====================
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """
        Get cache usage statistics.
        
        Returns:
            Dict: Cache statistics and health information
        """
        try:
            # Get cache info (this may vary by cache backend)
            cache_info = {}
            
            # Count keys by prefix
            prefixes = [
                self.LEADERBOARD_PREFIX,
                self.ANALYTICS_PREFIX,
                self.ACHIEVEMENTS_PREFIX,
                self.USER_STATS_PREFIX,
                self.CLASS_STATS_PREFIX
            ]
            
            key_counts = {}
            for prefix in prefixes:
                try:
                    keys = cache.keys(f"{prefix}:*")
                    key_counts[prefix] = len(keys) if keys else 0
                except:
                    key_counts[prefix] = 0
            
            return {
                'cache_backend': str(cache.__class__.__name__),
                'key_counts': key_counts,
                'total_keys': sum(key_counts.values()),
                'timestamp': timezone.now().isoformat(),
                'cache_timeouts': {
                    'leaderboard': self.LEADERBOARD_TIMEOUT,
                    'analytics': self.ANALYTICS_TIMEOUT,
                    'user_stats': self.USER_STATS_TIMEOUT,
                    'class_stats': self.CLASS_STATS_TIMEOUT,
                    'achievements': self.ACHIEVEMENTS_TIMEOUT
                }
            }
            
        except Exception as e:
            self.logger.error(f"Error getting cache stats: {e}")
            return {
                'error': str(e),
                'timestamp': timezone.now().isoformat()
            }
    
    def clear_all_caches(self) -> bool:
        """
        Clear all gamification-related caches.
        
        WARNING: This will clear all cached data and may impact performance.
        
        Returns:
            bool: True if clearing was successful
        """
        try:
            patterns_to_delete = [
                f"{self.LEADERBOARD_PREFIX}:*",
                f"{self.ANALYTICS_PREFIX}:*",
                f"{self.ACHIEVEMENTS_PREFIX}:*",
                f"{self.USER_STATS_PREFIX}:*",
                f"{self.CLASS_STATS_PREFIX}:*"
            ]
            
            total_deleted = 0
            for pattern in patterns_to_delete:
                keys = cache.keys(pattern)
                if keys:
                    cache.delete_many(keys)
                    total_deleted += len(keys)
            
            self.logger.warning(f"Cleared {total_deleted} cache entries")
            return True
            
        except Exception as e:
            self.logger.error(f"Error clearing all caches: {e}")
            return False


# Global cache service instance
cache_service = CacheService()


# Utility functions for easy access
def get_cached_leaderboard(leaderboard_type: str = 'global', class_id: str = None,
                          page: int = 1, page_size: int = 20) -> Optional[Dict]:
    """Utility function to get cached leaderboard data."""
    return cache_service.get_leaderboard(leaderboard_type, class_id, page, page_size)


def cache_leaderboard(data: Dict, leaderboard_type: str = 'global',
                     class_id: str = None, page: int = 1, page_size: int = 20) -> bool:
    """Utility function to cache leaderboard data."""
    return cache_service.set_leaderboard(data, leaderboard_type, class_id, page, page_size)


def get_cached_user_analytics(user_id: Union[str, int],
                             data_type: str = "summary") -> Optional[Dict]:
    """Utility function to get cached user analytics."""
    return cache_service.get_user_analytics(user_id, data_type)


def cache_user_analytics(user_id: Union[str, int], data: Dict,
                        data_type: str = "summary") -> bool:
    """Utility function to cache user analytics."""
    return cache_service.set_user_analytics(user_id, data, data_type)


def invalidate_user_caches(user_id: Union[str, int]) -> bool:
    """Utility function to invalidate user-related caches."""
    return cache_service.invalidate_user_caches(user_id)


def invalidate_leaderboard_caches(leaderboard_type: str = None,
                                 class_id: str = None) -> bool:
    """Utility function to invalidate leaderboard caches."""
    return cache_service.invalidate_leaderboard_caches(leaderboard_type, class_id)