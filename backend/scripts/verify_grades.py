import os
import django
import sys

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from classes.models import Class, Enrollment
from django.contrib.auth import get_user_model
from submissions.models import Submission
from assignments.models import Assignment

User = get_user_model()

def test_grades_query():
    print("Testing grades query logic...")
    try:
        # Get first class
        class_obj = Class.objects.first()
        if not class_obj:
            print("No classes found. Please create one.")
            return

        print(f"Class: {class_obj.name}")

        # 1. Assignments
        assignments = class_obj.assignments.all().order_by('created_at')
        assign_data = [{'id': a.id, 'title': a.title, 'points': a.points} for a in assignments]
        print(f"Assignments count: {len(assign_data)}")

        # 2. Students
        students = User.objects.filter(
            enrollments__class_obj=class_obj,
            enrollments__role='student',
            enrollments__status='active'
        ).distinct().order_by('last_name', 'first_name')
        print(f"Students count: {len(students)}")

        # 3. Submissions
        submissions = Submission.objects.filter(
            assignment__class_obj=class_obj
        ).values('student_id', 'assignment_id', 'final_score', 'status')
        print(f"Submissions count: {len(submissions)}")
        
        # Test serialization structure
        grades_map = {}
        for sub in submissions:
            s_id = sub['student_id']
            a_id = sub['assignment_id']
            if s_id not in grades_map: grades_map[s_id] = {}
            grades_map[s_id][a_id] = sub['final_score']

        roster = []
        for student in students:
            student_grades = grades_map.get(student.id, {})
            roster.append({
                'id': student.id,
                'name': f"{student.first_name} {student.last_name}",
                'email': student.email,
                'grades': student_grades
            })
        print("Roster constructed successfully.")
        print("Sample student:", roster[0] if roster else "None")

    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_grades_query()
