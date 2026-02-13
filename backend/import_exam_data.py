
import os
import sys
import django
import pandas as pd
from datetime import datetime, timedelta

# Setup Django Environment
sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from users.models import User
from classes.models import Class, Module
from assignments.models import Assignment
from submissions.models import GradebookEntry

def import_exam_scores():
    excel_path = '/home/anshul/Projects/Autograder/backend/temp_data_folder/End Sem - CSL100 copy.xlsx'
    print(f"Reading scores from {excel_path}...")
    
    try:
        # Read Excel - No header
        df = pd.read_excel(excel_path, sheet_name='LetterGrades-CSL100-Intro_Progr', header=None)
        
        # 1. Get Class and Owner
        class_obj = Class.objects.get(name="CSL100", section="EE")
        owner = class_obj.owner
        module = class_obj.modules.first()
        
        # 2. Define Assessments to Create (Map to Excel Columns)
        # Based on inspection:
        # Col 4: Quiz 1 (approx, labelled '15' max ?) -> Let's assume Col 4 is Quiz 1
        # Col 8: Mid Sem (approx, labelled '18' max ?) -> Let's assume Col 8 is Mid Sem
        # Col 12: End Sem (approx, labelled '80' max ?) -> Let's assume Col 12 is End Sem
        
        assessments_config = [
            {
                'title': 'Quiz 1',
                'col_index': 4,
                'max_points': 15,
                'weight': 15,
                'type': 'quiz'
            },
            {
                'title': 'Mid Semester Exam',
                'col_index': 8,
                'max_points': 30, # Guessing based on data usually around 20-30
                'weight': 30,
                'type': 'assignment',
                'mode': 'exam'
            },
            {
                'title': 'End Semester Exam',
                'col_index': 11, # Col 12 in 1-based, 11 in 0-based
                'max_points': 100,
                'weight': 50,
                'type': 'assignment',
                'mode': 'exam'
            }
        ]
        
        assessments = {}
        
        # Create Assessments in DB
        for config in assessments_config:
            title = config['title']
            
            # Check if exists
            item = Assignment.objects.filter(title=title, module=module).first()
            if not item:
                item = Assignment.objects.create(
                    title=title,
                    module=module,
                    type=config['type'],
                    description=f"Imported {title} Scores",
                    is_published=True,
                    mode=config.get('mode', 'practice'),
                    points_total=config['max_points'],
                    difficulty='Medium'
                )
                print(f"Created Assessment: {title}")
            else:
                print(f"Using Assessment: {title}")
            
            assessments[config['col_index']] = item

        count = 0
        skipped = 0
        
        for index, row in df.iterrows():
            if index < 1: continue # Skip header row if we think row 0 is header-ish
            
            roll_no = str(row[1]).strip()
            
            # Filter for EE students
            if not roll_no.upper().startswith('B25EE'):
                continue
                
            try:
                student = User.objects.get(username=roll_no)
            except User.DoesNotExist:
                # print(f"Student not found: {roll_no}")
                skipped += 1
                continue
            
            # For each assessment, get score and create GradebookEntry
            for col_idx, item in assessments.items():
                try:
                    score_val = row[col_idx]
                    # Handle NaN or non-numeric
                    score = float(score_val) if pd.notnull(score_val) and str(score_val).strip() != '' else 0.0
                except ValueError:
                    score = 0.0
                
                # Update/Create Gradebook Entry
                entry, created = GradebookEntry.objects.get_or_create(
                    student=student,
                    content_item=item,
                    defaults={
                        'final_score': score,
                        'status': 'graded'
                    }
                )
                if not created:
                    entry.final_score = score
                    entry.status = 'graded'
                    entry.save()
            
            count += 1
            
        print(f"Imported scores for {count} students.")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    import_exam_scores()
