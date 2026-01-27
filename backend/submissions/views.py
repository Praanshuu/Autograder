from rest_framework import viewsets, status
from django.db import models
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import SubmissionAttempt, AssignmentProgress, TestResult, GradebookEntry
from .serializers import SubmissionAttemptSerializer, AssignmentProgressSerializer
from .services import execute_code
from assignments.models import AssignmentQuestion, ContentItem
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

        # Check for existing successful attempt (Optional: Block if strict exam, but usually allowed)
        # if SubmissionAttempt.objects.filter(student=request.user, assignment_question=aq, status='success').exists():
        #    return Response({'message': 'You have already successfully completed this question.'}, status=status.HTTP_400_BAD_REQUEST)
            
        # Create Attempt
        attempt = SubmissionAttempt.objects.create(
            student=request.user,
            assignment_question=aq,
            attempt_number=SubmissionAttempt.objects.filter(student=request.user, assignment_question=aq).count() + 1,
            status='processing',
            source_code=code # Save the code
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
                    score=1 if status_res == 'pass' else 0,
                    actual_output=res.get('console_output', ''),
                    error_message=res.get('error_message', '')
                )
            
            # Determine final status
            if passed_count == len(results) and len(results) > 0:
                attempt.status = 'success'
            else:
                attempt.status = 'fail'
            
            attempt.save()
            
            # Auto-update gradebook
            self._update_gradebook(request.user, aq.assignment)
            
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


    @action(detail=True, methods=['put', 'patch'], url_path='grade')
    def grade(self, request, pk=None):
        """
        Manually grade a submission.
        """
        attempt = self.get_object()
        manual_score = request.data.get('manual_score')
        feedback = request.data.get('feedback_text')
        
        if manual_score is not None:
             attempt.manual_score = float(manual_score)
        if feedback is not None:
             attempt.feedback_text = feedback
             
        attempt.save()
        
        # Trigger Gradebook Recalculation
        self._update_gradebook(attempt.student, attempt.assignment_question.assignment)
        
        serializer = self.get_serializer(attempt)
        return Response(serializer.data)

    def _update_gradebook(self, student, assignment):
        """
        Recalculate total score for assignment and update gradebook.
        Logic: Weighted by number of test cases (Total Passed / Total Tests).
        If Manual Score is present, it counts as (Score% * NumTests) passed.
        """
        aqs = AssignmentQuestion.objects.filter(assignment=assignment)
        total_questions = aqs.count()
        
        sum_question_percentages = 0
        questions_counted = 0
        
        for aq in aqs:
            # Get latest attempt
            latest = SubmissionAttempt.objects.filter(
                student=student,
                assignment_question=aq
            ).order_by('-created_at').first()
            
            # Determine score for this question (0-100 scale)
            question_score = 0
            
            # aq.question.test_cases is a list of dicts
            test_cases = aq.question.test_cases or []
            num_tests = len(test_cases)
            
            if latest:
                if latest.manual_score is not None:
                    # Manual override (rubric score)
                    question_score = latest.manual_score
                elif num_tests > 0:
                    # Auto-calculated based on tests
                    results = latest.test_results.all()
                    if results:
                         passed = results.filter(status='pass').count()
                         passed = min(passed, num_tests) # Cap at max tests
                         question_score = (passed / num_tests) * 100
                else:
                    # No tests, no manual score. Default to 0? Or 100 if submitted? 
                    # Usually 0 if purely auto-graded until manual grade comes in.
                    question_score = 0
            else:
                # No attempt
                question_score = 0
            
            sum_question_percentages += question_score
            questions_counted += 1

        # Final Calculation: Average of Question Scores
        final_assignment_score = 0
        if total_questions > 0:
            final_assignment_score = sum_question_percentages / total_questions
             
        # Update Gradebook
        content_item = ContentItem.objects.get(id=assignment.id)
        entry, _ = GradebookEntry.objects.get_or_create(student=student, content_item=content_item)
        entry.final_score = final_assignment_score
        
        # Check for Manual Grading Status
        # If any question has a manual score, mark the whole assignment as 'graded' (or partially graded?)
        # User said: "if teacher updates the score in rubric, we will show that as final score with graded"
        has_manual = SubmissionAttempt.objects.filter(
            student=student, 
            assignment_question__assignment=assignment, 
            manual_score__isnull=False
        ).exists()
        
        if has_manual:
            entry.status = 'graded'
        
        # Ensure we don't overwrite 'graded' with 'submitted' if we just ran an autograder for a new submission
        # But here we are just updating score. 
            
        entry.save()


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

    @action(detail=False, methods=['post'], url_path='finish-assignment')
    def finish_assignment(self, request):
        assignment_id = request.data.get('assignment_id')
        
        if not assignment_id:
            return Response({'message': 'Missing Assignment ID'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            # Find ContentItem for this assignment
            # Assuming Assignment ID is ContentItem ID (since inheritance)
            content_item = ContentItem.objects.get(id=assignment_id)
            
            entry, created = GradebookEntry.objects.get_or_create(
                student=request.user,
                content_item=content_item
            )
            
            entry.status = 'submitted'
            entry.updated_at = timezone.now()
            entry.save()
            
            return Response({'success': True, 'status': 'submitted'})
            
        except ContentItem.DoesNotExist:
             return Response({'message': 'Assignment not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
             logger.error(f"Finish Assignment failed: {e}")
             return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], url_path='assignment-status')
    def get_assignment_status(self, request):
        assignment_id = request.query_params.get('assignment_id')
        
        if not assignment_id:
             return Response({'message': 'Missing Assignment ID'}, status=status.HTTP_400_BAD_REQUEST)
             
        try:
             # Check GradebookEntry
             entry = GradebookEntry.objects.filter(
                 student=request.user,
                 content_item_id=assignment_id
             ).first()
             
             status_val = entry.status if entry else 'in_progress'
             
             return Response({'status': status_val})
             
        except Exception as e:
             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], url_path='summary')
    def get_assignment_summary(self, request):
        """
        Returns aggregated list of students for an assignment.
        Teacher only.
        """
        # if not request.user.role == 'teacher': return 403
        assignment_id = request.query_params.get('assignment_id')
        if not assignment_id: return Response({'message': 'Missing ID'}, status=400)
        
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Get all students (naive: all students in system, or enrolled in class if strict)
        # Ideally get from Class Enrollments. 
        # For now, get students who have ATTEMPTED or are in Gradebook
        
        # 1. Get Gradebook Entries
        entries = GradebookEntry.objects.filter(content_item_id=assignment_id).select_related('student')
        
        # 2. Get Submissions to count progress
        attempts = SubmissionAttempt.objects.filter(assignment_question__assignment_id=assignment_id)
        
        data = []
        # Group by student
        student_map = {}
        for entry in entries:
            student_map[entry.student_id] = {
                'student': {
                    'id': entry.student.id,
                    'first_name': entry.student.first_name,
                    'last_name': entry.student.last_name,
                    'email': entry.student.email,
                    'username': entry.student.username
                },
                'status': entry.status,
                'final_score': entry.final_score,
                'updated_at': entry.updated_at,
                'questions_completed': 0,
                'total_questions': 0 # To be filled
            }
            
        # Get Total Questions Count
        total_questions = AssignmentQuestion.objects.filter(assignment_id=assignment_id).count()

        # Fill in attempts info (even if no gradebook entry yet, though finish_assignment creates it)
        # If student worked but didn't finish, they might not have GradebookEntry (depending on logic).
        # We should also include them.
        
        # ... simplifying for time: Just use Gradebook entries as "Submitted" list
        # If we want "In Progress", we query AssignmentProgress.
        
        progress_rows = AssignmentProgress.objects.filter(assignment_question__assignment_id=assignment_id).values('student_id').distinct()
        for p in progress_rows:
            sid = p['student_id']
            if sid not in student_map:
                # Fetch user
                stu = User.objects.get(id=sid)
                student_map[sid] = {
                    'student': {
                        'id': stu.id,
                        'first_name': stu.first_name,
                        'last_name': stu.last_name,
                        'email': stu.email,
                         'username': stu.username
                    },
                    'status': 'in_progress',
                    'final_score': 0,
                    'updated_at': None,
                    'questions_completed': 0,
                    'total_questions': total_questions
                }
        
        # Count completed questions per student
        # We count SUCCESSFUL attempts
        completed_counts = SubmissionAttempt.objects.filter(
            assignment_question__assignment_id=assignment_id,
            status='success'
        ).values('student_id').annotate(count=models.Count('assignment_question', distinct=True))
        
        for c in completed_counts:
            sid = c['student_id']
            if sid in student_map:
                student_map[sid]['questions_completed'] = c['count']
                student_map[sid]['total_questions'] = total_questions
        
        return Response(list(student_map.values()))

    @action(detail=False, methods=['get'], url_path='student-report')
    def get_student_report(self, request):
        """
        Detailed report for a student on an assignment.
        """
        assignment_id = request.query_params.get('assignment_id')
        student_id = request.query_params.get('student_id')
        
        if not assignment_id or not student_id: return Response({'message': 'Missing IDs'}, status=400)
        
        # Get Assignment Questions
        aqs = AssignmentQuestion.objects.filter(assignment_id=assignment_id).select_related('question').order_by('order')
        
        report = []
        for aq in aqs:
            # Get latest submission
            latest = SubmissionAttempt.objects.filter(
                assignment_question=aq,
                student_id=student_id
            ).order_by('-created_at').first()
            
            # Serialize submission if exists
            sub_data = None
            if latest:
                sub_data = SubmissionAttemptSerializer(latest).data
                
            report.append({
                'question': {
                    'id': aq.question.id,
                    'title': aq.question.title,
                    'description': aq.question.description,
                    'test_cases': aq.question.test_cases
                },
                'submission': sub_data,
                'status': latest.status if latest else 'not_attempted'
            })
            
        return Response(report)
