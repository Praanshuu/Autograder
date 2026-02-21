import uuid
from django.db import models
from django.conf import settings
from assignments.models import AssignmentQuestion, ContentItem


class AssignmentProgress(models.Model):
    """
    Mutable draft. Overwritten frequently.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progress')
    assignment_question = models.ForeignKey(AssignmentQuestion, on_delete=models.CASCADE, related_name='progress')
    current_code = models.TextField()
    time_spent = models.IntegerField(default=0)  # seconds
    started_at = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'assignment_progress'
        unique_together = ['student', 'assignment_question']


class SubmissionAttempt(models.Model):
    """
    Immutable submission log.
    For Exam: Only 1 row allowed per student/question (logic enforced in view).
    For Practice: Multiple rows allowed.
    """
    STATUS_CHOICES = [
        ('queued', 'Queued'),
        ('processing', 'Processing'),
        ('success', 'Success'),
        ('fail', 'Fail'),
        ('error', 'Error'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attempts')
    assignment_question = models.ForeignKey(AssignmentQuestion, on_delete=models.CASCADE, related_name='attempts')
    attempt_number = models.IntegerField(default=1)
    code_blob_ref = models.CharField(max_length=255, null=True, blank=True)  # Path in MinIO
    execution_time_ms = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='queued')
    created_at = models.DateTimeField(auto_now_add=True)
    manual_score = models.FloatField(null=True, blank=True)
    feedback_text = models.TextField(blank=True)
    detected_keywords = models.JSONField(default=list, blank=True)
    source_code = models.TextField(blank=True) # Snapshot of code at submission time
    ai_analysis_data = models.JSONField(null=True, blank=True)  # New field for AI analysis results
    
    class Meta:
        db_table = 'submission_attempts'
        ordering = ['student', 'assignment_question', '-attempt_number']


class TestResult(models.Model):
    """
    Details for a specific attempt.
    """
    STATUS_CHOICES = [
        ('pass', 'Pass'),
        ('fail', 'Fail'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attempt = models.ForeignKey(SubmissionAttempt, on_delete=models.CASCADE, related_name='test_results')
    test_case_id = models.CharField(max_length=50) # ID from JSONB in Question
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    score = models.FloatField(default=0.0)
    actual_output = models.TextField(blank=True, default='')
    error_message = models.TextField(blank=True, default='')
    execution_time_ms = models.IntegerField(null=True, blank=True, default=0)
    
    class Meta:
        db_table = 'test_result_details'


class GradebookEntry(models.Model):
    """
    Summary for gradebook.
    """
    STATUS_CHOICES = [
        ('graded', 'Graded'),
        ('submitted', 'Submitted'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='grades')
    content_item = models.ForeignKey(ContentItem, on_delete=models.CASCADE)
    final_score = models.FloatField(default=0.0)
    points_earned = models.IntegerField(default=0)  # Points earned from gamification system
    status = models.CharField(max_length=20, choices=[('graded', 'Graded'), ('pending', 'Pending')], default='pending')
    completion_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'gradebook_entries'
        unique_together = ('student', 'content_item')


class AIAnalysisTask(models.Model):
    """
    Tracks a bulk AI analysis run for an assignment.
    Stores Celery task IDs per batch so we can cancel mid-run,
    and exposes real-time progress (completed_batches / total_batches).
    """
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('running',   'Running'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('failed',    'Failed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    assignment = models.ForeignKey(
        'assignments.Assignment',
        on_delete=models.CASCADE,
        related_name='ai_analysis_tasks'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    # Celery task IDs for each batch — stored so we can revoke them on cancel
    task_ids = models.JSONField(default=list)

    total_batches     = models.IntegerField(default=0)
    completed_batches = models.IntegerField(default=0)
    total_submissions = models.IntegerField(default=0)
    analyzed          = models.IntegerField(default=0)

    error_message = models.TextField(blank=True, default='')
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ai_analysis_tasks'
        ordering = ['-created_at']

    @property
    def percent(self):
        if self.total_batches == 0:
            return 0
        return round((self.completed_batches / self.total_batches) * 100)
