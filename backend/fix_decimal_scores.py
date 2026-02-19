import os
import sys
import django

# Setup Django Environment
sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from submissions.models import SubmissionAttempt

def run():
    print("Rounding decimal scores to integers...")
    attempts = SubmissionAttempt.objects.filter(manual_score__isnull=False)
    count = 0
    for attempt in attempts:
        if attempt.manual_score % 1 != 0:
            attempt.manual_score = round(attempt.manual_score)
            attempt.save()
            count += 1
            
    print(f"Updated {count} submission scores.")

if __name__ == '__main__':
    run()
