from rest_framework import serializers
from .models import Class, Enrollment, Announcement, Comment
from users.serializers import UserSerializer


class ClassSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    student_count = serializers.IntegerField(read_only=True)
    assignment_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Class
        fields = ['id', 'name', 'section', 'owner', 'join_code',
                  'settings', 'created_at', 'updated_at',
                  'student_count', 'assignment_count']
        read_only_fields = ['id', 'join_code', 'created_at', 'updated_at', 'owner']
    
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class_obj = ClassSerializer(read_only=True)
    class_obj_id = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all(), 
        source='class_obj',
        write_only=True
    )
    
    class Meta:
        model = Enrollment
        fields = ['id', 'class_obj', 'class_obj_id', 'user', 'role',
                  'joined_at']
        read_only_fields = ['id', 'user', 'joined_at']


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'updated_at', 'announcement', 'assignment']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class AnnouncementSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Announcement
        fields = ['id', 'class_obj', 'author', 'content', 'is_pinned', 'created_at', 'updated_at', 'comments', 'comments_count']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at', 'comments', 'comments_count']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
