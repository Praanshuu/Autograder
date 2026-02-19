import os
import django
import sys
import json
from django.conf import settings

sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from classes.models import Class, Module
from assignments.models import Assignment, Question, AssignmentQuestion, Assignment
from submissions.models import SubmissionAttempt

User = get_user_model()

def run():
    print("🚀 Starting reproduction script...")
    
    # 1. Setup Data
    user, _ = User.objects.get_or_create(username="crash_tester", defaults={'email': 'crash@test.com'})
    student, _ = User.objects.get_or_create(username="student_crash", defaults={'email': 'student_crash@test.com', 'role': 'student'})
    
    print(f"User: {student.username}")
    
    # Create Class & Assignment
    c, _ = Class.objects.get_or_create(name="CrashClass", owner=user)
    m, _ = Module.objects.get_or_create(class_obj=c, title="CrashModule")
    
    assign, _ = Assignment.objects.get_or_create(
        module=m, 
        title="Crash Assignment",
        defaults={
            'description': 'Test assignment to crash the view',
            'points_total': 100,
            'type': 'assignment'
        }
    )
    
    # Question WITH CONFIG needed for Batch Runner
    q_config = {
        'timeout': 2,
        'language': 'python',
        # 'entry_point': 'solution',  <-- REMOVED
        # 'execution_mode': {'type': 'function', 'entry_point': 'solution'} <-- REMOVED
    }
    
    q, _ = Question.objects.get_or_create(
        slug="crash-q-1",
        defaults={
            'title': 'Crash Question',
            'config': q_config,
            'created_by': user,
            'test_cases': [
                {'input': 'hello', 'expected_output': 'hello', 'name': 'test1'}
            ]
        }
    )
    # Force update config
    q.config = q_config
    q.save()
        
    aq, _ = AssignmentQuestion.objects.get_or_create(
        assignment=assign, 
        question=q, 
        defaults={'order': 1}
    )
    
    print(f"Assignment Question ID: {aq.id}")
    
    # 2. Simulate Submission Request
    client = APIClient()
    client.force_authenticate(user=student)
    
    payload = {
        'assignment_id': str(assign.id),
        'assignment_question_id': str(aq.id),
        'question_id': str(q.id),
        'code_content': "def solution(x): return x",
        'language': 'python',
        'time_spent': 10
    }
    
    print("📡 Sending POST request to /api/v1/submissions/attempts/ ...")
    
    # Check URLconf for correct path. 
    # In api.js: SUBMISSIONS: { LIST: '/submissions/attempts/' }
    # So POST to /api/v1/submissions/attempts/
    
    url = '/api/submissions/attempts/'
    
    try:
        response = client.post(url, payload, format='json')
        print(f"Response Status: {response.status_code}")
        
        if response.status_code == 500:
            print("❌ Captured 500 Error!")
            print(json.dumps(response.data, indent=2))
        elif response.status_code == 201:
            print("✅ Submission Successful!")
            print(json.dumps(response.data, indent=2))
        else:
            print(f"⚠️ Unexpected Status: {response.status_code}")
            print(response.content)
            
    except Exception as e:
        print(f"❌ Client failed: {e}")

if __name__ == "__main__":
    run()
