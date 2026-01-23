from django.contrib import admin
from .models import SubmissionAttempt, AssignmentProgress, TestResult, GradebookEntry

@admin.register(SubmissionAttempt)
class SubmissionAttemptAdmin(admin.ModelAdmin):
    list_display = ['student', 'assignment_question', 'status', 'attempt_number', 'created_at']
    list_filter = ['status']

@admin.register(AssignmentProgress)
class AssignmentProgressAdmin(admin.ModelAdmin):
    list_display = ['student', 'assignment_question', 'last_updated']

@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ['attempt', 'test_case_id', 'status', 'score']
    list_filter = ['status']

@admin.register(GradebookEntry)
class GradebookEntryAdmin(admin.ModelAdmin):
    list_display = ['student', 'content_item', 'final_score', 'status']
    list_filter = ['status']
