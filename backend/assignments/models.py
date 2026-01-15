from django.db import models
from django.conf import settings
from classes.models import Class


class TestCase(models.Model):
    input = models.TextField()
    expected_output = models.TextField()
    is_hidden = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'test_cases'


class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('cpp', 'C++'),
        ('c', 'C'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    hint = models.TextField(blank=True, help_text="Hint to help students solve the problem")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='Medium')
    test_cases = models.ManyToManyField(TestCase, related_name='questions')
    time_limit = models.IntegerField(default=5000)  # milliseconds
    memory_limit = models.IntegerField(default=256)  # MB
    allowed_languages = models.JSONField(default=list)
    starter_code = models.TextField(blank=True, help_text="Starter code template for students")
    order = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'questions'
        ordering = ['order']


class Assignment(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('closed', 'Closed'),
    ]
    
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    points = models.IntegerField(default=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    questions = models.ManyToManyField(Question, related_name='assignments')
    allow_late_submission = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_assignments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'assignments'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.class_obj.name}"
