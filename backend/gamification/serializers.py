"""
Serializers for gamification API endpoints.

This module provides DRF serializers for:
- User points and point tracking
- Achievements and user achievements
- Leaderboard entries
- Student analytics
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model
from assignments.models import Question
from .models import (
    UserPoints, Achievement, UserAchievement, LeaderboardEntry,
    StudentAnalytics, PracticeSubmission, PracticeProgress,
    PracticeQuestionLibrary
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Basic user information for gamification features"""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        read_only_fields = ['id', 'username', 'email']


class UserPointsSerializer(serializers.ModelSerializer):
    """Serializer for user points with user information"""
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserPoints
        fields = [
            'id', 'user', 'total_points', 'practice_points', 
            'assignment_points', 'last_updated'
        ]
        read_only_fields = ['id', 'last_updated']


class AchievementSerializer(serializers.ModelSerializer):
    """Serializer for achievement definitions"""
    
    class Meta:
        model = Achievement
        fields = [
            'id', 'name', 'description', 'icon', 'badge_type',
            'criteria', 'point_threshold', 'rarity', 'is_active'
        ]
        read_only_fields = ['id']


class UserAchievementSerializer(serializers.ModelSerializer):
    """Serializer for user achievements with achievement details"""
    achievement = AchievementSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserAchievement
        fields = ['id', 'user', 'achievement', 'earned_at']
        read_only_fields = ['id', 'earned_at']


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    """Serializer for leaderboard entries with user information"""
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = LeaderboardEntry
        fields = [
            'id', 'user', 'rank', 'total_points', 'completed_problems',
            'leaderboard_type', 'class_id', 'updated_at'
        ]
        read_only_fields = ['id', 'updated_at']


class StudentAnalyticsSerializer(serializers.ModelSerializer):
    """Serializer for student analytics data"""
    student = UserSerializer(read_only=True)
    
    class Meta:
        model = StudentAnalytics
        fields = [
            'id', 'student', 'total_practice_completed', 'total_assignments_completed',
            'average_score', 'current_streak', 'longest_streak', 'total_time_spent',
            'last_activity', 'performance_trend', 'concept_mastery', 'updated_at'
        ]
        read_only_fields = ['id', 'updated_at']


class PracticeQuestionSerializer(serializers.ModelSerializer):
    """Serializer for practice questions (using unified Question model)"""
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Question
        fields = [
            'id', 'title', 'description', 'difficulty', 'category',
            'test_cases', 'starter_code', 'point_value', 'created_by',
            'is_active', 'created_at', 'updated_at', 'config', 'question_type'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if not ret.get('starter_code'):
            config = instance.config or {}
            entry_point = config.get('entry_point')
            if entry_point:
                ret['starter_code'] = (
                    f"# Write your solution below\n"
                    f"# The function '{entry_point}' will be called with the test case inputs.\n"
                    f"def {entry_point}():\n"
                    f"    pass\n"
                )
            else:
                ret['starter_code'] = "# Write your solution below\n"
        return ret



class PracticeQuestionLibrarySerializer(serializers.ModelSerializer):
    """Serializer for practice question library entries"""
    question = PracticeQuestionSerializer(read_only=True)
    
    class Meta:
        model = PracticeQuestionLibrary
        fields = ['id', 'question', 'is_public', 'tags', 'created_at']
        read_only_fields = ['id', 'created_at']


class PracticeSubmissionSerializer(serializers.ModelSerializer):
    """Serializer for practice submissions with question details"""
    student = serializers.PrimaryKeyRelatedField(read_only=True)
    question_title = serializers.CharField(source='question.title', read_only=True)
    question_difficulty = serializers.CharField(source='question.difficulty', read_only=True)
    
    class Meta:
        model = PracticeSubmission
        fields = [
            'id', 'student', 'question', 'question_title',
            'question_difficulty', 'source_code', 'language', 'status',
            'test_results', 'points_earned', 'attempt_number', 'execution_time_ms',
            'submitted_at'
        ]
        read_only_fields = ['id', 'submitted_at']


class PracticeProgressSerializer(serializers.ModelSerializer):
    """Serializer for practice progress tracking"""
    student = UserSerializer(read_only=True)
    question_title = serializers.CharField(source='question.title', read_only=True)
    question_difficulty = serializers.CharField(source='question.difficulty', read_only=True)
    
    class Meta:
        model = PracticeProgress
        fields = [
            'id', 'student', 'question', 'question_title',
            'question_difficulty', 'is_completed', 'attempts_count',
            'best_score', 'time_spent', 'first_attempt_at', 'completed_at',
            'last_updated'
        ]
        read_only_fields = ['id', 'first_attempt_at', 'last_updated']


class PointsHistorySerializer(serializers.Serializer):
    """Serializer for points earning history"""
    date = serializers.DateTimeField()
    points = serializers.IntegerField()
    type = serializers.CharField()  # 'practice' or 'assignment'
    source = serializers.CharField()  # Question title or assignment name
    difficulty = serializers.CharField(required=False)


class LeaderboardRankingSerializer(serializers.Serializer):
    """Serializer for leaderboard ranking data"""
    rank = serializers.IntegerField()
    user = UserSerializer()
    total_points = serializers.IntegerField()
    completed_problems = serializers.IntegerField()


class UserRankSerializer(serializers.Serializer):
    """Serializer for user rank information"""
    current_rank = serializers.IntegerField(allow_null=True)
    total_points = serializers.IntegerField()
    nearby_users = LeaderboardRankingSerializer(many=True)


class PerformanceTrendSerializer(serializers.Serializer):
    """Serializer for performance trend data"""
    date = serializers.DateField()
    submissions = serializers.IntegerField()
    success_rate = serializers.FloatField()
    points_earned = serializers.IntegerField()


class ClassStatsSerializer(serializers.Serializer):
    """Serializer for class-wide statistics"""
    total_students = serializers.IntegerField()
    active_students = serializers.IntegerField()
    engagement_rate = serializers.FloatField()


class RecentActivitySerializer(serializers.Serializer):
    """Serializer for recent activity data"""
    student = serializers.CharField()
    question = serializers.CharField()
    points = serializers.IntegerField()
    submitted_at = serializers.DateTimeField()


class DashboardAnalyticsSerializer(serializers.Serializer):
    """Serializer for student dashboard analytics"""
    analytics = StudentAnalyticsSerializer()
    points = serializers.DictField()
    rank = UserRankSerializer()
    recent_activity = serializers.ListField(child=serializers.DictField())


class ClassOverviewSerializer(serializers.Serializer):
    """Serializer for class overview analytics"""
    class_stats = ClassStatsSerializer()
    top_performers = LeaderboardRankingSerializer(many=True)
    recent_activity = RecentActivitySerializer(many=True)