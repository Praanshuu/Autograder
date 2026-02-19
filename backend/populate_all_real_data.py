import os
import sys
import django
import pandas as pd
from django.db import transaction

# Setup Django Environment
sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from classes.models import Class, Enrollment, Module
from assignments.models import Assignment

User = get_user_model()

def run():
    print("--- Starting Full Real Data Population ---")
    
    # 0. Flush existing Student Data
    print("Flushing existing student data...")
    User.objects.filter(role='student').delete()
    
    # 1. Ensure Teacher Exists
    print("Ensuring Teacher Exists...")
    teacher, _ = User.objects.get_or_create(
        username="Vaishnavi",
        defaults={
            'email': "vaishnavi@iitbhilai.ac.in",
            'role': 'teacher',
            'first_name': 'Vaishnavi'
        }
    )
    teacher.set_password("Rinvu2-ganqyh-rowbyx")
    teacher.save()
    
    # 2. Ensure Class Exists
    print("Ensuring Class Exists...")
    cls, _ = Class.objects.get_or_create(
        name="CSL100-CS",
        owner=teacher,
        defaults={
            'section': "Intro to Programming (Main)",
            'join_code': "CSL100MAIN"
        }
    )
    
    # 3. Read Excel
    file_path = '/home/anshul/Projects/Autograder/backend/temp_data_folder/End Sem - CSL100 copy.xlsx'
    sheet_name = "Copy of Total-CSL100-Intro_Prog"
    
    print(f"Reading Excel: {file_path}")
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    except Exception as e:
        print(f"Error reading excel: {e}")
        return

    print(f"Found {len(df)} rows.")
    
    count = 0
    created_users = []
    
    with transaction.atomic():
        for index, row in df.iterrows():
            student_id = str(row['ID']).strip()
            name = str(row['Name']).strip()
            email = str(row['SIS Login ID']).strip()
            
            # Basic validation
            if not student_id or pd.isna(student_id) or student_id.lower() == 'nan':
                continue
                
            # If email is weird/numeric, fallback
            if '@' not in email:
                 email = f"{student_id}@iitbhilai.ac.in"
                 
            # Create User
            user, created = User.objects.get_or_create(
                username=student_id,
                defaults={
                    'email': email,
                    'first_name': name,
                    'role': 'student'
                }
            )
            
            # Reset password to ID for consistency in testing
            user.set_password(student_id) 
            user.save()
            
            # Enroll
            Enrollment.objects.get_or_create(
                user=user, 
                class_obj=cls, 
                defaults={'role': 'student'}
            )
            
            count += 1
            if count % 50 == 0:
                print(f"Processed {count} students...")

    print(f"Successfully populated {count} students.")

if __name__ == '__main__':
    run()
