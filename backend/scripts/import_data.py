import os
import sys
import django
import pandas as pd
from datetime import timedelta
from django.utils import timezone
from django.db import transaction

# Setup Django Environment
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autograder.settings")
django.setup()

from django.contrib.auth import get_user_model
from classes.models import Class, Enrollment
from assignments.models import Assignment, Question, TestCase
from submissions.models import Submission

User = get_user_model()

def run():
    print("Starting optimized import...")
    with transaction.atomic():
        _run_inner()
    print("Import complete!")

def _run_inner():
    file_path = r"d:\Programming\internshipiit\Autograder_UI_Proj\autograder\public\data\End Sem - CSL100 copy.xlsx"
    sheet_name = 'LetterGrades-CSL100-Intro_Progr'
    
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    except Exception as e:
        print(f"Failed to read sheet '{sheet_name}'. Available sheets: {pd.ExcelFile(file_path).sheet_names}")
        return

    print("Analyzing columns...")
    
    # 1. Identify Email Column
    email_col_idx = -1
    name_col_idx = 0 # Assume col 0 is name
    
    # Check first few rows to find email column
    for idx, row in df.head(5).iterrows():
        for col_idx, val in enumerate(row):
            if isinstance(val, str) and '@' in val:
                email_col_idx = col_idx
                break
        if email_col_idx != -1:
            break
            
    if email_col_idx == -1:
        print("CRITICAL: Could not identify email column (looking for '@').")
        return
        
    print(f"Identified Email at Column {email_col_idx}")
    
    # 2. Identify Grade Columns (Numeric columns after email)
    grade_col_indices = []
    # Sample a middle row to check for numeric values
    sample_row = df.iloc[len(df)//2] if len(df) > 1 else df.iloc[0]
    
    for col_idx in range(len(df.columns)):
        if col_idx <= email_col_idx: continue # Skip name/email cols
        
        # Check if column has mostly numeric data
        val = sample_row.iloc[col_idx]
        try:
            float(val)
            if pd.notna(val):
                grade_col_indices.append(col_idx)
        except:
            continue
            
    print(f"Found {len(grade_col_indices)} potential assignment columns: {grade_col_indices}")

    # 3. Setup Class
    teacher = User.objects.filter(role='teacher').first()
    if not teacher:
        print("Error: No teacher found.")
        return

    course_name = "CSL100"
    class_obj, _ = Class.objects.get_or_create(
        name=course_name,
        defaults={'owner': teacher, 'description': 'Intro to Programming (Imported Data)'}
    )
    Enrollment.objects.get_or_create(user=teacher, class_obj=class_obj, role='teacher')

    # 4. Create Assignments and Questions
    assignments_data = {} # {col_idx: (assignment, question)}
    for i, col_idx in enumerate(grade_col_indices):
        title = f"Assignment {i+1}"
        assign, _ = Assignment.objects.get_or_create(
            class_obj=class_obj,
            title=title,
            defaults={
                'points': 100,
                'status': 'published',
                'created_by': teacher,
                'due_date': timezone.now() - timedelta(days=1)
            }
        )
        
        # Create Unique Question for this assignment
        question, _ = Question.objects.get_or_create(
            title=f"Question {i+1}",
            defaults={
                'description': f'Main task for assignment {i+1}.',
                'order': 1
            }
        )
        assign.questions.add(question)
        assignments_data[col_idx] = (assign, question)

    # 5. Import Rows
    count = 0
    for idx, row in df.iterrows():
        email = row.iloc[email_col_idx]
        
        if pd.isna(email) or not isinstance(email, str) or '@' not in email:
            continue
            
        name = row.iloc[name_col_idx] if pd.notna(row.iloc[name_col_idx]) else "Student"
        username = email.split('@')[0]
        
        # Handle duplicates if username exists but email differs (not covered by get_or_create)
        # But we wiped data, so it's fine.
        
        student, created = User.objects.get_or_create(
            email=email,
            defaults={
                'username': username,
                'first_name': str(name).split()[0],
                'last_name': ' '.join(str(name).split()[1:]) if len(str(name).split()) > 1 else '',
                'role': 'student'
            }
        )
        if created:
            student.set_password('password')
            student.save()
            
        Enrollment.objects.get_or_create(user=student, class_obj=class_obj, defaults={'role': 'student'})
        
        # Add Submissions
        for col_idx, (assign, question) in assignments_data.items():
            val = row.iloc[col_idx]
            try:
                score = float(val)
                if pd.notna(score):
                    Submission.objects.update_or_create(
                        assignment=assign,
                        question=question,
                        student=student,
                        defaults={
                            'status': 'graded',
                            'final_score': score,
                            'is_graded': True,
                            'is_published': True,
                            'code_content': '// Imported code'
                        }
                    )
            except Exception as e:
                # print(f"Error creating submission: {e}")
                pass
                
        count += 1
        if count % 50 == 0:
            print(f"Processed {count} students...")
            
    print(f"Done! Imported {count} students.")

if __name__ == '__main__':
    run()
