"""
Cached Analytics Aggregator with performance optimization.

This module extends the AnalyticsAggregator with comprehensive caching strategies:
- Cache-first analytics retrieval with database fallback
- Intelligent cache invalidation on data changes
- Background cache warming for frequently accessed analytics
- Performance monitoring and optimization
"""

import logging
from typing import Dict, List, Optional, Any, Union
from datetime import datetime, timedelta
from django.db import transaction
from django.utils import timezone
from django.contrib.auth import get_user_model

from .analytics_aggregator import AnalyticsAggregator, analytics_aggregator
from .cache_service import cache_service
from .models import StudentAnalytics, UserPoints

logger = logging.getLogger(__name__)
User = get_user_model()


class CachedAnalyticsAggregator(AnalyticsAggregator):
    """
    Enhanced AnalyticsAggregator with comprehensive caching.
    
    This class provides:
    - Cache-first analytics retrieval with database fallback
    - Automatic cache invalidation on data updates
    - Background cache warming for performance
    - Cache hit rate monitoring and statistics
    """
    
    def __init__(self):
        super().__init__()
        self.cache_service = cache_service
        self.cache_hits = 0
        self.cache_misses = 0
    
    # ==================== CACHED ANALYTICS OPERATIONS ====================
    
    def get_student_performance_summary(self, student) -> Dict[str, Any]:
        """
        Get student performance summary with caching support.
        
        Args:
            student: User object
            
        Returns:
            Dict: Comprehensive performance data
        """
        # Try cache first
        cached_data = self.cache_service.get_user_analytics(
            user_id=student.id,
            data_type="summary"
        )
        
        if cached_data and 'data' in cached_data:
            self.cache_hits += 1
            self.logger.debug(f"Cache hit for student analytics: {student.username}")
            return cached_data['data']
        
        # Cache miss - get from database
        self.cache_misses += 1
        self.logger.debug(f"Cache miss for student analytics: {student.username}")
        
        # Get fresh data from parent class
        analytics_data = super().get_student_performance_summary(student)
        
        # Cache the result
        if analytics_data:
            self.cache_service.set_user_analytics(
                user_id=student.id,
                data=analytics_data,
                data_type="summary"
            )
        
        return analytics_data
    
    def get_class_analytics_summary(self, class_obj) -> Dict[str, Any]:
        """
        Get class analytics summary with caching support.
        
        Args:
            class_obj: Class object
            
        Returns:
            Dict: Class-wide analytics summary
        """
        # Try cache first
        cached_data = self.cache_service.get_class_analytics(
            class_id=str(class_obj.id),
            data_type="summary"
        )
        
        if cached_data and 'data' in cached_data:
            self.cache_hits += 1
            self.logger.debug(f"Cache hit for class analytics: {class_obj.name}")
            return cached_data['data']
        
        # Cache miss - get from database
        self.cache_misses += 1
        self.logger.debug(f"Cache miss for class analytics: {class_obj.name}")
        
        # Get fresh data from parent class
        analytics_data = super().get_class_analytics_summary(class_obj)
        
        # Cache the result
        if analytics_data and 'error' not in analytics_data:
            self.cache_service.set_class_analytics(
                class_id=str(class_obj.id),
                data=analytics_data,
                data_type="summary"
            )
        
        return analytics_data
    
    def get_student_performance_trends(self, student, days: int = 30) -> List[Dict]:
        """
        Get student performance trends with caching support.
        
        Args:
            student: User object
            days: Number of days to analyze
            
        Returns:
            List[Dict]: Performance trend data
        """
        cache_key_suffix = f"trends_{days}d"
        
        # Try cache first
        cached_data = self.cache_service.get_user_analytics(
            user_id=student.id,
            data_type=cache_key_suffix
        )
        
        if cached_data and 'data' in cached_data:
            self.cache_hits += 1
            self.logger.debug(f"Cache hit for student trends: {student.username}")
            return cached_data['data']
        
        # Cache miss - calculate trends
        self.cache_misses += 1
        self.logger.debug(f"Cache miss for student trends: {student.username}")
        
        # Calculate performance trends
        trend_data = self._calculate_performance_trend(student, days)
        
        # Cache the result (shorter timeout for trend data)
        if trend_data:
            self.cache_service.set_user_analytics(
                user_id=student.id,
                data=trend_data,
                data_type=cache_key_suffix
            )
        
        return trend_data
    
    def get_concept_mastery_data(self, student) -> Dict[str, float]:
        """
        Get concept mastery data with caching support.
        
        Args:
            student: User object
            
        Returns:
            Dict: Concept mastery percentages by category
        """
        # Try cache first
        cached_data = self.cache_service.get_user_analytics(
            user_id=student.id,
            data_type="concept_mastery"
        )
        
        if cached_data and 'data' in cached_data:
            self.cache_hits += 1
            return cached_data['data']
        
        # Cache miss - calculate concept mastery
        self.cache_misses += 1
        concept_data = self._calculate_concept_mastery(student)
        
        # Cache the result
        if concept_data:
            self.cache_service.set_user_analytics(
                user_id=student.id,
                data=concept_data,
                data_type="concept_mastery"
            )
        
        return concept_data
    
    # ==================== CACHED UPDATE OPERATIONS ====================
    
    @transaction.atomic
    def update_student_analytics(self, student) -> StudentAnalytics:
        """
        Update student analytics with cache invalidation.
        
        Args:
            student: User object for the student
            
        Returns:
            StudentAnalytics: Updated analytics object
        """
        # Invalidate user caches before update
        self.cache_service.invalidate_user_caches(student.id)
        
        # Update analytics
        analytics = super().update_student_analytics(student)
        
        # Pre-warm cache with fresh data
        self._warm_student_analytics_cache(student)
        
        self.logger.info(f"Updated analytics for {student.username} and invalidated caches")
        return analytics
    
    def update_analytics_on_activity(self, student, activity_type: str = 'practice'):
        """
        Update analytics when a student completes an activity with caching.
        
        Args:
            student: User object
            activity_type: Type of activity ('practice' or 'assignment')
        """
        # Invalidate user caches
        self.cache_service.invalidate_user_caches(student.id)
        
        # Update analytics
        super().update_analytics_on_activity(student, activity_type)
        
        # Invalidate class caches if user belongs to classes
        self._invalidate_user_class_caches(student)
        
        self.logger.info(f"Updated analytics for {student.username} after {activity_type} activity")
    
    # ==================== CACHE WARMING ====================
    
    def _warm_student_analytics_cache(self, student) -> bool:
        """
        Warm analytics cache for a specific student.
        
        Args:
            student: User object
            
        Returns:
            bool: True if warming was successful
        """
        try:
            # Warm summary data
            summary_data = super().get_student_performance_summary(student)
            if summary_data:
                self.cache_service.set_user_analytics(
                    user_id=student.id,
                    data=summary_data,
                    data_type="summary"
                )
            
            # Warm trend data (30 days)
            trend_data = self._calculate_performance_trend(student, 30)
            if trend_data:
                self.cache_service.set_user_analytics(
                    user_id=student.id,
                    data=trend_data,
                    data_type="trends_30d"
                )
            
            # Warm concept mastery data
            concept_data = self._calculate_concept_mastery(student)
            if concept_data:
                self.cache_service.set_user_analytics(
                    user_id=student.id,
                    data=concept_data,
                    data_type="concept_mastery"
                )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error warming analytics cache for {student.username}: {e}")
            return False
    
    def warm_class_analytics_cache(self, class_obj) -> bool:
        """
        Warm analytics cache for a specific class.
        
        Args:
            class_obj: Class object
            
        Returns:
            bool: True if warming was successful
        """
        try:
            # Warm class summary data
            summary_data = super().get_class_analytics_summary(class_obj)
            if summary_data and 'error' not in summary_data:
                self.cache_service.set_class_analytics(
                    class_id=str(class_obj.id),
                    data=summary_data,
                    data_type="summary"
                )
                return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error warming class analytics cache for {class_obj.name}: {e}")
            return False
    
    def batch_warm_student_caches(self, student_ids: List[Union[str, int]]) -> int:
        """
        Batch warm analytics caches for multiple students.
        
        Args:
            student_ids: List of student IDs to warm caches for
            
        Returns:
            int: Number of students successfully cached
        """
        warmed_count = 0
        
        try:
            for student_id in student_ids:
                try:
                    student = User.objects.get(id=student_id, role='student')
                    if self._warm_student_analytics_cache(student):
                        warmed_count += 1
                        
                except User.DoesNotExist:
                    self.logger.warning(f"Student {student_id} not found for cache warming")
                    continue
                except Exception as e:
                    self.logger.error(f"Error warming cache for student {student_id}: {e}")
                    continue
            
            self.logger.info(f"Warmed analytics cache for {warmed_count} students")
            return warmed_count
            
        except Exception as e:
            self.logger.error(f"Error in batch cache warming: {e}")
            return 0
    
    # ==================== CACHE INVALIDATION HELPERS ====================
    
    def _invalidate_user_class_caches(self, student):
        """Invalidate class caches for classes the student belongs to."""
        try:
            from classes.models import Class, Enrollment
            
            user_classes = Class.objects.filter(
                enrollments__user=student,
                enrollments__role='student'
            )
            
            for class_obj in user_classes:
                self.cache_service.invalidate_class_caches(str(class_obj.id))
                
        except ImportError:
            pass
        except Exception as e:
            self.logger.error(f"Error invalidating class caches for {student.username}: {e}")
    
    def invalidate_analytics_for_class(self, class_id: str):
        """
        Invalidate all analytics caches related to a specific class.
        
        Args:
            class_id: Class ID to invalidate caches for
        """
        try:
            # Invalidate class-specific caches
            self.cache_service.invalidate_class_caches(class_id)
            
            # Invalidate student caches for students in this class
            from classes.models import Class, Enrollment
            
            class_obj = Class.objects.get(id=class_id)
            students = [
                enrollment.user for enrollment in 
                Enrollment.objects.filter(class_obj=class_obj, role='student').select_related('user')
            ]
            
            for student in students:
                self.cache_service.invalidate_user_caches(student.id)
            
            self.logger.info(f"Invalidated analytics caches for class {class_id} and {len(students)} students")
            
        except Exception as e:
            self.logger.error(f"Error invalidating analytics for class {class_id}: {e}")
    
    # ==================== PERFORMANCE MONITORING ====================
    
    def get_cache_performance_stats(self) -> Dict[str, Any]:
        """
        Get cache performance statistics for analytics.
        
        Returns:
            Dict: Cache hit rates and performance metrics
        """
        total_requests = self.cache_hits + self.cache_misses
        hit_rate = (self.cache_hits / total_requests * 100) if total_requests > 0 else 0
        
        return {
            'analytics_cache_hits': self.cache_hits,
            'analytics_cache_misses': self.cache_misses,
            'total_analytics_requests': total_requests,
            'analytics_hit_rate_percentage': round(hit_rate, 2),
            'cache_service_stats': self.cache_service.get_cache_stats(),
            'timestamp': timezone.now().isoformat()
        }
    
    def reset_performance_counters(self):
        """Reset cache performance counters."""
        self.cache_hits = 0
        self.cache_misses = 0
        self.logger.info("Reset analytics cache performance counters")
    
    # ==================== BATCH OPERATIONS ====================
    
    def batch_update_analytics(self, student_ids: List[Union[str, int]] = None,
                              class_ids: List[str] = None) -> Dict[str, Any]:
        """
        Batch update analytics for multiple students and classes.
        
        Args:
            student_ids: List of student IDs to update, or None for all active students
            class_ids: List of class IDs to update, or None for all active classes
            
        Returns:
            Dict: Update results and statistics
        """
        results = {
            'students_updated': 0,
            'classes_updated': 0,
            'errors': []
        }
        
        try:
            # Update student analytics
            if student_ids:
                target_students = User.objects.filter(id__in=student_ids, role='student')
            else:
                # Get active students (those with recent activity)
                recent_date = timezone.now() - timedelta(days=30)
                target_students = User.objects.filter(
                    role='student',
                    analytics__last_activity__gte=recent_date
                )[:100]  # Limit to prevent overload
            
            for student in target_students:
                try:
                    self.update_student_analytics(student)
                    results['students_updated'] += 1
                except Exception as e:
                    error_msg = f"Error updating analytics for student {student.username}: {e}"
                    self.logger.error(error_msg)
                    results['errors'].append(error_msg)
            
            # Update class analytics
            if class_ids:
                from classes.models import Class
                target_classes = Class.objects.filter(id__in=class_ids)
            else:
                # Get active classes
                try:
                    from classes.models import Class
                    target_classes = Class.objects.filter(is_active=True)[:20]  # Limit to prevent overload
                except ImportError:
                    target_classes = []
            
            for class_obj in target_classes:
                try:
                    # Invalidate and warm class cache
                    self.cache_service.invalidate_class_caches(str(class_obj.id))
                    self.warm_class_analytics_cache(class_obj)
                    results['classes_updated'] += 1
                except Exception as e:
                    error_msg = f"Error updating analytics for class {class_obj.name}: {e}"
                    self.logger.error(error_msg)
                    results['errors'].append(error_msg)
            
            self.logger.info(f"Batch updated analytics: {results['students_updated']} students, {results['classes_updated']} classes")
            return results
            
        except Exception as e:
            error_msg = f"Error in batch analytics update: {e}"
            self.logger.error(error_msg)
            results['errors'].append(error_msg)
            return results
    
    def preload_popular_analytics(self) -> Dict[str, Any]:
        """
        Preload commonly accessed analytics data into cache.
        
        Returns:
            Dict: Success status for each preload operation
        """
        results = {}
        
        try:
            # Warm top student analytics (by points)
            try:
                top_students = User.objects.filter(
                    role='student',
                    points__isnull=False
                ).order_by('-points__total_points')[:50]
                
                student_ids = [student.id for student in top_students]
                warmed_count = self.batch_warm_student_caches(student_ids)
                results['top_students'] = {
                    'attempted': len(student_ids),
                    'successful': warmed_count
                }
                
            except Exception as e:
                self.logger.error(f"Error warming top student analytics: {e}")
                results['top_students'] = {'error': str(e)}
            
            # Warm active class analytics
            try:
                from classes.models import Class
                active_classes = Class.objects.filter(is_active=True)[:10]
                
                class_results = []
                for class_obj in active_classes:
                    success = self.warm_class_analytics_cache(class_obj)
                    class_results.append({
                        'class_id': str(class_obj.id),
                        'class_name': class_obj.name,
                        'success': success
                    })
                
                results['active_classes'] = class_results
                
            except ImportError:
                results['active_classes'] = {'error': 'Class model not available'}
            
            # Warm recent activity analytics
            try:
                recent_date = timezone.now() - timedelta(days=7)
                recent_students = User.objects.filter(
                    role='student',
                    analytics__last_activity__gte=recent_date
                )[:30]
                
                recent_ids = [student.id for student in recent_students]
                recent_warmed = self.batch_warm_student_caches(recent_ids)
                results['recent_activity'] = {
                    'attempted': len(recent_ids),
                    'successful': recent_warmed
                }
                
            except Exception as e:
                self.logger.error(f"Error warming recent activity analytics: {e}")
                results['recent_activity'] = {'error': str(e)}
            
            self.logger.info(f"Preloaded popular analytics: {results}")
            return results
            
        except Exception as e:
            self.logger.error(f"Error preloading popular analytics: {e}")
            return {'error': str(e)}


# Global cached analytics aggregator instance
cached_analytics_aggregator = CachedAnalyticsAggregator()


# Utility functions for easy access
def get_cached_student_analytics(student) -> Dict[str, Any]:
    """Get student analytics with caching."""
    return cached_analytics_aggregator.get_student_performance_summary(student)


def get_cached_class_analytics(class_obj) -> Dict[str, Any]:
    """Get class analytics with caching."""
    return cached_analytics_aggregator.get_class_analytics_summary(class_obj)


def update_student_analytics_with_cache(student) -> StudentAnalytics:
    """Update student analytics with cache management."""
    return cached_analytics_aggregator.update_student_analytics(student)


def warm_analytics_caches() -> Dict[str, Any]:
    """Warm commonly accessed analytics caches."""
    return cached_analytics_aggregator.preload_popular_analytics()