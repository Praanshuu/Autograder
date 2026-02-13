import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from assignments.models import Question, Assignment, AssignmentQuestion
from classes.models import Class, Enrollment, Module
from submissions.models import SubmissionAttempt
from rest_framework.test import APIRequestFactory
from classes.views import ClassViewSet

User = get_user_model()

def setup_and_test():
    print("Setting up test data...")
    
    # 1. Create Teacher and Student
    teacher, _ = User.objects.get_or_create(username='verify_teacher', defaults={'email': 'teacher@test.com', 'role': 'teacher'})
    student, _ = User.objects.get_or_create(username='verify_student', defaults={'email': 'student@test.com', 'role': 'student'})
    
    # 2. Create Class
    cls, _ = Class.objects.get_or_create(name='Verify Topic Class', owner=teacher, defaults={'section': 'A'})
    Enrollment.objects.get_or_create(class_obj=cls, user=student, role='student')
    
    # 3. Create Module
    module, _ = Module.objects.get_or_create(class_obj=cls, title='Topic Module')
    
    # 4. Create Assignment
    assignment, _ = Assignment.objects.get_or_create(
        title='Topic Assignment',
        module=module,
        defaults={'points_total': 100, 'type': 'assignment'}
    )
    
    # 5. Create Questions with Tags
    q1, _ = Question.objects.get_or_create(
        title='Loop Q', 
        slug='loop-q', 
        created_by=teacher,
        defaults={
            'description': 'Loop test',
            'tags': ['Loops', 'Basic']
        }
    )
    # Update tags just in case
    q1.tags = ['Loops', 'Basic']
    q1.save()
    
    q2, _ = Question.objects.get_or_create(
        title='Array Q', 
        slug='array-q',
        created_by=teacher,
        defaults={
            'description': 'Array test',
            'tags': ['Arrays', 'Basic']
        }
    )
    q2.tags = ['Arrays', 'Basic']
    q2.save()
    
    # 6. Link to Assignment
    aq1, _ = AssignmentQuestion.objects.get_or_create(assignment=assignment, question=q1, order=1)
    aq2, _ = AssignmentQuestion.objects.get_or_create(assignment=assignment, question=q2, order=2)
    
    # 7. Create Submissions
    # Success on Loops (100%)
    SubmissionAttempt.objects.create(
        student=student, 
        assignment_question=aq1, 
        status='success', 
        attempt_number=1
    )
    
    # Fail on Arrays (0%)
    SubmissionAttempt.objects.create(
        student=student,
        assignment_question=aq2,
        status='fail',
        attempt_number=1
    )
    
    print("Data setup complete.")
    
    # 8. Call View Method directly
    print("Testing 'student_topic_grades' logic...")
    factory = APIRequestFactory()
    request = factory.get(f'/classes/{cls.id}/student-topic-grades/?student_id={student.id}')
    
    from rest_framework.test import force_authenticate
    force_authenticate(request, user=teacher)
    
    view = ClassViewSet.as_view({'get': 'student_topic_grades'})
    response = view(request, pk=cls.id)
    
    print(f"Response Status: {response.status_code}")
    print(f"Response Data: {json.dumps(response.data, indent=2)}")
    
    # Verification
    # Expected: 
    # Loops: 100 (1 question)
    # Arrays: 0 (1 question)
    # Basic: (100 + 0) / 2 = 50 (2 questions)
    
    data = response.data
    loops = next((item for item in data if item['topic'] == 'Loops'), None)
    arrays = next((item for item in data if item['topic'] == 'Arrays'), None)
    basic = next((item for item in data if item['topic'] == 'Basic'), None)
    
    if loops and loops['score'] == 100 and loops['questions_count'] == 1:
        print("✅ Loops Check Passed")
    else:
        print(f"❌ Loops Check Failed: {loops}")
        
    if arrays and arrays['score'] == 0 and arrays['questions_count'] == 1:
        print("✅ Arrays Check Passed")
    else:
        print(f"❌ Arrays Check Failed: {arrays}")

    if basic and basic['score'] == 50 and basic['questions_count'] == 2:
        print("✅ Basic Check Passed")
    else:
        print(f"❌ Basic Check Failed: {basic}")

if __name__ == '__main__':
    try:
        setup_and_test()
    except Exception as e:
        print(f"An error occurred: {e}")
