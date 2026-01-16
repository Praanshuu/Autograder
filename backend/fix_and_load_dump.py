#!/usr/bin/env python3
import os
import sys
import django
import json

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()

def load_users_from_dump():
    """Load only user data from the corrupted dump file"""
    print("Reading db_dump.json...")
    
    with open('db_dump.json', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Parse as much as we can
    # Try to fix the JSON by finding where it breaks
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"JSON error at position {e.pos}, trying to salvage...")
        # Take only the valid part
        content = content[:e.pos]
        # Try to close the array
        content = content.rstrip().rstrip(',') + '\n]'
        try:
            data = json.loads(content)
        except:
            print("Could not fix JSON, trying alternative method...")
            data = []
    
    # Filter only user records
    user_records = [d for d in data if d.get('model') == 'users.user']
    print(f"Found {len(user_records)} user records")
    
    users_created = 0
    users_updated = 0
    
    with transaction.atomic():
        for user_data in user_records:
            try:
                fields = user_data['fields']
                username = fields['username']
                
                # Skip if user already exists with correct data
                user, created = User.objects.get_or_create(
                    username=username,
                    defaults={
                        'email': fields.get('email', f'{username}@example.com'),
                        'first_name': fields.get('first_name', ''),
                        'last_name': fields.get('last_name', ''),
                        'role': fields.get('role', 'student'),
                        'is_active': fields.get('is_active', True),
                        'is_staff': fields.get('is_staff', False),
                        'is_superuser': fields.get('is_superuser', False),
                    }
                )
                
                # Set the hashed password from dump
                if 'password' in fields:
                    user.password = fields['password']
                    user.save()
                
                if created:
                    users_created += 1
                    if users_created <= 5:
                        print(f"  Created: {username}")
                else:
                    users_updated += 1
                    
            except Exception as e:
                print(f"Error processing user {username}: {e}")
                continue
    
    print(f"\nDone!")
    print(f"  Created: {users_created} users")
    print(f"  Updated: {users_updated} users")
    print(f"  Total users in DB: {User.objects.count()}")

if __name__ == '__main__':
    load_users_from_dump()
