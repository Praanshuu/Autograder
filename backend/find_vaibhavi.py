import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username_query = 'vaibhavi'

# Try exact match first
try:
    user = User.objects.get(username=username_query)
    print(f"User found: {user.username} (ID: {user.id})")
except User.DoesNotExist:
    # Try partial match
    users = User.objects.filter(username__icontains=username_query)
    if users.exists():
        user = users.first()
        print(f"Partial match found: {user.username} (ID: {user.id})")
    else:
        print("User not found. Creating new user...")
        user = User.objects.create_user(
            username='vaibhavi',
            email='vaibhavi@student.com',
            password='vaibhavi123',
            first_name='Vaibhavi',
            last_name='Student',
            role='student'
        )
        print(f"Created user: {user.username}")

# Reset Password just in case
if user:
    user.set_password('vaibhavi123')
    user.save()
    print(f"Password set to 'vaibhavi123' for user: {user.username}")
