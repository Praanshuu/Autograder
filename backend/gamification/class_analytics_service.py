"""
Enhanced class analytics and reporting service.

This module provides comprehensive class analytics functionality including:
- Advanced class-wide performance aggregation
- Sophisticated struggling student identification
- Detailed problem-specific analytics
- Exportable report generation
- Engagement metrics and insights
"""

import logging
import csv
import io
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from django.db import transaction
from django.db.models import Avg, Count, Sum, Max, Min, Q, F
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.http import HttpResponse

from .models import (
    StudentAnalytics, PracticeSubmission, PracticeProgress, 
    PracticeQuestion, UserPoints
)
from .analytics_aggregator import analytics_aggregator

logger = logging.getLogger(__name__)
User = get_user_model()


class ClassAnalyticsService:
    """
    Enhanced service for comprehensive class analytics and reporting.
    
    This service provides:
    - Advanced class performance aggregation
    - Struggling student identification with multiple criteria
    - Problem-specific failure pattern analysis
    - Engagement metrics and time-based analytics
    - Exportable reports in multiple formats
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def get_comprehensive_class_analytics(self, class_obj) -> Dict[str, Any]:
        """
        Get comprehensive class analytics with advanced metrics.
        
        Args:
            class_obj: Class object
            
        Returns:
            Dict: Comprehensive class analytics data
        """
        try:
            from classes.models import Enrollment
            
            # Get all students in the class
            students = [
                enrollment.user for enrollment in 
                Enrollment.objects.filter(class_obj=class_obj, role='student').select_related('user')
            ]
            
            if not students:
                return self._empty_class_analytics()
            
            # Get comprehensive analytics
            class_performance = self._calculate_class_performance_metrics(students)
            struggling_students = self._identify_struggling_students(students)
            engagement_metrics = self._calculate_engagement_metrics(students)
            problem_analytics = self._analyze_problem_performance(students)
            time_analytics = self._calculate_time_analytics(students)
            progress_distribution = self._calculate_progress_distribution(students)
            
            return {
                'class_info': {
                    'total_students': len(students),
                    'active_students': len([s for s in students if self._is_student_active(s)]),
                    'class_name': class_obj.name if hasattr(class_obj, 'name') else 'Unknown Class',
                    'analysis_date': timezone.now().isoformat()
                },
                'performance_metrics': class_performance,
                'struggling_students': struggling_students,
                'engagement_metrics': engagement_metrics,
                'problem_analytics': problem_analytics,
                'time_analytics': time_analytics,
                'progress_distribution': progress_distribution
            }
            
        except ImportError:
            return {'error': 'Class model not available'}
        except Exception as e:
            self.logger.error(f"Error getting comprehensive class analytics: {e}")
            return {'error': 'Failed to generate class analytics'}
    
    def _empty_class_analytics(self) -> Dict[str, Any]:
        """Return empty analytics structure for classes with no students."""
        return {
            'class_info': {
                'total_students': 0,
                'active_students': 0,
                'class_name': 'Empty Class',
                'analysis_date': timezone.now().isoformat()
            },
            'performance_metrics': {},
            'struggling_students': [],
            'engagement_metrics': {},
            'problem_analytics': {},
            'time_analytics': {},
            'progress_distribution': {}
        }
    
    def _calculate_class_performance_metrics(self, students: List) -> Dict[str, Any]:
        """Calculate comprehensive class performance metrics."""
        class_analytics = StudentAnalytics.objects.filter(student__in=students)
        
        if not class_analytics.exists():
            return {}
        
        # Basic averages
        averages = class_analytics.aggregate(
            avg_practice_completed=Avg('total_practice_completed'),
            avg_assignments_completed=Avg('total_assignments_completed'),
            avg_score=Avg('average_score'),
            avg_streak=Avg('current_streak'),
            avg_time_spent=Avg('total_time_spent')
        )
        
        # Performance distribution
        score_ranges = {
            'excellent': class_analytics.filter(average_score__gte=90).count(),
            'good': class_analytics.filter(average_score__gte=70, average_score__lt=90).count(),
            'fair': class_analytics.filter(average_score__gte=50, average_score__lt=70).count(),
            'poor': class_analytics.filter(average_score__lt=50).count()
        }
        
        # Completion rates
        total_students = len(students)
        completion_stats = {
            'high_completers': class_analytics.filter(total_practice_completed__gte=10).count(),
            'medium_completers': class_analytics.filter(
                total_practice_completed__gte=5, 
                total_practice_completed__lt=10
            ).count(),
            'low_completers': class_analytics.filter(total_practice_completed__lt=5).count()
        }
        
        # Top performers (top 10% or minimum 3)
        top_count = max(3, int(total_students * 0.1))
        top_performers = class_analytics.order_by('-average_score')[:top_count]
        
        return {
            'averages': {
                'practice_completed': round(averages['avg_practice_completed'] or 0, 2),
                'assignments_completed': round(averages['avg_assignments_completed'] or 0, 2),
                'average_score': round(averages['avg_score'] or 0, 2),
                'current_streak': round(averages['avg_streak'] or 0, 2),
                'time_spent_minutes': round(averages['avg_time_spent'] or 0, 2)
            },
            'score_distribution': score_ranges,
            'completion_distribution': completion_stats,
            'top_performers': [
                {
                    'student': {
                        'id': analytics.student.id,
                        'username': analytics.student.username,
                        'first_name': analytics.student.first_name,
                        'last_name': analytics.student.last_name
                    },
                    'average_score': analytics.average_score,
                    'total_completed': analytics.total_practice_completed + analytics.total_assignments_completed,
                    'current_streak': analytics.current_streak
                }
                for analytics in top_performers
            ]
        }
    
    def _identify_struggling_students(self, students: List) -> List[Dict[str, Any]]:
        """
        Identify struggling students using multiple criteria.
        
        Criteria for struggling students:
        1. Low average score (< 50%)
        2. Low completion rate (< 3 problems completed)
        3. No recent activity (> 7 days)
        4. Declining performance trend
        """
        struggling_students = []
        recent_date = timezone.now() - timedelta(days=7)
        
        for student in students:
            analytics = StudentAnalytics.objects.filter(student=student).first()
            if not analytics:
                # Student with no analytics is definitely struggling
                struggling_students.append({
                    'student': {
                        'id': student.id,
                        'username': student.username,
                        'first_name': student.first_name,
                        'last_name': student.last_name
                    },
                    'struggle_indicators': ['no_activity'],
                    'average_score': 0,
                    'total_completed': 0,
                    'last_activity': None,
                    'recommendations': ['Start with basic practice questions', 'Schedule one-on-one session']
                })
                continue
            
            struggle_indicators = []
            recommendations = []
            
            # Check low average score
            if analytics.average_score < 50:
                struggle_indicators.append('low_score')
                recommendations.append('Review fundamental concepts')
            
            # Check low completion rate
            total_completed = analytics.total_practice_completed + analytics.total_assignments_completed
            if total_completed < 3:
                struggle_indicators.append('low_completion')
                recommendations.append('Encourage more practice')
            
            # Check recent activity
            if not analytics.last_activity or analytics.last_activity < recent_date:
                struggle_indicators.append('inactive')
                recommendations.append('Check in with student')
            
            # Check declining trend (if performance trend data exists)
            if analytics.performance_trend:
                recent_scores = [day['average_score'] for day in analytics.performance_trend[-7:] if day['has_activity']]
                if len(recent_scores) >= 2:
                    trend = sum(recent_scores[-2:]) / 2 - sum(recent_scores[:2]) / 2 if len(recent_scores) >= 4 else 0
                    if trend < -10:  # Declining by more than 10 points
                        struggle_indicators.append('declining_performance')
                        recommendations.append('Identify specific problem areas')
            
            # Check low streak
            if analytics.current_streak == 0:
                struggle_indicators.append('no_streak')
                recommendations.append('Set daily practice goals')
            
            # If student has any struggle indicators, add to list
            if struggle_indicators:
                struggling_students.append({
                    'student': {
                        'id': student.id,
                        'username': student.username,
                        'first_name': student.first_name,
                        'last_name': student.last_name
                    },
                    'struggle_indicators': struggle_indicators,
                    'average_score': analytics.average_score,
                    'total_completed': total_completed,
                    'last_activity': analytics.last_activity,
                    'current_streak': analytics.current_streak,
                    'recommendations': recommendations
                })
        
        # Sort by severity (more indicators = more struggling)
        struggling_students.sort(key=lambda x: len(x['struggle_indicators']), reverse=True)
        
        return struggling_students
    
    def _calculate_engagement_metrics(self, students: List) -> Dict[str, Any]:
        """Calculate student engagement metrics."""
        total_students = len(students)
        if total_students == 0:
            return {}
        
        # Activity in different time periods
        now = timezone.now()
        periods = {
            'last_24h': now - timedelta(hours=24),
            'last_week': now - timedelta(days=7),
            'last_month': now - timedelta(days=30)
        }
        
        engagement_data = {}
        for period_name, start_date in periods.items():
            active_students = StudentAnalytics.objects.filter(
                student__in=students,
                last_activity__gte=start_date
            ).count()
            
            engagement_data[period_name] = {
                'active_students': active_students,
                'engagement_rate': round((active_students / total_students) * 100, 2)
            }
        
        # Submission frequency analysis
        recent_submissions = PracticeSubmission.objects.filter(
            student__in=students,
            submitted_at__gte=now - timedelta(days=7)
        ).count()
        
        # Average submissions per active student
        active_students_week = engagement_data['last_week']['active_students']
        avg_submissions = round(recent_submissions / active_students_week, 2) if active_students_week > 0 else 0
        
        return {
            'activity_periods': engagement_data,
            'submission_metrics': {
                'total_submissions_week': recent_submissions,
                'avg_submissions_per_active_student': avg_submissions
            },
            'overall_engagement_score': self._calculate_engagement_score(students)
        }
    
    def _calculate_engagement_score(self, students: List) -> float:
        """Calculate overall class engagement score (0-100)."""
        if not students:
            return 0.0
        
        total_score = 0
        total_students = len(students)
        
        for student in students:
            analytics = StudentAnalytics.objects.filter(student=student).first()
            if not analytics:
                continue
            
            # Factors contributing to engagement score
            score = 0
            
            # Recent activity (0-25 points)
            if analytics.last_activity:
                days_since_activity = (timezone.now() - analytics.last_activity).days
                if days_since_activity <= 1:
                    score += 25
                elif days_since_activity <= 3:
                    score += 20
                elif days_since_activity <= 7:
                    score += 15
                elif days_since_activity <= 14:
                    score += 10
            
            # Completion rate (0-25 points)
            total_completed = analytics.total_practice_completed + analytics.total_assignments_completed
            if total_completed >= 20:
                score += 25
            elif total_completed >= 10:
                score += 20
            elif total_completed >= 5:
                score += 15
            elif total_completed >= 1:
                score += 10
            
            # Current streak (0-25 points)
            if analytics.current_streak >= 7:
                score += 25
            elif analytics.current_streak >= 3:
                score += 20
            elif analytics.current_streak >= 1:
                score += 15
            
            # Performance (0-25 points)
            if analytics.average_score >= 90:
                score += 25
            elif analytics.average_score >= 70:
                score += 20
            elif analytics.average_score >= 50:
                score += 15
            elif analytics.average_score >= 30:
                score += 10
            
            total_score += score
        
        return round(total_score / total_students, 2) if total_students > 0 else 0.0
    
    def _analyze_problem_performance(self, students: List) -> Dict[str, Any]:
        """Analyze performance on specific problems and identify common failure patterns."""
        # Get all practice questions attempted by students
        attempted_questions = PracticeProgress.objects.filter(
            student__in=students
        ).values_list('practice_question', flat=True).distinct()
        
        problem_stats = []
        
        for question_id in attempted_questions:
            try:
                question = PracticeQuestion.objects.get(id=question_id)
                progress_records = PracticeProgress.objects.filter(
                    student__in=students,
                    practice_question=question
                )
                
                total_attempts = progress_records.count()
                completed = progress_records.filter(is_completed=True).count()
                completion_rate = (completed / total_attempts * 100) if total_attempts > 0 else 0
                
                # Average attempts to completion
                completed_records = progress_records.filter(is_completed=True)
                avg_attempts = completed_records.aggregate(avg_attempts=Avg('attempts_count'))['avg_attempts'] or 0
                
                # Average time spent
                avg_time = progress_records.aggregate(avg_time=Avg('time_spent'))['avg_time'] or 0
                
                problem_stats.append({
                    'question': {
                        'id': str(question.id),
                        'title': question.title,
                        'difficulty': question.difficulty,
                        'category': question.category
                    },
                    'stats': {
                        'total_attempts': total_attempts,
                        'completed': completed,
                        'completion_rate': round(completion_rate, 2),
                        'avg_attempts_to_complete': round(avg_attempts, 2),
                        'avg_time_minutes': round(avg_time / 60, 2)
                    }
                })
                
            except PracticeQuestion.DoesNotExist:
                continue
        
        # Sort by completion rate (lowest first to identify problem areas)
        problem_stats.sort(key=lambda x: x['stats']['completion_rate'])
        
        # Identify categories with low performance
        category_performance = {}
        for stat in problem_stats:
            category = stat['question']['category']
            if category not in category_performance:
                category_performance[category] = {'total': 0, 'completion_sum': 0}
            
            category_performance[category]['total'] += 1
            category_performance[category]['completion_sum'] += stat['stats']['completion_rate']
        
        category_averages = {
            category: round(data['completion_sum'] / data['total'], 2)
            for category, data in category_performance.items()
        }
        
        return {
            'problem_statistics': problem_stats[:20],  # Top 20 most problematic
            'category_performance': category_averages,
            'most_difficult_problems': problem_stats[:5],
            'easiest_problems': problem_stats[-5:] if len(problem_stats) > 5 else []
        }
    
    def _calculate_time_analytics(self, students: List) -> Dict[str, Any]:
        """Calculate time-based analytics for the class."""
        class_analytics = StudentAnalytics.objects.filter(student__in=students)
        
        if not class_analytics.exists():
            return {}
        
        # Time distribution
        time_stats = class_analytics.aggregate(
            avg_time=Avg('total_time_spent'),
            max_time=Max('total_time_spent'),
            min_time=Min('total_time_spent')
        )
        
        # Time categories
        time_categories = {
            'high_time': class_analytics.filter(total_time_spent__gte=300).count(),  # 5+ hours
            'medium_time': class_analytics.filter(
                total_time_spent__gte=120, 
                total_time_spent__lt=300
            ).count(),  # 2-5 hours
            'low_time': class_analytics.filter(total_time_spent__lt=120).count()  # < 2 hours
        }
        
        return {
            'time_statistics': {
                'avg_time_minutes': round(time_stats['avg_time'] or 0, 2),
                'max_time_minutes': time_stats['max_time'] or 0,
                'min_time_minutes': time_stats['min_time'] or 0
            },
            'time_distribution': time_categories
        }
    
    def _calculate_progress_distribution(self, students: List) -> Dict[str, Any]:
        """Calculate progress distribution across the class."""
        progress_data = {
            'beginners': 0,      # 0-2 completed
            'intermediate': 0,   # 3-9 completed
            'advanced': 0,       # 10+ completed
            'inactive': 0        # No analytics record
        }
        
        for student in students:
            analytics = StudentAnalytics.objects.filter(student=student).first()
            if not analytics:
                progress_data['inactive'] += 1
                continue
            
            total_completed = analytics.total_practice_completed + analytics.total_assignments_completed
            
            if total_completed <= 2:
                progress_data['beginners'] += 1
            elif total_completed <= 9:
                progress_data['intermediate'] += 1
            else:
                progress_data['advanced'] += 1
        
        return progress_data
    
    def _is_student_active(self, student) -> bool:
        """Check if a student is considered active (activity in last 14 days)."""
        analytics = StudentAnalytics.objects.filter(student=student).first()
        if not analytics or not analytics.last_activity:
            return False
        
        return analytics.last_activity >= timezone.now() - timedelta(days=14)
    
    def generate_class_report(self, class_obj, format_type='csv') -> HttpResponse:
        """
        Generate exportable class report.
        
        Args:
            class_obj: Class object
            format_type: 'csv' or 'json'
            
        Returns:
            HttpResponse: Downloadable report
        """
        analytics_data = self.get_comprehensive_class_analytics(class_obj)
        
        if format_type.lower() == 'csv':
            return self._generate_csv_report(analytics_data, class_obj)
        elif format_type.lower() == 'json':
            return self._generate_json_report(analytics_data, class_obj)
        else:
            raise ValueError(f"Unsupported format type: {format_type}")
    
    def _generate_csv_report(self, analytics_data: Dict, class_obj) -> HttpResponse:
        """Generate CSV report."""
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Header information
        writer.writerow(['Class Analytics Report'])
        writer.writerow(['Class:', analytics_data.get('class_info', {}).get('class_name', 'Unknown')])
        writer.writerow(['Generated:', analytics_data.get('class_info', {}).get('analysis_date', '')])
        writer.writerow(['Total Students:', analytics_data.get('class_info', {}).get('total_students', 0)])
        writer.writerow([])
        
        # Performance metrics
        writer.writerow(['Class Performance Metrics'])
        performance = analytics_data.get('performance_metrics', {})
        if 'averages' in performance:
            writer.writerow(['Metric', 'Value'])
            for metric, value in performance['averages'].items():
                writer.writerow([metric.replace('_', ' ').title(), value])
        writer.writerow([])
        
        # Struggling students
        writer.writerow(['Struggling Students'])
        struggling = analytics_data.get('struggling_students', [])
        if struggling:
            writer.writerow(['Student', 'Username', 'Average Score', 'Total Completed', 'Struggle Indicators'])
            for student_data in struggling:
                student = student_data['student']
                writer.writerow([
                    f"{student['first_name']} {student['last_name']}",
                    student['username'],
                    student_data['average_score'],
                    student_data['total_completed'],
                    ', '.join(student_data['struggle_indicators'])
                ])
        writer.writerow([])
        
        # Problem analytics
        writer.writerow(['Problem Performance'])
        problems = analytics_data.get('problem_analytics', {}).get('problem_statistics', [])
        if problems:
            writer.writerow(['Problem', 'Difficulty', 'Category', 'Completion Rate', 'Avg Attempts'])
            for problem in problems[:10]:  # Top 10 most problematic
                writer.writerow([
                    problem['question']['title'],
                    problem['question']['difficulty'],
                    problem['question']['category'],
                    f"{problem['stats']['completion_rate']}%",
                    problem['stats']['avg_attempts_to_complete']
                ])
        
        # Create response
        response = HttpResponse(output.getvalue(), content_type='text/csv')
        filename = f"class_analytics_{class_obj.id}_{timezone.now().strftime('%Y%m%d_%H%M%S')}.csv"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        
        return response
    
    def _generate_json_report(self, analytics_data: Dict, class_obj) -> HttpResponse:
        """Generate JSON report."""
        import json
        
        # Add metadata
        report_data = {
            'metadata': {
                'report_type': 'class_analytics',
                'generated_at': timezone.now().isoformat(),
                'class_id': str(class_obj.id)
            },
            'analytics': analytics_data
        }
        
        response = HttpResponse(
            json.dumps(report_data, indent=2, default=str),
            content_type='application/json'
        )
        filename = f"class_analytics_{class_obj.id}_{timezone.now().strftime('%Y%m%d_%H%M%S')}.json"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        
        return response


# Global instance
class_analytics_service = ClassAnalyticsService()