import os
import sys
import django
from django.contrib.auth import authenticate, get_user_model

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

User = get_user_model()

def verify_student_login():
    print("--- Verifying Student Login ---")
    
    # 1. Start by finding the user by EMAIL
    email = "student_315@example.com"
    student = User.objects.filter(email=email).first()
    
    if not student:
        print(f"CRITICAL: No user found with email {email}")
        return

    print(f"User Found: {student}")
    print(f"  ID: {student.id}")
    print(f"  Username: '{student.username}'")  # This is likely what is needed for login
    print(f"  Email: '{student.email}'")
    print(f"  Role: '{student.role}'")
    
    # 2. Reset Password again just to be 100% sure
    student.set_password('password')
    student.save()
    print("  Password reset to: 'password'")

    # 3. Test Authentication (Standard with USERNAME)
    print("\n--- Testing 'authenticate(username=..., password=...)' ---")
    user_auth = authenticate(username=student.username, password='password')
    if user_auth:
        print(f"SUCCESS: Authenticated using Username: '{student.username}'")
    else:
        print(f"FAILED: Could not authenticate using Username: '{student.username}'")

    # 4. Test Authentication (Using EMAIL as username - unlikely to work unless custom backend)
    print("\n--- Testing 'authenticate(username=EMAIL, password=...)' ---")
    email_auth = authenticate(username=student.email, password='password')
    if email_auth:
        print(f"SUCCESS: Authenticated using Email: '{student.email}'")
    else:
        print(f"FAILED: Could not authenticate using Email: '{student.email}'")

if __name__ == "__main__":
    verify_student_login()
