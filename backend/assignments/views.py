from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Assignment, Question
from .serializers import AssignmentSerializer, QuestionSerializer
from classes.models import Enrollment


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        class_id = self.request.query_params.get('class_id', None)
        
        # Select related module -> class for filtering
        queryset = Assignment.objects.select_related('module__class_obj').prefetch_related('questions')
        
        if class_id:
            queryset = queryset.filter(module__class_obj_id=class_id)
            
        # Filter for student visualization (only published)
        if user.role == 'student':
            enrolled_classes = Enrollment.objects.filter(
                user=user
            ).values_list('class_obj_id', flat=True)
            
            queryset = queryset.filter(
                is_published=True,
                module__class_obj_id__in=enrolled_classes
            )
        else:
            # Teachers/TAs can see all in their classes
            enrolled_classes = Enrollment.objects.filter(
                user=user
            ).values_list('class_obj_id', flat=True)
            
            # Teachers can see drafts
            queryset = queryset.filter(module__class_obj_id__in=enrolled_classes)
        
        return queryset
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'publish', 'close']:
            # Only teachers/admins can modify assignments
            # Permissions logic can be refined to check specific class ownership
            return [IsAuthenticated()]
        return [IsAuthenticated()]
    
    def create(self, request, *args, **kwargs):
        # Handle 'class_obj_id' from frontend -> 'module' for backend
        class_id = request.data.get('class_obj_id')
        if class_id and 'module' not in request.data:
            from classes.models import Module, Class
            # Find/Create a default module for this class
            # For now, just grab the first module or create "Default"
            try:
                print(f"DEBUG: Looking for Class ID: {class_id} (Type: {type(class_id)})")
                class_obj = Class.objects.get(id=class_id)
                module, _ = Module.objects.get_or_create(
                    class_obj=class_obj,
                    defaults={'title': 'Assignments', 'order_index': 0}
                )
                request.data['module'] = module.id
            except Class.DoesNotExist:
                print(f"DEBUG: Class {class_id} not found!")
                return Response(
                    {'message': 'Invalid Class ID'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            except Exception as e:
                print(f"DEBUG: Error finding class: {e}")
                return Response(
                    {'message': f'Error finding class: {str(e)}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        # Ensure 'type' is set to 'assignment'
        if 'type' not in request.data:
            request.data['type'] = 'assignment'

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        assignment = serializer.save()
        
        # Handle question_ids linkage
        question_ids = self.request.data.get('question_ids', [])
        if question_ids:
            from .models import AssignmentQuestion, Question
            for index, q_id in enumerate(question_ids):
                try:
                    question = Question.objects.get(id=q_id)
                    AssignmentQuestion.objects.create(
                        assignment=assignment,
                        question=question,
                        order=index
                    )
                except Question.DoesNotExist:
                    pass # Ignore invalid question IDs
    
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        """Publish an assignment"""
        assignment = self.get_object()
        
        # Check authorization relative to class owner/teacher
        class_owner = assignment.module.class_obj.owner
        if class_owner != request.user and request.user.role not in ['admin', 'teacher']:
             return Response(
                {'message': 'Not authorized'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        assignment.is_published = True
        assignment.save()
        
        return Response({
            'success': True,
            'data': AssignmentSerializer(assignment).data
        })
    
    @action(detail=True, methods=['post'])
    def close(self, request, pk=None):
        """Close an assignment (unpublish or set due date passed?)"""
        # "Closed" state doesn't exist in boolean is_published.
        # Maybe set is_published = False? Or we need a status Enum?
        # Schema v3 ContentItem has is_published (Bool).
        # Assignment has mode (Practice/Exam).
        # Maybe "Close" means unpublish?
        
        assignment = self.get_object()
        
        if assignment.module.class_obj.owner != request.user and request.user.role != 'admin':
            return Response(
                {'message': 'Not authorized'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        assignment.is_published = False
        assignment.save()
        
        return Response({
            'success': True,
            'data': AssignmentSerializer(assignment).data
        })


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
