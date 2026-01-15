#!/usr/bin/env python3
"""
Database Setup Script
Automatically fixes and loads the database dump file
"""
import os
import sys
import json
import django
from django.core.management import call_command

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

def fix_dump_file():
    """Fix encoding issues and truncate incomplete JSON"""
    print("📁 Reading db_dump.json...")
    
    # Read with error handling
    with open('db_dump.json', 'rb') as f:
        content = f.read()
    
    # Fix encoding issues
    print("🔧 Fixing encoding issues...")
    content = content.replace(b'\x96', b'-')  # Replace en-dash
    content = content.replace(b'\x97', b'-')  # Replace em-dash
    content = content.replace(b'\x93', b'"')  # Replace left quote
    content = content.replace(b'\x94', b'"')  # Replace right quote
    
    # Decode
    content = content.decode('utf-8', errors='ignore')
    
    # Find last complete record
    print("✂️  Truncating to last complete record...")
    last_complete = content.rfind('},\n{')
    if last_complete == -1:
        last_complete = content.rfind('}\n]')
    
    if last_complete != -1:
        content = content[:last_complete + 1] + '\n]'
    
    # Write fixed version
    with open('db_dump_fixed.json', 'w') as f:
        f.write(content)
    
    # Validate
    try:
        with open('db_dump_fixed.json', 'r') as f:
            data = json.load(f)
        
        users = [d for d in data if d.get('model') == 'users.user']
        print(f"✅ Valid JSON with {len(data)} records ({len(users)} users)")
        return True
    except Exception as e:
        print(f"❌ Error validating JSON: {e}")
        return False

def load_database():
    """Load the fixed database dump"""
    print("\n🗑️  Flushing existing database...")
    call_command('flush', interactive=False, verbosity=0)
    
    print("📥 Loading database dump...")
    call_command('loaddata', 'db_dump_fixed.json', verbosity=1)
    
    print("✅ Database loaded successfully!")

def verify_setup():
    """Verify the database is set up correctly"""
    from django.contrib.auth import get_user_model, authenticate
    
    User = get_user_model()
    
    print(f"\n📊 Database Statistics:")
    print(f"   Total users: {User.objects.count()}")
    
    # Test authentication
    print(f"\n🔐 Testing Authentication:")
    test_users = [
        ('student_315', 'password'),
        ('teacher', 'password'),
        ('Sharingan', 'testpass123'),
    ]
    
    for username, password in test_users:
        user = authenticate(username=username, password=password)
        status = '✅' if user else '❌'
        print(f"   {status} {username}")
    
    print("\n🎉 Setup complete! You can now run the servers:")
    print("   Backend:  python3 manage.py runserver")
    print("   Frontend: npm run dev (from parent directory)")

def main():
    print("=" * 60)
    print("  Autograder Database Setup")
    print("=" * 60)
    print()
    
    try:
        # Step 1: Fix the dump file
        if not fix_dump_file():
            print("\n❌ Failed to fix dump file")
            return 1
        
        # Step 2: Load the database
        load_database()
        
        # Step 3: Verify
        verify_setup()
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error during setup: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
