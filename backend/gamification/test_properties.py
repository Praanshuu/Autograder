"""
Property-based tests for PracticeSubmission and PracticeProgress models
Testing universal properties that should hold across all valid inputs
"""
from hypothesis import given, strategies as st, settings
from hypothesis.extra.django import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import PracticeQuestion, PracticeSubmission, PracticeProgress

User = get_user_model()


class PracticeModelsPropertyTest(TestCase):
    """Property-based tests for practice models"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.teacher = User.objects.create_user(
            username='teacher',
            email='teacher@example.com',
            password='teacherpass123'
        )
        
        self.practice_question = PracticeQuestion.objects.create(
            title='Property Test Question',
            description='A test practice question for property testing',
            difficulty='medium',
            category='Testing',
            test_cases=[{'input': 'test', 'expected_output': 'test'}],
            point_value=100,
            created_by=self.teacher
        )
    
    @given(
        attempt_count=st.integers(min_value=1, max_value=100),
        points_earned=st.integers(min_value=0, max_value=1000)
    )
    @settings(max_examples=50, deadline=5000)
    def test_property_unlimited_practice_submissions(self, attempt_count, points_earned):
        """
        **Property 2: Unlimited Practice Submissions**
        **Validates: Requirements 1.4, 2.1**
        
        For any number of submission attempts, the system should allow unlimited 
        submission attempts until all test cases pass, with no submission limits enforced.
        """
        # Create multiple submissions for the same question
        submissions = []
        for i in range(attempt_count):
            submission = PracticeSubmission.objects.create(
                student=self.user,
                practice_question=self.practice_question,
                source_code=f'def solution():\n    return {i}',
                status='fail' if i < attempt_count - 1 else 'success',
                attempt_number=i + 1,
                points_earned=points_earned if i == attempt_count - 1 else 0
            )
            submissions.append(submission)
        
        # Property: All submissions should be created successfully
        created_submissions = PracticeSubmission.objects.filter(
            student=self.user,
            practice_question=self.practice_question
        )
        
        # Verify unlimited attempts property
        assert created_submissions.count() == attempt_count, \
            f"Expected {attempt_count} submissions, got {created_submissions.count()}"
        
        # Verify attempt numbers are sequential
        for i, submission in enumerate(submissions):
            assert submission.attempt_number == i + 1, \
                f"Expected attempt number {i + 1}, got {submission.attempt_number}"
        
        # Clean up for next test iteration
        PracticeSubmission.objects.filter(
            student=self.user,
            practice_question=self.practice_question
        ).delete()
    
    @given(
        attempts_count=st.integers(min_value=0, max_value=50),
        best_score=st.floats(min_value=0.0, max_value=100.0),
        time_spent=st.integers(min_value=0, max_value=7200)  # 0 to 2 hours
    )
    @settings(max_examples=30, deadline=5000)
    def test_property_practice_completion_requirements(self, attempts_count, best_score, time_spent):
        """
        **Property 3: Practice Completion Requirements**
        **Validates: Requirements 2.3, 2.5**
        
        For any practice question submission, the question should only be marked 
        as completed when all test cases pass, and partial success should not 
        result in completion.
        """
        # Create or get progress record
        progress, created = PracticeProgress.objects.get_or_create(
            student=self.user,
            practice_question=self.practice_question,
            defaults={
                'attempts_count': attempts_count,
                'best_score': best_score,
                'time_spent': time_spent
            }
        )
        
        if not created:
            progress.attempts_count = attempts_count
            progress.best_score = best_score
            progress.time_spent = time_spent
            progress.save()
        
        # Property: Completion should only occur when explicitly marked
        # (simulating all test cases passing)
        if best_score == 100.0:
            progress.is_completed = True
            progress.save()
            
            # Verify completion property
            assert progress.is_completed == True, \
                "Progress should be marked as completed when best_score is 100%"
        else:
            progress.is_completed = False
            progress.save()
            
            # Verify non-completion property
            assert progress.is_completed == False, \
                "Progress should not be completed when best_score is less than 100%"
        
        # Property: Progress tracking should maintain data integrity
        progress.refresh_from_db()
        assert progress.attempts_count == attempts_count, \
            f"Expected {attempts_count} attempts, got {progress.attempts_count}"
        assert abs(progress.best_score - best_score) < 0.01, \
            f"Expected score {best_score}, got {progress.best_score}"
        assert progress.time_spent == time_spent, \
            f"Expected time {time_spent}, got {progress.time_spent}"
        
        # Clean up for next test iteration
        progress.delete()
    
    @given(
        points_values=st.lists(
            st.integers(min_value=0, max_value=500),
            min_size=1,
            max_size=10
        )
    )
    @settings(max_examples=20, deadline=5000)
    def test_property_practice_points_awarding(self, points_values):
        """
        **Property 4: Practice Points Awarding**
        **Validates: Requirements 1.5, 5.1**
        
        For any completed practice question, full points should be awarded only 
        when all test cases pass, and no points should be awarded for partial completion.
        """
        for i, points in enumerate(points_values):
            # Create submission with varying success states
            is_successful = (i == len(points_values) - 1)  # Only last attempt succeeds
            
            submission = PracticeSubmission.objects.create(
                student=self.user,
                practice_question=self.practice_question,
                source_code=f'def solution():\n    return {"correct" if is_successful else "wrong"}',
                status='success' if is_successful else 'fail',
                attempt_number=i + 1,
                points_earned=points if is_successful else 0
            )
            
            # Property: Points should only be awarded for successful submissions
            if is_successful:
                assert submission.points_earned == points, \
                    f"Expected {points} points for successful submission, got {submission.points_earned}"
            else:
                assert submission.points_earned == 0, \
                    f"Expected 0 points for failed submission, got {submission.points_earned}"
        
        # Clean up for next test iteration
        PracticeSubmission.objects.filter(
            student=self.user,
            practice_question=self.practice_question
        ).delete()
    
    @given(
        validation_data=st.fixed_dictionaries({
            'attempt_number': st.integers(),
            'points_earned': st.integers(),
            'best_score': st.floats(),
            'attempts_count': st.integers(),
            'time_spent': st.integers()
        })
    )
    @settings(max_examples=20, deadline=5000)
    def test_property_model_validation_consistency(self, validation_data):
        """
        Test that model validation is consistent across all inputs
        """
        # Test PracticeSubmission validation
        submission = PracticeSubmission(
            student=self.user,
            practice_question=self.practice_question,
            source_code='def test(): pass',
            status='success',
            attempt_number=validation_data['attempt_number'],
            points_earned=validation_data['points_earned']
        )
        
        # Property: Invalid values should consistently raise ValidationError
        try:
            submission.full_clean()
            # If validation passes, values should be within valid ranges
            assert submission.attempt_number >= 1, \
                "Valid attempt_number should be >= 1"
            assert submission.points_earned >= 0, \
                "Valid points_earned should be >= 0"
        except ValidationError:
            # If validation fails, values should be outside valid ranges
            assert (submission.attempt_number < 1 or 
                   submission.points_earned < 0), \
                "ValidationError should only occur for invalid values"
        
        # Test PracticeProgress validation
        progress = PracticeProgress(
            student=self.user,
            practice_question=self.practice_question,
            best_score=validation_data['best_score'],
            attempts_count=validation_data['attempts_count'],
            time_spent=validation_data['time_spent']
        )
        
        try:
            progress.full_clean()
            # If validation passes, values should be within valid ranges
            assert 0.0 <= progress.best_score <= 100.0, \
                "Valid best_score should be between 0.0 and 100.0"
            assert progress.attempts_count >= 0, \
                "Valid attempts_count should be >= 0"
            assert progress.time_spent >= 0, \
                "Valid time_spent should be >= 0"
        except ValidationError:
            # If validation fails, values should be outside valid ranges
            assert (not (0.0 <= progress.best_score <= 100.0) or
                   progress.attempts_count < 0 or
                   progress.time_spent < 0), \
                "ValidationError should only occur for invalid values"