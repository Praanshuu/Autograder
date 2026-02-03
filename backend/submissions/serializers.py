from rest_framework import serializers
from .models import SubmissionAttempt, AssignmentProgress, TestResult, GradebookEntry
from assignments.serializers import AssignmentQuestionSerializer
from users.serializers import UserSerializer


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ['id', 'test_case_id', 'status', 'score', 'actual_output', 'error_message']


class SubmissionAttemptSerializer(serializers.ModelSerializer):
    assignment_question = AssignmentQuestionSerializer(read_only=True)
    student = UserSerializer(read_only=True)
    test_results = TestResultSerializer(many=True, read_only=True)
    
    # Flattened/Convenience fields for frontend
    question = serializers.SerializerMethodField()
    final_score = serializers.SerializerMethodField()
    is_graded = serializers.SerializerMethodField()
    feedback_tags = serializers.SerializerMethodField()
    assignment_id = serializers.UUIDField(source='assignment_question.assignment.id', read_only=True)
    assignment_title = serializers.CharField(source='assignment_question.assignment.title', read_only=True)
    code_content = serializers.CharField(source='source_code', read_only=True)
    time_spent = serializers.SerializerMethodField()

    class Meta:
        model = SubmissionAttempt
        fields = ['id', 'assignment_question', 'question', 'attempt_number', 'status', 
                  'test_results', 'created_at', 'student', 'final_score', 'is_graded', 
                  'feedback_tags', 'assignment_id', 'assignment_title', 'manual_score', 'feedback_text', 
                  'code_content', 'time_spent']

    def get_question(self, obj):
        from assignments.serializers import QuestionSerializer
        return QuestionSerializer(obj.assignment_question.question).data

    def get_final_score(self, obj):
        # Return manual score if present
        if obj.manual_score is not None:
             return obj.manual_score

        # Calculate score based on passed test cases
        # This is a naive implementation; real logic might depend on custom_points
        results = obj.test_results.all()
        if not results:
            return 0
        
        # Calculate percentage of passed tests
        passed = sum(1 for r in results if r.status == 'pass')
        total = len(results)
        
        if total == 0:
            return 0
            
        return round((passed / total) * 100)

    def get_time_spent(self, obj):
        # Fetch draft progress to get time spent
        progress = AssignmentProgress.objects.filter(
            assignment_question=obj.assignment_question,
            student=obj.student
        ).first()
        return progress.time_spent if progress else 0

    def get_is_graded(self, obj):
        return obj.status in ['success', 'fail']

    def get_feedback_tags(self, obj):
        return "" # Placeholder


class AssignmentProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentProgress
        fields = ['assignment_question', 'current_code', 'time_spent', 'last_updated']


class GradebookEntrySerializer(serializers.ModelSerializer):
    """Serializer for gradebook entries including points information"""
    student = UserSerializer(read_only=True)
    content_item_title = serializers.CharField(source='content_item.title', read_only=True)
    content_item_type = serializers.CharField(source='content_item.content_type', read_only=True)
    
    class Meta:
        model = GradebookEntry
        fields = ['id', 'student', 'content_item', 'content_item_title', 'content_item_type',
                  'final_score', 'points_earned', 'status', 'updated_at']
