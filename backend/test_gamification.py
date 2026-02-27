import os
import django
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.test import RequestFactory
from rest_framework.test import force_authenticate
from gamification.views import PracticeQuestionViewSet
from gamification.models import PracticeQuestion
from assignments.models import Question
from users.models import User

user, _ = User.objects.get_or_create(username='teststudent', email='test@example.com')
pq, _ = PracticeQuestion.objects.get_or_create(
    title='Syntax Error Test',
    description='test syntax',
    difficulty='easy',
    points=50,
    test_cases=[{'input': '5', 'expected_output': '10'}]
)

factory = RequestFactory()
request = factory.post(f'/api/gamification/practice/{pq.id}/submit/', {
    'code': "for i in range n:\n  pass",
    'language': 'python'
}, content_type='application/json')

force_authenticate(request, user=user)
view = PracticeQuestionViewSet.as_view({'post': 'submit'})
response = view(request, pk=pq.id)

print("API SUBMIT RESPONSE DATA:", response.data)
