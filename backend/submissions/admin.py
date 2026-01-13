from django.contrib import admin
from .models import Submission, TestResult


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'execution_time', 'points_earned']
    list_filter = ['status']


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['student', 'assignment', 'question', 'language', 'status',
                    'final_score', 'is_graded', 'is_published', 'submitted_at']
    list_filter = ['status', 'is_graded', 'is_published', 'language', 'submitted_at']
    search_fields = ['student__username', 'assignment__title', 'question__title']
