
import os
import sys
import django
import csv
import re
import random
from datetime import timedelta
from django.utils import timezone
from django.db import transaction

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autograder.settings")
django.setup()

from django.contrib.auth import get_user_model
from assignments.models import Assignment, AssignmentQuestion
from submissions.models import SubmissionAttempt, AssignmentProgress, TestResult, GradebookEntry

User = get_user_model()

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp_data_folder/CSL100/CSL100/Prac_30Q')
ASSIGNMENT_TITLE = "Practice Sheet - Whole Syllabus"

def parse_student_id(raw_id):
    """
    Extracts student username from raw ID like 'B25MT020_q3' or 'B25DS027_q1'.
    Assumes the username is the part before the last underscore.
    """
    if '_' in raw_id:
        return raw_id.rsplit('_', 1)[0]
    return raw_id

def get_assignments():
    assignments = Assignment.objects.filter(title=ASSIGNMENT_TITLE)
    if not assignments.exists():
        print(f"Error: No Assignment with title '{ASSIGNMENT_TITLE}' found.")
        return []
    return list(assignments)

def populate_question(q_num, assignment):
    dir_name = f"q{q_num}"
    dir_path = os.path.join(DATA_DIR, dir_name)
    
    if not os.path.exists(dir_path):
        # print(f"Directory {dir_path} does not exist. Skipping.")
        return

    # Find the summary CSV file
    csv_file = None
    for filename in os.listdir(dir_path):
        if filename.startswith("Summary_") and filename.endswith(".csv"):
            csv_file = os.path.join(dir_path, filename)
            break
    
    if not csv_file:
        # print(f"No Summary CSV found in {dir_path}. Skipping.")
        return

    print(f"Processing {dir_name} for Assignment ID: {assignment.id}...")

    # Get AssignmentQuestion mapped to this order
    # logic: q1 -> order 1, etc.
    try:
        assignment_question = AssignmentQuestion.objects.get(assignment=assignment, order=q_num)
    except AssignmentQuestion.DoesNotExist:
        print(f"No AssignmentQuestion found for order {q_num} in '{ASSIGNMENT_TITLE}' (ID: {assignment.id}). Skipping.")
        return

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        # Clean header keys if necessary (sometimes there are BOM or spaces)
        if reader.fieldnames:
            reader.fieldnames = [name.strip().lstrip('\ufeff') for name in reader.fieldnames]

        for row in reader:
            raw_student_id = row.get('student_id', '')
            username = parse_student_id(raw_student_id)
            
            # Find User
            try:
                # Case insensitive search might be safer, but usernames here seem distinct
                student = User.objects.get(username__iexact=username)
            except User.DoesNotExist:
                # print(f"User {username} not found. Skipping.")
                continue

            try:
                score_percentage = float(row.get('score_percentage', 0))
            except ValueError:
                score_percentage = 0.0
                
            try:
                tests_total = int(row.get('tests_total', 5))
            except ValueError:
                tests_total = 5
                
            try:
                tests_passed = int(row.get('tests_passed', int((score_percentage / 100.0) * tests_total)))
            except ValueError:
                tests_passed = 0

            code_snippet = row.get('code_snippet', '')
            
            # Create/Update SubmissionAttempt
            # Delete existing to avoid duplicates
            SubmissionAttempt.objects.filter(
                student=student,
                assignment_question=assignment_question,
                attempt_number=1
            ).delete()
            
            submission = SubmissionAttempt.objects.create(
                student=student,
                assignment_question=assignment_question,
                attempt_number=1,
                status='success',
                manual_score=float(tests_passed),
                source_code=code_snippet,
                execution_time_ms=random.randint(100, 2000),
                created_at=timezone.now() - timedelta(days=random.randint(1, 30))
            )
            created = True

            # Create AssignmentProgress (for time spent analytics)
            time_spent_seconds = random.randint(5 * 60, 60 * 60) # 5 to 60 minutes
            AssignmentProgress.objects.update_or_create(
                student=student,
                assignment_question=assignment_question,
                defaults={
                    'current_code': code_snippet,
                    'time_spent': time_spent_seconds,
                    'last_updated': submission.created_at
                }
            )

            # Create TestResults
            # Delete existing to regenerate
            TestResult.objects.filter(attempt=submission).delete()
            
            # Create "Pass" results
            for i in range(tests_passed):
                TestResult.objects.create(
                    attempt=submission,
                    test_case_id=f"test_{i+1}",
                    status='pass',
                    score=1.0,
                    execution_time_ms=random.randint(10, 100)
                )
            
            # Create "Fail" results
            for i in range(tests_total - tests_passed):
                TestResult.objects.create(
                    attempt=submission,
                    test_case_id=f"test_{tests_passed + i + 1}",
                    status='fail',
                    score=0.0,
                    error_message="AssertionError: Expected X but got Y",
                    execution_time_ms=random.randint(10, 100)
                )
    # print(f"Completed {dir_name}")

def main():
    assignments = get_assignments()
    if not assignments:
        return

    for assignment in assignments:
        print(f"Populating data for Assignment ID: {assignment.id}")
        # Process all 30 questions
        for i in range(1, 31):
            with transaction.atomic():
                populate_question(i, assignment)

    print("Data population complete.")

if __name__ == "__main__":
    main()
