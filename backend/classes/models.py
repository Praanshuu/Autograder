from django.db import models
from django.conf import settings
import random
import string


def generate_join_code():
    """Generate a unique 6-character join code"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


class Class(models.Model):
    name = models.CharField(max_length=200)
    section = models.CharField(max_length=100)
    subject = models.CharField(max_length=200, blank=True)
    room = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    theme_color = models.CharField(max_length=7, default='#6366f1')
    bg_pattern = models.CharField(max_length=50, default='bg-indigo-600')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_classes')
    join_code = models.CharField(max_length=10, unique=True, default=generate_join_code)
    is_archived = models.BooleanField(default=False)
    semester = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'classes'
        ordering = ['-created_at']
        verbose_name_plural = 'Classes'
    
    def __str__(self):
        return f"{self.name} - {self.section}"


class Enrollment(models.Model):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('ta', 'Teaching Assistant'),
        ('student', 'Student'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('removed', 'Removed'),
    ]
    
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='enrollments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    joined_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'enrollments'
        unique_together = ['class_obj', 'user']
        ordering = ['-joined_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.class_obj.name} ({self.role})"
