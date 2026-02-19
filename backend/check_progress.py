import os
import sys
import django
from django.db.models import Count

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autograder.settings")
django.setup()

from django.contrib.auth import get_user_model
from submissions.models import SubmissionAttempt
from gamification.models import UserPoints

User = get_user_model()
ASSIGNMENT_TITLE = "Practice Sheet - Whole Syllabus"

def check():
    print("Checking population progress...")
    
    # Get top student by submission count
    top_submitter = SubmissionAttempt.objects.filter(
        assignment_question__assignment__title=ASSIGNMENT_TITLE
    ).values('student__username').annotate(
        count=Count('id')
    ).order_by('-count').first()
    
    if top_submitter:
        username = top_submitter['student__username']
        count = top_submitter['count']
        print(f"Top Student by Submissions: {username} ({count} submissions)")
        
        # Get points
        try:
            up = UserPoints.objects.get(user__username=username)
            print(f"Points: {up.total_points}")
        except UserPoints.DoesNotExist:
            print("No points record found yet.")
            
        # Reset password for this user
        user = User.objects.get(username=username)
        password = "password123"
        user.set_password(password)
        user.save()
        print(f"Password reset to '{password}' for {username}")
        
    else:
        print("No submissions found yet.")

if __name__ == "__main__":
    check()
