import os
import sys
import django
from django.conf import settings
# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autograder.settings")
django.setup()

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from analytics.views import AnalyticsViewSet
import submissions.views
print("submissions.views file:", submissions.views.__file__)
from submissions.views import SubmissionAttemptViewSet
from assignments.models import Assignment
from django.contrib.auth import get_user_model

User = get_user_model()
ASSIGNMENT_ID = "1474b14a-7944-4486-a21e-a85420c9710c"

def verify():
    print(f"Verifying data for Assignment ID: {ASSIGNMENT_ID}")
    
    try:
        assignment = Assignment.objects.get(id=ASSIGNMENT_ID)
    except Assignment.DoesNotExist:
        print("Assignment not found.")
        return

    class_obj = assignment.module.class_obj
    enrolled_count = User.objects.filter(enrollments__class_obj=class_obj, enrollments__role='student').count()
    print(f"Total Enrolled Students: {enrolled_count}")

    # Test Performance Matrix
    factory = APIRequestFactory()
    request = factory.get(f'/analytics/performance-matrix/?assignment_id={ASSIGNMENT_ID}')
    view = AnalyticsViewSet.as_view({'get': 'performance_matrix'})
    
    # Authenticate
    teacher = User.objects.filter(role='teacher').first()
    if not teacher:
        teacher = User.objects.create(username='teacher', role='teacher')
    from rest_framework.test import force_authenticate
    force_authenticate(request, user=teacher)

    response = view(request)
    
    if response.status_code != 200:
        print(f"Performance Matrix Failed: {response.status_code}")
        print(response.data)
    else:
        data = response.data['data']
        print(f"Performance Matrix Rows: {len(data)}")
        if len(data) == enrolled_count:
            print("PASS: Performance Matrix includes all enrolled students.")
        else:
            print(f"FAIL: Performance Matrix missing students. Expected {enrolled_count}, got {len(data)}")

    # Test Assignment Summary
    request = factory.get(f'/submissions/summary/?assignment_id={ASSIGNMENT_ID}')
    view = SubmissionAttemptViewSet.as_view({'get': 'get_assignment_summary'})
    force_authenticate(request, user=teacher)
    
    print("SubmissionAttemptViewSet methods:", [m for m in dir(SubmissionAttemptViewSet) if 'summary' in m])
    
    # Check if view has the method
    if not hasattr(SubmissionAttemptViewSet, 'get_assignment_summary'):
        print("ERROR: SubmissionAttemptViewSet missing 'get_assignment_summary'")
    else:
        try:
            response = view(request)
            if response.status_code != 200:
                print(f"Assignment Summary Failed: {response.status_code}")
                if hasattr(response, 'data'): print(response.data)
            else:
                data = response.data
                print(f"Assignment Summary Rows: {len(data)}")
                if len(data) == enrolled_count:
                    print("PASS: Assignment Summary includes all enrolled students.")
                else:
                    print(f"FAIL: Assignment Summary missing students. Expected {enrolled_count}, got {len(data)}")
        except Exception as e:
            print(f"Assignment Summary Crash: {e}")

if __name__ == "__main__":
    verify()
