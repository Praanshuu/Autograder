#!/usr/bin/env python3
"""
Simple test script to verify practice submission processing.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
sys.path.append('backend')
django.setup()

from django.contrib.auth import get_user_model
from gamification.models import PracticeQuestion, PracticeSubmission, PracticeProgress
from gamification.serializers import PracticeSubmissionCreateSerializer

User = get_user_model()

def test_submission_processing():
    """Test the submission processing directly"""
    
    # Get or create a test student
    student, created = User.objects.get_or_create(
        username='test_student2',
        defaults={
            'email': 'test2@example.com',
            'role': 'student',
            'first_name': 'Test',
            'last_name': 'Student2'
        }
    )
    
    if created:
        student.set_password('testpass123')
        student.save()
        print(f"Created test student: {student.username}")
    else:
        print(f"Using existing test student: {student.username}")
    
    # Get the first practice question
    practice_question = PracticeQuestion.objects.first()
    if not practice_question:
        print("No practice questions found!")
        return
    
    print(f"Testing with practice question: {practice_question.title}")
    print(f"Test cases: {practice_question.test_cases}")
    
    # Create a submission directly
    correct_code = 'print("Hello, World!")'
    
    # Create submission using the serializer
    submission_data = {
        'practice_question': practice_question,
        'source_code': correct_code,
        'language': 'python',
        'student': student,
        'attempt_number': 1,
        'status': 'processing'
    }
    
    submission = PracticeSubmission.objects.create(**submission_data)
    print(f"Created submission: {submission.id}")
    
    # Test the processing method directly
    from gamification.views import PracticeQuestionViewSet
    view = PracticeQuestionViewSet()
    
    print("\n=== Processing submission ===")
    try:
        view._process_submission(submission)
        
        # Refresh from database
        submission.refresh_from_db()
        
        print(f"Final status: {submission.status}")
        print(f"Points earned: {submission.points_earned}")
        print(f"Execution time: {submission.execution_time_ms}ms")
        print(f"Test results count: {len(submission.test_results)}")
        
        for i, result in enumerate(submission.test_results):
            print(f"  Test {i+1}: {result['status']} - {result.get('actual_output', 'No output')}")
            if result.get('error_message'):
                print(f"    Error: {result['error_message']}")
        
        # Check progress
        try:
            progress = PracticeProgress.objects.get(
                student=student,
                practice_question=practice_question
            )
            print(f"\nProgress:")
            print(f"  Completed: {progress.is_completed}")
            print(f"  Attempts: {progress.attempts_count}")
            print(f"  Best score: {progress.best_score}")
            print(f"  Completed at: {progress.completed_at}")
        except PracticeProgress.DoesNotExist:
            print("No progress record found")
        
        # Check user points
        from gamification.models import UserPoints
        try:
            user_points = UserPoints.objects.get(user=student)
            print(f"\nUser Points:")
            print(f"  Total: {user_points.total_points}")
            print(f"  Practice: {user_points.practice_points}")
            print(f"  Assignment: {user_points.assignment_points}")
        except UserPoints.DoesNotExist:
            print("No user points record found")
        
    except Exception as e:
        print(f"Error during processing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_submission_processing()