from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Q
from .models import Class, Enrollment, Module
from .serializers import ClassSerializer, EnrollmentSerializer
from django.contrib.auth import get_user_model
from submissions.models import GradebookEntry
from core.permissions import IsTeacher
from assignments.models import Assignment

User = get_user_model()


class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        archived = self.request.query_params.get('archived', None)
        
        enrollments = Enrollment.objects.filter(
            user=user
        ).values_list('class_obj_id', flat=True)
        
        owned_classes = Class.objects.filter(owner=user).values_list('id', flat=True)
        all_class_ids = list(set(list(enrollments) + list(owned_classes)))
        
        queryset = Class.objects.filter(id__in=all_class_ids)
        
        return queryset.select_related('owner').prefetch_related('enrollments').annotate(
            student_count=Count('enrollments', filter=Q(enrollments__role='student'), distinct=True),
            assignment_count=Count('modules__items', filter=Q(modules__items__type='assignment'), distinct=True)
        ).order_by('-created_at')
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'archive']:
            # Only teachers/admins can create/update classes
            return [IsAuthenticated(), IsTeacher()]
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
            # Removed is_archived check
            class_obj = Class.objects.get(join_code=join_code)
        except Class.DoesNotExist:
             return Response(
                {'message': 'Invalid join code'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Check if already enrolled
        enrollment, created = Enrollment.objects.get_or_create(
            class_obj=class_obj,
            user=request.user,
            defaults={
                'role': 'teacher' if request.user.role == 'teacher' else 'student',
            }
        )
        
        if not created:
             return Response(
                {'message': 'Already enrolled in this class'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return Response({
            'success': True,
            'message': 'Joined class successfully',
            'class': ClassSerializer(class_obj).data,
            'enrollment': EnrollmentSerializer(enrollment).data
        })

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        """Join a class using join code (legacy, requires ID)"""
        return self.join_by_code(request)
    
    # Archive action removed as is_archived field is gone
    
    @action(detail=True, methods=['get'])
    def people(self, request, pk=None):
        """Get class roster"""
        class_obj = self.get_object()
        enrollments = Enrollment.objects.filter(
            class_obj=class_obj
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

    @action(detail=True, methods=['get'])
    def grades(self, request, pk=None):
        """Get gradebook data (Assignments x Students)"""
        class_obj = self.get_object()
        
        # 1. Assignments (ContentItems of type assignment in this class)
        assignments = Assignment.objects.filter(module__class_obj=class_obj).order_by('created_at')
        assign_data = [{'id': a.id, 'title': a.title, 'points': a.points_total} for a in assignments]
        
        # 2. Students
        students = User.objects.filter(
            enrollments__class_obj=class_obj,
            enrollments__role='student'
        ).distinct().order_by('last_name', 'first_name')
        
        # 3. GradebookEntries
        entries = GradebookEntry.objects.filter(
            content_item__module__class_obj=class_obj
        ).values('student_id', 'content_item_id', 'final_score', 'status')
        
        # Map: student_id -> { content_item_id: score }
        grades_map = {}
        for entry in entries:
            s_id = entry['student_id']
            c_id = entry['content_item_id']
            if s_id not in grades_map: grades_map[s_id] = {}
            grades_map[s_id][c_id] = entry['final_score']
            
        # 4. Construct Roster
        roster = []
        for student in students:
            student_grades = grades_map.get(student.id, {})
            roster.append({
                'id': student.id,
                'name': f"{student.first_name} {student.last_name}",
                'email': student.email,
                'grades': student_grades
            })
            
        return Response({
            'assignments': assign_data,
            'roster': roster
        })


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Enrollment.objects.filter(
            user=self.request.user
        ).select_related('class_obj', 'user')
