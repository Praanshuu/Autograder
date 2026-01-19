from rest_framework import serializers
from .models import Assignment, Question, TestCase
from classes.models import Class
from classes.serializers import ClassSerializer
from users.serializers import UserSerializer


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id', 'input', 'expected_output', 'is_hidden', 'points']


class QuestionSerializer(serializers.ModelSerializer):
    test_cases = TestCaseSerializer(many=True, read_only=True)
    test_case_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=TestCase.objects.all(),
        source='test_cases',
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'hint', 'difficulty', 'test_cases',
                  'test_case_ids', 'time_limit', 'memory_limit', 'allowed_languages', 
                  'starter_code', 'order']
    
    def create(self, validated_data):
        test_cases = validated_data.pop('test_cases', [])
        question = Question.objects.create(**validated_data)
        question.test_cases.set(test_cases)
        return question


class AssignmentSerializer(serializers.ModelSerializer):
    class_obj = ClassSerializer(read_only=True)
    class_obj_id = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all(),
        source='class_obj',
        write_only=True
    )
    questions = QuestionSerializer(many=True, read_only=True)
    question_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Question.objects.all(),
        source='questions',
        write_only=True,
        required=False
    )
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Assignment
        fields = ['id', 'class_obj', 'class_obj_id', 'title', 'description',
                  'due_date', 'points', 'status', 'questions', 'question_ids',
                  'allow_late_submission', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        questions = validated_data.pop('questions', [])
        validated_data['created_by'] = self.context['request'].user
        assignment = Assignment.objects.create(**validated_data)
        assignment.questions.set(questions)
        return assignment
