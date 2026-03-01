import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import transaction
from django.utils import timezone
from typing import List, Dict, Optional
from assignments.models import Question
# PracticeQuestion model removed - merged into assignments.Question


class PracticeQuestionLibrary(models.Model):
    """Pre-built practice questions that teachers can assign"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    tags = models.JSONField(default=list)  # For filtering and search
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'practice_question_library'
        indexes = [
            models.Index(fields=['is_public']),
        ]


class UserPoints(models.Model):
    """Track total points earned by each user"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='points')
    total_points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    practice_points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    assignment_points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_points'
        ordering = ['-total_points']
        indexes = [
            models.Index(fields=['-total_points']),
        ]
    
    def __str__(self):
        return f"{self.user.username}: {self.total_points} points"


class Achievement(models.Model):
    """Define available achievement badges"""
    BADGE_TYPE_CHOICES = [
        ('first_completion', 'First Completion'),
        ('streak', 'Streak Achievement'),
        ('perfect_score', 'Perfect Score'),
        ('speed', 'Speed Achievement'),
        ('milestone', 'Milestone Achievement')
    ]
    
    RARITY_CHOICES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('legendary', 'Legendary')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)  # Emoji or icon class
    badge_type = models.CharField(max_length=50, choices=BADGE_TYPE_CHOICES)
    criteria = models.JSONField()  # Flexible criteria definition
    point_threshold = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'achievements'
        indexes = [
            models.Index(fields=['badge_type', 'is_active']),
            models.Index(fields=['rarity']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.rarity})"


class UserAchievement(models.Model):
    """Track achievements earned by users"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'user_achievements'
        unique_together = ['user', 'achievement']
        ordering = ['-earned_at']
        indexes = [
            models.Index(fields=['user', '-earned_at']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.achievement.name}"


class PracticeSubmission(models.Model):
    """Track practice question submissions"""
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('success', 'Success'),
        ('fail', 'Failed'),
        ('error', 'Error')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='practice_submissions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='practice_submissions')
    source_code = models.TextField()
    language = models.CharField(max_length=20, default='python')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    test_results = models.JSONField(default=list)
    points_earned = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    attempt_number = models.IntegerField(validators=[MinValueValidator(1)])
    execution_time_ms = models.IntegerField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'practice_submissions'
        ordering = ['-submitted_at']
        indexes = [
            models.Index(fields=['student', 'question']),
            models.Index(fields=['student', '-submitted_at']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"{self.student.username} - {self.question.title} (Attempt {self.attempt_number})"


class PracticeProgress(models.Model):
    """Track student progress on practice questions"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='practice_progress')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='practice_progress')
    is_completed = models.BooleanField(default=False)
    attempts_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    best_score = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    time_spent = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # seconds
    first_attempt_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'practice_progress'
        unique_together = ['student', 'question']
        indexes = [
            models.Index(fields=['student', 'is_completed']),
            models.Index(fields=['question', 'is_completed']),
        ]
    
    def __str__(self):
        status = "Completed" if self.is_completed else "In Progress"
        return f"{self.student.username} - {self.question.title} ({status})"


