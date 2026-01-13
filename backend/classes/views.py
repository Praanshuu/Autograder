from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Class, Enrollment
from .serializers import ClassSerializer, EnrollmentSerializer


class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        archived = self.request.query_params.get('archived', None)
        
        # Get classes user is enrolled in or owns
        enrollments = Enrollment.objects.filter(
            user=user,
            status='active'
        ).values_list('class_obj_id', flat=True)
        
        owned_classes = Class.objects.filter(owner=user).values_list('id', flat=True)
        all_class_ids = list(set(list(enrollments) + list(owned_classes)))
        
        queryset = Class.objects.filter(id__in=all_class_ids)
        
        if archived is not None:
            queryset = queryset.filter(is_archived=(archived.lower() == 'true'))
        
        return queryset.select_related('owner').prefetch_related('enrollments')
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'archive']:
            # Only teachers/admins can create/update classes
            return [IsAuthenticated()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # Auto-enroll creator as teacher
        Enrollment.objects.create(
            class_obj=serializer.instance,
            user=self.request.user,
            role='teacher'
        )
    
    @action(detail=False, methods=['post'], url_path='join-by-code')
    def join_by_code(self, request):
        """Join a class using join code (no class ID needed)"""
        join_code = request.data.get('join_code', '').strip()
        
        if not join_code:
            return Response(
                {'message': 'Join code is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            class_obj = Class.objects.get(join_code=join_code, is_archived=False)
        except Class.DoesNotExist:
             return Response(
                {'message': 'Invalid join code or class is archived'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Check if already enrolled
        enrollment, created = Enrollment.objects.get_or_create(
            class_obj=class_obj,
            user=request.user,
            defaults={
                'role': 'teacher' if request.user.role == 'teacher' else 'student',
                'status': 'active'
            }
        )
        
        if not created:
            if enrollment.status == 'active':
                return Response(
                    {'message': 'Already enrolled in this class'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                enrollment.status = 'active'
                enrollment.save()
        
        return Response({
            'success': True,
            'message': 'Joined class successfully',
            'class': ClassSerializer(class_obj).data,
            'enrollment': EnrollmentSerializer(enrollment).data
        })

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        """Join a class using join code (legacy, requires ID)"""
        # ... logic if needed, or deprecate
        return self.join_by_code(request)
    
    @action(detail=True, methods=['post'])
    def archive(self, request, pk=None):
        """Archive or unarchive a class"""
        class_obj = self.get_object()
        
        if class_obj.owner != request.user and request.user.role != 'admin':
            return Response(
                {'message': 'Not authorized'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        class_obj.is_archived = not class_obj.is_archived
        class_obj.save()
        
        return Response({
            'success': True,
            'data': ClassSerializer(class_obj).data
        })
    
    @action(detail=True, methods=['get'])
    def people(self, request, pk=None):
        """Get class roster"""
        class_obj = self.get_object()
        enrollments = Enrollment.objects.filter(
            class_obj=class_obj,
            status='active'
        ).select_related('user')
        
        people = []
        for enrollment in enrollments:
            people.append({
                'id': enrollment.user.id,
                'name': f"{enrollment.user.first_name} {enrollment.user.last_name}",
                'email': enrollment.user.email,
                'avatar_url': enrollment.user.avatar_url,
                'role': enrollment.role,
                'joined_at': enrollment.joined_at
            })
        
        return Response({
            'success': True,
            'data': people
        })


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Enrollment.objects.filter(
            user=self.request.user,
            status='active'
        ).select_related('class_obj', 'user')
