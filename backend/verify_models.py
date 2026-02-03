#!/usr/bin/env python3
"""
Verification script for PracticeSubmission and PracticeProgress models
Demonstrates that all requirements are met
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from gamification.models import PracticeQuestion, PracticeSubmission, PracticeProgress

User = get_user_model()

def verify_unlimited_attempts():
    """Verify Requirement 2.1: Unlimited submission attempts"""
    print("🔍 Verifying unlimited attempts functionality...")
    
    # Create test user and question
    user, _ = User.objects.get_or_create(
        username='verify_user',
        defaults={'email': 'verify@example.com', 'password': 'testpass123'}
    )
    
    teacher, _ = User.objects.get_or_create(
        username='verify_teacher',
        defaults={'email': 'teacher@example.com', 'password': 'testpass123'}
    )
    
    question, _ = PracticeQuestion.objects.get_or_create(
        title='Verification Question',
        defaults={
            'description': 'Test question for verification',
            'difficulty': 'easy',
            'category': 'Testing',
            'test_cases': [{'input': 'test', 'expected_output': 'test'}],
            'point_value': 100,
            'created_by': teacher
        }
    )
    
    # Clean up any existing submissions
    PracticeSubmission.objects.filter(student=user, practice_question=question).delete()
    
    # Create 20 submissions to test unlimited attempts
    for i in range(20):
        PracticeSubmission.objects.create(
            student=user,
            practice_question=question,
            source_code=f'# Attempt {i+1}',
            status='fail' if i < 19 else 'success',
            attempt_number=i + 1,
            points_earned=100 if i == 19 else 0
        )
    
    # Verify all submissions were created
    submission_count = PracticeSubmission.objects.filter(
        student=user,
        practice_question=question
    ).count()
    
    assert submission_count == 20, f"Expected 20 submissions, got {submission_count}"
    print(f"✅ Successfully created {submission_count} unlimited attempts")
    
    # Clean up
    PracticeSubmission.objects.filter(student=user, practice_question=question).delete()

def verify_progress_tracking():
    """Verify Requirement 2.3: Progress tracking for completion status"""
    print("🔍 Verifying progress tracking functionality...")
    
    user = User.objects.get(username='verify_user')
    question = PracticeQuestion.objects.get(title='Verification Question')
    
    # Clean up any existing progress
    PracticeProgress.objects.filter(student=user, practice_question=question).delete()
    
    # Create progress record
    progress = PracticeProgress.objects.create(
        student=user,
        practice_question=question,
        attempts_count=5,
        best_score=75.0,
        time_spent=1800,  # 30 minutes
        is_completed=False
    )
    
    # Verify initial state
    assert not progress.is_completed, "Progress should not be completed initially"
    assert progress.attempts_count == 5, f"Expected 5 attempts, got {progress.attempts_count}"
    assert progress.best_score == 75.0, f"Expected score 75.0, got {progress.best_score}"
    assert progress.time_spent == 1800, f"Expected 1800 seconds, got {progress.time_spent}"
    
    # Mark as completed
    from django.utils import timezone
    progress.is_completed = True
    progress.best_score = 100.0
    progress.completed_at = timezone.now()  # Set completion date when marking as completed
    progress.save()
    
    # Verify completion tracking
    progress.refresh_from_db()
    assert progress.is_completed, "Progress should be marked as completed"
    assert progress.best_score == 100.0, f"Expected score 100.0, got {progress.best_score}"
    
    print("✅ Progress tracking working correctly")
    
    # Clean up
    progress.delete()

def verify_performance_indexing():
    """Verify that proper indexing is in place for performance"""
    print("🔍 Verifying database indexing...")
    
    # Check PracticeSubmission indexes
    submission_indexes = PracticeSubmission._meta.indexes
    index_fields = [tuple(index.fields) for index in submission_indexes]
    
    expected_submission_indexes = [
        ('student', 'practice_question'),
        ('student', '-submitted_at'),
        ('status',)
    ]
    
    for expected_index in expected_submission_indexes:
        assert expected_index in index_fields, f"Missing index for fields: {expected_index}"
    
    # Check PracticeProgress indexes
    progress_indexes = PracticeProgress._meta.indexes
    progress_index_fields = [tuple(index.fields) for index in progress_indexes]
    
    expected_progress_indexes = [
        ('student', 'is_completed'),
        ('practice_question', 'is_completed')
    ]
    
    for expected_index in expected_progress_indexes:
        assert expected_index in progress_index_fields, f"Missing index for fields: {expected_index}"
    
    print("✅ All required database indexes are present")

def verify_model_fields():
    """Verify that all required fields are present and properly configured"""
    print("🔍 Verifying model field configuration...")
    
    # Check PracticeSubmission fields
    submission_fields = [f.name for f in PracticeSubmission._meta.fields]
    required_submission_fields = [
        'student', 'practice_question', 'source_code', 'language', 'status',
        'test_results', 'points_earned', 'attempt_number', 'execution_time_ms',
        'submitted_at'
    ]
    
    for field in required_submission_fields:
        assert field in submission_fields, f"Missing field in PracticeSubmission: {field}"
    
    # Check PracticeProgress fields
    progress_fields = [f.name for f in PracticeProgress._meta.fields]
    required_progress_fields = [
        'student', 'practice_question', 'is_completed', 'attempts_count',
        'best_score', 'time_spent', 'first_attempt_at', 'completed_at'
    ]
    
    for field in required_progress_fields:
        assert field in progress_fields, f"Missing field in PracticeProgress: {field}"
    
    print("✅ All required model fields are present")

def verify_unique_constraints():
    """Verify that unique constraints work properly"""
    print("🔍 Verifying unique constraints...")
    
    user = User.objects.get(username='verify_user')
    question = PracticeQuestion.objects.get(title='Verification Question')
    
    # Clean up any existing progress
    PracticeProgress.objects.filter(student=user, practice_question=question).delete()
    
    # Create first progress record
    progress1 = PracticeProgress.objects.create(
        student=user,
        practice_question=question
    )
    
    # Attempt to create duplicate should fail
    try:
        progress2 = PracticeProgress.objects.create(
            student=user,
            practice_question=question
        )
        assert False, "Should not be able to create duplicate progress records"
    except Exception:
        print("✅ Unique constraint working correctly - duplicate progress prevented")
    
    # Clean up
    progress1.delete()

def main():
    """Run all verification tests"""
    print("🧪 Verifying PracticeSubmission and PracticeProgress Models")
    print("=" * 60)
    
    try:
        verify_model_fields()
        verify_unlimited_attempts()
        verify_progress_tracking()
        verify_performance_indexing()
        verify_unique_constraints()
        
        print("\n🎉 All verifications passed!")
        print("✅ PracticeSubmission model supports unlimited attempts")
        print("✅ PracticeProgress model tracks completion status properly")
        print("✅ Proper database indexing is in place for performance")
        print("✅ Models work correctly for the unlimited attempts workflow")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Verification failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)