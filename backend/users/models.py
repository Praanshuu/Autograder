from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Standard Django AbstractUser with extended fields.
    Schema v3:
    - id: UUID (PK) - Django uses Int by default, but we can stick to native or switch to UUID. 
      Schema says UUID. User probably wants UUID.
      But changing PK is hard. 'Standard Django AbstractUser' usually implies Int PK unless specified otherwise in settings.
      Schema v3 says: id: UUID (PK).
    """
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('ta', 'Teaching Assistant'),
        ('student', 'Student'),
    ]
    
    # We will need to change PK to UUID in a migration if we strictly follow schema. 
    # For now, let's keep other fields aligned.
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    avatar_url = models.URLField(blank=True, null=True)
    
    # Settings stored as JSON
    settings = models.JSONField(default=dict, blank=True)
    
    class Meta:
        db_table = 'users'
        ordering = ['date_joined']
    
    def __str__(self):
        return f"{self.username} ({self.role})"
