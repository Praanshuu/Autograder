import os
import sys
import django

sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from classes.models import Enrollment, Class

User = get_user_model()
try:
    u = User.objects.get(username='Vaishnavi')
    print(f"User: {u.username} (ID: {u.id})")
    
    enrollments = Enrollment.objects.filter(user=u)
    print(f"Enrollments count: {enrollments.count()}")
    for e in enrollments:
        print(f"  - Class: {e.class_obj.name} ({e.class_obj.id}), Role: {e.role}")
        
    owned = Class.objects.filter(owner=u)
    print(f"Owned Classes count: {owned.count()}")
    for c in owned:
        print(f"  - Class: {c.name} ({c.id})")
        
except User.DoesNotExist:
    print("User Vaishnavi not found")
