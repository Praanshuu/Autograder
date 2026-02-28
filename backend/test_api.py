import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User = get_user_model()
client = APIClient()
user = User.objects.first()
client.force_authenticate(user=user)

response = client.get('/api/gamification/practice-library/')
print("Status:", response.status_code)
if 'results' in response.data:
    data = response.data['results']
else:
    data = response.data

print("Count:", len(data))
if len(data) > 0:
    print("Keys of first item:", data[0].keys())
    if 'question' in data[0]:
        print("Keys of nested question:", data[0]['question'].keys())
