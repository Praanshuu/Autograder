import os
import django
import sys
import uuid
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.test import RequestFactory
from rest_framework.test import force_authenticate
from submissions.views import SubmissionAttemptViewSet
from assignments.models import Assignment, Question, AssignmentQuestion
from users.models import User
from submissions.models import SubmissionAttempt

user, _ = User.objects.get_or_create(username='teststudent2', email='test2@example.com')

assignment_uuid = uuid.uuid4()
assignment, _ = Assignment.objects.get_or_create(id=assignment_uuid, title="Test Assgn2", type="assignment")

question, _ = Question.objects.get_or_create(title="q2", description="desc", difficulty="easy", type="coding",
    config={"execution_mode": {"type": "program"}},
    test_cases=[{"input": "5", "expected_output": "10"}])
    
aq, _ = AssignmentQuestion.objects.get_or_create(assignment=assignment, question=question, custom_points=10)

factory = RequestFactory()
request = factory.post(f'/api/submissions/submit/{aq.id}/', {
    'code': "for i in range n:\n  pass",
    'language': 'python',
}, content_type='application/json')

force_authenticate(request, user=user)
view = SubmissionAttemptViewSet.as_view({'post': 'submit'})
response = view(request, assignment_question_id=aq.id)

print("API SUBMIT RESPONSE STATUS:", response.status_code)
print("API SUBMIT DATA:", response.data)
