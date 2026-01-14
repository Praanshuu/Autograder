import os
import sys
import django
from django.contrib.auth import get_user_model

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

User = get_user_model()

def get_student_login():
    # Find a user who is NOT a teacher and NOT a superuser
    student = User.objects.filter(role='student').first()
    
    if student:
        # Reset password to 'password' to be absolutely sure
        student.set_password('password')
        student.save()
        
        print(f"\n--- Student Credentials ---")
        print(f"Email: {student.email}")
        print(f"Password: password")
        print(f"Name: {student.first_name} {student.last_name}")
        print(f"User ID: {student.id}")
    else:
        print("No student users found.")

if __name__ == "__main__":
    get_student_login()
