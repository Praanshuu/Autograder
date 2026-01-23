import uuid
from django.db import models
from submissions.models import SubmissionAttempt
from assignments.models import Question

class SubmissionAnalysis(models.Model):
    """
    AI / Heavy ML analysis.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attempt = models.OneToOneField(SubmissionAttempt, on_delete=models.CASCADE, related_name='analysis')
    detected_keywords = models.JSONField(default=list)  # Storing array of strings as JSON
    umap_x = models.FloatField(null=True, blank=True)
    umap_y = models.FloatField(null=True, blank=True)
    ai_feedback = models.TextField(blank=True)
    
    class Meta:
        db_table = 'submission_analysis'

class ProblemAnalytics(models.Model):
    """
    Pre-calculated stats for Heatmaps per question/testcase.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='analytics')
    test_case_id = models.CharField(max_length=50)
    pass_count = models.IntegerField(default=0)
    fail_count = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'problem_analytics'
        unique_together = ['question', 'test_case_id']
