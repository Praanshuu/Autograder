import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class PracticeQuestion(models.Model):
    """Standalone practice problems separate from assignments"""
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'), 
        ('hard', 'Hard')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    category = models.CharField(max_length=100)  # e.g., "Arrays", "Recursion"
    test_cases = models.JSONField()  # Same format as existing questions
    starter_code = models.TextField(blank=True)
    point_value = models.IntegerField(validators=[MinValueValidator(1)])  # Points awarded for completion
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'practice_questions'
        ordering = ['difficulty', 'title']
        indexes = [
            models.Index(fields=['difficulty', 'category']),
            models.Index(fields=['is_active', 'created_at']),
        ]
    
    def __str__(self):
        return f"{self.title} ({self.difficulty})"


class PracticeQuestionLibrary(models.Model):
    """Pre-built practice questions that teachers can assign"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(PracticeQuestion, on_delete=models.CASCADE)
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
    practice_question = models.ForeignKey(PracticeQuestion, on_delete=models.CASCADE, related_name='submissions')
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
            models.Index(fields=['student', 'practice_question']),
            models.Index(fields=['student', '-submitted_at']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"{self.student.username} - {self.practice_question.title} (Attempt {self.attempt_number})"


class PracticeProgress(models.Model):
    """Track student progress on practice questions"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='practice_progress')
    practice_question = models.ForeignKey(PracticeQuestion, on_delete=models.CASCADE, related_name='progress')
    is_completed = models.BooleanField(default=False)
    attempts_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    best_score = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    time_spent = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # seconds
    first_attempt_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'practice_progress'
        unique_together = ['student', 'practice_question']
        indexes = [
            models.Index(fields=['student', 'is_completed']),
            models.Index(fields=['practice_question', 'is_completed']),
        ]
    
    def __str__(self):
        status = "Completed" if self.is_completed else "In Progress"
        return f"{self.student.username} - {self.practice_question.title} ({status})"


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


class LeaderboardEntry(models.Model):
    """Cached leaderboard data for performance"""
    LEADERBOARD_TYPE_CHOICES = [
        ('global', 'Global'),
        ('class', 'Class-specific')
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