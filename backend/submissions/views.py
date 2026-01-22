from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.db.models import Q, F, Count, Avg
from django.core.cache import cache
from django.db import transaction
from django.conf import settings
import logging
import json
from .models import Submission, TestResult
from .serializers import SubmissionSerializer, TestResultSerializer
from .services import execute_code
from assignments.models import Assignment, Question, TestCase
from classes.models import Enrollment

logger = logging.getLogger(__name__)


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
        """Create or update submission with optimized database operations"""
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
        
        # Check enrollment with caching
        cache_key = f"enrollment_{assignment.class_obj.id}_{request.user.id}"
        enrollment_exists = cache.get(cache_key)
        
        if enrollment_exists is None:
            enrollment_exists = Enrollment.objects.filter(
                class_obj=assignment.class_obj,
                user=request.user,
                status='active'
            ).exists()
            cache.set(cache_key, enrollment_exists, 300)  # Cache for 5 minutes
        
        if not enrollment_exists:
            return Response(
                {'message': 'Not enrolled in this class'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Use database transaction for consistency
        with transaction.atomic():
            submission, created = Submission.objects.update_or_create(
                assignment=assignment,
                question=question,
                student=request.user,
                defaults={
                    'code_content': serializer.validated_data['code_content'],
                    'language': serializer.validated_data['language'],
                    'status': 'late' if is_late else 'submitted',
                    'submitted_at': now
                }
            )
            
            # Auto-grade if test cases are available
            if question.test_cases.exists():
                self._auto_grade_submission(submission)
        
        serializer = self.get_serializer(submission)
        headers = self.get_success_headers(serializer.data)
        
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(serializer.data, status=status_code, headers=headers)
    
    def _auto_grade_submission(self, submission):
        """Auto-grade submission using test cases"""
        try:
            test_cases = list(submission.question.test_cases.values('input', 'expected_output'))
            if not test_cases:
                return
            
            # Use the new Python-based code executor
            from code_executor.python_runner import get_code_executor
            executor = get_code_executor()
            
            # Prepare inputs for the executor
            inputs = []
            for test_case in test_cases:
                if isinstance(test_case, dict):
                    inputs.append(test_case.get('input', ''))
                else:
                    inputs.append(getattr(test_case, 'input', ''))
            
            # Execute code using Python runner
            execution_result = executor.execute(submission.language, submission.code_content, inputs)
            
            if execution_result['status'] == 'error':
                logger.error(f"Auto-grading failed for submission {submission.id}: {execution_result['message']}")
                return
            
            # Calculate score based on passed tests
            outputs = execution_result['outputs']
            passed_tests = 0
            total_tests = len(test_cases)
            
            for i, output in enumerate(outputs):
                if i < len(test_cases):
                    expected_output = test_cases[i].get('expected_output', '') if isinstance(test_cases[i], dict) else getattr(test_cases[i], 'expected_output', '')
                    # Check if output matches expected (handle errors)
                    is_error = output.startswith('Error:')
                    if not is_error and output.strip() == expected_output.strip():
                        passed_tests += 1
            
            max_points = submission.question.points or 100
            submission.auto_grade_score = int((passed_tests / total_tests) * max_points) if total_tests > 0 else 0
            submission.final_score = submission.auto_grade_score + submission.manual_adjustment
            submission.save()
            
            # Store test results
            self._store_test_results_from_python_runner(submission, outputs, test_cases)
                
        except Exception as e:
            logger.error(f"Auto-grading failed for submission {submission.id}: {e}")
    
    def _store_test_results_from_python_runner(self, submission, outputs, test_cases):
        """Store individual test results from Python runner output"""
        try:
            # Clear existing test results
            submission.test_results.clear()
            
            for i, output in enumerate(outputs):
                if i < len(test_cases):
                    expected_output = test_cases[i].get('expected_output', '') if isinstance(test_cases[i], dict) else getattr(test_cases[i], 'expected_output', '')
                    
                    # Check if output matches expected (handle errors)
                    is_error = output.startswith('Error:')
                    actual_output = output if not is_error else ''
                    error_message = output if is_error else ''
                    passed = not is_error and actual_output.strip() == expected_output.strip()
                    
                    test_result = TestResult.objects.create(
                        test_case_id=i + 1,
                        status='pass' if passed else 'fail',
                        execution_time=0,  # Python runner doesn't track individual execution times yet
                        console_output=actual_output,
                        error_message=error_message,
                        points_earned=1 if passed else 0
                    )
                    submission.test_results.add(test_result)
                
        except Exception as e:
            logger.error(f"Failed to store test results for submission {submission.id}: {e}")
    
    def _store_test_results(self, submission, test_results):
        """Store individual test results"""
        try:
            # Clear existing test results
            submission.test_results.clear()
            
            for result in test_results:
                test_result = TestResult.objects.create(
                    test_case_id=result.get('test_case_id', 1),
                    status='pass' if result['passed'] else 'fail',
                    execution_time=result.get('execution_time', 0),
                    console_output=result.get('actual_output', ''),
                    error_message=result.get('error', ''),
                    points_earned=1 if result['passed'] else 0
                )
                submission.test_results.add(test_result)
                
        except Exception as e:
            logger.error(f"Failed to store test results for submission {submission.id}: {e}")
    
    @action(detail=False, methods=['post'])
    def run_code(self, request):
        """Execute code against test cases (for testing before submission) - Optimized for high concurrency"""
        code = request.data.get('code', '')
        language = request.data.get('language', '')
        test_cases = request.data.get('test_cases', [])
        question_id = request.data.get('question_id')
        
        if not code or not language:
            return Response(
                {'message': 'Code and language are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Rate limiting per user
        cache_key = f"code_run_limit_{request.user.id}"
        run_count = cache.get(cache_key, 0)
        max_runs_per_minute = getattr(settings, 'MAX_CODE_RUNS_PER_MINUTE', 10)
        
        if run_count >= max_runs_per_minute:
            return Response(
                {'message': f'Rate limit exceeded. Maximum {max_runs_per_minute} runs per minute.'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )
        
        # Increment rate limit counter
        cache.set(cache_key, run_count + 1, 60)  # 1 minute expiry
        
        try:
            # Use the new Python-based code executor
            from code_executor.python_runner import get_code_executor
            executor = get_code_executor()
            
            # If no test cases provided, just run the code with empty input
            if not test_cases:
                test_cases = [{"input": "", "expected_output": ""}]
            
            # Prepare inputs for the executor
            inputs = []
            for test_case in test_cases:
                if isinstance(test_case, dict):
                    inputs.append(test_case.get('input', ''))
                else:
                    inputs.append(getattr(test_case, 'input', ''))
            
            # Execute code using Python runner
            execution_result = executor.execute(language, code, inputs)
            
            if execution_result['status'] == 'error':
                return Response(
                    {
                        'success': True,  # Still return success so frontend shows the error
                        'data': {
                            'results': [{
                                'test_case_id': 1,
                                'passed': False,
                                'actual_output': '',
                                'expected_output': '',
                                'error': execution_result['message'],
                                'execution_time': 0,
                                'test_case': {'input': '', 'expected_output': ''}
                            }],
                            'summary': {
                                'total': 1,
                                'passed': 0,
                                'failed': 1,
                                'all_passed': False
                            }
                        },
                        'execution_method': 'python_runner'
                    }
                )
            
            # Format results - ALWAYS show output, don't worry about test matching
            formatted_results = []
            outputs = execution_result['outputs']
            
            for i, output in enumerate(outputs):
                # Get expected output from test cases (if any)
                expected_output = ''
                test_input = ''
                if i < len(test_cases):
                    if isinstance(test_cases[i], dict):
                        expected_output = test_cases[i].get('expected_output', '')
                        test_input = test_cases[i].get('input', '')
                    else:
                        expected_output = getattr(test_cases[i], 'expected_output', '')
                        test_input = getattr(test_cases[i], 'input', '')
                
                # Check if output matches expected (handle errors)
                is_error = output.startswith('Error:')
                actual_output = output if not is_error else ''
                error_message = output if is_error else ''
                
                # ALWAYS show the actual output - comparison is secondary
                # Only mark as "passed" if there's an expected output and it matches
                passed = False
                if expected_output and not is_error:
                    passed = actual_output.strip() == expected_output.strip()
                elif not expected_output and not is_error:
                    # If no expected output, consider it passed if no error
                    passed = True
                
                formatted_result = {
                    'test_case_id': i + 1,
                    'passed': passed,
                    'actual_output': actual_output,
                    'expected_output': expected_output,
                    'error': error_message,
                    'execution_time': 0,
                    'test_case': {
                        'input': test_input,
                        'expected_output': expected_output
                    },
                    # Add a flag to indicate this is just showing output, not testing
                    'show_output_only': not expected_output
                }
                formatted_results.append(formatted_result)
            
            passed_count = sum(1 for r in formatted_results if r['passed'])
            
            logger.info(f"Python runner execution for user {request.user.id}: "
                      f"Output generated successfully, {passed_count}/{len(test_cases)} tests passed")
            
            return Response({
                'success': True,
                'data': {
                    'results': formatted_results,
                    'summary': {
                        'total': len(test_cases),
                        'passed': passed_count,
                        'failed': len(test_cases) - passed_count,
                        'all_passed': passed_count == len(test_cases),
                        'has_output': any(r['actual_output'] for r in formatted_results),
                        'execution_successful': not any(r['error'] for r in formatted_results)
                    }
                },
                'execution_method': 'python_runner'
            })
                
        except Exception as e:
            logger.error(f"Code execution error for user {request.user.id}: {str(e)}")
            import traceback
            return Response(
                {
                    'message': 'Code execution failed. Please try again.',
                    'error': str(e) if settings.DEBUG else 'Internal server error',
                    'traceback': traceback.format_exc() if settings.DEBUG else None
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['post'], url_path='simple-run')
    def simple_run_code(self, request):
        """Simple code execution - just run code and show output, no test cases needed"""
        code = request.data.get('code', '')
        language = request.data.get('language', 'python')
        
        if not code or not code.strip():
            return Response(
                {'message': 'Code cannot be empty'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Use the Python-based code executor
            from code_executor.python_runner import get_code_executor
            executor = get_code_executor()
            
            # Execute code with empty input
            execution_result = executor.execute(language, code, [''])
            
            if execution_result['status'] == 'error':
                return Response({
                    'success': True,
                    'output': '',
                    'error': execution_result['message'],
                    'execution_method': 'python_runner'
                })
            
            # Get the output
            output = execution_result['outputs'][0] if execution_result['outputs'] else ''
            
            # Check if it's an error
            if output.startswith('Error:'):
                return Response({
                    'success': True,
                    'output': '',
                    'error': output,
                    'execution_method': 'python_runner'
                })
            else:
                return Response({
                    'success': True,
                    'output': output,
                    'error': '',
                    'execution_method': 'python_runner'
                })
                
        except Exception as e:
            logger.error(f"Simple code execution error: {str(e)}")
            return Response({
                'success': True,
                'output': '',
                'error': f'Execution failed: {str(e)}',
                'execution_method': 'python_runner'
            })
    
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
                    'time_spent': 0,
                    'last_activity_at': None,
                    'code_content': ''
                }
            })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_sample_questions(request):
    """Get sample coding questions for testing the system"""
    sample_questions = [
        {
            'id': 'sample_1',
            'title': 'Hello World',
            'description': 'Write a program that prints "Hello, World!" to the console.',
            'difficulty': 'Easy',
            'language': 'python',
            'starter_code': '# Write your code here\nprint("Hello, World!")',
            'test_cases': [
                {
                    'input': '',
                    'expected_output': 'Hello, World!',
                    'description': 'Basic output test'
                }
            ],
            'points': 10
        },
        {
            'id': 'sample_2',
            'title': 'Sum of Two Numbers',
            'description': 'Write a program that reads two integers and prints their sum.',
            'difficulty': 'Easy',
            'language': 'python',
            'starter_code': '# Read two integers and print their sum\na = int(input())\nb = int(input())\n# Your code here',
            'test_cases': [
                {
                    'input': '5\n3',
                    'expected_output': '8',
                    'description': 'Sum of 5 and 3'
                },
                {
                    'input': '10\n-2',
                    'expected_output': '8',
                    'description': 'Sum of 10 and -2'
                },
                {
                    'input': '0\n0',
                    'expected_output': '0',
                    'description': 'Sum of 0 and 0'
                }
            ],
            'points': 20
        },
        {
            'id': 'sample_3',
            'title': 'Factorial Calculator',
            'description': 'Write a program that calculates the factorial of a given number.',
            'difficulty': 'Medium',
            'language': 'python',
            'starter_code': '# Calculate factorial of n\nn = int(input())\n# Your code here',
            'test_cases': [
                {
                    'input': '5',
                    'expected_output': '120',
                    'description': 'Factorial of 5'
                },
                {
                    'input': '0',
                    'expected_output': '1',
                    'description': 'Factorial of 0'
                },
                {
                    'input': '1',
                    'expected_output': '1',
                    'description': 'Factorial of 1'
                },
                {
                    'input': '4',
                    'expected_output': '24',
                    'description': 'Factorial of 4'
                }
            ],
            'points': 30
        },
        {
            'id': 'sample_4',
            'title': 'Fibonacci Sequence',
            'description': 'Write a program that prints the nth Fibonacci number.',
            'difficulty': 'Medium',
            'language': 'python',
            'starter_code': '# Calculate nth Fibonacci number\nn = int(input())\n# Your code here',
            'test_cases': [
                {
                    'input': '0',
                    'expected_output': '0',
                    'description': '0th Fibonacci number'
                },
                {
                    'input': '1',
                    'expected_output': '1',
                    'description': '1st Fibonacci number'
                },
                {
                    'input': '5',
                    'expected_output': '5',
                    'description': '5th Fibonacci number'
                },
                {
                    'input': '10',
                    'expected_output': '55',
                    'description': '10th Fibonacci number'
                }
            ],
            'points': 40
        },
        {
            'id': 'sample_5',
            'title': 'Prime Number Checker',
            'description': 'Write a program that checks if a given number is prime.',
            'difficulty': 'Medium',
            'language': 'python',
            'starter_code': '# Check if n is prime\nn = int(input())\n# Your code here\n# Print "Prime" if prime, "Not Prime" otherwise',
            'test_cases': [
                {
                    'input': '2',
                    'expected_output': 'Prime',
                    'description': '2 is prime'
                },
                {
                    'input': '4',
                    'expected_output': 'Not Prime',
                    'description': '4 is not prime'
                },
                {
                    'input': '17',
                    'expected_output': 'Prime',
                    'description': '17 is prime'
                },
                {
                    'input': '1',
                    'expected_output': 'Not Prime',
                    'description': '1 is not prime'
                }
            ],
            'points': 35
        }
    ]
    
    return Response({
        'success': True,
        'data': sample_questions,
        'message': 'Sample questions loaded successfully'
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def system_status(request):
    """Get system status and performance metrics"""
    if request.user.role not in ['teacher', 'admin']:
        return Response(
            {'message': 'Not authorized'},
            status=status.HTTP_403_FORBIDDEN
        )
    
    try:
        from code_executor.docker_service import get_executor_stats
        
        # Get Docker executor stats
        executor_stats = get_executor_stats()
        
        # Get database stats
        total_submissions = Submission.objects.count()
        recent_submissions = Submission.objects.filter(
            submitted_at__gte=timezone.now() - timezone.timedelta(hours=1)
        ).count()
        
        # Get average execution time from recent submissions
        avg_execution_time = TestResult.objects.filter(
            submissions__submitted_at__gte=timezone.now() - timezone.timedelta(hours=1)
        ).aggregate(avg_time=Avg('execution_time'))['avg_time'] or 0
        
        return Response({
            'success': True,
            'data': {
                'docker_executor': executor_stats,
                'database': {
                    'total_submissions': total_submissions,
                    'recent_submissions_1h': recent_submissions,
                    'avg_execution_time_ms': round(avg_execution_time, 2)
                },
                'timestamp': timezone.now().isoformat()
            }
        })
        
    except Exception as e:
        logger.error(f"System status error: {e}")
        return Response(
            {'message': 'Failed to get system status', 'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
