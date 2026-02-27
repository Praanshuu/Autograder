from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Q
from .models import Class, Enrollment, Module, Announcement, Comment
from .serializers import ClassSerializer, EnrollmentSerializer, AnnouncementSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from submissions.models import GradebookEntry, SubmissionAttempt
from core.permissions import IsTeacher
from assignments.models import Assignment, AssignmentQuestion

User = get_user_model()
from django.core.mail import send_mail
from django.conf import settings
from notifications.models import Notification


class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        archived = self.request.query_params.get('archived', 'false').lower() == 'true'
        
        enrollments = Enrollment.objects.filter(
            user=user
        ).values_list('class_obj_id', flat=True)
        
        owned_classes = Class.objects.filter(owner=user).values_list('id', flat=True)
        all_class_ids = list(set(list(enrollments) + list(owned_classes)))
        
        queryset = Class.objects.filter(id__in=all_class_ids)
        
        if self.action == 'list':
            queryset = queryset.filter(is_archived=archived)
        
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

        # Check for enrollment lock
        settings = class_obj.settings or {}
        if settings.get('enrollment_locked', False):
             return Response(
                {'message': 'Enrollment is currently locked for this class.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Check if already enrolled
        enrollment, created = Enrollment.objects.get_or_create(
            class_obj=class_obj,
            user=request.user,
            defaults={
                'role': request.user.role if request.user.role in ['teacher', 'ta'] else 'student',
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

    @action(detail=True, methods=['post'], url_path='regenerate-code')
    def regenerate_code(self, request, pk=None):
        """Regenerate the join code for a class"""
        class_obj = self.get_object()
        
        # Only owner/teacher can regenerate
        if class_obj.owner != request.user:
             return Response(
                {'message': 'Not authorized. Only the class owner can regenerate the code.'},
                status=status.HTTP_403_FORBIDDEN
            )
            
        from .models import generate_join_code
        new_code = generate_join_code()
        # Ensure uniqueness (simple retry)
        while Class.objects.filter(join_code=new_code).exists():
            new_code = generate_join_code()
            
        class_obj.join_code = new_code
        class_obj.save()
        
        return Response({
            'success': True,
            'message': 'Join code regenerated successfully',
            'join_code': new_code
        })
    
    @action(detail=True, methods=['post'])
    def archive(self, request, pk=None):
        """Archive or Unarchive a class"""
        class_obj = self.get_object()
        
        # Only owner can archive
        if class_obj.owner != request.user:
             return Response(
                {'message': 'Not authorized. Only the class owner can archive.'},
                status=status.HTTP_403_FORBIDDEN
            )
            
        # Toggle status
        class_obj.is_archived = not class_obj.is_archived
        class_obj.save()
        
        return Response({
            'success': True,
            'message': f"Class {'archived' if class_obj.is_archived else 'unarchived'} successfully",
            'class': ClassSerializer(class_obj).data
        })
    
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

    @action(detail=True, methods=['post'], url_path='add-member')
    def add_member(self, request, pk=None):
        """Add a member (TA or Student) by email manually"""
        class_obj = self.get_object()
        
        # Only owner or teacher can add members
        is_owner = class_obj.owner == request.user
        is_teacher = Enrollment.objects.filter(class_obj=class_obj, user=request.user, role='teacher').exists()
        
        if not (is_owner or is_teacher):
             return Response({'message': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)

        email = request.data.get('email')
        role = request.data.get('role', 'student')
        
        if not email:
            return Response({'message': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if role not in ['student', 'ta', 'teacher']:
             return Response({'message': 'Invalid role'}, status=status.HTTP_400_BAD_REQUEST)
             
        user_created = False
        users_found = User.objects.filter(email=email)
        
        if users_found.exists():
            user_to_add = users_found.first()
        else:
            # Create new user
            from django.utils.crypto import get_random_string
            username = email.split('@')[0] + '_' + get_random_string(4)
            # Ensure username is unique
            while User.objects.filter(username=username).exists():
                username = email.split('@')[0] + '_' + get_random_string(4)
                
            user_to_add = User.objects.create_user(
                username=username,
                email=email,
                password=get_random_string(32), # Random complex password
                first_name='Invited',
                last_name='User',
                role=role if role in ['ta', 'teacher'] else 'student' # Set initial role
            )
            user_created = True
        
        # Check if already enrolled
        if Enrollment.objects.filter(class_obj=class_obj, user=user_to_add).exists():
             return Response({'message': 'User already enrolled'}, status=status.HTTP_400_BAD_REQUEST)
             
        Enrollment.objects.create(
            class_obj=class_obj,
            user=user_to_add,
            role=role
        )

        # Send Email Invitation
        try:
            role_display = 'Teaching Assistant' if role == 'ta' else role.capitalize()
            
            if user_created:
                # Generate Password Reset Token
                from django.contrib.auth.tokens import default_token_generator
                from django.utils.http import urlsafe_base64_encode
                from django.utils.encoding import force_bytes
                
                uid = urlsafe_base64_encode(force_bytes(user_to_add.pk))
                token = default_token_generator.make_token(user_to_add)
                reset_link = f"http://localhost:5173/reset-password/{uid}/{token}"
                
                subject = f'Welcome to Autograder - Invitation to join {class_obj.name}'
                message = (
                    f'Hello,\n\n'
                    f'You have been invited to join the class "{class_obj.name}" as a {role_display}.\n\n'
                    f'An account has been created for you. Please click the link below to set your password and log in:\n\n'
                    f'{reset_link}\n\n'
                    f'If you did not expect this invitation, please ignore this email.'
                )
            else:
                subject = f'Invitation to join {class_obj.name}'
                message = (
                    f'Hello {user_to_add.first_name},\n\n'
                    f'You have been added to the class "{class_obj.name}" as a {role_display}.\n\n'
                    f'Log in to view your class: http://localhost:5173/login'
                )

            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user_to_add.email],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Failed to send email: {e}")

        # Create In-App Notification
        try:
            Notification.objects.create(
                user=user_to_add,
                type='invite',
                title=f'Added to {class_obj.name}',
                message=f'You have been added to {class_obj.name} as a {role_display}.',
                reference_link=f'/student/class/{class_obj.id}' if role == 'student' else f'/teacher/class/{class_obj.id}'
            )
        except Exception as e:
             print(f"Failed to create notification: {e}")
        
        return Response({'success': True, 'message': f'Added {user_to_add.email} as {role}'})

    @action(detail=True, methods=['delete'], url_path='remove-member')
    def remove_member(self, request, pk=None):
        """Remove a member from the class"""
        class_obj = self.get_object()

        # Only owner or teacher can remove members
        is_owner = class_obj.owner == request.user
        is_teacher = Enrollment.objects.filter(class_obj=class_obj, user=request.user, role='teacher').exists()

        if not (is_owner or is_teacher):
            return Response({'message': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)

        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'message': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Cannot remove the class owner
        if class_obj.owner_id == int(user_id):
            return Response({'message': 'Cannot remove the class owner'}, status=status.HTTP_400_BAD_REQUEST)

        # Cannot remove yourself
        if request.user.id == int(user_id):
            return Response({'message': 'You cannot remove yourself from the class'}, status=status.HTTP_400_BAD_REQUEST)

        deleted_count, _ = Enrollment.objects.filter(class_obj=class_obj, user_id=user_id).delete()

        if deleted_count == 0:
            return Response({'message': 'Member not found in this class'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'success': True, 'message': 'Member removed from class'})

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
            s_id = str(entry['student_id'])
            c_id = str(entry['content_item_id'])
            if s_id not in grades_map: grades_map[s_id] = {}
            grades_map[s_id][c_id] = entry['final_score']
            
        # 4. Construct Roster
        roster = []
        for student in students:
            student_grades = grades_map.get(str(student.id), {})
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

    @action(detail=True, methods=['get'], url_path='student-topic-grades')
    def student_topic_grades(self, request, pk=None):
        """
        Get aggregated grades by topic (tags) for a student in this class.
        """
        class_obj = self.get_object()
        student_id = request.query_params.get('student_id')
        
        if not student_id:
            return Response({'message': 'Student ID is required'}, status=status.HTTP_400_BAD_REQUEST)
            
        # Verify student is enrollment in class
        if not Enrollment.objects.filter(class_obj=class_obj, user_id=student_id, role='student').exists():
             return Response({'message': 'Student not found in this class'}, status=status.HTTP_404_NOT_FOUND)

        # Get all attempts for this student in this class
        # Path: Attempt -> AssignmentQuestion -> Assignment -> Module -> Class
        attempts = SubmissionAttempt.objects.filter(
            student_id=student_id,
            assignment_question__assignment__module__class_obj=class_obj
            # status='success' <-- REMOVED to include failed attempts
        ).select_related('assignment_question__question')
        
        # We need "Latest Attempt" per Question to avoid counting multiple attempts for same question
        # Group by AssignmentQuestion
        latest_attempts = {}
        for attempt in attempts:
            aq_id = attempt.assignment_question_id
            # If we haven't seen this AQ or this attempt is newer
            if aq_id not in latest_attempts or attempt.created_at > latest_attempts[aq_id].created_at:
                latest_attempts[aq_id] = attempt
                
        # Now aggregate by Tag
        tag_stats = {} # { tag: { total_score: 0, count: 0 } }
        
        for attempt in latest_attempts.values():
            question = attempt.assignment_question.question
            tags = question.tags or [] # List of strings
            
            # Calculate percentage score for this attempt
            aq = attempt.assignment_question
            max_points = aq.custom_points if aq.custom_points is not None else 10
            if max_points <= 0: max_points = 10
            
            if attempt.manual_score is not None:
                # Normalize to 0-100
                score = (attempt.manual_score / max_points) * 100
            else:
                score = 100 if attempt.status == 'success' else 0
            
            # Cap at 100
            if score > 100: score = 100
            
            # If no tags, maybe categorize as "Uncategorized"?
            if not tags:
                tags = ["General"]
                
            for tag in tags:
                if tag not in tag_stats:
                    tag_stats[tag] = {'total_score': 0, 'count': 0}
                tag_stats[tag]['total_score'] += score
                tag_stats[tag]['count'] += 1
                
        # Format for response
        results = []
        for tag, stats in tag_stats.items():
            results.append({
                'topic': tag,
                'score': round(stats['total_score'] / stats['count']),
                'questions_count': stats['count']
            })
            
        return Response(results)


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Enrollment.objects.filter(
            user=self.request.user
        ).select_related('class_obj', 'user')


class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        class_id = self.request.query_params.get('class_id')
        if class_id:
             # Ensure user is enrolled or owner
             # For now, simplistic check or reliance on frontend passing valid IDs
             return Announcement.objects.filter(class_obj_id=class_id).select_related('author').annotate(
                 comments_count=Count('comments', distinct=True)
             ).order_by('-is_pinned', '-created_at')
        return Announcement.objects.none()
    
    def perform_create(self, serializer):
        # In a real app, verify user has permission to post in this class
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
         announcement_id = self.request.query_params.get('announcement_id')
         assignment_id = self.request.query_params.get('assignment_id')
         
         queryset = Comment.objects.select_related('author').order_by('created_at')
         
         if announcement_id:
             return queryset.filter(announcement_id=announcement_id)
         if assignment_id:
             return queryset.filter(assignment_id=assignment_id)
             
         return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
