
import os
import sys
import django
import pandas as pd
import uuid

# Setup Django Environment
sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from users.models import User
from classes.models import Class
from assignments.models import Assignment, Question, AssignmentQuestion
from submissions.models import SubmissionAttempt, TestResult

def import_practice_submissions():
    csv_path = '/home/anshul/Projects/Autograder/backend/temp_data_folder/CSL100/CSL100/Prac_30Q/merged_output/merged_q1_q30.csv'
    print(f"Reading submissions from {csv_path}...")
    
    try:
        df = pd.read_csv(csv_path)
        
        # 1. Get Class and Owner
        class_obj = Class.objects.get(name="CSL100", section="EE")
        owner = class_obj.owner
        
        # Ensure at least one module exists
        module = class_obj.modules.first()
        if not module:
            print("No module found for CSL100-EE. Creating 'Week 1'...")
            from classes.models import Module
            module = Module.objects.create(class_obj=class_obj, title="Week 1", order_index=0)

        # 2. Create/Get "Practice Sheet 1" Assignment
        # Use filter().first() pattern or try/except to avoid get_or_create issues with foreign keys in defaults sometimes
        assignment = Assignment.objects.filter(title="Practice Sheet 1", module=module).first()
        
        if not assignment:
            assignment = Assignment.objects.create(
                title="Practice Sheet 1",
                module=module,
                type='assignment',
                description='Comprehensive Practice Sheet with 30 Questions',
                is_published=True,
                mode='practice',
                points_total=300,
                difficulty='Medium'
            )
            print(f"Created Assignment: {assignment.title}")
        else:
            print(f"Using Assignment: {assignment.title}")

        # 3. Process Questions and Submissions
        # We need to map q1..q30 to Question objects
        
        # Cache questions to avoid DB hits
        question_cache = {} 
        
        submission_count = 0
        skipped_count = 0
        
        for index, row in df.iterrows():
            student_id_raw = str(row['student_id']) # e.g. B25DS027_q1
            
            # Parse Roll No and Question ID
            parts = student_id_raw.split('_')
            if len(parts) < 2:
                continue
                
            roll_no = parts[0]
            q_code = parts[1] # e.g. q1 or Q1 or q1.py
            
            # Clean q_code (remove .py, etc)
            q_code = q_code.lower().replace('.py', '').replace('q', '')
            try:
                q_num = int(q_code)
                q_code = f"q{q_num}" # Standardize to q1, q2...
            except ValueError:
                # print(f"Skipping invalid q_code: {q_code}")
                continue
            
            # Filter for EE students only
            if not roll_no.upper().startswith('B25EE'):
                continue
                
            # Find Student
            try:
                student = User.objects.get(username=roll_no)
            except User.DoesNotExist:
                # print(f"Student not found: {roll_no}")
                skipped_count += 1
                continue
                
            # Find/Create Question
            if q_code not in question_cache:
                question, q_created = Question.objects.get_or_create(
                    title=f"Question {q_code.upper()}",
                    slug=f"csl100-practice-{q_code}",
                    defaults={
                        'description': f"Practice problem {q_code}",
                        'created_by': owner
                    }
                )
                question_cache[q_code] = question
                
                # Link to Assignment
                AssignmentQuestion.objects.get_or_create(
                    assignment=assignment,
                    question=question,
                    defaults={'order': q_num}
                )
            
            question = question_cache[q_code]
            assign_q = AssignmentQuestion.objects.get(assignment=assignment, question=question)

            # Create Submission Attempt
            tests_passed = int(row['tests_passed'])
            tests_total = int(row['tests_total'])
            score_pct = float(row['score_percentage'])
            code_snippet = row['code_snippet']
            feedback = str(row['semantic_summary'])
            
            status = 'success' if score_pct == 100 else 'fail'
            
            # Check if this specific submission already exists to avoid dupes on re-run
            # We assume one submission per q per student for this import logic
            if not SubmissionAttempt.objects.filter(student=student, assignment_question=assign_q).exists():
                attempt = SubmissionAttempt.objects.create(
                    student=student,
                    assignment_question=assign_q,
                    attempt_number=1,
                    status=status,
                    manual_score=tests_passed, # Store raw tests passed as score
                    source_code=code_snippet,
                    feedback_text=feedback
                )
                
                # Create detailed Test Results (Mocked based on count)
                for i in range(tests_total):
                    is_pass = i < tests_passed
                    TestResult.objects.create(
                        attempt=attempt,
                        test_case_id=f"test_{i+1}",
                        status='pass' if is_pass else 'fail',
                        score=1.0 if is_pass else 0.0
                    )
                submission_count += 1
            else:
                skipped_count += 1

        print(f"Imported {submission_count} submissions.")
        print(f"Skipped {skipped_count} (existing or student not found).")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    import_practice_submissions()
