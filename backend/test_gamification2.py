import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from submissions.models import GradebookEntry
from submissions.serializers import GradebookEntrySerializer
from gamification.models import StudentAnalytics, UserPoints
from gamification.points_calculator import get_top_users_by_points
from classes.models import Class
from django.db.models import Avg
from gamification.views import LeaderboardViewSet, AnalyticsViewSet
from rest_framework.test import APIRequestFactory

User = get_user_model()
student = User.objects.filter(role='student').first()

print("--- 1. Class Comparison Test ---")
try:
    enrolled_class_ids = Class.objects.filter(
        enrollments__user=student,
        enrollments__role='student'
    ).values_list('id', flat=True)
    
    if enrolled_class_ids.exists():
        # Using points instead of analytics
        student_pts = getattr(student, 'points', None)
        student_avg = student_pts.total_points if student_pts else 0
        print(f"Student Pts: {student_avg}")
        
        classmates = User.objects.filter(
            enrollments__class_obj_id__in=enrolled_class_ids,
            enrollments__role='student'
        ).distinct()
        
        class_avg = UserPoints.objects.filter(
            user__in=classmates
        ).aggregate(avg=Avg('total_points')).get('avg') or 0
        print(f"Class Avg: {class_avg}")
        
except Exception as e:
    print(f"EXCEPTION in Class Comparison: {e}")

print("\n--- 2. GradebookEntrySerializer Test ---")
try:
    gb = GradebookEntry.objects.filter(student=student).first()
    if gb:
        sz = GradebookEntrySerializer(gb)
        print(f"Serialized Data for content_item_type: {sz.data.get('content_item_type', 'NOT_FOUND')}")
    else:
        print("No GradebookEntry found for student.")
except Exception as e:
    print(f"EXCEPTION in Serializer test: {e}")

print("\n--- 3. Leaderboard Test ---")
try:
    factory = APIRequestFactory()
    request = factory.get('/api/gamification/leaderboard/')
    view = LeaderboardViewSet.as_view({'get': 'list'})
    response = view(request)
    print(f"Leaderboard API response keys: {response.data.keys()}")
    if 'leaderboard' in response.data:
        items = response.data['leaderboard']
        print(f"First item: {items[0] if items else 'Empty array'}")
    else:
        print(f"Actual payload: {response.data}")
except Exception as e:
    print(f"EXCEPTION in Leaderboard API test: {e}")

