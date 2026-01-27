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

def inspect_classes():
    print("--- Users ---")
    users = User.objects.all()
    for u in users:
        print(f"ID: {u.id} | {u.email} | Role: {u.role}")

    print("\n--- Classes ---")
    classes = Class.objects.all()
    if not classes:
        print("No classes found in DB.")
    for c in classes:
        print(f"ID: {c.id} | Name: {c.name} | Owner: {c.owner.email} (ID: {c.owner.id})")

    print("\n--- Enrollments (Teacher) ---")
    enrollments = Enrollment.objects.filter(role='teacher')
    if not enrollments:
        print("No teacher enrollments found.")
    for e in enrollments:
        print(f"User: {e.user.email} -> Class: {e.class_obj.name} (Status: {e.status})")

if __name__ == "__main__":
    inspect_classes()
