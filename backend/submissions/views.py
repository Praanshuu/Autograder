from rest_framework import viewsets, status
from django.db import models
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import SubmissionAttempt, AssignmentProgress, TestResult, GradebookEntry
from .serializers import SubmissionAttemptSerializer, AssignmentProgressSerializer, GradebookEntrySerializer
from .services import execute_code, analyze_code_structure
from assignments.models import AssignmentQuestion, ContentItem, Question
from gamification.points_calculator import PointsCalculator
import logging

logger = logging.getLogger(__name__)

class SubmissionAttemptViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionAttemptSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None
    ordering_fields = ['created_at', 'status', 'final_score', 'student__username']
    filterset_fields = ['status', 'student']
    
    def get_queryset(self):
        user = self.request.user
        queryset = SubmissionAttempt.objects.select_related(
            'assignment_question',
            'assignment_question__assignment',
            'assignment_question__question',
            'student',
        ).prefetch_related(
            'test_results',
        )
        
        # Filter by Assignment ID (via AssignmentQuestion)
        assignment_id = self.request.query_params.get('assignment_id')
        if assignment_id:
            queryset = queryset.filter(assignment_question__assignment_id=assignment_id)
            
        if user.role == 'student':
            queryset = queryset.filter(student=user)
            
        return queryset

    @action(detail=False, methods=['get'], url_path='analytics')
    def analytics(self, request):
        """Lightweight endpoint for analytics charts — no pagination, 
        minimal fields, much smaller response payload."""
        from .serializers import SubmissionAnalyticsSerializer
        queryset = self.get_queryset()
        serializer = SubmissionAnalyticsSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='summary')
    def get_assignment_summary(self, request):
        """
        Returns aggregated list of students for an assignment.
        Teacher only.
        """
        assignment_id = request.query_params.get('assignment_id')
        if not assignment_id: return Response({'message': 'Missing ID'}, status=400)
        
        from assignments.models import Assignment
        try:
            assignment = Assignment.objects.select_related('module__class_obj').get(id=assignment_id)
        except Assignment.DoesNotExist:
             return Response({'message': 'Assignment not found'}, status=404)

        # 0. Get All Enrolled Students (from the Class)
        class_obj = assignment.module.class_obj
        # Local import User if not imported at top level
        from django.contrib.auth import get_user_model
        User = get_user_model()
        enrolled_students = User.objects.filter(enrollments__class_obj=class_obj, enrollments__role='student')
        
        student_map = {}
        for student in enrolled_students:
             student_map[student.id] = {
                'student': {
                    'id': student.id,
                    'first_name': student.first_name,
                    'last_name': student.last_name,
                    'email': student.email,
                    'username': student.username
                },
                'status': 'not_started',
                'final_score': 0,
                'updated_at': None,
                'questions_completed': 0,
                'total_questions': 0 
            }

        # 1. Get Gradebook
        entries = GradebookEntry.objects.filter(content_item_id=assignment_id).select_related('student')
        for entry in entries:
            if entry.student_id in student_map:
                student_map[entry.student_id]['status'] = entry.status
                student_map[entry.student_id]['final_score'] = entry.final_score
                student_map[entry.student_id]['updated_at'] = entry.updated_at
        
        # 2. Get Progress
        progress_rows = AssignmentProgress.objects.filter(assignment_question__assignment_id=assignment_id).values('student_id').distinct()
        for p in progress_rows:
            sid = p['student_id']
            if sid in student_map and student_map[sid]['status'] == 'not_started':
                student_map[sid]['status'] = 'in_progress'

        # Total questions
        total_questions = AssignmentQuestion.objects.filter(assignment_id=assignment_id).count()
        for sid in student_map:
            student_map[sid]['total_questions'] = total_questions
        
        # Completed
        completed_counts = SubmissionAttempt.objects.filter(
            assignment_question__assignment_id=assignment_id,
            status='success'
        ).values('student_id').annotate(count=models.Count('assignment_question', distinct=True))
        
        for c in completed_counts:
            sid = c['student_id']
            if sid in student_map:
                student_map[sid]['questions_completed'] = c['count']
        
        return Response(list(student_map.values()))

        
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
            
        language = request.data.get('language', 'python')  # Get language from request
        
        # Analyze code structure
        keywords = []
        if language == 'python' and code:
             keywords = analyze_code_structure(code)

        # Create Attempt
        attempt = SubmissionAttempt.objects.create(
            student=request.user,
            assignment_question=aq,
            attempt_number=SubmissionAttempt.objects.filter(student=request.user, assignment_question=aq).count() + 1,
            status='processing',
            source_code=code, # Save the code
            detected_keywords=keywords
        )
        
        # Execute Code (Async)
        from .tasks import execute_submission_task
        
        # Enqueue task
        transaction_on_commit = getattr(timezone, 'now', None) # minimal dummy
        # Better: use django transaction.on_commit if wrapped in atomicty, 
        # but view is not atomic by default.
        
        execute_submission_task.delay(attempt.id, language)
        
        serializer = self.get_serializer(attempt)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
        
        # Validate language support
        supported_languages = ['python', 'c', 'java']
        if language.lower() not in supported_languages:
            return Response({
                'message': f'Unsupported language: {language}. Supported languages: {", ".join(supported_languages)}'
            }, status=status.HTTP_400_BAD_REQUEST)
             
        try:
            # Fetch config if question_id is provided
            config = {}
            question_id = request.data.get('question_id')
            if question_id:
                try:
                    question = Question.objects.get(id=question_id)
                    config = question.config
                    logger.info(f"Running code with config from Question {question_id}: {config}")
                except Question.DoesNotExist:
                    logger.warning(f"Question {question_id} not found for run_code config lookup.")
            
            results = execute_code(code, language, test_cases, config=config)
            
            formatted_results = []
            for r in results:
                formatted_results.append({
                    'actual_output': r.get('console_output'),
                    'expected_output': r.get('test_case', {}).get('expected_output') if isinstance(r.get('test_case'), dict) else '',
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
        except Exception as e:
            logger.error(f"Sandbox execution failed: {e}")
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @action(detail=True, methods=['post'], url_path='analyze-ai')
    def analyze_ai(self, request, pk=None):
        """
        Trigger Bulk AI Analysis for this assignment.
        """
        try:
             # Verify assignment exists
             from assignments.models import Assignment
             try:
                 assignment = Assignment.objects.get(id=pk)
             except Assignment.DoesNotExist:
                 return Response({'message': 'Assignment not found'}, status=status.HTTP_404_NOT_FOUND)
            
             # Trigger Celery Task
             from .tasks import analyze_assignment_ai_task
             task = analyze_assignment_ai_task.delay(pk)
             
             return Response({
                 'message': f'AI Analysis started for assignment {assignment.title}',
                 'task_id': task.id
             })
             
        except Exception as e:
            logger.error(f"Failed to trigger AI analysis: {e}")
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
        Now also includes points information from the gamification system.
        """
        aqs = AssignmentQuestion.objects.filter(assignment=assignment)
        total_questions = aqs.count()
        
        sum_question_percentages = 0
        questions_counted = 0
        total_points_earned = 0
        
        for aq in aqs:
            # Get latest attempt
            latest = SubmissionAttempt.objects.filter(
                student=student,
                assignment_question=aq
            ).order_by('-created_at').first()
            
            # Determine score for this question (0-100 scale)
            question_score = 0
            
            # Get Max Points for this question
            max_points = aq.custom_points if aq.custom_points is not None else 10 # Default to 10 if not set
            if max_points <= 0: max_points = 10 # Prevent division by zero

            # aq.question.test_cases is a list of dicts
            test_cases = aq.question.test_cases or []
            num_tests = len(test_cases)
            
            if latest:
                if latest.manual_score is not None:
                    # Manual override (rubric score is in POINTS)
                    # Normalize to 0-100 scale for aggregation
                    question_score = (latest.manual_score / max_points) * 100
                    if question_score > 100: question_score = 100 # Cap at 100%
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

                    
                # Calculate points earned for this question
                try:
                    test_results_data = []
                    for test_result in latest.test_results.all():
                        test_results_data.append({
                            'status': test_result.status,
                            'score': test_result.score
                        })
                    
                    if test_results_data:
                        calculator = PointsCalculator()
                        question_points = calculator.calculate_assignment_points(
                            test_results=test_results_data,
                            attempt_number=latest.attempt_number,
                            assignment_question=aq
                        )
                        total_points_earned += question_points
                except Exception as e:
                    logger.error(f"Error calculating points for gradebook: {e}")
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
        entry.points_earned = total_points_earned  # Store points in gradebook
        
        # Log points information
        if total_points_earned > 0:
            logger.info(f"Assignment {assignment.id} for {student.username}: {total_points_earned} points earned")
        
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

    def _award_assignment_points(self, submission_attempt, test_results_data):
        """
        Award points for assignment submissions using the gamification system.
        
        Args:
            submission_attempt: The SubmissionAttempt instance
            test_results_data: List of test result dictionaries
        """
        try:
            calculator = PointsCalculator()
            points_awarded = calculator.calculate_and_award_assignment_points(
                submission_attempt=submission_attempt,
                test_results=test_results_data
            )
            
            if points_awarded > 0:
                logger.info(
                    f"Awarded {points_awarded} assignment points to {submission_attempt.student.username} "
                    f"for {submission_attempt.assignment_question}"
                )
                
        except Exception as e:
            logger.error(
                f"Error awarding assignment points for submission {submission_attempt.id}: {e}",
                exc_info=True
            )


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
        
        # Get code content (Draft -> Last Submission -> Empty)
        code_content = progress.current_code
        
        if not code_content:
            # Fallback to latest submission if no draft
            latest_submission = SubmissionAttempt.objects.filter(
                student=request.user,
                assignment_question=aq_id
            ).order_by('-created_at').first()
            
            if latest_submission:
                code_content = latest_submission.source_code
        
        return Response({
            'time_spent': progress.time_spent,
            'started_at': progress.started_at,
            'code_content': code_content  # Return code to frontend
        })

    @action(detail=False, methods=['get'], url_path='points-summary')
    def get_points_summary(self, request):
        """
        Get points summary for the current user.
        Shows total points, assignment points, and recent point earnings.
        """
        try:
            from gamification.points_calculator import PointsCalculator
            calculator = PointsCalculator()
            points_summary = calculator.get_user_points_summary(request.user)
            
            # Get recent assignment submissions with points
            recent_submissions = SubmissionAttempt.objects.filter(
                student=request.user,
                status__in=['success', 'fail']
            ).order_by('-created_at')[:10]
            
            recent_points = []
            for submission in recent_submissions:
                test_results_data = []
                for test_result in submission.test_results.all():
                    test_results_data.append({
                        'status': test_result.status,
                        'score': test_result.score
                    })
                
                if test_results_data:
                    points = calculator.calculate_assignment_points(
                        test_results=test_results_data,
                        attempt_number=submission.attempt_number,
                        assignment_question=submission.assignment_question
                    )
                    
                    recent_points.append({
                        'assignment_question': submission.assignment_question.question.title,
                        'points_earned': points,
                        'submitted_at': submission.created_at,
                        'status': submission.status
                    })
            
            return Response({
                'points_summary': points_summary,
                'recent_assignment_points': recent_points
            })
            
        except Exception as e:
            logger.error(f"Error getting points summary: {e}")
            return Response({'error': 'Failed to get points summary'}, status=500)

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

    @action(detail=False, methods=['get'], url_path='assignment-progress-with-points')
    def get_assignment_progress_with_points(self, request):
        """
        Get assignment progress including points information.
        Shows completion status, scores, and points earned for each question.
        """
        assignment_id = request.query_params.get('assignment_id')
        if not assignment_id:
            return Response({'message': 'Missing assignment_id'}, status=400)
        
        try:
            from gamification.points_calculator import PointsCalculator
            calculator = PointsCalculator()
            
            # Get assignment questions
            aqs = AssignmentQuestion.objects.filter(assignment_id=assignment_id).select_related('question').order_by('order')
            
            progress_data = []
            total_points_earned = 0
            
            for aq in aqs:
                # Get latest submission
                latest = SubmissionAttempt.objects.filter(
                    student=request.user,
                    assignment_question=aq
                ).order_by('-created_at').first()
                
                question_data = {
                    'question_id': aq.question.id,
                    'assignment_question_id': aq.id,
                    'title': aq.question.title,
                    'status': 'not_attempted',
                    'score': 0,
                    'points_earned': 0,
                    'attempt_count': 0
                }
                
                if latest:
                    question_data['status'] = latest.status
                    question_data['attempt_count'] = latest.attempt_number
                    
                    # Calculate score
                    test_cases = aq.question.test_cases or []
                    if test_cases and latest.test_results.exists():
                        passed = latest.test_results.filter(status='pass').count()
                        question_data['score'] = (passed / len(test_cases)) * 100
                    
                    # Calculate points
                    test_results_data = []
                    for test_result in latest.test_results.all():
                        test_results_data.append({
                            'status': test_result.status,
                            'score': test_result.score
                        })
                    
                    if test_results_data:
                        points = calculator.calculate_assignment_points(
                            test_results=test_results_data,
                            attempt_number=latest.attempt_number,
                            assignment_question=aq
                        )
                        question_data['points_earned'] = points
                        total_points_earned += points
                
                progress_data.append(question_data)
            
            return Response({
                'assignment_id': assignment_id,
                'questions': progress_data,
                'total_points_earned': total_points_earned,
                'total_questions': len(progress_data),
                'completed_questions': len([q for q in progress_data if q['status'] == 'success'])
            })
            
        except Exception as e:
            logger.error(f"Error getting assignment progress with points: {e}")
            return Response({'error': str(e)}, status=500)


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
                'max_points': aq.custom_points if aq.custom_points is not None else 10,
                'submission': sub_data,
                'status': latest.status if latest else 'not_attempted'
            })
            
        return Response(report)


class GradebookViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for gradebook entries with points information"""
    serializer_class = GradebookEntrySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        queryset = GradebookEntry.objects.select_related('student', 'content_item')
        
        if user.role == 'student':
            # Students can only see their own grades
            queryset = queryset.filter(student=user)
        elif user.role == 'teacher':
            # Teachers can see all grades, optionally filtered by class
            class_id = self.request.query_params.get('class_id')
            if class_id:
                # Filter by class enrollment (assuming there's a way to get class students)
                # This would need to be implemented based on your class/enrollment system
                pass
        
        return queryset.order_by('-updated_at')
    
    @action(detail=False, methods=['get'], url_path='student-summary')
    def student_summary(self, request):
        """Get summary of student's grades and points"""
        try:
            from gamification.points_calculator import PointsCalculator
            calculator = PointsCalculator()
            
            # Get user's gradebook entries
            entries = GradebookEntry.objects.filter(student=request.user).select_related('content_item')
            
            # Calculate totals
            total_assignments = entries.count()
            total_score = sum(entry.final_score for entry in entries) / total_assignments if total_assignments > 0 else 0
            total_assignment_points = sum(entry.points_earned for entry in entries)
            
            # Get overall points summary
            points_summary = calculator.get_user_points_summary(request.user)
            
            # Get recent entries
            recent_entries = entries.order_by('-updated_at')[:5]
            
            return Response({
                'summary': {
                    'total_assignments': total_assignments,
                    'average_score': round(total_score, 2),
                    'total_assignment_points': total_assignment_points,
                    'overall_points': points_summary
                },
                'recent_entries': GradebookEntrySerializer(recent_entries, many=True).data
            })
            
        except Exception as e:
            logger.error(f"Error getting student summary: {e}")
            return Response({'error': 'Failed to get student summary'}, status=500)
    
    @action(detail=False, methods=['get'], url_path='class-summary')
    def class_summary(self, request):
        """Get class-wide gradebook summary with points (teachers only)"""
        if request.user.role != 'teacher':
            return Response({'error': 'Permission denied'}, status=403)
        
        try:
            assignment_id = request.query_params.get('assignment_id')
            if not assignment_id:
                return Response({'message': 'Missing assignment_id'}, status=400)
            
            # Get gradebook entries for this assignment
            entries = GradebookEntry.objects.filter(
                content_item_id=assignment_id
            ).select_related('student').order_by('student__last_name', 'student__first_name')
            
            class_data = []
            total_points = 0
            total_score = 0
            
            for entry in entries:
                student_data = {
                    'student': {
                        'id': entry.student.id,
                        'username': entry.student.username,
                        'first_name': entry.student.first_name,
                        'last_name': entry.student.last_name,
                        'email': entry.student.email
                    },
                    'final_score': entry.final_score,
                    'points_earned': entry.points_earned,
                    'status': entry.status,
                    'updated_at': entry.updated_at
                }
                class_data.append(student_data)
                total_points += entry.points_earned
                total_score += entry.final_score
            
            avg_score = total_score / len(entries) if entries else 0
            avg_points = total_points / len(entries) if entries else 0
            
            return Response({
                'assignment_id': assignment_id,
                'students': class_data,
                'class_statistics': {
                    'total_students': len(entries),
                    'average_score': round(avg_score, 2),
                    'average_points': round(avg_points, 2),
                    'total_points_awarded': total_points
                }
            })
            
        except Exception as e:
            logger.error(f"Error getting class summary: {e}")
            return Response({'error': str(e)}, status=500)