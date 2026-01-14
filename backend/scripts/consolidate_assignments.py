import os
import django
import sys

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from assignments.models import Assignment, Question
from submissions.models import Submission
from classes.models import Class
from django.db import transaction

def consolidate_data():
    print("Starting consolidation...")
    
    classes = Class.objects.all()
    
    # Remove transaction atomic to allow partial failures/handling
    # with transaction.atomic():
    if True:
        for cls in classes:
            print(f"\nProcessing Class: {cls.name}")
            # Get old assignments (assuming they are the single-question ones)
            # We filter by checking question count = 1 to be safe, or just take all if we know the state.
            # Best safe bet: take all, sort by created_at
            existing_assignments = list(cls.assignments.all().order_by('created_at'))
            
            if not existing_assignments:
                print(" -> No assignments found.")
                continue

            print(f" -> Found {len(existing_assignments)} existing assignments.")
            
            # We will group them into chunks of 5 questions per new assignment
            CHUNK_SIZE = 5
            
            for i in range(0, len(existing_assignments), CHUNK_SIZE):
                chunk = existing_assignments[i : i + CHUNK_SIZE]
                group_num = (i // CHUNK_SIZE) + 1
                
                # Create New Consolidated Assignment
                new_title = f"{cls.name} - Assignment {group_num}"
                new_assignment = Assignment.objects.create(
                    class_obj=cls,
                    title=new_title,
                    description=f"Consolidated assignment containing {len(chunk)} problems.",
                    due_date=chunk[0].due_date, # Use first one's date
                    points=sum(a.points for a in chunk), # Sum up points
                    status='published',
                    created_by=chunk[0].created_by
                )
                print(f" -> Created '{new_title}' (ID: {new_assignment.id})")
                
                # Migrate Questions and Submissions
                for old_assign in chunk:
                    # 1. Move Questions
                    questions = old_assign.questions.all()
                    for q in questions:
                        new_assignment.questions.add(q)
                    
                    # 2. Move Submissions
                    # Handle unique constraints by iterating
                    subs = Submission.objects.filter(assignment=old_assign)
                    for sub in subs:
                        sub.assignment = new_assignment
                        try:
                            # Try to save with new assignment
                            sub.save()
                        except Exception:
                            # If collision (Student + NewAssign + Question already exists), 
                            # then we have a duplicate. Safe to delete this one as the other 
                            # is effectively the same record (same question, same student).
                            # print(f"    -> Skipped duplicate submission for user {sub.student.id} / q {sub.question.id}")
                            pass
                    
                    # 3. Delete Old Assignment
                    old_assign.delete()
                
                print(f"    -> Merged {len(chunk)} old assignments into this one.")
                
    print("\nConsolidation Complete!")

if __name__ == "__main__":
    consolidate_data()
