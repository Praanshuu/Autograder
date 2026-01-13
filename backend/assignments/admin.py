from django.contrib import admin
from .models import Assignment, Question, TestCase


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_hidden', 'points']
    list_filter = ['is_hidden']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'order']
    list_filter = ['difficulty']
    search_fields = ['title']


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'class_obj', 'status', 'due_date', 'created_by']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'class_obj__name']
