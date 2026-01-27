import os
import sys
import django
from django.core.management import call_command

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model

# Import sibling scripts
# Ensure current directory is in path so we can import siblings
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import import_data
import consolidate_assignments
import anonymize_enrich
import fix_ownership

User = get_user_model()

def run():
    print("!!! MASTER DATABASE RESET & RE-SEED !!!")
    
    # 1. Flush DB
    print("\n1. Flushing Database...")
    call_command('flush', interactive=False)
    
    # 2. Create Base Users
    print("\n2. Creating Base Users...")
    # Admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@test.com', 'password')
        print(" -> Created Admin (admin / password)")

    # Teacher (Role='teacher' is needed for import)
    if not User.objects.filter(username='teacher').exists():
        # Using create_user helper which handles hashing
        # Assuming AbstractUser with 'role' field
        u = User.objects.create_user(username='teacher', email='teacher@test.com', password='password')
        u.role = 'teacher'
        u.save()
        print(" -> Created Teacher (teacher / password)")

    # 3. Import Data
    print("\n3. Importing Excel Data...")
    import_data.run()

    # 4. Consolidate Assignments
    print("\n4. Consolidating Assignments...")
    consolidate_assignments.consolidate_data()

    # 5. Anonymize & Enrich
    print("\n5. Anonymizing & Enriching...")
    anonymize_enrich.run()

    # 6. Fix Ownership (Just in case)
    print("\n6. Standardizing Ownership...")
    fix_ownership.fix_ownership()

    print("\nDONE! Database is fresh and optimized.")

if __name__ == "__main__":
    run()
