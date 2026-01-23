
import os
import django
import sys
from django.db import connection

# Add project root to path
sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

assignment_id = 'cb9b5840-c1ac-42b5-ac0c-b49ab7e0cf4e'

with connection.cursor() as cursor:
    # 1. Find AssignmentQuestion IDs
    cursor.execute("""
        SELECT id FROM assignment_questions 
        WHERE assignment_id = %s
    """, [assignment_id])
    aq_rows = cursor.fetchall()
    aq_ids = [str(r[0]) for r in aq_rows]
    
    if not aq_ids:
        print("No assignment questions found.")
        sys.exit(0)

    print(f"Found Assignment Questions: {aq_ids}")
    
    # 2. Find Attempts to delete
    if len(aq_ids) == 1:
        cursor.execute("""
            SELECT id FROM submission_attempts WHERE assignment_question_id = %s
        """, [aq_ids[0]])
    else:
        placeholders = ','.join(['%s'] * len(aq_ids))
        cursor.execute(f"""
            SELECT id FROM submission_attempts WHERE assignment_question_id IN ({placeholders})
        """, aq_ids)
    
    attempt_rows = cursor.fetchall()
    attempt_ids = [str(r[0]) for r in attempt_rows]
    
    if not attempt_ids:
        print("No attempts found.")
        sys.exit(0)
        
    print(f"Found {len(attempt_ids)} attempts to delete.")

    # 3. Delete Test Results (Child)
    if len(attempt_ids) == 1:
         cursor.execute("DELETE FROM test_result_details WHERE attempt_id = %s", [attempt_ids[0]])
    else:
         placeholders = ','.join(['%s'] * len(attempt_ids))
         cursor.execute(f"DELETE FROM test_result_details WHERE attempt_id IN ({placeholders})", attempt_ids)
    print(f"Deleted test_result_details: {cursor.rowcount}")

    # 4. Delete Attempts (Parent)
    if len(aq_ids) == 1:
        cursor.execute("DELETE FROM submission_attempts WHERE assignment_question_id = %s", [aq_ids[0]])
    else:
        placeholders = ','.join(['%s'] * len(aq_ids))
        cursor.execute(f"DELETE FROM submission_attempts WHERE assignment_question_id IN ({placeholders})", aq_ids)
        
    print(f"Deleted submission_attempts: {cursor.rowcount}")
