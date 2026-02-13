import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
email = 'b25ee003@iitbhilai.ac.in'
username = 'B25EE003'

try:
    # Try getting by email first
    users = User.objects.filter(email__iexact=email)
    if users.exists():
        user = users.first()
        print(f"User found by email: {user.username} (ID: {user.id})")
    else:
        # Try by username
        users = User.objects.filter(username__iexact=username)
        if users.exists():
            user = users.first()
            print(f"User found by username: {user.username} (ID: {user.id})")
        else:
            print("User not found. Creating...")
            user = User.objects.create_user(
                username=username,
                email=email,
                password=username, # Default password is username
                first_name='Student',
                last_name=username
            )
            print(f"Created user: {user.username}")

    # Set password to be sure
    password = username  # Setting password to username for simplicity
    user.set_password(password)
    user.save()
    print(f"Password set to: {password}")

except Exception as e:
    print(f"Error: {e}")
