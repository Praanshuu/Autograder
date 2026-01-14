import os
import sys
import django

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def run():
    print("--- Resetting Teacher Password ---")
    try:
        user = User.objects.get(username='teacher')
        user.set_password('password')
        user.save()
        print(f"SUCCESS: Password for '{user.username}' (ID: {user.id}) has been set to 'password'.")
        print(f"Role: {user.role}")
        print(f"Is Active: {user.is_active}")
    except User.DoesNotExist:
        print("ERROR: User 'teacher' does not exist! Creating it now...")
        user = User.objects.create_user(username='teacher', email='teacher@test.com', password='password')
        user.role = 'teacher'
        user.save()
        print("CREATED: User 'teacher' created with password 'password'.")

if __name__ == "__main__":
    run()
