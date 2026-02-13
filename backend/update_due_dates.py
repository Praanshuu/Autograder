
import os
import sys
import django
from datetime import timedelta
from django.utils import timezone

# Setup Django Environment
sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from assignments.models import Assignment

def update_dates():
    print("Updating assignment due dates to the past (December 2025)...")
    
    # Target assignments
    assignments = Assignment.objects.filter(title="Practice Sheet - Whole Syllabus")
    
    if not assignments.exists():
        print("No assignments found with title 'Practice Sheet - Whole Syllabus'")
        return

    # Set date to Dec 15, 2025
    # Calculate offset from now (Feb 2026) -> Dec 2025 is approx 60 days ago
    past_date = timezone.now() - timedelta(days=60)
    
    count = 0
    for assign in assignments:
        assign.due_date = past_date
        assign.save()
        print(f"Updated '{assign.title}' (ID: {assign.id}) due date to {past_date}")
        count += 1
        
    print(f"Successfully updated {count} assignments.")

if __name__ == '__main__':
    update_dates()
