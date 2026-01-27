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

User = get_user_model()

def fix_ownership():
    print("Fixing teacher ownership/enrollment...")
    
    # 1. Get all teachers
    teachers = User.objects.filter(role='teacher')
    print(f"Found {teachers.count()} teachers.")
    
    all_classes = Class.objects.all()
    print(f"Found {all_classes.count()} classes.")

    for teacher in teachers:
        print(f"\nProcessing Teacher: {teacher.username} (ID: {teacher.id})")
        for cls in all_classes:
            # Ensure enrollment exists
            enrollment, created = Enrollment.objects.get_or_create(
                class_obj=cls,
                user=teacher,
                defaults={'role': 'teacher', 'status': 'active'}
            )
            if created:
                print(f" -> Enrolled in {cls.name}")
            else:
                if enrollment.status != 'active':
                    enrollment.status = 'active'
                    enrollment.save()
                    print(f" -> Reactivated enrollment in {cls.name}")
                else:
                    print(f" -> Already active in {cls.name}")

    print("\nDone. All teachers should see all classes now.")

if __name__ == "__main__":
    fix_ownership()
