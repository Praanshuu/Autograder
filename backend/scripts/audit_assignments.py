import os
import django
import sys

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from assignments.models import Assignment, Question

def audit_assignments():
    print("--- Assignment Audit ---")
    assignments = Assignment.objects.all().prefetch_related('questions')
    
    if not assignments.exists():
        print("No assignments found.")
        return

    print(f"Total Assignments: {assignments.count()}")
    
    multi_question_count = 0
    single_question_count = 0
    zero_question_count = 0

    for a in assignments[:20]: # Inspect first 20
        q_count = a.questions.count()
        q_ids = [q.id for q in a.questions.all()]
        print(f"ID: {a.id} | Title: '{a.title}' | Questions: {q_count} | IDs: {q_ids}")
        if q_count > 1:
            multi_question_count += 1
        elif q_count == 1:
            single_question_count += 1
        else:
            zero_question_count += 1

    print(f"\n... (Total Stats)")
    # Re-calculate totals for full DB if needed, but loop above just showed sample.
    # Let's do a quick aggregate check
    
    total_single = 0
    total_multi = 0
    
    for a in assignments:
        c = a.questions.count()
        if c == 1: total_single += 1
        elif c > 1: total_multi += 1
    
    print(f"Assignments with 1 Question: {total_single}")
    print(f"Assignments with >1 Questions: {total_multi}")
    print(f"Assignments with 0 Questions: {assignments.count() - total_single - total_multi}")

if __name__ == "__main__":
    audit_assignments()
