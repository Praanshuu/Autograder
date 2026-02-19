import os
import django
import pandas as pd
import random
import re
import sys
from datetime import timedelta, datetime

# Setup Django Environment
sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import transaction
from classes.models import Class, Enrollment, Module
from assignments.models import Assignment, Question, AssignmentQuestion, ContentItem
from submissions.models import SubmissionAttempt, AssignmentProgress, TestResult, GradebookEntry
from analytics.models import SubmissionAnalysis, ProblemAnalytics
from utils.pdf_parser import parse_practice_sheet
import pytz

User = get_user_model()

def run():
    print("--- Starting Final Data Population (With Gradebook Generation) ---")
    
    # 0. Flush existing Student Data
    print("Flushing existing student data... SKIPPED (Preserving Real Data)")
    # User.objects.filter(role='student').delete()
    
    # 1. Create Teacher
    teacher_username = "Vaishnavi"
    teacher_email = "vaishnavi@iitbhilai.ac.in"
    teacher, created = User.objects.get_or_create(
        username=teacher_username,
        defaults={
            'email': teacher_email,
            'role': 'teacher',
            'first_name': 'Vaishnavi',
            'last_name': 'Instructor'
        }
    )
    if created:
        teacher.set_password("Rinvu2-ganqyh-rowbyx")
        teacher.save()
        print(f"Created Teacher: {teacher.username}")
    else:
        print(f"Found Teacher: {teacher.username}")

    # 2. Create Classes (CS and EE)
    print("Creating Classes...")
    def create_class_stack(suffix, unique_code):
        cls_name = f"CSL100-{suffix}"
        cls, _ = Class.objects.get_or_create(
            name=cls_name,
            owner=teacher,
            defaults={
                'section': f"Intro to Programming ({suffix})",
                'join_code': unique_code
            }
        )
        Enrollment.objects.get_or_create(class_obj=cls, user=teacher, defaults={'role': 'teacher'})
        mod, _ = Module.objects.get_or_create(class_obj=cls, title="Practice Sheets", defaults={'order_index': 1})
        
        assign, _ = Assignment.objects.get_or_create(
            module=mod,
            title="Practice Sheet - Whole Syllabus",
            defaults={
                'type': 'assignment',
                'description': f'Practice Sheet for {suffix} Batch.',
                'mode': 'practice',
                # 30 questions * 6 points = 180 total
                'points_total': 180, 
                'is_published': True,
                'due_date': timezone.now() - timedelta(days=60)
            }
        )
        return cls, assign

    class_cs, assign_cs = create_class_stack("CS", "CSL100CS")
    class_ee, assign_ee = create_class_stack("EE", "CSL100EE")
    
    print(f"Created {class_cs.name} and {class_ee.name}")

    # 3. Parse Questions
    txt_path = '/home/anshul/Projects/Autograder/backend/temp_data_folder/Csl_100_30Q_practice_sheet_Whole_syllabus-1.txt'
    parsed_questions = parse_practice_sheet(txt_path)
    print(f"Parsed {len(parsed_questions)} questions.")

    # 4. Process Questions & Submissions
    qs_base = '/home/anshul/Projects/Autograder/backend/temp_data_folder/CSL100/CSL100/Prac_30Q'
    pattern = re.compile(r'^([A-Z])(25)(CS|EE)(\d{3})$', re.IGNORECASE)

    total_submissions_created = 0
    # Track scores per student to batch create GradebookEntries later
    # student_id -> { 'total_pct': 0.0, 'assign_obj': assignment }
    student_scores = {}

    for i in range(1, 31):
        q_dir = os.path.join(qs_base, f'q{i}')
        if not os.path.exists(q_dir):
            continue
            
        q_data = parsed_questions[i-1] if i-1 < len(parsed_questions) else {
            'title': f"Q{i}. Practice Question", 'description': 'Practice problem.'
        }
        
        question, _ = Question.objects.get_or_create(
            title=q_data['title'][:200],
            defaults={
                'description': q_data['description'],
                'slug': f"csl100-q{i}",
                'created_by': teacher,
                'test_cases': []
            }
        )
        
        for assign in [assign_cs, assign_ee]:
            AssignmentQuestion.objects.get_or_create(
                assignment=assign, question=question,
                defaults={'order': i, 'custom_points': 6}
            )

        csv_path = os.path.join(q_dir, f'Summary_csl100_q{i}.csv')
        if not os.path.exists(csv_path):
            continue
            
        try:
            df = pd.read_csv(csv_path)
        except Exception as e:
            print(f"Failed to read CSV for Q{i}: {e}")
            continue

        pass_count = 0
        fail_count = 0
        
        for _, row in df.iterrows():
            raw_id = str(row.get('student_id', row.iloc[0])).strip().upper()
            clean_id_base = re.split(r'[_\.]', raw_id)[0]
            
            match = pattern.match(clean_id_base)
            if not match: continue
                
            branch = match.group(3).upper() # CS or EE
            student_id = match.group(0)     # B25CS001
            
            if branch == 'CS':
                target_assign = assign_cs
                target_class = class_cs
            else:
                target_assign = assign_ee
                target_class = class_ee
            
            student, created_student = User.objects.get_or_create(
                username=student_id,
                defaults={
                    'email': f"{student_id.lower()}@iitbhilai.ac.in",
                    'role': 'student',
                    'first_name': student_id,
                    'last_name': ''
                }
            )
            if created_student or not student.check_password(student_id):
                student.set_password(student_id)
                student.save()
                
            Enrollment.objects.get_or_create(class_obj=target_class, user=student, defaults={'role': 'student'})
            
            try:
                score_pct = float(row.get('score_percentage', 0))
                final_score = (score_pct / 100.0) * 6.0
                feedback = row.get('semantic_summary', '')
                code = row.get('code_snippet', '# Code not found')
                if pd.isna(feedback): feedback = ""
                if pd.isna(code): code = "# Code not found"
            except:
                score_pct = 0.0
                final_score = 0.0
                feedback = ""
                code = "# Parse Error"
                
            status = 'success' if final_score > 0 else 'fail'
            if status == 'success': pass_count += 1
            else: fail_count += 1
            
            aq = AssignmentQuestion.objects.get(assignment=target_assign, question=question)

            # Randomize submission time (last 60 days)
            # Higher score -> maybe less time? Or just random.
            # Let's say random time within the assignment duration.
            days_ago = random.randint(0, 60)
            hours_ago = random.randint(0, 23)
            minutes_ago = random.randint(0, 59)
            submission_time = timezone.now() - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)
            
            sub = SubmissionAttempt.objects.create(
                student=student,
                assignment_question=aq,
                attempt_number=1,
                source_code=str(code),
                status=status,
                execution_time_ms=random.randint(50, 250),
                manual_score=final_score,
                feedback_text=str(feedback)
            )
            # Update created_at (auto_now_add makes it read-only on create, need to update after)
            sub.created_at = submission_time
            sub.save()
            
            # Create AssignmentProgress for analytics (Time Spent)
            # Random duration between 5 mins (300s) and 4 hours (14400s)
            time_spent_seconds = random.randint(300, 14400)
            AssignmentProgress.objects.update_or_create(
                student=student,
                assignment_question=aq,
                defaults={
                    'current_code': str(code),
                    'time_spent': time_spent_seconds,
                    'last_updated': submission_time
                }
            )

            # Create Test Results for Heatmap
            for tc_idx in range(1, 6):
                tc_id = f"tc_00{tc_idx}"
                
                is_pass = False
                if score_pct >= 90:
                    is_pass = True
                elif score_pct >= 50:
                    # Pass first 3, fail last 2
                    is_pass = (tc_idx <= 3)
                else:
                    # Pass first 1, fail rest
                    is_pass = (tc_idx <= 1)
                
                tr_status = 'pass' if is_pass else 'fail'
                error_msg = ""
                if not is_pass:
                    errors = ["TimeoutError: Time limit exceeded", "IndexError: list index out of range", "SyntaxError: invalid syntax", "AssertionError: 5 != 3", "TypeError: unsupported operand type(s)"]
                    error_msg = random.choice(errors)
                
                TestResult.objects.create(
                    attempt=sub,
                    test_case_id=tc_id,
                    status=tr_status,
                    score=1.0 if is_pass else 0.0,
                    execution_time_ms=random.randint(10, 100),
                    error_message=error_msg
                )
            
            total_submissions_created += 1
            
            # Aggregate Score for Gradebook
            # Key: (student_id, assignment_id)
            key = (student.id, target_assign.id)
            if key not in student_scores:
                student_scores[key] = {'total_pct': 0.0, 'count': 0, 'student': student, 'assignment': target_assign}
            
            student_scores[key]['total_pct'] += score_pct
            student_scores[key]['count'] += 1
            
        # Analytics
        pa, _ = ProblemAnalytics.objects.get_or_create(
            question=question,
            test_case_id="OVERALL",
            defaults={'pass_count': 0, 'fail_count': 0}
        )
        pa.pass_count = pass_count
        pa.fail_count = fail_count
        pa.save()
        
        print(f"Processed Q{i}: {pass_count+fail_count} submissions.")

    # 5. Generate Gradebook Entries
    print("Generating Gradebook Entries...")
    created_entries = 0
    for key, data in student_scores.items():
        # Score is average of percentages across 30 questions
        # If student didn't attempt all 30, we divide by 30 to penalize logic? 
        # Usually yes. The assignment has 30 questions.
        total_questions = 30
        
        # Current data['total_pct'] is sum of percentages (e.g. 100+100+50...)
        final_grade_pct = data['total_pct'] / total_questions
        
        # Safety cap
        if final_grade_pct > 100: final_grade_pct = 100.0
        
        content_item = ContentItem.objects.get(id=data['assignment'].id)
        
        GradebookEntry.objects.update_or_create(
            student=data['student'],
            content_item=content_item,
            defaults={
                'final_score': final_grade_pct,
                'status': 'graded',
                'completion_date': timezone.now() - timedelta(days=random.randint(0, 5))
            }
        )
        created_entries += 1

    print(f"--- Completed. Submissions: {total_submissions_created}, Gradebook Entries: {created_entries} ---")

if __name__ == '__main__':
    run()
