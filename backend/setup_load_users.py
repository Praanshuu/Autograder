import os
import sys
import django

sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from classes.models import Enrollment, Class

User = get_user_model()

# Get a class to enroll them in (CSL100-CS)
try:
    c = Class.objects.filter(name__icontains='CSL100-CS').first() # Or CSL100-CS
    if not c:
        c = Class.objects.first()
    print(f"Enrolling students in {c.name}")
except:
    print("No class found. Creating one.")
    # Assuming valid teacher exists or handled
    pass

count = 0
for i in range(1, 101):
    username = f"B25CS{str(i).zfill(3)}"
    u, created = User.objects.get_or_create(username=username)
    u.set_password(username)
    u.role = 'student'
    u.save()
    
    if c:
        Enrollment.objects.get_or_create(user=u, class_obj=c, defaults={'role': 'student'})
        
    print(f"User {u.username} ready.")
    count += 1
    
print(f"Setup {count} users.")
