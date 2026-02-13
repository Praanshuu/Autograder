import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from classes.models import Class
from assignments.models import Assignment

try:
    cros = Class.objects.filter(name__icontains='CSL100')
    if not cros.exists():
        print("No class found with 'CSL100'")
        exit()
        
    cls = cros.first()
    print(f"Class: {cls.name} (ID: {cls.id})")
    
    modules = cls.modules.all()
    for m in modules:
        print(f"\nModule: {m.title}")
        items = m.items.all()
        for item in items:
            if item.type == 'assignment':
                try:
                    assign = Assignment.objects.get(id=item.id)
                    print(f"  Assignment: {assign.title} (ID: {assign.id})")
                    aqs = assign.assignmentquestion_set.all().order_by('order')
                    for aq in aqs:
                        q = aq.question
                        tags = q.tags or []
                        print(f"    - Q: {q.title} [Tags: {tags}]")
                except Assignment.DoesNotExist:
                    print(f"  Assignment ID {item.id} not found in Assignment table")
            else:
                print(f"  Item: {item.title} ({item.type})")

except Exception as e:
    print(f"Error: {e}")
