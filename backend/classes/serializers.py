from rest_framework import serializers
from .models import Class, Enrollment
from users.serializers import UserSerializer


class ClassSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    
    class Meta:
        model = Class
        fields = ['id', 'name', 'section', 'subject', 'room', 'description',
                  'theme_color', 'bg_pattern', 'owner', 'join_code',
                  'is_archived', 'semester', 'start_date', 'end_date',
                  'created_at', 'updated_at']
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
        fields = ['id', 'class_obj', 'class_obj_id', 'user', 'role', 'status',
                  'joined_at', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'joined_at', 'created_at', 'updated_at']
