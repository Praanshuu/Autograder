import os
import sys
import django

sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
u = User.objects.get(username='Vaishnavi')
u.set_password('Rinvu2-ganqyh-rowbyx')
u.save()
print(f"Password updated for {u.username}")
