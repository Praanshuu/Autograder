import os
import django
import sys

# Add backend to path
sys.path.append('/home/anshul/Projects/Autograder/backend')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autograder.settings")
django.setup()

from rest_framework.test import APIRequestFactory, force_authenticate
from classes.views import CommentViewSet
from classes.models import Class, Announcement, Comment, Enrollment
from users.models import User
from classes.serializers import CommentSerializer

# Setup
factory = APIRequestFactory()

def test_add_comment():
    print("Finding a student and announcement...")
    # Find a student enrolled in a class
    enrollment = Enrollment.objects.filter(role='student').first()
    if not enrollment:
        print("No student enrollment found!")
        return

    student = enrollment.user
    class_obj = enrollment.class_obj
    print(f"User: {student.username}, Class: {class_obj.name}")

    # Find or create an announcement
    announcement = Announcement.objects.filter(class_obj=class_obj).first()
    if not announcement:
        print("No announcement found! Creating one...")
        teacher = Class.objects.get(id=class_obj.id).owner
        announcement = Announcement.objects.create(
            class_obj=class_obj,
            author=teacher,
            content="Test Announcement"
        )
    
    print(f"Announcement ID: {announcement.id}")

    # Prepare payload
    payload = {
        'content': 'Test comment from standalone script',
        'announcement': str(announcement.id)
    }
    
    # Test Serializer directly first
    print("\nTesting Serializer...")
    # Mock context with request.user
    class MockRequest:
        user = student
    
    serializer = CommentSerializer(data=payload, context={'request': MockRequest()})
    if serializer.is_valid():
        print("Serializer is valid.")
        try:
            comment = serializer.save()
            print(f"Comment created via serializer: {comment.id} - {comment.content}")
        except Exception as e:
            print(f"Serializer save failed: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"Serializer errors: {serializer.errors}")

    # Test ViewSet (Simulate HTTP Request)
    print("\nTesting ViewSet...")
    view = CommentViewSet.as_view({'post': 'create'})
    request = factory.post('/classes/comments/', payload, format='json')
    force_authenticate(request, user=student)
    
    try:
        response = view(request)
        print(f"Response Status: {response.status_code}")
        print(f"Response Data: {response.data}")
    except Exception as e:
        print(f"ViewSet execution failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_add_comment()
