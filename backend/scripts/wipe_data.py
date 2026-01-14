import os
import sys
import django

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autograder.settings")
django.setup()

from django.contrib.auth import get_user_model
from assignments.models import Assignment, Question
from submissions.models import Submission

User = get_user_model()

def run():
    print("Wiping data...")
    # Delete Students
    count, _ = User.objects.filter(role='student').delete()
    print(f"Deleted {count} students.")
    
    # Delete Assignments (cascades to submissions/questions)
    count, _ = Assignment.objects.all().delete()
    print(f"Deleted {count} assignments.")
    
    print("Wipe complete.")

if __name__ == '__main__':
    run()
