from django.contrib import admin
from .models import ContentItem, Question, Assignment, AssignmentQuestion, Module

@admin.register(ContentItem)
class ContentItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'module', 'due_date', 'is_published']
    list_filter = ['type', 'is_published']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_by']
    search_fields = ['title', 'slug']

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'mode', 'points_total', 'due_date']
    list_filter = ['mode', 'difficulty']

@admin.register(AssignmentQuestion)
class AssignmentQuestionAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'question', 'order']
    ordering = ['assignment', 'order']
