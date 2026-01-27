import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()

username = 'teacher'
email = 'teacher@example.com'
password = 'password'

if not User.objects.filter(username=username).exists():
    User.objects.create_user(username=username, email=email, password=password, role='teacher', is_staff=True)
    print(f"Created teacher user: {username}")
else:
    u = User.objects.get(username=username)
    u.role = 'teacher'
    u.is_staff = True
    u.set_password(password)
    u.save()
    print(f"Updated existing user {username} to teacher role.")
