"""
URL patterns for gamification API endpoints.

This module defines the URL routing for:
- Points and scoring endpoints
- Achievement tracking endpoints
- Leaderboard endpoints
- Analytics endpoints
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PracticeQuestionViewSet, PracticeSubmissionViewSet, PracticeProgressViewSet,
    PracticeQuestionLibraryViewSet, PracticeAnalyticsViewSet,
    PointsViewSet, AchievementViewSet, LeaderboardViewSet, AnalyticsViewSet
)

# Create router and register viewsets
router = DefaultRouter()
router.register(r'practice-questions', PracticeQuestionViewSet, basename='practice-questions')
router.register(r'practice-submissions', PracticeSubmissionViewSet, basename='practice-submissions')
router.register(r'practice-progress', PracticeProgressViewSet, basename='practice-progress')
router.register(r'practice-library', PracticeQuestionLibraryViewSet, basename='practice-library')
router.register(r'practice-analytics', PracticeAnalyticsViewSet, basename='practice-analytics')
router.register(r'points', PointsViewSet, basename='points')
router.register(r'achievements', AchievementViewSet, basename='achievements')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'analytics', AnalyticsViewSet, basename='analytics')

urlpatterns = [
    path('', include(router.urls)),
]