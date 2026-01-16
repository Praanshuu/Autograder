from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.db.models import Q
from .models import Submission, TestResult
from .serializers import SubmissionSerializer, TestResultSerializer
from .services import execute_code
from assignments.models import Assignment, Question
from classes.models import Enrollment


class SubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        assignment_id = self.request.query_params.get('assignment_id', None)
        question_id = self.request.query_params.get('question_id', None)
        
        queryset = Submission.objects.select_related(
            'assignment', 'question', 'student'
        ).prefetch_related('test_results')
        
        if assignment_id:
            queryset = queryset.filter(assignment_id=assignment_id)
        
        if question_id:
            queryset = queryset.filter(question_id=question_id)
        
        # Students can only see their own submissions
        if user.role == 'student':
            queryset = queryset.filter(student=user)
        else:
            # Teachers/TAs can see all submissions in their classes
            enrolled_classes = Enrollment.objects.filter(
                user=user,
                status='active'
            ).values_list('class_obj_id', flat=True)
            queryset = queryset.filter(assignment__class_obj_id__in=enrolled_classes)
        
        return queryset
    
    def create(self, request, *args, **kwargs):
        if request.user.role != 'student':
            return Response(
                {'message': 'Only students can submit code'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        assignment = serializer.validated_data['assignment']
        question = serializer.validated_data['question']
        
        # Check if assignment is published
        if assignment.status != 'published':
            return Response(
                {'message': 'Assignment is not published'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check deadline
        now = timezone.now()
        is_late = now > assignment.due_date
        if is_late and not assignment.allow_late_submission:
            return Response(
                {'message': 'Submission deadline has passed'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check enrollment
        enrollment = Enrollment.objects.filter(
            class_obj=assignment.class_obj,
            user=request.user,
            status='active'
        ).exists()
        
        if not enrollment:
            return Response(
                {'message': 'Not enrolled in this class'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        submission, created = Submission.objects.update_or_create(
            assignment=assignment,
            question=question,
            student=request.user,
            defaults={
                'code_content': serializer.validated_data['code_content'],
                'language': serializer.validated_data['language'],
                'status': 'late' if is_late else 'submitted'
            }
        )
        
        serializer = self.get_serializer(submission)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=False, methods=['post'])
    def run_code(self, request):
        """Execute code against test cases (for testing before submission)"""
        code = request.data.get('code', '')
        language = request.data.get('language', '')
        test_cases = request.data.get('test_cases', [])
        
        if not code or not language or not test_cases:
            return Response(
                {'message': 'Code, language, and test_cases are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            results = execute_code(code, language, test_cases)
            return Response({
                'success': True,
                'data': results
            })
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=True, methods=['put', 'patch'])
    def grade(self, request, pk=None):
        """Grade a submission (Teacher/TA only)"""
        if request.user.role not in ['teacher', 'ta', 'admin']:
            return Response(
                {'message': 'Not authorized'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        submission = self.get_object()
        
        if 'final_score' in request.data:
            submission.final_score = request.data['final_score']
        if 'teacher_feedback' in request.data:
            submission.teacher_feedback = request.data['teacher_feedback']
        if 'manual_adjustment' in request.data:
            submission.manual_adjustment = request.data['manual_adjustment']
            submission.final_score = submission.auto_grade_score + submission.manual_adjustment
        
        submission.is_graded = True
        submission.save()
        
        return Response({
            'success': True,
            'data': SubmissionSerializer(submission).data
        })
    
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        """Publish grade to student (Teacher/Admin only)"""
        if request.user.role not in ['teacher', 'admin']:
            return Response(
                {'message': 'Not authorized'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        submission = self.get_object()
        submission.is_published = True
        submission.save()
        
        # Create notification
        from notifications.models import Notification
        Notification.objects.create(
            user=submission.student,
            type='grade_published',
            title='Grade Published',
            message=f'Your submission for "{submission.assignment.title}" has been graded',
            reference_link=f'/student/results/{submission.assignment.id}'
        )
        
        return Response({
            'success': True,
            'message': 'Grade published successfully',
            'data': SubmissionSerializer(submission).data
        })
    
    @action(detail=False, methods=['post'])
    def run_autograder(self, request):
        """Run autograder on all submissions for an assignment (Teacher/Admin only)"""
        if request.user.role not in ['teacher', 'admin']:
            return Response(
                {'message': 'Not authorized'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        assignment_id = request.data.get('assignment_id')
        if not assignment_id:
            return Response(
                {'message': 'assignment_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            assignment = Assignment.objects.get(id=assignment_id)
        except Assignment.DoesNotExist:
            return Response(
                {'message': 'Assignment not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Get all submissions for this assignment
        submissions = Submission.objects.filter(assignment=assignment)
        
        # TODO: Integrate with AI grading service
        # For now, this is a placeholder
        # In production, this would:
        # 1. Execute code against test cases
        # 2. Get AI feedback
        # 3. Calculate auto_grade_score
        # 4. Update submissions
        
        return Response({
            'success': True,
            'message': 'Autograder queued for execution',
            'submissions_count': submissions.count()
        })
    
    @action(detail=False, methods=['post'], url_path='start-timer')
    def start_timer(self, request):
        """Start or resume timer for a question"""
        if request.user.role != 'student':
            return Response(
                {'message': 'Only students can track time'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        assignment_id = request.data.get('assignment_id')
        question_id = request.data.get('question_id')
        
        if not assignment_id or not question_id:
            return Response(
                {'message': 'assignment_id and question_id are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            assignment = Assignment.objects.get(id=assignment_id)
            question = Question.objects.get(id=question_id)
        except (Assignment.DoesNotExist, Question.DoesNotExist):
            return Response(
                {'message': 'Assignment or Question not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Get or create submission for tracking
        submission, created = Submission.objects.get_or_create(
            assignment=assignment,
            question=question,
            student=request.user,
            defaults={
                'code_content': '',
                'language': 'python',
                'started_at': timezone.now(),
                'last_activity_at': timezone.now()
            }
        )
        
        if not submission.started_at:
            submission.started_at = timezone.now()
        
        submission.last_activity_at = timezone.now()
        submission.save()
        
        return Response({
            'success': True,
            'data': {
                'started_at': submission.started_at,
                'time_spent': submission.time_spent,
                'last_activity_at': submission.last_activity_at
            }
        })
    
    @action(detail=False, methods=['post'], url_path='update-timer')
    def update_timer(self, request):
        """Update time spent on a question"""
        if request.user.role != 'student':
            return Response(
                {'message': 'Only students can track time'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        assignment_id = request.data.get('assignment_id')
        question_id = request.data.get('question_id')
        time_spent = request.data.get('time_spent', 0)  # in seconds
        
        if not assignment_id or not question_id:
            return Response(
                {'message': 'assignment_id and question_id are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            submission = Submission.objects.get(
                assignment_id=assignment_id,
                question_id=question_id,
                student=request.user
            )
        except Submission.DoesNotExist:
            return Response(
                {'message': 'Submission not found. Start timer first.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        submission.time_spent = time_spent
        submission.last_activity_at = timezone.now()
        submission.save()
        
        return Response({
            'success': True,
            'data': {
                'time_spent': submission.time_spent,
                'last_activity_at': submission.last_activity_at
            }
        })
    
    @action(detail=False, methods=['get'], url_path='get-timer')
    def get_timer(self, request):
        """Get current timer state for a question"""
        if request.user.role != 'student':
            return Response(
                {'message': 'Only students can track time'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        assignment_id = request.query_params.get('assignment_id')
        question_id = request.query_params.get('question_id')
        
        if not assignment_id or not question_id:
            return Response(
                {'message': 'assignment_id and question_id are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            submission = Submission.objects.get(
                assignment_id=assignment_id,
                question_id=question_id,
                student=request.user
            )
            
            return Response({
                'success': True,
                'data': {
                    'started_at': submission.started_at,
                    'time_spent': submission.time_spent,
                    'last_activity_at': submission.last_activity_at,
                    'code_content': submission.code_content
                }
            })
        except Submission.DoesNotExist:
            return Response({
                'success': True,
                'data': {
                    'started_at': None,
                    'time_spent': 0,
                    'last_activity_at': None,
                    'code_content': ''
                }
            })
