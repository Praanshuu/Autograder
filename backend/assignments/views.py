from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Assignment, Question, TestCase
from .serializers import AssignmentSerializer, QuestionSerializer, TestCaseSerializer
from classes.models import Enrollment


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        class_id = self.request.query_params.get('class_id', None)
        status_filter = self.request.query_params.get('status', None)
        
        queryset = Assignment.objects.select_related('class_obj', 'created_by').prefetch_related('questions')
        
        if class_id:
            queryset = queryset.filter(class_obj_id=class_id)
        
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        # Students can only see published assignments from classes they are enrolled in
        if user.role == 'student':
            enrolled_classes = Enrollment.objects.filter(
                user=user,
                status='active'
            ).values_list('class_obj_id', flat=True)
            
            queryset = queryset.filter(
                status='published',
                class_obj_id__in=enrolled_classes
            )
        else:
            # Teachers/TAs can see all assignments in their classes
            enrolled_classes = Enrollment.objects.filter(
                user=user,
                status='active'
            ).values_list('class_obj_id', flat=True)
            queryset = queryset.filter(
                Q(class_obj_id__in=enrolled_classes) | Q(created_by=user)
            )
        
        return queryset
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'publish', 'close']:
            # Only teachers/admins can modify assignments
            return [IsAuthenticated()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        """Publish an assignment"""
        assignment = self.get_object()
        
        if assignment.created_by != request.user and request.user.role != 'admin':
            return Response(
                {'message': 'Not authorized'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        assignment.status = 'published'
        assignment.save()
        
        return Response({
            'success': True,
            'data': AssignmentSerializer(assignment).data
        })
    
    @action(detail=True, methods=['post'])
    def close(self, request, pk=None):
        """Close an assignment"""
        assignment = self.get_object()
        
        if assignment.created_by != request.user and request.user.role != 'admin':
            return Response(
                {'message': 'Not authorized'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        assignment.status = 'closed'
        assignment.save()
        
        return Response({
            'success': True,
            'data': AssignmentSerializer(assignment).data
        })


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [IsAuthenticated]
