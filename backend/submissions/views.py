from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import SubmissionAttempt, AssignmentProgress, TestResult
from .serializers import SubmissionAttemptSerializer, AssignmentProgressSerializer
from .services import execute_code
from assignments.models import AssignmentQuestion
import logging

logger = logging.getLogger(__name__)

class SubmissionAttemptViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionAttemptSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['created_at', 'status', 'final_score', 'student__username']
    filterset_fields = ['status', 'student']
    
    def get_queryset(self):
        user = self.request.user
        queryset = SubmissionAttempt.objects.all()
        
        # Filter by Assignment ID (via AssignmentQuestion)
        assignment_id = self.request.query_params.get('assignment_id')
        if assignment_id:
            queryset = queryset.filter(assignment_question__assignment_id=assignment_id)
            
        if user.role == 'student':
            queryset = queryset.filter(student=user)
            
        return queryset
        
    def create(self, request, *args, **kwargs):
        assignment_question_id = request.data.get('assignment_question_id')
        code = request.data.get('code_content') # Client sends code_content
        
        if not assignment_question_id or code is None:
             return Response({'message': 'Missing data'}, status=status.HTTP_400_BAD_REQUEST)
             
        try:
            aq = AssignmentQuestion.objects.get(id=assignment_question_id)
        except AssignmentQuestion.DoesNotExist:
            return Response({'message': 'Invalid assignment question'}, status=status.HTTP_404_NOT_FOUND)

        # Check for existing successful attempt
        if SubmissionAttempt.objects.filter(student=request.user, assignment_question=aq, status='success').exists():
            return Response({'message': 'You have already successfully completed this question.'}, status=status.HTTP_400_BAD_REQUEST)
            
        # Create Attempt
        attempt = SubmissionAttempt.objects.create(
            student=request.user,
            assignment_question=aq,
            attempt_number=SubmissionAttempt.objects.filter(student=request.user, assignment_question=aq).count() + 1,
            status='processing'
        )
        
        # Execute Code
        # aq.question.test_cases is JSON now
        test_cases = aq.question.test_cases
        language = 'python' # TODO: Get from request or config
        
        # We need to adapt the execute_code service to handle the JSON test cases
        # Structure is list of dicts: {'input': '', 'output': ''}
        
        # Map JSON test cases to format expected by service (if different)
        # Service expects list of dicts.
        
        try:
            results = execute_code(code, language, test_cases)
            
            # Save Results
            passed_count = 0
            for idx, res in enumerate(results):
                status_res = res.get('status', 'fail')
                if status_res == 'pass': passed_count += 1
                
                TestResult.objects.create(
                    attempt=attempt,
                    test_case_id=str(idx),
                    status=status_res,
                    score=1 if status_res == 'pass' else 0
                )
            
            attempt.status = 'success'
            attempt.save()
            
            serializer = self.get_serializer(attempt)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            attempt.status = 'error'
            attempt.save()
            logger.error(f"Execution failed: {e}")
            return Response({'message': 'Execution failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'], url_path='run')
    def run_code(self, request):
        """
        Run code in sandbox without saving submission.
        Expects: code, language, test_cases, question_id
        """
        code = request.data.get('code')
        language = request.data.get('language', 'python')
        test_cases = request.data.get('test_cases', [])
        
        if not code:
             return Response({'message': 'Missing code'}, status=status.HTTP_400_BAD_REQUEST)
             
        try:
            results = execute_code(code, language, test_cases)
            
            formatted_results = []
            for r in results:
                formatted_results.append({
                    'actual_output': r.get('console_output'),
                    'expected_output': r.get('test_case', {}).get('output') if isinstance(r.get('test_case'), dict) else '',
                    'passed': r.get('status') == 'pass',
                    'error': r.get('error_message') if r.get('status') in ['error', 'timeout'] else None,
                    'status': r.get('status'),
                    'test_case': r.get('test_case')
                })

            response_data = {
                'summary': {
                    'execution_successful': True,
                    'has_output': any(r.get('console_output') for r in results)
                },
                'results': formatted_results
            }
            
            return Response({'data': response_data})
            
        except Exception as e:
            logger.error(f"Sandbox execution failed: {e}")
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AssignmentProgressViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentProgressSerializer
    permission_classes = [IsAuthenticated]
    queryset = AssignmentProgress.objects.all()
    
    def get_queryset(self):
        return AssignmentProgress.objects.filter(student=self.request.user)
    
    def perform_create(self, serializer):
        # Update or create logic is better handled by frontend calling a specific endpoint or us overriding create
        # Here we assume POST creates/updates
        pass
        
    @action(detail=False, methods=['post'], url_path='autosave')
    def autosave(self, request):
        aq_id = request.data.get('assignment_question_id')
        code = request.data.get('current_code')
        
        if not aq_id:
            return Response({'message': 'Missing ID'}, status=status.HTTP_400_BAD_REQUEST)
            
        progress, created = AssignmentProgress.objects.update_or_create(
            student=request.user,
            assignment_question_id=aq_id,
            defaults={'current_code': code}
        )
        
        return Response({'success': True})

    @action(detail=False, methods=['post'], url_path='start-timer')
    def start_timer(self, request):
        aq_id = request.data.get('assignment_question_id')
        # Fallback for inconsistent frontend payload if needed, 
        # but let's assume we fixed it to send assignment_question_id
        if not aq_id:
             # Try getting it from query params or other fields if legacy
             aq_id = request.data.get('question_id') # Legacy handling if it maps to AQ ID
        
        if not aq_id:
            return Response({'message': 'Missing ID'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure Progress exists
        progress, created = AssignmentProgress.objects.get_or_create(
            student=request.user,
            assignment_question_id=aq_id
        )
        
        if not progress.started_at:
            progress.started_at = timezone.now()
            progress.save()
            
        return Response({
            'success': True, 
            'started_at': progress.started_at,
            'time_spent': progress.time_spent
        })

    @action(detail=False, methods=['post'], url_path='update-timer')
    def update_timer(self, request):
        aq_id = request.data.get('assignment_question_id')
        time_spent = request.data.get('time_spent')
        
        if not aq_id:
             return Response({'message': 'Missing ID'}, status=status.HTTP_400_BAD_REQUEST)
             
        try:
            progress = AssignmentProgress.objects.get(
                student=request.user, 
                assignment_question_id=aq_id
            )
            progress.time_spent = time_spent
            progress.save()
            return Response({'success': True})
        except AssignmentProgress.DoesNotExist:
            return Response({'message': 'Progress not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path='get-timer')
    def get_timer(self, request):
        aq_id = request.query_params.get('assignment_question_id')
        if not aq_id:
             # Legacy fetch might send raw question_id and assignment_id
             # We need to resolve AQ ID.
             assignment_id = request.query_params.get('assignment_id')
             question_id = request.query_params.get('question_id') # This usually refers to Question definition ID
             
             if assignment_id and question_id:
                 try:
                     aq = AssignmentQuestion.objects.get(assignment_id=assignment_id, question_id=question_id)
                     aq_id = aq.id
                 except AssignmentQuestion.DoesNotExist:
                     pass
        
        if not aq_id:
            return Response({'message': 'Missing ID'}, status=status.HTTP_400_BAD_REQUEST)
            
        progress, created = AssignmentProgress.objects.get_or_create(
            student=request.user,
            assignment_question_id=aq_id
        )
        
        return Response({
            'time_spent': progress.time_spent,
            'started_at': progress.started_at
        })
