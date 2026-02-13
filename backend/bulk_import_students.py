
import os
import sys
import django
import pandas as pd
import random
import string
from pathlib import Path

# Setup Django Environment
sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from users.models import User
from classes.models import Class, Enrollment

def generate_random_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def import_students(excel_path):
    print(f"Reading students from {excel_path}...")
    
    # Read Excel - Row 0 seems to be the first data row based on inspection
    # Columns based on inspection:
    # 0: Name
    # 1: Roll No (Username)
    # 3: Email
    
    try:
        # Read header=None to access by index
        df = pd.read_excel(excel_path, sheet_name='LetterGrades-CSL100-Intro_Progr', header=None)
        
        # Filter valid rows (where Column 1 looks like a Roll No e.g. B24...)
        # A valid roll no starts with B or S or M and has digits
        
        students_to_create = []
        enrollments_to_create = []
        
        # Get or Create Class
        class_obj, created = Class.objects.get_or_create(
            name="CSL100",
            section="EE",
            defaults={'owner_id': 1} # Assuming admin/owner exists with ID 1
        )
        if created:
            print(f"Created Class: {class_obj}")
        else:
            print(f"Using Class: {class_obj}")

        count = 0
        updated_count = 0
        
        for index, row in df.iterrows():
            name = str(row[0]).strip()
            roll_no = str(row[1]).strip()
            email = str(row[3]).strip()
            
            # Filter for Electrical Engineering (EE) students only
            # Roll No format: B25EE...
            if not roll_no.upper().startswith('B25EE'):
                print(f"Skipping non-EE student: {roll_no}")
                continue
                
            # Check if user exists
            user, created = User.objects.get_or_create(
                username=roll_no,
                defaults={
                    'email': email,
                    'first_name': name.split()[0],
                    'last_name': ' '.join(name.split()[1:]) if len(name.split()) > 1 else '',
                    'role': 'student',
                    'is_active': True
                }
            )
            
            if created:
                user.set_password(roll_no) # Default password = username
                user.save()
                count += 1
            else:
                updated_count += 1
            
            # Enroll in CSL100
            if not Enrollment.objects.filter(user=user, class_obj=class_obj).exists():
                Enrollment.objects.create(
                    user=user, 
                    class_obj=class_obj, 
                    role='student'
                )
                
        print(f"Imported {count} new students.")
        print(f"Found {updated_count} existing students.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    excel_file = '/home/anshul/Projects/Autograder/backend/temp_data_folder/End Sem - CSL100 copy.xlsx'
    import_students(excel_file)
