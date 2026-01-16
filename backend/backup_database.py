#!/usr/bin/env python3
"""
Database Backup Script
Creates a clean database dump for version control
"""
import os
import sys
import django
from django.core.management import call_command
from datetime import datetime

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

def backup_database():
    """Create a database dump"""
    print("=" * 60)
    print("  Autograder Database Backup")
    print("=" * 60)
    print()
    
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        print(f"📊 Current Database Stats:")
        print(f"   Total users: {User.objects.count()}")
        
        # Create dump
        print(f"\n💾 Creating database dump...")
        with open('db_dump.json', 'w') as f:
            call_command('dumpdata', indent=2, stdout=f)
        
        # Get file size
        size = os.path.getsize('db_dump.json')
        size_kb = size / 1024
        
        print(f"✅ Database dump created: db_dump.json ({size_kb:.1f} KB)")
        print(f"\n📝 Next steps:")
        print(f"   1. Review the changes: git diff backend/db_dump.json")
        print(f"   2. Commit the dump: git add backend/db_dump.json")
        print(f"   3. Push to remote: git commit -m 'Update database dump' && git push")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error during backup: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(backup_database())
