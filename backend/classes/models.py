import uuid
from django.db import models
from django.conf import settings
import random
import string


def generate_join_code():
    """Generate a unique 6-character join code"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


class Class(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_classes')
    name = models.CharField(max_length=200)
    section = models.CharField(max_length=100)
    join_code = models.CharField(max_length=10, unique=True, default=generate_join_code)
    settings = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'classes'
        ordering = ['-created_at']
        verbose_name_plural = 'Classes'
    
    def __str__(self):
        return f"{self.name} - {self.section}"


class Module(models.Model):
    """
    Grouping unit (e.g., "Week 1").
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    order_index = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'modules'
        ordering = ['order_index']
    
    def __str__(self):
        return f"{self.title} ({self.class_obj.name})"


class Enrollment(models.Model):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('ta', 'Teaching Assistant'),
        ('student', 'Student'),
    ]
    
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='enrollments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'enrollments'
        unique_together = ['class_obj', 'user']
        ordering = ['-joined_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.class_obj.name} ({self.role})"


class Announcement(models.Model):
    """
    Teacher announcements for the class stream.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='announcements')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='announcements')
    content = models.TextField()
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'announcements'
        ordering = ['-is_pinned', '-created_at']

    def __str__(self):
        return f"{self.author.username} - {self.class_obj.name}"


class Comment(models.Model):
    """
    Comments on Announcements or Assignments.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='class_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Parent objects
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    # Use string reference to avoid circular import with assignments app
    assignment = models.ForeignKey('assignments.Assignment', on_delete=models.CASCADE, related_name='class_comments', null=True, blank=True)

    class Meta:
        db_table = 'class_comments'
        ordering = ['created_at']
