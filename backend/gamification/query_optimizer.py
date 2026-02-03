"""
Database query optimization utilities for gamification features.

This module provides:
- Optimized query builders for common analytics operations
- Database index recommendations and management
- Query performance monitoring and analysis
- Bulk operation utilities for better performance
"""

import logging
from typing import Dict, List, Optional, Any, Union, Tuple
from datetime import datetime, timedelta
from django.db import models, connection
from django.db.models import Q, F, Count, Sum, Avg, Max, Min, Prefetch
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

from .models import (
    PracticeQuestion, PracticeSubmission, PracticeProgress,
    UserPoints, Achievement, UserAchievement, StudentAnalytics,
    LeaderboardEntry
)

logger = logging.getLogger(__name__)
User = get_user_model()


class QueryOptimizer:
    """
    Database query optimization utilities for gamification features.
    
    Provides optimized queries for:
    - Leaderboard calculations with minimal database hits
    - Analytics aggregation with efficient joins
    - Bulk operations for data updates
    - Performance monitoring and index analysis
    """
    
    def __init__(self):
        self.logger = logger
        self.query_count = 0
        self.query_time = 0.0
    
    # ==================== OPTIMIZED LEADERBOARD QUERIES ====================
    
    def get_optimized_global_leaderboard(self, limit: int = 50, offset: int = 0) -> List[Dict]:
        """
        Get global leaderboard with optimized single query.
        
        Args:
            limit: Maximum number of entries to return
            offset: Number of entries to skip
            
        Returns:
            List[Dict]: Optimized leaderboard data
        """
        try:
            # Single query with all necessary joins and annotations
            queryset = User.objects.filter(
                role='student',
                points__isnull=False
            ).select_related(
                'points'
            ).prefetch_related(
                Prefetch(
                    'practice_progress',
                    queryset=PracticeProgress.objects.filter(is_completed=True),
                    to_attr='completed_practice'
                )
            ).annotate(
                total_points=F('points__total_points'),
                practice_points=F('points__practice_points'),
                assignment_points=F('points__assignment_points'),
                completed_problems=Count(
                    'practice_progress',
                    filter=Q(practice_progress__is_completed=True)
                ),
                last_activity=Max('analytics__last_activity')
            ).order_by(
                '-total_points',
                '-completed_problems',
                '-last_activity',
                'username'
            )[offset:offset + limit]
            
            # Convert to leaderboard format
            leaderboard_data = []
            for rank, user in enumerate(queryset, start=offset + 1):
                leaderboard_data.append({
                    'rank': rank,
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    },
                    'total_points': user.total_points,
                    'practice_points': user.practice_points,
                    'assignment_points': user.assignment_points,
                    'completed_problems': user.completed_problems,
                    'last_activity': user.last_activity
                })
            
            self.logger.debug(f"Optimized global leaderboard query returned {len(leaderboard_data)} entries")
            return leaderboard_data
            
        except Exception as e:
            self.logger.error(f"Error in optimized global leaderboard query: {e}")
            return []
    
    def get_optimized_class_leaderboard(self, class_id: str, limit: int = 50, 
                                      offset: int = 0) -> List[Dict]:
        """
        Get class leaderboard with optimized single query.
        
        Args:
            class_id: UUID of the class
            limit: Maximum number of entries to return
            offset: Number of entries to skip
            
        Returns:
            List[Dict]: Optimized class leaderboard data
        """
        try:
            from classes.models import Class, Enrollment
            
            # Single query with all necessary joins
            queryset = User.objects.filter(
                enrollments__class_obj_id=class_id,
                enrollments__role='student',
                points__isnull=False
            ).select_related(
                'points'
            ).prefetch_related(
                Prefetch(
                    'practice_progress',
                    queryset=PracticeProgress.objects.filter(is_completed=True),
                    to_attr='completed_practice'
                )
            ).annotate(
                total_points=F('points__total_points'),
                practice_points=F('points__practice_points'),
                assignment_points=F('points__assignment_points'),
                completed_problems=Count(
                    'practice_progress',
                    filter=Q(practice_progress__is_completed=True)
                ),
                last_activity=Max('analytics__last_activity')
            ).order_by(
                '-total_points',
                '-completed_problems',
                '-last_activity',
                'username'
            )[offset:offset + limit]
            
            # Convert to leaderboard format
            leaderboard_data = []
            for rank, user in enumerate(queryset, start=offset + 1):
                leaderboard_data.append({
                    'rank': rank,
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    },
                    'total_points': user.total_points,
                    'practice_points': user.practice_points,
                    'assignment_points': user.assignment_points,
                    'completed_problems': user.completed_problems,
                    'last_activity': user.last_activity,
                    'class_id': class_id
                })
            
            self.logger.debug(f"Optimized class leaderboard query returned {len(leaderboard_data)} entries")
            return leaderboard_data
            
        except Exception as e:
            self.logger.error(f"Error in optimized class leaderboard query: {e}")
            return []
    
    def get_user_rank_optimized(self, user, leaderboard_type: str = 'global',
                               class_id: str = None) -> Optional[int]:
        """
        Get user rank with optimized query.
        
        Args:
            user: User instance
            leaderboard_type: 'global' or 'class'
            class_id: Required for class leaderboards
            
        Returns:
            Optional[int]: User's rank or None if not found
        """
        try:
            user_points = getattr(user, 'points', None)
            if not user_points:
                return None
            
            # Count users with better performance
            if leaderboard_type == 'global':
                better_users_query = User.objects.filter(
                    role='student',
                    points__isnull=False
                )
            else:
                better_users_query = User.objects.filter(
                    enrollments__class_obj_id=class_id,
                    enrollments__role='student',
                    points__isnull=False
                )
            
            # Annotate with completed problems for tie-breaking
            better_users_query = better_users_query.annotate(
                completed_problems=Count(
                    'practice_progress',
                    filter=Q(practice_progress__is_completed=True)
                )
            )
            
            # Count users with better stats
            user_completed = PracticeProgress.objects.filter(
                student=user,
                is_completed=True
            ).count()
            
            better_count = better_users_query.filter(
                Q(points__total_points__gt=user_points.total_points) |
                Q(
                    points__total_points=user_points.total_points,
                    completed_problems__gt=user_completed
                ) |
                Q(
                    points__total_points=user_points.total_points,
                    completed_problems=user_completed,
                    analytics__last_activity__gt=F('analytics__last_activity')
                ) |
                Q(
                    points__total_points=user_points.total_points,
                    completed_problems=user_completed,
                    analytics__last_activity=F('analytics__last_activity'),
                    username__lt=user.username
                )
            ).count()
            
            return better_count + 1
            
        except Exception as e:
            self.logger.error(f"Error in optimized user rank query: {e}")
            return None
    
    # ==================== OPTIMIZED ANALYTICS QUERIES ====================
    
    def get_optimized_student_analytics(self, student) -> Dict[str, Any]:
        """
        Get comprehensive student analytics with optimized queries.
        
        Args:
            student: User object
            
        Returns:
            Dict: Optimized analytics data
        """
        try:
            # Single query for practice statistics
            practice_stats = PracticeProgress.objects.filter(
                student=student
            ).aggregate(
                total_completed=Count('id', filter=Q(is_completed=True)),
                total_attempted=Count('id'),
                avg_score=Avg('best_score'),
                total_time=Sum('time_spent'),
                last_practice=Max('completed_at')
            )
            
            # Single query for submission statistics
            submission_stats = PracticeSubmission.objects.filter(
                student=student
            ).aggregate(
                total_submissions=Count('id'),
                successful_submissions=Count('id', filter=Q(status='success')),
                total_points_earned=Sum('points_earned'),
                last_submission=Max('submitted_at')
            )
            
            # Get user points
            try:
                user_points = UserPoints.objects.get(user=student)
                points_data = {
                    'total_points': user_points.total_points,
                    'practice_points': user_points.practice_points,
                    'assignment_points': user_points.assignment_points
                }
            except UserPoints.DoesNotExist:
                points_data = {
                    'total_points': 0,
                    'practice_points': 0,
                    'assignment_points': 0
                }
            
            # Calculate derived metrics
            success_rate = 0.0
            if submission_stats['total_submissions'] and submission_stats['total_submissions'] > 0:
                success_rate = (submission_stats['successful_submissions'] / 
                              submission_stats['total_submissions']) * 100
            
            completion_rate = 0.0
            if practice_stats['total_attempted'] and practice_stats['total_attempted'] > 0:
                completion_rate = (practice_stats['total_completed'] / 
                                 practice_stats['total_attempted']) * 100
            
            # Determine last activity
            last_activities = [
                practice_stats['last_practice'],
                submission_stats['last_submission']
            ]
            last_activity = max([dt for dt in last_activities if dt is not None], default=None)
            
            return {
                'practice_stats': {
                    'total_completed': practice_stats['total_completed'] or 0,
                    'total_attempted': practice_stats['total_attempted'] or 0,
                    'completion_rate': round(completion_rate, 2),
                    'average_score': round(practice_stats['avg_score'] or 0, 2),
                    'total_time_minutes': (practice_stats['total_time'] or 0) // 60
                },
                'submission_stats': {
                    'total_submissions': submission_stats['total_submissions'] or 0,
                    'successful_submissions': submission_stats['successful_submissions'] or 0,
                    'success_rate': round(success_rate, 2),
                    'points_earned': submission_stats['total_points_earned'] or 0
                },
                'points': points_data,
                'last_activity': last_activity,
                'calculated_at': timezone.now()
            }
            
        except Exception as e:
            self.logger.error(f"Error in optimized student analytics query: {e}")
            return {}
    
    def get_optimized_class_analytics(self, class_id: str) -> Dict[str, Any]:
        """
        Get class analytics with optimized queries.
        
        Args:
            class_id: UUID of the class
            
        Returns:
            Dict: Optimized class analytics data
        """
        try:
            from classes.models import Class, Enrollment
            
            # Get class students in single query
            class_students = User.objects.filter(
                enrollments__class_obj_id=class_id,
                enrollments__role='student'
            ).select_related('points', 'analytics').prefetch_related(
                Prefetch(
                    'practice_progress',
                    queryset=PracticeProgress.objects.filter(is_completed=True),
                    to_attr='completed_practice'
                )
            )
            
            if not class_students.exists():
                return {
                    'total_students': 0,
                    'class_averages': {},
                    'activity_summary': {},
                    'top_performers': [],
                    'struggling_students': []
                }
            
            # Calculate aggregated statistics
            total_students = class_students.count()
            
            # Aggregate class statistics
            class_stats = class_students.aggregate(
                avg_total_points=Avg('points__total_points'),
                avg_practice_points=Avg('points__practice_points'),
                avg_assignment_points=Avg('points__assignment_points'),
                total_class_points=Sum('points__total_points'),
                max_points=Max('points__total_points')
            )
            
            # Get practice completion statistics
            practice_stats = PracticeProgress.objects.filter(
                student__in=class_students
            ).aggregate(
                total_completed=Count('id', filter=Q(is_completed=True)),
                total_attempted=Count('id'),
                avg_completion_rate=Avg('best_score')
            )
            
            # Calculate completion rate
            completion_rate = 0.0
            if practice_stats['total_attempted'] and practice_stats['total_attempted'] > 0:
                completion_rate = (practice_stats['total_completed'] / 
                                 practice_stats['total_attempted']) * 100
            
            # Get top performers (top 5 by points)
            top_performers = class_students.order_by('-points__total_points')[:5]
            top_performers_data = [
                {
                    'student': {
                        'id': student.id,
                        'username': student.username,
                        'first_name': student.first_name,
                        'last_name': student.last_name
                    },
                    'total_points': student.points.total_points if student.points else 0,
                    'completed_problems': len(getattr(student, 'completed_practice', []))
                }
                for student in top_performers
            ]
            
            # Get struggling students (bottom 20% with recent activity)
            recent_date = timezone.now() - timedelta(days=7)
            struggling_threshold = max(1, int(total_students * 0.2))
            struggling_students = class_students.filter(
                analytics__last_activity__gte=recent_date
            ).order_by('points__total_points')[:struggling_threshold]
            
            struggling_data = [
                {
                    'student': {
                        'id': student.id,
                        'username': student.username,
                        'first_name': student.first_name,
                        'last_name': student.last_name
                    },
                    'total_points': student.points.total_points if student.points else 0,
                    'last_activity': student.analytics.last_activity if student.analytics else None
                }
                for student in struggling_students
            ]
            
            # Activity summary
            recent_submissions = PracticeSubmission.objects.filter(
                student__in=class_students,
                submitted_at__gte=recent_date
            ).count()
            
            active_students = class_students.filter(
                analytics__last_activity__gte=recent_date
            ).count()
            
            return {
                'total_students': total_students,
                'class_averages': {
                    'total_points': round(class_stats['avg_total_points'] or 0, 2),
                    'practice_points': round(class_stats['avg_practice_points'] or 0, 2),
                    'assignment_points': round(class_stats['avg_assignment_points'] or 0, 2),
                    'completion_rate': round(completion_rate, 2)
                },
                'class_totals': {
                    'total_points': class_stats['total_class_points'] or 0,
                    'max_points': class_stats['max_points'] or 0,
                    'problems_completed': practice_stats['total_completed'] or 0,
                    'problems_attempted': practice_stats['total_attempted'] or 0
                },
                'activity_summary': {
                    'recent_submissions': recent_submissions,
                    'active_students': active_students,
                    'activity_rate': round((active_students / total_students) * 100, 2) if total_students > 0 else 0
                },
                'top_performers': top_performers_data,
                'struggling_students': struggling_data,
                'calculated_at': timezone.now()
            }
            
        except Exception as e:
            self.logger.error(f"Error in optimized class analytics query: {e}")
            return {'error': str(e)}
    
    # ==================== BULK OPERATIONS ====================
    
    def bulk_update_user_points(self, point_updates: List[Dict]) -> int:
        """
        Bulk update user points efficiently.
        
        Args:
            point_updates: List of dicts with 'user_id', 'practice_points', 'assignment_points'
            
        Returns:
            int: Number of records updated
        """
        try:
            updated_count = 0
            
            # Group updates by user for efficiency
            user_updates = {}
            for update in point_updates:
                user_id = update['user_id']
                if user_id not in user_updates:
                    user_updates[user_id] = {
                        'practice_points': 0,
                        'assignment_points': 0
                    }
                
                user_updates[user_id]['practice_points'] += update.get('practice_points', 0)
                user_updates[user_id]['assignment_points'] += update.get('assignment_points', 0)
            
            # Bulk update using database-level operations
            for user_id, points in user_updates.items():
                total_points = points['practice_points'] + points['assignment_points']
                
                updated = UserPoints.objects.filter(user_id=user_id).update(
                    practice_points=F('practice_points') + points['practice_points'],
                    assignment_points=F('assignment_points') + points['assignment_points'],
                    total_points=F('total_points') + total_points,
                    last_updated=timezone.now()
                )
                
                if updated:
                    updated_count += 1
                else:
                    # Create new record if doesn't exist
                    UserPoints.objects.create(
                        user_id=user_id,
                        practice_points=points['practice_points'],
                        assignment_points=points['assignment_points'],
                        total_points=total_points
                    )
                    updated_count += 1
            
            self.logger.info(f"Bulk updated points for {updated_count} users")
            return updated_count
            
        except Exception as e:
            self.logger.error(f"Error in bulk points update: {e}")
            return 0
    
    def bulk_update_leaderboard_entries(self, leaderboard_data: List[Dict],
                                       leaderboard_type: str = 'global',
                                       class_id: str = None) -> int:
        """
        Bulk update leaderboard entries efficiently.
        
        Args:
            leaderboard_data: List of leaderboard entry data
            leaderboard_type: 'global' or 'class'
            class_id: Required for class leaderboards
            
        Returns:
            int: Number of entries updated
        """
        try:
            # Clear existing entries
            LeaderboardEntry.objects.filter(
                leaderboard_type=leaderboard_type,
                class_id=class_id
            ).delete()
            
            # Prepare bulk create data
            entries_to_create = []
            for entry_data in leaderboard_data:
                entries_to_create.append(
                    LeaderboardEntry(
                        user_id=entry_data['user']['id'],
                        rank=entry_data['rank'],
                        total_points=entry_data['total_points'],
                        completed_problems=entry_data['completed_problems'],
                        leaderboard_type=leaderboard_type,
                        class_id=class_id
                    )
                )
            
            # Bulk create
            created_entries = LeaderboardEntry.objects.bulk_create(
                entries_to_create,
                batch_size=100
            )
            
            self.logger.info(f"Bulk created {len(created_entries)} leaderboard entries")
            return len(created_entries)
            
        except Exception as e:
            self.logger.error(f"Error in bulk leaderboard update: {e}")
            return 0
    
    # ==================== PERFORMANCE MONITORING ====================
    
    def analyze_query_performance(self) -> Dict[str, Any]:
        """
        Analyze database query performance.
        
        Returns:
            Dict: Query performance statistics
        """
        try:
            # Get database connection statistics
            with connection.cursor() as cursor:
                # Check for slow queries (PostgreSQL specific)
                if 'postgresql' in connection.vendor:
                    cursor.execute("""
                        SELECT query, calls, total_time, mean_time
                        FROM pg_stat_statements
                        WHERE query LIKE '%gamification%'
                        ORDER BY mean_time DESC
                        LIMIT 10;
                    """)
                    slow_queries = cursor.fetchall()
                else:
                    slow_queries = []
                
                # Get table sizes
                cursor.execute("""
                    SELECT 
                        schemaname,
                        tablename,
                        attname,
                        n_distinct,
                        correlation
                    FROM pg_stats
                    WHERE tablename IN (
                        'user_points', 'leaderboard_entries', 'student_analytics',
                        'practice_submissions', 'practice_progress'
                    )
                    ORDER BY tablename, attname;
                """)
                table_stats = cursor.fetchall()
            
            return {
                'slow_queries': slow_queries,
                'table_statistics': table_stats,
                'connection_info': {
                    'vendor': connection.vendor,
                    'queries_count': len(connection.queries) if hasattr(connection, 'queries') else 0
                },
                'timestamp': timezone.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Error analyzing query performance: {e}")
            return {'error': str(e)}
    
    def get_index_recommendations(self) -> List[Dict[str, str]]:
        """
        Get database index recommendations for better performance.
        
        Returns:
            List[Dict]: Index recommendations
        """
        recommendations = [
            {
                'table': 'user_points',
                'columns': ['total_points', 'last_updated'],
                'type': 'composite',
                'reason': 'Optimize leaderboard queries with time-based filtering'
            },
            {
                'table': 'practice_submissions',
                'columns': ['student_id', 'submitted_at', 'status'],
                'type': 'composite',
                'reason': 'Optimize student activity queries'
            },
            {
                'table': 'practice_progress',
                'columns': ['student_id', 'is_completed', 'completed_at'],
                'type': 'composite',
                'reason': 'Optimize completion tracking queries'
            },
            {
                'table': 'leaderboard_entries',
                'columns': ['leaderboard_type', 'class_id', 'rank'],
                'type': 'composite',
                'reason': 'Optimize leaderboard retrieval queries'
            },
            {
                'table': 'student_analytics',
                'columns': ['last_activity', 'updated_at'],
                'type': 'composite',
                'reason': 'Optimize analytics freshness queries'
            }
        ]
        
        return recommendations
    
    def create_recommended_indexes(self) -> Dict[str, bool]:
        """
        Create recommended database indexes.
        
        Returns:
            Dict: Success status for each index creation
        """
        results = {}
        
        try:
            with connection.cursor() as cursor:
                # Create composite indexes
                index_queries = [
                    """
                    CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_user_points_leaderboard
                    ON user_points (total_points DESC, last_updated DESC);
                    """,
                    """
                    CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_practice_submissions_activity
                    ON practice_submissions (student_id, submitted_at DESC, status);
                    """,
                    """
                    CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_practice_progress_completion
                    ON practice_progress (student_id, is_completed, completed_at DESC);
                    """,
                    """
                    CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_leaderboard_entries_lookup
                    ON leaderboard_entries (leaderboard_type, class_id, rank);
                    """,
                    """
                    CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_student_analytics_freshness
                    ON student_analytics (last_activity DESC, updated_at DESC);
                    """
                ]
                
                for i, query in enumerate(index_queries):
                    try:
                        cursor.execute(query)
                        results[f'index_{i+1}'] = True
                        self.logger.info(f"Created index {i+1}")
                    except Exception as e:
                        results[f'index_{i+1}'] = False
                        self.logger.error(f"Failed to create index {i+1}: {e}")
            
            return results
            
        except Exception as e:
            self.logger.error(f"Error creating indexes: {e}")
            return {'error': str(e)}


# Global query optimizer instance
query_optimizer = QueryOptimizer()


# Utility functions for easy access
def get_optimized_leaderboard(leaderboard_type: str = 'global', class_id: str = None,
                             limit: int = 50, offset: int = 0) -> List[Dict]:
    """Get optimized leaderboard data."""
    if leaderboard_type == 'global':
        return query_optimizer.get_optimized_global_leaderboard(limit, offset)
    else:
        return query_optimizer.get_optimized_class_leaderboard(class_id, limit, offset)


def get_optimized_student_analytics(student) -> Dict[str, Any]:
    """Get optimized student analytics."""
    return query_optimizer.get_optimized_student_analytics(student)


def get_optimized_class_analytics(class_id: str) -> Dict[str, Any]:
    """Get optimized class analytics."""
    return query_optimizer.get_optimized_class_analytics(class_id)


def bulk_update_points(point_updates: List[Dict]) -> int:
    """Bulk update user points."""
    return query_optimizer.bulk_update_user_points(point_updates)


def create_performance_indexes() -> Dict[str, bool]:
    """Create recommended performance indexes."""
    return query_optimizer.create_recommended_indexes()