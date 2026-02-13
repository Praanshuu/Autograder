import requests
import json

# Login to get token (assuming simple login or just use a known token/session if possible, 
# but here I'll try to just hit the endpoint if I can mock auth or if I have a token)
# Since I don't have a token handy, I will rely on the fact that I can't easily curl without auth in this environment 
# unless I use the Django shell.

# Using Django Shell is better.
import os
import django
import sys

sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from submissions.views import SubmissionAttemptViewSet
from submissions.models import SubmissionAttempt
from rest_framework.test import APIRequestFactory

def verify_analytics():
    # Find a submission with a failure (status='fail') if possible, or just any submission
    # We need to see if serializer includes error_message
    
    # Get latest failed submission attempt
    attempt = SubmissionAttempt.objects.filter(status='fail').first()
    if not attempt:
        print("No failed attempts found to verify error_message.")
        return

    # Check serializer directly
    from submissions.serializers import SubmissionAnalyticsSerializer
    
    # Wrap in list as the view does many=True
    serializer = SubmissionAnalyticsSerializer([attempt], many=True)
    data = serializer.data
    
    print("Serialized Data (First Item):")
    print(json.dumps(data[0], indent=2))
    
    # Verify field existence
    test_results = data[0].get('test_results', [])
    if test_results:
        first_res = test_results[0]
        if 'error_message' in first_res:
            print(f"\nSUCCESS: 'error_message' is present in test_results. Value: {first_res['error_message']}")
        else:
            print("\nFAILURE: 'error_message' NOT found in test_results.")
    else:
        print("\nNo test results in this attempt.")

if __name__ == "__main__":
    verify_analytics()
