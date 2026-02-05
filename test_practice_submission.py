#!/usr/bin/env python3
"""
Test script to verify practice submission integration with code execution service.
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
from gamification.views import PracticeQuestionViewSet
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request

User = get_user_model()

def test_practice_submission():
    """Test the practice submission integration"""
    
    # Get or create a test student
    student, created = User.objects.get_or_create(
        username='test_student',
        defaults={
            'email': 'test@example.com',
            'role': 'student',
            'first_name': 'Test',
            'last_name': 'Student'
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
    
    # Create a simple correct solution for "Hello World"
    if "Hello" in practice_question.title:
        correct_code = 'print("Hello, World!")'
        incorrect_code = 'print("Hello World")'  # Missing comma and exclamation
    else:
        # Generic test code
        correct_code = 'print("test")'
        incorrect_code = 'print("wrong")'
    
    # Test with incorrect code first
    print("\n=== Testing with incorrect code ===")
    submission_data = {
        'source_code': incorrect_code,
        'language': 'python'
    }
    
    # Create request factory
    factory = APIRequestFactory()
    request = factory.post(f'/api/practice/{practice_question.id}/submit/', submission_data)
    request.user = student
    
    # Create view and test submission
    view = PracticeQuestionViewSet()
    view.request = request
    view.format_kwarg = None
    
    try:
        response = view.submit(request, pk=str(practice_question.id))
        print(f"Response status: {response.status_code}")
        print(f"Response data: {response.data}")
        
        if response.data.get('success'):
            submission_data = response.data.get('data', {})
            print(f"Submission status: {submission_data.get('status')}")
            print(f"Points earned: {submission_data.get('points_earned')}")
            print(f"Test results: {submission_data.get('test_results')}")
        
    except Exception as e:
        print(f"Error during submission: {e}")
        import traceback
        traceback.print_exc()
    
    # Test with correct code
    print("\n=== Testing with correct code ===")
    submission_data['source_code'] = correct_code
    request = factory.post(f'/api/practice/{practice_question.id}/submit/', submission_data)
    request.user = student
    
    try:
        response = view.submit(request, pk=str(practice_question.id))
        print(f"Response status: {response.status_code}")
        print(f"Response data: {response.data}")
        
        if response.data.get('success'):
            submission_data = response.data.get('data', {})
            print(f"Submission status: {submission_data.get('status')}")
            print(f"Points earned: {submission_data.get('points_earned')}")
            print(f"Test results: {submission_data.get('test_results')}")
        
    except Exception as e:
        print(f"Error during submission: {e}")
        import traceback
        traceback.print_exc()
    
    # Check progress
    print("\n=== Checking progress ===")
    try:
        progress = PracticeProgress.objects.get(
            student=student,
            practice_question=practice_question
        )
        print(f"Is completed: {progress.is_completed}")
        print(f"Attempts count: {progress.attempts_count}")
        print(f"Best score: {progress.best_score}")
        print(f"Completed at: {progress.completed_at}")
    except PracticeProgress.DoesNotExist:
        print("No progress record found")
    
    # Check submissions
    print("\n=== Checking submissions ===")
    submissions = PracticeSubmission.objects.filter(
        student=student,
        practice_question=practice_question
    ).order_by('-submitted_at')
    
    for i, submission in enumerate(submissions):
        print(f"Submission {i+1}:")
        print(f"  Status: {submission.status}")
        print(f"  Attempt: {submission.attempt_number}")
        print(f"  Points: {submission.points_earned}")
        print(f"  Results: {len(submission.test_results)} test cases")

if __name__ == '__main__':
    test_practice_submission()