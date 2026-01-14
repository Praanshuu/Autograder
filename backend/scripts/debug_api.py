import os
import sys
import django
import json

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from submissions.models import Submission
from submissions.serializers import SubmissionSerializer
from rest_framework import serializers

def debug_api():
    print("--- Debugging Serialization ---")
    
    # Get one submission
    sub = Submission.objects.first()
    if not sub:
        print("No submissions found.")
        return

    print(f"Submission ID: {sub.id}")
    print(f"Question ID (Database): {sub.question.id}")
    
    serializer = SubmissionSerializer(sub)
    data = serializer.data
    
    print("\n--- Serialized Data (Question Field) ---")
    # Pretty print the 'question' field specifically
    print(json.dumps(data.get('question'), indent=4))
    
    print("\n--- Enrichment Data ---")
    print(f"Time Spent: {data.get('time_spent')}")
    print(f"Feedback Tags: {data.get('feedback_tags')}")
    print(f"Final Score: {data.get('final_score')}")
    
    print("\n--- Full Data Keys ---")
    print(list(data.keys()))

if __name__ == "__main__":
    debug_api()
