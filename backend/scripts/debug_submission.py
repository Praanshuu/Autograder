import os
import sys
import django

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autograder.settings")
django.setup()

from django.contrib.auth import get_user_model
from assignments.models import Assignment, Question
from submissions.models import Submission

User = get_user_model()

def run():
    print("Debugging Submission Creation...")
    student = User.objects.filter(role='student').first()
    teacher = User.objects.filter(role='teacher').first()
    assign = Assignment.objects.first()
    
    if not student:
        print("No student found!")
        return
    if not assign: 
        print("No assignments found!")
        return
        
    # Check question via Relation
    question = assign.questions.first()
    if not question:
        print("No questions found for assignment!")
        
        # Try generic question query
        q = Question.objects.first()
        if q: print(f"Found orphaned question: {q}")
        return
        
    print(f"Student: {student.username}, Assign: {assign.title}, Q: {question.title}")
    
    try:
        sub = Submission.objects.create(
            assignment=assign,
            question=question,
            student=student,
            status='graded',
            final_score=99,
            is_graded=True,
            is_published=True,
            grader=teacher,
            code_content='// debug'
        )
        print(f"Success! Created submission: {sub.id}")
    except Exception as e:
        print(f"ERROR: {e}")
        # Print full validation errors if ValidationError
        if hasattr(e, 'message_dict'):
            print(f"Validation Details: {e.message_dict}")

if __name__ == '__main__':
    run()
