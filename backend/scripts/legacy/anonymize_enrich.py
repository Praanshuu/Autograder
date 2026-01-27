import os
import sys
import django
import random
from faker import Faker

# Setup Django Environment
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autograder.settings")
django.setup()

from django.contrib.auth import get_user_model
from submissions.models import Submission
from assignments.models import Assignment

from django.db import transaction

User = get_user_model()
fake = Faker()

def run():
    print("Starting Anonymization and Enrichment...")
    with transaction.atomic():
        _run_inner()

def _run_inner():
    # 1. Anonymize Students
    students = User.objects.filter(role='student')
    print(f"Anonymizing {students.count()} students...")
    
    for i, student in enumerate(students):
        # Generate fake identity
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = f"student_{student.id}"
        email = f"student_{student.id}@example.com"
        
        student.first_name = first_name
        student.last_name = last_name
        student.username = username
        student.email = email
        student.save()
        
    print("Students anonymized.")

    # 2. Enrich Submissions
    submissions = Submission.objects.all()
    print(f"Enriching {submissions.count()} submissions with mock analytics data...")
    
    # Common feedback tags
    tags_pool = [
        "Logic Error", "Syntax Optimization", "Clean Code", 
        "Efficiency", "Memory Leak", "Edge Case Missed", 
        "Perfect", "Great Variable Names", "Redundant Code"
    ]

    count = 0
    for sub in submissions:
        score = sub.final_score
        
        # Mock Time Spent (correlated with score slightly?)
        # Low score might mean low effort OR huge effort but stuck
        # Let's just randomise 10 - 120 mins
        sub.time_spent = random.randint(10, 120)
        
        # Mock Feedback Tags
        # High score -> Positive tags
        # Low score -> Negative tags
        if score >= 90:
            user_tags = random.sample(["Perfect", "Great Variable Names", "Clean Code", "Efficiency"], k=random.randint(1, 2))
        elif score >= 70:
            user_tags = random.sample(["Clean Code", "Efficiency", "Logic Error"], k=random.randint(1, 2))
        else:
            user_tags = random.sample(["Logic Error", "Memory Leak", "Edge Case Missed", "Redundant Code"], k=random.randint(1, 3))
            
        sub.feedback_tags = ",".join(user_tags)
        
        # Populate auto_grade_score if 0 (assume it matches final for now)
        if sub.auto_grade_score == 0:
            sub.auto_grade_score = score
            
        sub.save()
        count += 1
        
        if count % 500 == 0:
            print(f"Processed {count} submissions...")

    print("Data enrichment complete!")

if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        print(f"Error: {e}")
