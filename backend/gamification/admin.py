from django.contrib import admin
from .models import (
    PracticeQuestionLibrary, UserPoints, Achievement, 
    UserAchievement, PracticeSubmission, PracticeProgress, 
    StudentAnalytics, LeaderboardEntry
)


@admin.register(PracticeQuestionLibrary)
class PracticeQuestionLibraryAdmin(admin.ModelAdmin):
    list_display = ['question', 'is_public', 'created_at']
    list_filter = ['is_public', 'created_at']
    search_fields = ['question__title', 'tags']
    readonly_fields = ['id', 'created_at']


@admin.register(UserPoints)
class UserPointsAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_points', 'practice_points', 'assignment_points', 'last_updated']
    list_filter = ['last_updated']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    readonly_fields = ['id', 'last_updated']
    ordering = ['-total_points']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['name', 'badge_type', 'rarity', 'point_threshold', 'is_active']
    list_filter = ['badge_type', 'rarity', 'is_active']
    search_fields = ['name', 'description']
    readonly_fields = ['id', 'created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'icon')
        }),
        ('Achievement Settings', {
            'fields': ('badge_type', 'rarity', 'criteria', 'point_threshold')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Metadata', {
            'fields': ('id', 'created_at'),
            'classes': ('collapse',)
        })
    )


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ['user', 'achievement', 'earned_at']
    list_filter = ['achievement__badge_type', 'achievement__rarity', 'earned_at']
    search_fields = ['user__username', 'achievement__name']
    readonly_fields = ['id', 'earned_at']
    ordering = ['-earned_at']


@admin.register(PracticeSubmission)
class PracticeSubmissionAdmin(admin.ModelAdmin):
    list_display = ['student', 'question', 'status', 'attempt_number', 'points_earned', 'submitted_at']
    list_filter = ['status', 'language', 'submitted_at']
    search_fields = ['student__username', 'question__title']
    readonly_fields = ['id', 'submitted_at']
    ordering = ['-submitted_at']
    
    fieldsets = (
        ('Submission Info', {
            'fields': ('student', 'question', 'attempt_number', 'language')
        }),
        ('Code & Results', {
            'fields': ('source_code', 'status', 'test_results', 'points_earned', 'execution_time_ms')
        }),
        ('Metadata', {
            'fields': ('id', 'submitted_at'),
            'classes': ('collapse',)
        })
    )


@admin.register(PracticeProgress)
class PracticeProgressAdmin(admin.ModelAdmin):
    list_display = ['student', 'question', 'is_completed', 'attempts_count', 'best_score', 'completed_at']
    list_filter = ['is_completed', 'question__difficulty', 'completed_at']
    search_fields = ['student__username', 'question__title']
    readonly_fields = ['id', 'first_attempt_at', 'last_updated']
    ordering = ['-last_updated']


@admin.register(StudentAnalytics)
class StudentAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['student', 'total_practice_completed', 'total_assignments_completed', 'average_score', 'current_streak', 'last_activity']
    list_filter = ['last_activity', 'updated_at']
    search_fields = ['student__username', 'student__first_name', 'student__last_name']
    readonly_fields = ['id', 'updated_at']
    ordering = ['-updated_at']
    
    fieldsets = (
        ('Student', {
            'fields': ('student',)
        }),
        ('Completion Stats', {
            'fields': ('total_practice_completed', 'total_assignments_completed', 'average_score')
        }),
        ('Streaks & Time', {
            'fields': ('current_streak', 'longest_streak', 'total_time_spent', 'last_activity')
        }),
        ('Advanced Analytics', {
            'fields': ('performance_trend', 'concept_mastery'),
            'classes': ('collapse',)
        }),
        ('Metadata', {
            'fields': ('id', 'updated_at'),
            'classes': ('collapse',)
        })
    )


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ['rank', 'user', 'total_points', 'completed_problems', 'leaderboard_type', 'updated_at']
    list_filter = ['leaderboard_type', 'updated_at']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    readonly_fields = ['id', 'updated_at']
    ordering = ['leaderboard_type', 'rank']