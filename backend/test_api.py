import os
import django
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.test import RequestFactory
from rest_framework.test import force_authenticate
from submissions.views import SubmissionAttemptViewSet
from users.models import User

user, _ = User.objects.get_or_create(username='teststudent', email='test@example.com')

factory = RequestFactory()
request = factory.post('/api/submissions/run/', {
    'code': "for i in range n:\n  pass",
    'language': 'python',
    'test_cases': [{'input': '5', 'expected_output': '10'}]
}, content_type='application/json')

force_authenticate(request, user=user)
view = SubmissionAttemptViewSet.as_view({'post': 'run_code'})
response = view(request)

print("API RESPONSE DATA:", response.data)