class StudentAnalytics(models.Model):
    """Aggregated analytics data for students"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='analytics')
    total_practice_completed = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    total_assignments_completed = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    average_score = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    current_streak = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    longest_streak = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    total_time_spent = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # minutes
    last_activity = models.DateTimeField(null=True, blank=True)
    performance_trend = models.JSONField(default=list)  # Last 30 days
    concept_mastery = models.JSONField(default=dict)  # Category -> mastery %
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'student_analytics'
        indexes = [
            models.Index(fields=['last_activity']),
            models.Index(fields=['updated_at']),
        ]
    
    def __str__(self):
        return f"{self.student.username} Analytics"
    def __str__(self):
        return f"{self.student.username} Analytics"


class LeaderboardManager:
    """
    Manager for leaderboard operations including ranking calculation and caching.
    
    This class handles:
    - Ranking calculation with tie-breaking logic
    - Global and class-specific leaderboards
    - Cached leaderboard data for performance
    - Real-time updates on point changes
    """
    
    @staticmethod
    def calculate_global_leaderboard() -> List[Dict]:
        """
        Calculate global leaderboard rankings based on total points.
        
        Returns:
            List[Dict]: List of user rankings with tie-breaking
        """
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Get all users with points, ordered by total points (desc), then by last_updated (asc) for tie-breaking
        users_with_points = UserPoints.objects.select_related('user').order_by(
            '-total_points', 'last_updated'
        )
        
        rankings = []
        current_rank = 1
        
        for i, user_points in enumerate(users_with_points):
            # Handle ties - users with same points get same rank
            if i > 0 and user_points.total_points < users_with_points[i-1].total_points:
                current_rank = i + 1
            
            # Count completed problems
            completed_problems = PracticeProgress.objects.filter(
                student=user_points.user,
                is_completed=True
            ).count()
            
            rankings.append({
                'user': user_points.user,
                'rank': current_rank,
                'total_points': user_points.total_points,
                'practice_points': user_points.practice_points,
                'assignment_points': user_points.assignment_points,
                'completed_problems': completed_problems,
                'last_updated': user_points.last_updated
            })
        
        return rankings
    
    @staticmethod
    def calculate_class_leaderboard(class_id: str) -> List[Dict]:
        """
        Calculate class-specific leaderboard rankings.
        
        Args:
            class_id: UUID of the class
            
        Returns:
            List[Dict]: List of user rankings for the class
        """
        from classes.models import Class, Enrollment
        
        try:
            class_obj = Class.objects.get(id=class_id)
            # Get students enrolled in this class
            class_students = [
                enrollment.user for enrollment in 
                Enrollment.objects.filter(class_obj=class_obj, role='student').select_related('user')
            ]
        except Class.DoesNotExist:
            return []
        
        # Get points for students in this class
        student_points = UserPoints.objects.filter(
            user__in=class_students
        ).select_related('user').order_by('-total_points', 'last_updated')
        
        rankings = []
        current_rank = 1
        
        for i, user_points in enumerate(student_points):
            # Handle ties
            if i > 0 and user_points.total_points < student_points[i-1].total_points:
                current_rank = i + 1
            
            # Count completed problems
            completed_problems = PracticeProgress.objects.filter(
                student=user_points.user,
                is_completed=True
            ).count()
            
            rankings.append({
                'user': user_points.user,
                'rank': current_rank,
                'total_points': user_points.total_points,
                'practice_points': user_points.practice_points,
                'assignment_points': user_points.assignment_points,
                'completed_problems': completed_problems,
                'last_updated': user_points.last_updated,
                'class_id': class_id
            })
        
        return rankings

    @staticmethod
    def calculate_daily_leaderboard() -> List[Dict]:
        """
        Calculate daily leaderboard rankings based on points earned today.
        """
        from django.db.models import Sum as DSum
        today = timezone.now().date()

        practice_qs = (
            PracticeSubmission.objects
            .filter(status='success', submitted_at__date=today)
            .values('student')
            .annotate(pts=DSum('points_earned'))
        )
        combined: dict = {}
        for row in practice_qs:
            combined[row['student']] = (row['pts'] or 0)

        try:
            from submissions.models import SubmissionAttempt
            from django.db.models import Sum as ASum
            assign_qs = (
                SubmissionAttempt.objects
                .filter(created_at__date=today, status='success')
                .values('student')
                .annotate(pts=ASum('points_earned'))
            )
            for row in assign_qs:
                combined[row['student']] = combined.get(row['student'], 0) + (row['pts'] or 0)
        except Exception:
            pass

        from django.contrib.auth import get_user_model
        User = get_user_model()
        sorted_users = sorted(combined.items(), key=lambda x: -x[1])
        rankings = []
        for idx, (uid, pts) in enumerate(sorted_users):
            try:
                user = User.objects.get(id=uid)
            except User.DoesNotExist:
                continue
            completed_problems = PracticeProgress.objects.filter(
                student=user, is_completed=True
            ).count()
            rankings.append({
                'user': user,
                'rank': idx + 1,
                'total_points': pts,
                'completed_problems': completed_problems,
            })
        return rankings

    @staticmethod
    def calculate_weekly_leaderboard() -> List[Dict]:
        """
        Calculate weekly leaderboard rankings (Monday 00:00 to now).
        """
        from django.db.models import Sum as WSum
        now = timezone.now()
        week_start = (now - timezone.timedelta(days=now.weekday())).replace(
            hour=0, minute=0, second=0, microsecond=0
        )

        practice_qs = (
            PracticeSubmission.objects
            .filter(status='success', submitted_at__gte=week_start)
            .values('student')
            .annotate(pts=WSum('points_earned'))
        )
        combined: dict = {}
        for row in practice_qs:
            combined[row['student']] = (row['pts'] or 0)

        try:
            from submissions.models import SubmissionAttempt
            from django.db.models import Sum as ASum
            assign_qs = (
                SubmissionAttempt.objects
                .filter(created_at__gte=week_start, status='success')
                .values('student')
                .annotate(pts=ASum('points_earned'))
            )
            for row in assign_qs:
                combined[row['student']] = combined.get(row['student'], 0) + (row['pts'] or 0)
        except Exception:
            pass

        from django.contrib.auth import get_user_model
        User = get_user_model()
        sorted_users = sorted(combined.items(), key=lambda x: -x[1])
        rankings = []
        for idx, (uid, pts) in enumerate(sorted_users):
            try:
                user = User.objects.get(id=uid)
            except User.DoesNotExist:
                continue
            completed_problems = PracticeProgress.objects.filter(
                student=user, is_completed=True
            ).count()
            rankings.append({
                'user': user,
                'rank': idx + 1,
                'total_points': pts,
                'completed_problems': completed_problems,
            })
        return rankings

    @staticmethod
    @transaction.atomic
    def update_global_leaderboard():

        """
        Update the cached global leaderboard entries.
        This should be called when user points change.
        """
        from .realtime_service import realtime_service
        
        # Store old rankings for comparison
        old_rankings = {
            entry.user_id: entry.rank 
            for entry in LeaderboardEntry.objects.filter(leaderboard_type='global')
        }
        
        # Clear existing global leaderboard entries
        LeaderboardEntry.objects.filter(leaderboard_type='global').delete()
        
        # Calculate new rankings
        rankings = LeaderboardManager.calculate_global_leaderboard()
        
        # Create new leaderboard entries
        leaderboard_entries = []
        for ranking in rankings:
            leaderboard_entries.append(
                LeaderboardEntry(
                    user=ranking['user'],
                    rank=ranking['rank'],
                    total_points=ranking['total_points'],
                    completed_problems=ranking['completed_problems'],
                    leaderboard_type='global'
                )
            )
        
        # Bulk create for performance
        LeaderboardEntry.objects.bulk_create(leaderboard_entries)
        
        # Broadcast real-time updates
        # Notify users of rank changes
        for ranking in rankings:
            user_id = ranking['user'].id
            new_rank = ranking['rank']
            old_rank = old_rankings.get(user_id)
            
            if old_rank and old_rank != new_rank:
                realtime_service.notify_rank_change(
                    user=ranking['user'],
                    old_rank=old_rank,
                    new_rank=new_rank,
                    leaderboard_type='global'
                )
        
        # Broadcast leaderboard update
        leaderboard_data = LeaderboardManager.get_leaderboard_page('global', None, 1, 20)
        realtime_service.broadcast_leaderboard_update('global', data=leaderboard_data)
        
        return len(leaderboard_entries)
    
    @staticmethod
    @transaction.atomic
    def update_class_leaderboard(class_id: str):
        """
        Update the cached class leaderboard entries.
        
        Args:
            class_id: UUID of the class to update
        """
        from .realtime_service import realtime_service
        
        # Store old rankings for comparison
        old_rankings = {
            entry.user_id: entry.rank 
            for entry in LeaderboardEntry.objects.filter(
                leaderboard_type='class',
                class_id=class_id
            )
        }
        
        # Clear existing class leaderboard entries
        LeaderboardEntry.objects.filter(
            leaderboard_type='class',
            class_id=class_id
        ).delete()
        
        # Calculate new rankings
        rankings = LeaderboardManager.calculate_class_leaderboard(class_id)
        
        # Create new leaderboard entries
        leaderboard_entries = []
        for ranking in rankings:
            leaderboard_entries.append(
                LeaderboardEntry(
                    user=ranking['user'],
                    rank=ranking['rank'],
                    total_points=ranking['total_points'],
                    completed_problems=ranking['completed_problems'],
                    leaderboard_type='class',
                    class_id=class_id
                )
            )
        
        # Bulk create for performance
        LeaderboardEntry.objects.bulk_create(leaderboard_entries)
        
        # Broadcast real-time updates
        # Notify users of rank changes
        for ranking in rankings:
            user_id = ranking['user'].id
            new_rank = ranking['rank']
            old_rank = old_rankings.get(user_id)
            
            if old_rank and old_rank != new_rank:
                realtime_service.notify_rank_change(
                    user=ranking['user'],
                    old_rank=old_rank,
                    new_rank=new_rank,
                    leaderboard_type='class',
                    class_id=class_id
                )
        
        # Broadcast leaderboard update
        leaderboard_data = LeaderboardManager.get_leaderboard_page('class', class_id, 1, 20)
        realtime_service.broadcast_leaderboard_update('class', class_id=class_id, data=leaderboard_data)
        
        return len(leaderboard_entries)
    
    @staticmethod
    def get_user_rank(user, leaderboard_type='global', class_id=None) -> Optional[Dict]:
        """
        Get a specific user's rank and nearby competitors.
        
        Args:
            user: User object
            leaderboard_type: 'global' or 'class'
            class_id: Required for class leaderboards
            
        Returns:
            Dict with user rank and nearby competitors, or None if not found
        """
        try:
            # Get user's leaderboard entry
            user_entry = LeaderboardEntry.objects.get(
                user=user,
                leaderboard_type=leaderboard_type,
                class_id=class_id
            )
            
            # Get nearby competitors (3 above and 3 below)
            nearby_entries = LeaderboardEntry.objects.filter(
                leaderboard_type=leaderboard_type,
                class_id=class_id,
                rank__gte=max(1, user_entry.rank - 3),
                rank__lte=user_entry.rank + 3
            ).select_related('user').order_by('rank')
            
            return {
                'user_rank': user_entry.rank,
                'user_points': user_entry.total_points,
                'user_problems': user_entry.completed_problems,
                'nearby_competitors': [
                    {
                        'rank': entry.rank,
                        'user': entry.user,
                        'points': entry.total_points,
                        'problems': entry.completed_problems,
                        'is_current_user': entry.user == user
                    }
                    for entry in nearby_entries
                ]
            }
            
        except LeaderboardEntry.DoesNotExist:
            return None
    
    @staticmethod
    def get_leaderboard_page(leaderboard_type='global', class_id=None, page=1, page_size=20) -> Dict:
        """
        Get a paginated leaderboard.
        
        Args:
            leaderboard_type: 'global' or 'class'
            class_id: Required for class leaderboards
            page: Page number (1-based)
            page_size: Number of entries per page
            
        Returns:
            Dict with leaderboard data and pagination info
        """
        # Calculate offset
        offset = (page - 1) * page_size
        
        # Get leaderboard entries
        queryset = LeaderboardEntry.objects.filter(
            leaderboard_type=leaderboard_type,
            class_id=class_id
        ).select_related('user').order_by('rank')
        
        total_entries = queryset.count()
        entries = queryset[offset:offset + page_size]
        
        return {
            'entries': [
                {
                    'rank': entry.rank,
                    'user': entry.user,
                    'points': entry.total_points,
                    'problems': entry.completed_problems,
                    'updated_at': entry.updated_at
                }
                for entry in entries
            ],
            'pagination': {
                'current_page': page,
                'page_size': page_size,
                'total_entries': total_entries,
                'total_pages': (total_entries + page_size - 1) // page_size,
                'has_next': offset + page_size < total_entries,
                'has_previous': page > 1
            }
        }
    
    @staticmethod
    @transaction.atomic
    def update_daily_leaderboard() -> int:
        """Rebuild the daily leaderboard from today's submissions."""
        LeaderboardEntry.objects.filter(leaderboard_type='daily').delete()
        rankings = LeaderboardManager.calculate_daily_leaderboard()
        entries = [
            LeaderboardEntry(
                user=r['user'], rank=r['rank'],
                total_points=r['total_points'],
                completed_problems=r['completed_problems'],
                leaderboard_type='daily',
            )
            for r in rankings
        ]
        LeaderboardEntry.objects.bulk_create(entries)
        return len(entries)

    @staticmethod
    @transaction.atomic
    def update_weekly_leaderboard() -> int:
        """Rebuild the weekly leaderboard from this week's submissions."""
        LeaderboardEntry.objects.filter(leaderboard_type='weekly').delete()
        rankings = LeaderboardManager.calculate_weekly_leaderboard()
        entries = [
            LeaderboardEntry(
                user=r['user'], rank=r['rank'],
                total_points=r['total_points'],
                completed_problems=r['completed_problems'],
                leaderboard_type='weekly',
            )
            for r in rankings
        ]
        LeaderboardEntry.objects.bulk_create(entries)
        return len(entries)

    @staticmethod
    def update_leaderboards_for_user(user):
        """
        Update all leaderboards when a user's points change.
        """
        LeaderboardManager.update_global_leaderboard()
        LeaderboardManager.update_daily_leaderboard()
        LeaderboardManager.update_weekly_leaderboard()

        # Update class leaderboards for classes the user belongs to
        from classes.models import Class, Enrollment
        user_classes = Class.objects.filter(
            enrollments__user=user,
            enrollments__role='student'
        )
        for class_obj in user_classes:
            LeaderboardManager.update_class_leaderboard(str(class_obj.id))


class LeaderboardEntry(models.Model):
    """Cached leaderboard data for performance"""
    LEADERBOARD_TYPE_CHOICES = [
        ('global', 'Global'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('class', 'Class-specific'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leaderboard_entries')
    rank = models.IntegerField(validators=[MinValueValidator(1)])
    total_points = models.IntegerField(validators=[MinValueValidator(0)])
    completed_problems = models.IntegerField(validators=[MinValueValidator(0)])
    leaderboard_type = models.CharField(max_length=20, choices=LEADERBOARD_TYPE_CHOICES)
    class_id = models.UUIDField(null=True, blank=True)  # For class leaderboards
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard_entries'
        unique_together = ['user', 'leaderboard_type', 'class_id']
        ordering = ['rank']
        indexes = [
            models.Index(fields=['leaderboard_type', 'class_id', 'rank']),
            models.Index(fields=['updated_at']),
        ]
    
    def __str__(self):
        return f"#{self.rank} {self.user.username} ({self.leaderboard_type})"