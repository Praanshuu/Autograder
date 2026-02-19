"""
Analytics aggregation engine for comprehensive student analytics tracking.

This module provides the AnalyticsAggregator class that handles:
- Performance trend calculation over time
- Concept mastery tracking by category
- Streak calculation and maintenance
- Time tracking and activity monitoring
- Score averaging and progress analysis
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from django.db import transaction
from django.db.models import Avg, Count, Sum, Max, Min, Q
from django.utils import timezone
from django.contrib.auth import get_user_model

from .models import (
    StudentAnalytics, PracticeSubmission, PracticeProgress, 
    UserPoints
)

logger = logging.getLogger(__name__)
User = get_user_model()


class AnalyticsAggregator:
    """
    Aggregates and calculates comprehensive student analytics.
    
    This class handles:
    - Performance trend calculation over time periods
    - Concept mastery tracking by question categories
    - Streak calculation (daily, weekly activity)
    - Time tracking and activity monitoring
    - Score averaging and progress analysis
    - Real-time analytics updates
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    @transaction.atomic
    def update_student_analytics(self, student) -> StudentAnalytics:
        """
        Update comprehensive analytics for a specific student.
        
        Args:
            student: User object for the student
            
        Returns:
            StudentAnalytics: Updated analytics object
        """
        analytics, created = StudentAnalytics.objects.get_or_create(
            student=student,
            defaults={
                'total_practice_completed': 0,
                'total_assignments_completed': 0,
                'average_score': 0.0,
                'current_streak': 0,
                'longest_streak': 0,
                'total_time_spent': 0,
                'last_activity': None,
                'performance_trend': [],
                'concept_mastery': {}
            }
        )
        
        # Update basic counts
        analytics.total_practice_completed = self._calculate_practice_completed(student)
        analytics.total_assignments_completed = self._calculate_assignments_completed(student)
        
        # Update scores and performance
        analytics.average_score = self._calculate_average_score(student)
        
        # Update streaks
        current_streak, longest_streak = self._calculate_streaks(student)
        analytics.current_streak = current_streak
        analytics.longest_streak = longest_streak
        
        # Update time tracking
        analytics.total_time_spent = self._calculate_total_time_spent(student)
        analytics.last_activity = self._get_last_activity(student)
        
        # Update performance trends (last 30 days)
        analytics.performance_trend = self._calculate_performance_trend(student, days=30)
        
        # Update concept mastery by category
        analytics.concept_mastery = self._calculate_concept_mastery(student)
        
        analytics.save()
        
        self.logger.info(f"Updated analytics for student {student.username}")
        return analytics
    
    def _calculate_practice_completed(self, student) -> int:
        """Calculate total number of completed practice questions."""
        return PracticeProgress.objects.filter(
            student=student,
            is_completed=True
        ).count()
    
    def _calculate_assignments_completed(self, student) -> int:
        """Calculate total number of completed assignments."""
        # This would need to be implemented based on the assignment submission model
        # For now, we'll use a placeholder that counts successful submissions
        try:
            from submissions.models import SubmissionAttempt
            return SubmissionAttempt.objects.filter(
                student=student,
                status='success'
            ).values('assignment_question').distinct().count()
        except ImportError:
            return 0
    
    def _calculate_average_score(self, student) -> float:
        """Calculate average score across all completed work."""
        # Calculate average from practice questions (completed = 100%)
        practice_scores = PracticeProgress.objects.filter(
            student=student,
            is_completed=True
        ).aggregate(avg_score=Avg('best_score'))['avg_score'] or 0.0
        
        # Calculate average from assignment submissions
        try:
            from submissions.models import SubmissionAttempt
            assignment_scores = SubmissionAttempt.objects.filter(
                student=student,
                status__in=['success', 'fail'],
                manual_score__isnull=False
            ).aggregate(avg_score=Avg('manual_score'))['avg_score'] or 0.0
            
            # Weighted average (practice and assignments)
            practice_count = PracticeProgress.objects.filter(
                student=student, is_completed=True
            ).count()
            assignment_count = SubmissionAttempt.objects.filter(
                student=student, 
                status__in=['success', 'fail'],
                manual_score__isnull=False
            ).count()
            
            if practice_count + assignment_count == 0:
                return 0.0
            
            weighted_avg = (
                (practice_scores * practice_count) + 
                (assignment_scores * assignment_count)
            ) / (practice_count + assignment_count)
            
            return round(weighted_avg, 2)
            
        except ImportError:
            return round(practice_scores, 2)
    
    def _calculate_streaks(self, student) -> Tuple[int, int]:
        """
        Calculate current and longest activity streaks.
        
        Returns:
            Tuple[int, int]: (current_streak, longest_streak) in days
        """
        # Get all activity dates (practice completions and assignment submissions)
        activity_dates = set()
        
        # Practice completion dates
        practice_dates = PracticeProgress.objects.filter(
            student=student,
            is_completed=True,
            completed_at__isnull=False
        ).values_list('completed_at__date', flat=True)
        activity_dates.update(practice_dates)
        
        # Assignment submission dates
        try:
            from submissions.models import SubmissionAttempt
            assignment_dates = SubmissionAttempt.objects.filter(
                student=student,
                status__in=['success', 'fail']
            ).values_list('created_at__date', flat=True)
            activity_dates.update(assignment_dates)
        except ImportError:
            pass
        
        if not activity_dates:
            return 0, 0
        
        # Sort dates
        sorted_dates = sorted(activity_dates)
        
        # Calculate streaks
        current_streak = 0
        longest_streak = 0
        temp_streak = 1
        
        today = timezone.now().date()
        
        # Check if there's activity today or yesterday for current streak
        if today in sorted_dates:
            current_streak = 1
            check_date = today - timedelta(days=1)
        elif (today - timedelta(days=1)) in sorted_dates:
            current_streak = 1
            check_date = today - timedelta(days=2)
        else:
            current_streak = 0
            check_date = None
        
        # Calculate current streak backwards from today/yesterday
        if check_date:
            for i in range(len(sorted_dates) - 1, -1, -1):
                if sorted_dates[i] == check_date:
                    current_streak += 1
                    check_date -= timedelta(days=1)
                elif sorted_dates[i] < check_date:
                    break
        
        # Calculate longest streak
        for i in range(1, len(sorted_dates)):
            if sorted_dates[i] == sorted_dates[i-1] + timedelta(days=1):
                temp_streak += 1
            else:
                longest_streak = max(longest_streak, temp_streak)
                temp_streak = 1
        
        longest_streak = max(longest_streak, temp_streak, current_streak)
        
        return current_streak, longest_streak
    
    def _calculate_total_time_spent(self, student) -> int:
        """Calculate total time spent in minutes across all activities."""
        # Time from practice questions
        practice_time = PracticeProgress.objects.filter(
            student=student
        ).aggregate(total_time=Sum('time_spent'))['total_time'] or 0
        
        # Convert seconds to minutes
        practice_minutes = practice_time // 60
        
        # TODO: Add assignment time tracking when available
        # For now, estimate based on submissions (average 15 minutes per submission)
        try:
            from submissions.models import SubmissionAttempt
            assignment_count = SubmissionAttempt.objects.filter(
                student=student
            ).count()
            estimated_assignment_minutes = assignment_count * 15
        except ImportError:
            estimated_assignment_minutes = 0
        
        return practice_minutes + estimated_assignment_minutes
    
    def _get_last_activity(self, student) -> Optional[datetime]:
        """Get the timestamp of the student's last activity."""
        last_activities = []
        
        # Last practice submission
        last_practice = PracticeSubmission.objects.filter(
            student=student
        ).order_by('-submitted_at').first()
        if last_practice:
            last_activities.append(last_practice.submitted_at)
        
        # Last assignment submission
        try:
            from submissions.models import SubmissionAttempt
            last_assignment = SubmissionAttempt.objects.filter(
                student=student
            ).order_by('-created_at').first()
            if last_assignment:
                last_activities.append(last_assignment.created_at)
        except ImportError:
            pass
        
        return max(last_activities) if last_activities else None
    
    def _calculate_performance_trend(self, student, days: int = 30) -> List[Dict]:
        """
        Calculate performance trend over the specified number of days.
        
        Args:
            student: User object
            days: Number of days to analyze
            
        Returns:
            List[Dict]: Daily performance data
        """
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=days-1)
        
        trend_data = []
        
        for i in range(days):
            current_date = start_date + timedelta(days=i)
            
            # Count activities for this date
            practice_count = PracticeSubmission.objects.filter(
                student=student,
                submitted_at__date=current_date,
                status='success'
            ).count()
            
            assignment_count = 0
            try:
                from submissions.models import SubmissionAttempt
                assignment_count = SubmissionAttempt.objects.filter(
                    student=student,
                    created_at__date=current_date,
                    status='success'
                ).count()
            except ImportError:
                pass
            
            # Calculate average score for the day
            daily_scores = []
            
            # Practice scores (successful = 100%)
            if practice_count > 0:
                daily_scores.extend([100.0] * practice_count)
            
            # Assignment scores
            try:
                from submissions.models import SubmissionAttempt
                assignment_scores = SubmissionAttempt.objects.filter(
                    student=student,
                    created_at__date=current_date,
                    status__in=['success', 'fail'],
                    manual_score__isnull=False
                ).values_list('manual_score', flat=True)
                daily_scores.extend([score for score in assignment_scores if score is not None])
            except ImportError:
                pass
            
            avg_score = sum(daily_scores) / len(daily_scores) if daily_scores else 0.0
            
            trend_data.append({
                'date': current_date.isoformat(),
                'practice_completed': practice_count,
                'assignments_completed': assignment_count,
                'total_activities': practice_count + assignment_count,
                'average_score': round(avg_score, 2),
                'has_activity': (practice_count + assignment_count) > 0
            })
        
        return trend_data
    
    def _calculate_concept_mastery(self, student) -> Dict[str, float]:
        """
        Calculate mastery percentage by concept/category.
        
        Returns:
            Dict[str, float]: Category -> mastery percentage
        """
        concept_mastery = {}
        
        # Get all categories from practice questions the student has attempted
        attempted_categories = PracticeProgress.objects.filter(
            student=student
        ).values_list('question__category', flat=True).distinct()
        
        for category in attempted_categories:
            # Count total questions in this category that the student has attempted
            total_attempted = PracticeProgress.objects.filter(
                student=student,
                question__category=category
            ).count()
            
            # Count completed questions in this category
            completed = PracticeProgress.objects.filter(
                student=student,
                question__category=category,
                is_completed=True
            ).count()
            
            # Calculate mastery percentage
            if total_attempted > 0:
                mastery_percentage = (completed / total_attempted) * 100
                concept_mastery[category] = round(mastery_percentage, 2)
        
        # TODO: Add assignment-based concept mastery when assignment categories are available
        
        return concept_mastery
    
    def get_student_performance_summary(self, student) -> Dict[str, Any]:
        """
        Get a comprehensive performance summary for a student.
        
        Args:
            student: User object
            
        Returns:
            Dict: Comprehensive performance data
        """
        analytics = StudentAnalytics.objects.filter(student=student).first()
        if not analytics:
            analytics = self.update_student_analytics(student)
        
        # Get recent activity (last 7 days)
        recent_activity = self._calculate_performance_trend(student, days=7)
        
        # Get points information
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
        
        # Get rank information
        try:
            from .models import LeaderboardManager
            rank_data = LeaderboardManager.get_user_rank(student, 'global')
            
            # Convert User objects to serializable format
            if rank_data and 'nearby_competitors' in rank_data:
                serializable_competitors = []
                for competitor in rank_data['nearby_competitors']:
                    serializable_competitors.append({
                        'rank': competitor['rank'],
                        'user': {
                            'id': competitor['user'].id,
                            'username': competitor['user'].username,
                            'first_name': competitor['user'].first_name,
                            'last_name': competitor['user'].last_name
                        },
                        'points': competitor['points'],
                        'problems': competitor['problems'],
                        'is_current_user': competitor['is_current_user']
                    })
                rank_data['nearby_competitors'] = serializable_competitors
        except:
            rank_data = None
        
        return {
            'analytics': {
                'total_practice_completed': analytics.total_practice_completed,
                'total_assignments_completed': analytics.total_assignments_completed,
                'average_score': analytics.average_score,
                'current_streak': analytics.current_streak,
                'longest_streak': analytics.longest_streak,
                'total_time_spent': analytics.total_time_spent,
                'last_activity': analytics.last_activity,
                'concept_mastery': analytics.concept_mastery
            },
            'points': points_data,
            'rank': rank_data,
            'recent_activity': recent_activity,
            'performance_trend': analytics.performance_trend
        }
    
    def get_class_analytics_summary(self, class_obj) -> Dict[str, Any]:
        """
        Get aggregated analytics for an entire class.
        
        Args:
            class_obj: Class object
            
        Returns:
            Dict: Class-wide analytics summary
        """
        try:
            from classes.models import Enrollment
            
            # Get all students in the class
            students = [
                enrollment.user for enrollment in 
                Enrollment.objects.filter(class_obj=class_obj, role='student').select_related('user')
            ]
            
            if not students:
                return {
                    'total_students': 0,
                    'class_averages': {},
                    'top_performers': [],
                    'struggling_students': [],
                    'activity_summary': {}
                }
            
            # Calculate class averages
            class_analytics = StudentAnalytics.objects.filter(student__in=students)
            
            averages = class_analytics.aggregate(
                avg_practice_completed=Avg('total_practice_completed'),
                avg_assignments_completed=Avg('total_assignments_completed'),
                avg_score=Avg('average_score'),
                avg_streak=Avg('current_streak'),
                avg_time_spent=Avg('total_time_spent')
            )
            
            # Get top performers (top 5 by average score)
            top_performers = class_analytics.order_by('-average_score')[:5]
            
            # Get struggling students (bottom 20% by average score, with activity in last 7 days)
            recent_date = timezone.now() - timedelta(days=7)
            struggling_threshold = len(students) * 0.2
            struggling_students = class_analytics.filter(
                last_activity__gte=recent_date
            ).order_by('average_score')[:int(struggling_threshold)]
            
            # Activity summary for last 7 days
            activity_summary = self._calculate_class_activity_summary(students, days=7)
            
            return {
                'total_students': len(students),
                'class_averages': {
                    'practice_completed': round(averages['avg_practice_completed'] or 0, 2),
                    'assignments_completed': round(averages['avg_assignments_completed'] or 0, 2),
                    'average_score': round(averages['avg_score'] or 0, 2),
                    'current_streak': round(averages['avg_streak'] or 0, 2),
                    'time_spent': round(averages['avg_time_spent'] or 0, 2)
                },
                'top_performers': [
                    {
                        'student': {
                            'id': analytics.student.id,
                            'username': analytics.student.username,
                            'first_name': analytics.student.first_name,
                            'last_name': analytics.student.last_name
                        },
                        'average_score': analytics.average_score,
                        'total_completed': analytics.total_practice_completed + analytics.total_assignments_completed
                    }
                    for analytics in top_performers
                ],
                'struggling_students': [
                    {
                        'student': {
                            'id': analytics.student.id,
                            'username': analytics.student.username,
                            'first_name': analytics.student.first_name,
                            'last_name': analytics.student.last_name
                        },
                        'average_score': analytics.average_score,
                        'last_activity': analytics.last_activity
                    }
                    for analytics in struggling_students
                ],
                'activity_summary': activity_summary
            }
            
        except ImportError:
            return {'error': 'Class model not available'}
    
    def _calculate_class_activity_summary(self, students: List, days: int = 7) -> Dict[str, Any]:
        """Calculate activity summary for a group of students."""
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=days-1)
        
        total_practice = PracticeSubmission.objects.filter(
            student__in=students,
            submitted_at__date__gte=start_date,
            status='success'
        ).count()
        
        total_assignments = 0
        try:
            from submissions.models import SubmissionAttempt
            total_assignments = SubmissionAttempt.objects.filter(
                student__in=students,
                created_at__date__gte=start_date,
                status='success'
            ).count()
        except ImportError:
            pass
        
        # Get active students from practice submissions
        practice_active = set(PracticeSubmission.objects.filter(
            student__in=students,
            submitted_at__date__gte=start_date
        ).values_list('student_id', flat=True))
        
        # Get active students from assignment submissions
        assignment_active = set()
        try:
            from submissions.models import SubmissionAttempt
            assignment_active = set(SubmissionAttempt.objects.filter(
                student__in=students,
                created_at__date__gte=start_date
            ).values_list('student_id', flat=True))
        except ImportError:
            pass
        
        active_students = len(practice_active | assignment_active)
        
        return {
            'total_practice_completed': total_practice,
            'total_assignments_completed': total_assignments,
            'active_students': active_students,
            'activity_rate': round((active_students / len(students)) * 100, 2) if students else 0
        }
    
    def update_analytics_on_activity(self, student, activity_type: str = 'practice'):
        """
        Update analytics when a student completes an activity.
        
        Args:
            student: User object
            activity_type: Type of activity ('practice' or 'assignment')
        """
        try:
            # Update analytics in the background
            self.update_student_analytics(student)
            
            # Broadcast real-time analytics update if needed
            from .realtime_service import realtime_service
            analytics_data = self.get_student_performance_summary(student)
            
            # This could be extended to broadcast analytics updates
            # realtime_service.broadcast_analytics_update(student, analytics_data)
            
            self.logger.info(f"Updated analytics for {student.username} after {activity_type} activity")
            
        except Exception as e:
            self.logger.error(f"Error updating analytics for {student.username}: {e}")


# Global instance
analytics_aggregator = AnalyticsAggregator()