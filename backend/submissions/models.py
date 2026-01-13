from django.db import models
from django.conf import settings
from assignments.models import Assignment, Question, TestCase


class TestResult(models.Model):
    STATUS_CHOICES = [
        ('pass', 'Pass'),
        ('fail', 'Fail'),
        ('error', 'Error'),
        ('timeout', 'Timeout'),
    ]
    
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    execution_time = models.IntegerField(default=0)  # milliseconds
    memory_usage = models.IntegerField(default=0)  # MB
    console_output = models.TextField(blank=True)
    error_message = models.TextField(blank=True)
    points_earned = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'test_results'


class Submission(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('late', 'Late'),
        ('missing', 'Missing'),
    ]
    
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('cpp', 'C++'),
        ('c', 'C'),
    ]
    
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submissions')
    code_content = models.TextField()
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    test_results = models.ManyToManyField(TestResult, related_name='submissions', blank=True)
    auto_grade_score = models.IntegerField(default=0)
    manual_adjustment = models.IntegerField(default=0)
    final_score = models.IntegerField(default=0)
    teacher_feedback = models.TextField(blank=True)
    ai_feedback = models.TextField(blank=True)
    is_graded = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'submissions'
        unique_together = ['assignment', 'question', 'student']
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.student.username} - {self.assignment.title} - {self.question.title}"
