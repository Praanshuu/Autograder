from rest_framework import serializers
from .models import Submission, TestResult
from assignments.serializers import AssignmentSerializer, QuestionSerializer, TestCaseSerializer
from users.serializers import UserSerializer


class TestResultSerializer(serializers.ModelSerializer):
    test_case = TestCaseSerializer(read_only=True)
    
    class Meta:
        model = TestResult
        fields = ['id', 'test_case', 'status', 'execution_time', 'memory_usage',
                  'console_output', 'error_message', 'points_earned']


class SubmissionSerializer(serializers.ModelSerializer):
    assignment = AssignmentSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)
    student = UserSerializer(read_only=True)
    test_results = TestResultSerializer(many=True, read_only=True)
    
    class Meta:
        model = Submission
        fields = ['id', 'assignment', 'question', 'student', 'code_content',
                  'language', 'submitted_at', 'status', 'test_results',
                  'auto_grade_score', 'manual_adjustment', 'final_score',
                  'teacher_feedback', 'ai_feedback', 'is_graded', 'is_published',
                  'created_at', 'updated_at', 'time_spent', 'feedback_tags']
        read_only_fields = ['id', 'student', 'submitted_at', 'test_results',
                          'auto_grade_score', 'is_graded', 'is_published',
                          'created_at', 'updated_at']
