"""
API views for gamification features including points, leaderboards, and achievements.

This module provides REST API endpoints for:
- Practice questions and submissions
- User points and point history
- Leaderboard rankings (global and class-specific)
- Achievement tracking and progress
- Analytics and statistics
"""

from rest_framework import viewsets, status, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsTeacher
from django.contrib.auth import get_user_model
from django.db.models import Q, Count, Sum, Avg, Max
from django.utils import timezone
from datetime import timedelta
from typing import List, Dict, Any

from .models import (
    UserPoints, Achievement, UserAchievement, LeaderboardEntry,
    PracticeSubmission, PracticeProgress, StudentAnalytics,
    PracticeQuestionLibrary
)
from assignments.models import Question
from .points_calculator import (
    PointsCalculator, get_top_users_by_points, get_user_rank
)
from .serializers import (
    UserPointsSerializer, AchievementSerializer, UserAchievementSerializer,
    LeaderboardEntrySerializer, StudentAnalyticsSerializer,
    PracticeQuestionSerializer, PracticeSubmissionSerializer,
    PracticeProgressSerializer, PracticeQuestionLibrarySerializer
)

import logging

logger = logging.getLogger(__name__)
User = get_user_model()


class PracticeQuestionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for practice questions.
    Teachers can create, update, and manage practice questions.
    Students can view and submit solutions to practice questions.
    """
    serializer_class = PracticeQuestionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'description', 'category']
    ordering_fields = ['difficulty', 'created_at', 'point_value']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """Filter questions based on user role and query parameters"""
        user = self.request.user
        
        if user.role == 'student':
            # Students can only see active questions
            queryset = Question.objects.filter(is_active=True)
        elif user.role in ['teacher', 'admin']:
            # Teachers can see all questions they created
            queryset = Question.objects.filter(created_by=user)
        else:
            queryset = Question.objects.none()
        
        # Apply filters
        difficulty_filter = self.request.query_params.get('difficulty')
        if difficulty_filter:
            # Capitalize difficulty for filtering as Question model uses Capitalized choices
            difficulties = [d.capitalize() for d in difficulty_filter.split(',')]
            queryset = queryset.filter(difficulty__in=difficulties)
        
        category_filter = self.request.query_params.get('category')
        if category_filter:
            queryset = queryset.filter(category__icontains=category_filter)
        
        return queryset.select_related('created_by')
    
    def perform_create(self, serializer):
        """Set the created_by field to the current user"""
        serializer.save(created_by=self.request.user)
    
    def create(self, request, *args, **kwargs):
        """Only teachers can create practice questions"""
        if request.user.role not in ['teacher', 'admin']:
            return Response(
                {'success': False, 'message': 'Only teachers can create practice questions'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        """Only teachers can update practice questions"""
        if request.user.role not in ['teacher', 'admin']:
            return Response(
                {'success': False, 'message': 'Only teachers can update practice questions'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)
    
    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        """
        Submit a practice question answer.
        Supports both coding (source_code) and MCQ (selected_option) questions.
        """
        practice_question = self.get_object()

        # Only students can submit
        if request.user.role not in ['student']:
            return Response(
                {'success': False, 'message': 'Only students can submit practice questions'},
                status=status.HTTP_403_FORBIDDEN
            )

        # ── MCQ Branch ─────────────────────────────────────────────────────
        if practice_question.question_type == 'mcq':
            selected_option = request.data.get('selected_option')
            if selected_option is None:
                return Response(
                    {'success': False, 'message': 'selected_option is required for MCQ questions'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # MCQ grading: read the correct answer from config.correct_option (integer index).
            # config = { "options": [...], "correct_option": 2 }  — set by McqEditorDialog.
            correct_option = practice_question.config.get('correct_option')

            if correct_option is None:
                return Response(
                    {
                        'success': False,
                        'message': (
                            'This MCQ question has no answer configured. '
                            'Please ask your teacher to re-save the quiz/assignment to fix this.'
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Normalize selected_option: could arrive as int, str int ("2"), or bool/string-bool ("True")
            try:
                if isinstance(selected_option, bool):
                    selected_option_int = 1 if selected_option else 0
                elif str(selected_option).strip().lower() == 'true':
                    selected_option_int = 1
                elif str(selected_option).strip().lower() == 'false':
                    selected_option_int = 0
                else:
                    selected_option_int = int(selected_option)
            except (ValueError, TypeError):
                return Response(
                    {'success': False, 'message': 'selected_option must be a valid option index (integer)'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Normalize correct_option: historically some questions might have "True" instead of index 1
            try:
                if isinstance(correct_option, bool):
                    correct_option_int = 1 if correct_option else 0
                elif str(correct_option).strip().lower() == 'true':
                    correct_option_int = 1
                elif str(correct_option).strip().lower() == 'false':
                    correct_option_int = 0
                else:
                    correct_option_int = int(correct_option)
            except (ValueError, TypeError):
                return Response(
                    {'success': False, 'message': 'correct_option in config must be a valid option index'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            all_passed = selected_option_int == correct_option_int

            current_attempts = PracticeSubmission.objects.filter(
                student=request.user, question=practice_question
            ).count()
            attempt_number = current_attempts + 1

            formatted_results = [{
                'test_case_id': 0,
                'selected_option': selected_option_int,
                'correct_option': correct_option,
                'status': 'pass' if all_passed else 'fail',
                'passed': all_passed
            }]

            submission = PracticeSubmission.objects.create(
                student=request.user,
                question=practice_question,
                source_code=f"selected_option:{selected_option_int}",
                language='mcq',
                status='success' if all_passed else 'fail',
                test_results=formatted_results,
                attempt_number=attempt_number,
                execution_time_ms=0
            )

            points_awarded = 0
            if all_passed:
                try:
                    calculator = PointsCalculator()
                    points_awarded = calculator.calculate_and_award_practice_points(submission=submission)
                except Exception as e:
                    logger.error(f"Points calculation failed for MCQ: {e}")

            # Update progress
            progress, created = PracticeProgress.objects.get_or_create(
                student=request.user,
                question=practice_question,
                defaults={
                    'attempts_count': attempt_number,
                    'best_score': 100.0 if all_passed else 0.0,
                    'time_spent': 0
                }
            )
            if not created:
                progress.attempts_count = attempt_number
                if all_passed and not progress.is_completed:
                    progress.is_completed = True
                    progress.completed_at = timezone.now()
                    progress.best_score = 100.0
                progress.save()
            elif all_passed:
                progress.is_completed = True
                progress.completed_at = timezone.now()
                progress.best_score = 100.0
                progress.save()

            return Response({
                'success': True,
                'data': {
                    'submission_id': str(submission.id),
                    'status': submission.status,
                    'all_passed': all_passed,
                    'points_awarded': points_awarded,
                    'attempt_number': attempt_number,
                    'results': formatted_results,
                    'summary': {
                        'total_tests': 1,
                        'passed_tests': 1 if all_passed else 0,
                        'execution_time_ms': 0,
                        'is_completed': all_passed
                    }
                }
            })

        # ── Coding Branch ────────────────────────────────────────────────────
        # Validate required fields
        source_code = request.data.get('source_code', '').strip()
        if not source_code:
            return Response(
                {'success': False, 'message': 'Source code is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if practice question has test cases
        if not practice_question.test_cases:
            return Response(
                {'success': False, 'message': 'This practice question has no test cases configured'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            from submissions.services import execute_code

            language = request.data.get('language', 'python')
            test_cases = practice_question.test_cases

            # Get current attempt number
            current_attempts = PracticeSubmission.objects.filter(
                student=request.user,
                question=practice_question
            ).count()
            attempt_number = current_attempts + 1

            # Execute code using the existing service
            execution_results = execute_code(source_code, language, test_cases)

            # Process results and determine success
            all_passed = True
            formatted_results = []
            total_execution_time = 0

            for i, result in enumerate(execution_results):
                test_case = test_cases[i] if i < len(test_cases) else {}

                result_status = result.get('status', 'fail')
                if result_status != 'pass':
                    all_passed = False

                execution_time = result.get('execution_time', 0)
                total_execution_time += execution_time

                err_msg = result.get('error_message', '')
                formatted_results.append({
                    'test_case_id': i,
                    'input': test_case.get('input', ''),
                    'expected_output': test_case.get('expected_output', ''),
                    'actual_output': result.get('console_output', ''),
                    'status': result_status,
                    'error_message': err_msg,
                    'error': err_msg,
                    'execution_time_ms': execution_time,
                    'passed': result_status == 'pass'
                })

            # Create submission record
            submission = PracticeSubmission.objects.create(
                student=request.user,
                question=practice_question,
                source_code=source_code,
                language=language,
                status='success' if all_passed else 'fail',
                test_results=formatted_results,
                attempt_number=attempt_number,
                execution_time_ms=total_execution_time
            )

            # Award points if successful (this will be handled by signals)
            points_awarded = 0
            if all_passed:
                calculator = PointsCalculator()
                points_awarded = calculator.calculate_and_award_practice_points(
                    submission=submission
                )

            
            # Update or create progress record
            progress, created = PracticeProgress.objects.get_or_create(
                student=request.user,
                question=practice_question,
                defaults={
                    'attempts_count': attempt_number,
                    'best_score': 100.0 if all_passed else (len([r for r in formatted_results if r['passed']]) / len(formatted_results) * 100),
                    'time_spent': 0
                }
            )
            
            if not created:
                progress.attempts_count = attempt_number
                if all_passed and not progress.is_completed:
                    progress.is_completed = True
                    progress.completed_at = timezone.now()
                    progress.best_score = 100.0
                elif not all_passed:
                    # Update best score if this attempt was better
                    current_score = len([r for r in formatted_results if r['passed']]) / len(formatted_results) * 100
                    if current_score > progress.best_score:
                        progress.best_score = current_score
                progress.save()
            elif all_passed:
                progress.is_completed = True
                progress.completed_at = timezone.now()
                progress.best_score = 100.0
                progress.save()
            
            return Response({
                'success': True,
                'data': {
                    'submission_id': submission.id,
                    'status': submission.status,
                    'all_passed': all_passed,
                    'points_awarded': points_awarded,
                    'attempt_number': attempt_number,
                    'results': formatted_results,
                    'summary': {
                        'total_tests': len(formatted_results),
                        'passed_tests': len([r for r in formatted_results if r['passed']]),
                        'execution_time_ms': total_execution_time,
                        'is_completed': all_passed
                    }
                }
            })
            
        except Exception as e:
            logger.error(f"Error processing practice submission: {e}", exc_info=True)
            
            # Create error submission record
            PracticeSubmission.objects.create(
                student=request.user,
                question=practice_question,
                source_code=source_code,
                language=language,
                status='error',
                test_results=[],
                attempt_number=attempt_number,
                execution_time_ms=0
            )
            
            return Response(
                {'success': False, 'message': f'Code execution failed: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=True, methods=['post'])
    def run_code(self, request, pk=None):
        """
        Run code for a practice question without saving submission.
        Useful for testing code before final submission.
        """
        practice_question = self.get_object()
        
        # Only students can run code
        if request.user.role not in ['student']:
            return Response(
                {'success': False, 'message': 'Only students can run practice code'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Validate required fields
        source_code = request.data.get('source_code', '').strip()
        if not source_code:
            return Response(
                {'success': False, 'message': 'Source code is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if practice question has test cases
        if not practice_question.test_cases:
            return Response(
                {'success': False, 'message': 'This practice question has no test cases configured'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            from submissions.services import execute_code
            
            language = request.data.get('language', 'python')
            test_cases = practice_question.test_cases
            
            # Execute code using the existing service
            execution_results = execute_code(source_code, language, test_cases)
            
            # Format results for response
            formatted_results = []
            all_passed = True
            
            for i, result in enumerate(execution_results):
                test_case = test_cases[i] if i < len(test_cases) else {}
                
                result_status = result.get('status', 'fail')
                if result_status != 'pass':
                    all_passed = False
                
                err_msg = result.get('error_message', '')
                formatted_results.append({
                    'test_case_id': i,
                    'input': test_case.get('input', ''),
                    'expected_output': test_case.get('expected_output', ''),
                    'actual_output': result.get('console_output', ''),
                    'status': result_status,
                    'error_message': err_msg,
                    'error': err_msg,
                    'execution_time_ms': result.get('execution_time', 0),
                    'passed': result_status == 'pass'
                })
            
            return Response({
                'success': True,
                'data': {
                    'results': formatted_results,
                    'summary': {
                        'total_tests': len(formatted_results),
                        'passed_tests': sum(1 for r in formatted_results if r['passed']),
                        'all_passed': all_passed,
                        'execution_successful': True
                    }
                }
            })
            
        except Exception as e:
            logger.error(f"Error running practice code: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': f'Code execution failed: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class PracticeSubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for practice submissions.
    Students can view their own submissions.
    Teachers can view submissions for questions they created.
    """
    serializer_class = PracticeSubmissionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['submitted_at', 'attempt_number', 'points_earned']
    ordering = ['-submitted_at']
    
    def get_queryset(self):
        """Filter submissions based on user role"""
        user = self.request.user
        
        if user.role == 'student':
            # Students can only see their own submissions
            queryset = PracticeSubmission.objects.filter(student=user)
        elif user.role in ['teacher', 'admin']:
            # Teachers can see submissions for questions they created
            queryset = PracticeSubmission.objects.filter(
                question__created_by=user
            )
        else:
            queryset = PracticeSubmission.objects.none()
        
        # Apply additional filters
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        language_filter = self.request.query_params.get('language')
        if language_filter:
            queryset = queryset.filter(language=language_filter)
        
        practice_question_filter = self.request.query_params.get('practice_question')
        if practice_question_filter:
            queryset = queryset.filter(question_id=practice_question_filter)
        
        return queryset.select_related('student', 'question')


class PracticeProgressViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for tracking practice question progress.
    Students can view their own progress and update time tracking.
    Teachers can view progress for questions they created.
    """
    serializer_class = PracticeProgressSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['question__title', 'question__category']
    ordering_fields = ['last_updated', 'completed_at', 'best_score', 'attempts_count', 'time_spent']
    ordering = ['-last_updated']
    
    def get_queryset(self):
        """Filter progress based on user role and query parameters"""
        user = self.request.user
        
        if user.role == 'student':
            # Students can only see their own progress
            queryset = PracticeProgress.objects.filter(student=user).select_related('question')
        elif user.role in ['teacher', 'admin']:
            # Teachers can see progress for questions they created
            queryset = PracticeProgress.objects.filter(
                question__created_by=user
            ).select_related('student', 'question')
        else:
            queryset = PracticeProgress.objects.none()
        
        # Apply additional filters
        completion_status = self.request.query_params.get('completion_status')
        if completion_status is not None:
            if completion_status.lower() == 'completed':
                queryset = queryset.filter(is_completed=True)
            elif completion_status.lower() == 'in_progress':
                queryset = queryset.filter(is_completed=False, attempts_count__gt=0)
            elif completion_status.lower() == 'not_started':
                queryset = queryset.filter(attempts_count=0)
        
        difficulty_filter = self.request.query_params.get('difficulty')
        if difficulty_filter:
            difficulties = [d.capitalize() for d in difficulty_filter.split(',')]
            queryset = queryset.filter(question__difficulty__in=difficulties)
        
        category_filter = self.request.query_params.get('category')
        if category_filter:
            queryset = queryset.filter(question__category__icontains=category_filter)
        
        return queryset
    
    @action(detail=False, methods=['post'])
    def start_session(self, request):
        """Start a practice session for a specific question"""
        if request.user.role != 'student':
            return Response(
                {'success': False, 'message': 'Only students can start practice sessions'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        practice_question_id = request.data.get('practice_question_id')
        if not practice_question_id:
            return Response(
                {'success': False, 'message': 'practice_question_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            practice_question = Question.objects.get(
                id=practice_question_id,
                is_active=True
            )
        except Question.DoesNotExist:
            return Response(
                {'success': False, 'message': 'Practice question not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Get or create progress record
        progress, created = PracticeProgress.objects.get_or_create(
            student=request.user,
            question=practice_question,
            defaults={
                'attempts_count': 0,
                'best_score': 0.0,
                'time_spent': 0
            }
        )
        
        return Response({
            'success': True,
            'data': PracticeProgressSerializer(progress).data,
            'message': 'Practice session started' if created else 'Practice session resumed'
        })
    
    @action(detail=False, methods=['post'])
    def update_time(self, request):
        """Update time spent on a practice question"""
        if request.user.role != 'student':
            return Response(
                {'success': False, 'message': 'Only students can update time tracking'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        practice_question_id = request.data.get('practice_question_id')
        time_spent = request.data.get('time_spent')
        
        if not practice_question_id:
            return Response(
                {'success': False, 'message': 'practice_question_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if time_spent is None:
            return Response(
                {'success': False, 'message': 'Valid time_spent (in seconds) is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            time_spent = int(time_spent)
        except (ValueError, TypeError):
            return Response(
                {'success': False, 'message': 'Valid time_spent (in seconds) is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if time_spent < 0:
            return Response(
                {'success': False, 'message': 'time_spent cannot be negative'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Get or create progress record - timer might sync before first submission
        try:
            practice_question = Question.objects.get(
                id=practice_question_id,
                is_active=True
            )
        except Question.DoesNotExist:
            return Response(
                {'success': False, 'message': 'Practice question not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        progress, created = PracticeProgress.objects.get_or_create(
            student=request.user,
            question=practice_question,
            defaults={
                'attempts_count': 0,
                'best_score': 0.0,
                'time_spent': 0
            }
        )
        
        # Update time spent (cumulative)
        progress.time_spent = time_spent
        progress.save()
        
        return Response({
            'success': True,
            'data': {
                'time_spent': progress.time_spent,
                'updated_at': progress.last_updated
            }
        })


class PracticeQuestionLibraryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for practice question library.
    Provides access to public practice questions.
    Teachers can add questions to the library.
    """
    serializer_class = PracticeQuestionLibrarySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['question__title', 'question__description', 'tags']
    ordering_fields = ['created_at', 'question__difficulty']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """Return public library questions"""
        return PracticeQuestionLibrary.objects.filter(
            is_public=True,
            question__is_active=True
        ).select_related('question', 'question__created_by')
    
    def get_permissions(self):
        """
        Instantiate and return the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Only teachers can modify library
            permission_classes = [IsAuthenticated, IsTeacher]
        else:
            # Anyone authenticated can view
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]


class PracticeAnalyticsViewSet(viewsets.ViewSet):
    """
    ViewSet for practice question analytics.
    Provides various analytics endpoints for practice questions.
    """
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        """Get summary statistics for student's practice progress"""
        if request.user.role != 'student':
            return Response(
                {'success': False, 'message': 'Only students can view progress summary'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        progress_records = PracticeProgress.objects.filter(student=request.user).select_related('question')
        
        # Calculate summary statistics
        total_attempted = progress_records.count()
        total_completed = progress_records.filter(is_completed=True).count()
        avg_score = progress_records.aggregate(avg_score=Avg('best_score'))['avg_score'] or 0
        total_time = progress_records.aggregate(total_time=Sum('time_spent'))['total_time'] or 0
        total_attempts = progress_records.aggregate(total_attempts=Sum('attempts_count'))['total_attempts'] or 0
        
        # Get category breakdown
        category_stats = {}
        for progress in progress_records:
            category = progress.question.category
            if category not in category_stats:
                category_stats[category] = {'attempted': 0, 'completed': 0}
            category_stats[category]['attempted'] += 1
            if progress.is_completed:
                category_stats[category]['completed'] += 1
        
        return Response({
            'success': True,
            'data': {
                'total_attempted': total_attempted,
                'total_completed': total_completed,
                'completion_rate': (total_completed / total_attempted * 100) if total_attempted > 0 else 0,
                'average_score': round(avg_score, 2),
                'total_time_minutes': round(total_time / 60, 2),
                'total_attempts': total_attempts,
                'category_breakdown': category_stats
            }
        })


class PointsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for user points and point-related operations.
    
    Provides endpoints for:
    - Viewing user points
    - Getting leaderboard rankings
    - Checking user rank and nearby competitors
    """
    serializer_class = UserPointsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Return points for the current user or all users for teachers"""
        if self.request.user.role == 'teacher':
            return UserPoints.objects.all().select_related('user')
        else:
            return UserPoints.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def my_points(self, request):
        """Get current user's point summary"""
        calculator = PointsCalculator()
        points_summary = calculator.get_user_points_summary(request.user)
        
        return Response({
            'user': {
                'id': request.user.id,
                'username': request.user.username,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name
            },
            'points': points_summary
        })
    
    @action(detail=False, methods=['get'])
    def leaderboard(self, request):
        """Get leaderboard rankings"""
        limit = int(request.query_params.get('limit', 50))
        point_type = request.query_params.get('type', 'total')  # total, practice, assignment
        
        try:
            top_users = get_top_users_by_points(limit=limit, point_type=point_type)
            return Response({
                'leaderboard': top_users,
                'total_users': UserPoints.objects.count(),
                'point_type': point_type
            })
        except Exception as e:
            logger.error(f"Error getting leaderboard: {e}")
            return Response(
                {'error': 'Failed to get leaderboard'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def my_rank(self, request):
        """Get current user's rank and nearby competitors"""
        try:
            rank_info = get_user_rank(request.user)
            return Response(rank_info)
        except Exception as e:
            logger.error(f"Error getting user rank: {e}")
            return Response(
                {'error': 'Failed to get rank information'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def point_history(self, request):
        """Get user's point earning history"""
        days = int(request.query_params.get('days', 30))
        start_date = timezone.now() - timedelta(days=days)
        
        # Get practice submissions with points
        practice_history = PracticeSubmission.objects.filter(
            student=request.user,
            status='success',
            submitted_at__gte=start_date,
            points_earned__gt=0
        ).select_related('question').order_by('-submitted_at')
        
        history_data = []
        for submission in practice_history:
            history_data.append({
                'date': submission.submitted_at,
                'points': submission.points_earned,
                'type': 'practice',
                'source': submission.question.title,
                'difficulty': submission.question.difficulty
            })
        
        # TODO: Add assignment point history when assignment points are implemented
        
        return Response({
            'history': history_data,
            'total_entries': len(history_data),
            'date_range': {
                'start': start_date,
                'end': timezone.now()
            }
        })
    
    @action(detail=False, methods=['post'])
    def recalculate(self, request):
        """Recalculate points for current user (admin/debug endpoint)"""
        if not request.user.is_staff:
            return Response(
                {'error': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        try:
            calculator = PointsCalculator()
            updated_summary = calculator.recalculate_user_points(request.user)
            
            return Response({
                'message': 'Points recalculated successfully',
                'points': updated_summary
            })
        except Exception as e:
            logger.error(f"Error recalculating points: {e}")
            return Response(
                {'error': 'Failed to recalculate points'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AchievementViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for achievements and user achievement progress.
    
    Provides endpoints for:
    - Viewing available achievements
    - Getting user's earned achievements
    - Checking progress toward achievements
    - Achievement notifications
    """
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]
    queryset = Achievement.objects.filter(is_active=True)
    
    @action(detail=False, methods=['get'])
    def earned(self, request):
        """Get achievements earned by current user"""
        earned_achievements = UserAchievement.objects.filter(
            user=request.user
        ).select_related('achievement').order_by('-earned_at')
        
        serializer = UserAchievementSerializer(earned_achievements, many=True)
        return Response({
            'success': True,
            'data': {
                'earned_achievements': serializer.data,
                'total_earned': earned_achievements.count()
            }
        })
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get available achievements and progress"""
        from .achievement_engine import AchievementEngine
        
        all_achievements = Achievement.objects.filter(is_active=True)
        earned_ids = UserAchievement.objects.filter(
            user=request.user
        ).values_list('achievement_id', flat=True)
        
        engine = AchievementEngine()
        available_achievements = []
        
        for achievement in all_achievements:
            is_earned = achievement.id in earned_ids
            
            # Get progress information
            if is_earned:
                progress = {'current': 1, 'required': 1, 'percentage': 100}
                earned_at = UserAchievement.objects.get(
                    user=request.user, 
                    achievement=achievement
                ).earned_at
            else:
                progress = engine.get_achievement_progress(request.user, achievement)
                earned_at = None
            
            available_achievements.append({
                'achievement': AchievementSerializer(achievement).data,
                'is_earned': is_earned,
                'progress': progress,
                'earned_at': earned_at
            })
        
        return Response({
            'success': True,
            'data': {
                'achievements': available_achievements,
                'total_available': len(available_achievements),
                'total_earned': len([a for a in available_achievements if a['is_earned']])
            }
        })
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Get recently earned achievements"""
        days = int(request.query_params.get('days', 7))
        start_date = timezone.now() - timedelta(days=days)
        
        recent_achievements = UserAchievement.objects.filter(
            user=request.user,
            earned_at__gte=start_date
        ).select_related('achievement').order_by('-earned_at')
        
        serializer = UserAchievementSerializer(recent_achievements, many=True)
        return Response({
            'success': True,
            'data': {
                'recent_achievements': serializer.data,
                'count': recent_achievements.count()
            }
        })
    
    @action(detail=True, methods=['get'])
    def progress(self, request, pk=None):
        """Get progress toward a specific achievement"""
        from .achievement_engine import AchievementEngine
        
        achievement = self.get_object()
        
        # Check if already earned
        is_earned = UserAchievement.objects.filter(
            user=request.user,
            achievement=achievement
        ).exists()
        
        if is_earned:
            earned_achievement = UserAchievement.objects.get(
                user=request.user,
                achievement=achievement
            )
            return Response({
                'success': True,
                'data': {
                    'achievement': AchievementSerializer(achievement).data,
                    'is_earned': True,
                    'earned_at': earned_achievement.earned_at,
                    'progress': {'current': 1, 'required': 1, 'percentage': 100}
                }
            })
        
        # Get progress information
        engine = AchievementEngine()
        progress = engine.get_achievement_progress(request.user, achievement)
        
        return Response({
            'success': True,
            'data': {
                'achievement': AchievementSerializer(achievement).data,
                'is_earned': False,
                'earned_at': None,
                'progress': progress
            }
        })
    
    @action(detail=False, methods=['get'])
    def categories(self, request):
        """Get achievement categories and counts"""
        achievements_by_type = {}
        
        for achievement in Achievement.objects.filter(is_active=True):
            badge_type = achievement.badge_type
            if badge_type not in achievements_by_type:
                achievements_by_type[badge_type] = {
                    'total': 0,
                    'earned': 0,
                    'achievements': []
                }
            
            achievements_by_type[badge_type]['total'] += 1
            achievements_by_type[badge_type]['achievements'].append(achievement.id)
            
            # Check if user has earned this achievement
            if UserAchievement.objects.filter(
                user=request.user,
                achievement=achievement
            ).exists():
                achievements_by_type[badge_type]['earned'] += 1
        
        return Response({
            'success': True,
            'data': {
                'categories': achievements_by_type
            }
        })
    
    @action(detail=False, methods=['post'])
    def check_achievements(self, request):
        """Manually trigger achievement checking (for testing/admin)"""
        if not request.user.is_staff:
            return Response(
                {'success': False, 'message': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        try:
            from .achievement_engine import check_user_achievements
            
            target_user_id = request.data.get('user_id')
            if target_user_id:
                target_user = User.objects.get(id=target_user_id)
            else:
                target_user = request.user
            
            newly_awarded = check_user_achievements(
                user=target_user,
                trigger_event='manual_check'
            )
            
            return Response({
                'success': True,
                'data': {
                    'user': target_user.username,
                    'newly_awarded': [
                        {
                            'achievement_name': ua.achievement.name,
                            'achievement_id': ua.achievement.id,
                            'earned_at': ua.earned_at
                        }
                        for ua in newly_awarded
                    ],
                    'count': len(newly_awarded)
                }
            })
            
        except User.DoesNotExist:
            return Response(
                {'success': False, 'message': 'User not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f"Error in manual achievement check: {e}")
            return Response(
                {'success': False, 'message': 'Achievement check failed'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for leaderboard functionality with caching optimization.
    
    Provides endpoints for:
    - Global leaderboards with pagination and caching
    - Class-specific leaderboards with performance optimization
    - User ranking information with nearby competitors
    - Leaderboard filtering and sorting with cache support
    """
    serializer_class = LeaderboardEntrySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Get leaderboard entries based on type and filters"""
        leaderboard_type = self.request.query_params.get('type', 'global')
        class_id = self.request.query_params.get('class_id')
        
        queryset = LeaderboardEntry.objects.filter(
            leaderboard_type=leaderboard_type
        ).select_related('user')
        
        if leaderboard_type == 'class' and class_id:
            queryset = queryset.filter(class_id=class_id)
        
        return queryset.order_by('rank')
    
    @action(detail=False, methods=['get'])
    def global_ranking(self, request):
        """Get paginated global leaderboard ranking with caching"""
        from .cached_leaderboard_manager import cached_leaderboard_manager
        
        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 20))
        offset = (page - 1) * page_size
        
        # Get cached leaderboard data
        leaderboard_entries = cached_leaderboard_manager.get_leaderboard(
            leaderboard_type='global',
            limit=page_size,
            offset=offset
        )
        
        # Calculate pagination info
        total_entries = LeaderboardEntry.objects.filter(
            leaderboard_type='global',
            class_id__isnull=True
        ).count()
        
        pagination = {
            'page': page,
            'page_size': page_size,
            'total_entries': total_entries,
            'total_pages': (total_entries + page_size - 1) // page_size,
            'has_next': offset + page_size < total_entries,
            'has_previous': page > 1
        }
        
        return Response({
            'success': True,
            'data': {
                'leaderboard': leaderboard_entries,
                'pagination': pagination
            }
        })
    
    @action(detail=False, methods=['get'])
    def class_ranking(self, request):
        """Get paginated class-specific leaderboard ranking with caching"""
        from .cached_leaderboard_manager import cached_leaderboard_manager
        
        class_id = request.query_params.get('class_id')
        if not class_id:
            return Response(
                {'success': False, 'message': 'class_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 20))
        offset = (page - 1) * page_size
        
        # Get cached leaderboard data
        leaderboard_entries = cached_leaderboard_manager.get_leaderboard(
            leaderboard_type='class',
            class_id=class_id,
            limit=page_size,
            offset=offset
        )
        
        # Calculate pagination info
        total_entries = LeaderboardEntry.objects.filter(
            leaderboard_type='class',
            class_id=class_id
        ).count()
        
        pagination = {
            'page': page,
            'page_size': page_size,
            'total_entries': total_entries,
            'total_pages': (total_entries + page_size - 1) // page_size,
            'has_next': offset + page_size < total_entries,
            'has_previous': page > 1
        }
        
        return Response({
            'success': True,
            'data': {
                'leaderboard': leaderboard_entries,
                'pagination': pagination,
                'class_id': class_id
            }
        })

    @action(detail=False, methods=['get'])
    def daily_ranking(self, request):
        """Get daily leaderboard — points earned since midnight today."""
        from .models import LeaderboardManager
        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 20))

        # Rebuild daily leaderboard from live submissions
        LeaderboardManager.update_daily_leaderboard()

        offset = (page - 1) * page_size
        entries = LeaderboardEntry.objects.filter(
            leaderboard_type='daily'
        ).select_related('user').order_by('rank')[offset:offset + page_size]

        total_entries = LeaderboardEntry.objects.filter(leaderboard_type='daily').count()

        leaderboard = [
            {
                'rank': e.rank,
                'user': {
                    'id': e.user.id,
                    'username': e.user.username,
                    'first_name': e.user.first_name,
                    'last_name': e.user.last_name,
                },
                'total_points': e.total_points,
                'completed_problems': e.completed_problems,
            }
            for e in entries
        ]

        return Response({
            'success': True,
            'data': {
                'leaderboard': leaderboard,
                'leaderboard_type': 'daily',
                'total_users': UserPoints.objects.count(),
                'pagination': {
                    'page': page,
                    'page_size': page_size,
                    'total_entries': total_entries,
                    'total_pages': max(1, (total_entries + page_size - 1) // page_size),
                    'has_next': offset + page_size < total_entries,
                    'has_previous': page > 1,
                }
            }
        })

    @action(detail=False, methods=['get'])
    def weekly_ranking(self, request):
        """Get weekly leaderboard — points earned since Monday 00:00."""
        from .models import LeaderboardManager
        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 20))

        LeaderboardManager.update_weekly_leaderboard()

        offset = (page - 1) * page_size
        entries = LeaderboardEntry.objects.filter(
            leaderboard_type='weekly'
        ).select_related('user').order_by('rank')[offset:offset + page_size]

        total_entries = LeaderboardEntry.objects.filter(leaderboard_type='weekly').count()

        leaderboard = [
            {
                'rank': e.rank,
                'user': {
                    'id': e.user.id,
                    'username': e.user.username,
                    'first_name': e.user.first_name,
                    'last_name': e.user.last_name,
                },
                'total_points': e.total_points,
                'completed_problems': e.completed_problems,
            }
            for e in entries
        ]

        return Response({
            'success': True,
            'data': {
                'leaderboard': leaderboard,
                'leaderboard_type': 'weekly',
                'total_users': UserPoints.objects.count(),
                'pagination': {
                    'page': page,
                    'page_size': page_size,
                    'total_entries': total_entries,
                    'total_pages': max(1, (total_entries + page_size - 1) // page_size),
                    'has_next': offset + page_size < total_entries,
                    'has_previous': page > 1,
                }
            }
        })

    @action(detail=False, methods=['get'])
    def my_rank(self, request):

        """Get current user's rank and nearby competitors with caching"""
        from .cached_leaderboard_manager import cached_leaderboard_manager
        
        leaderboard_type = request.query_params.get('type', 'global')
        class_id = request.query_params.get('class_id')
        
        # Validate class_id for class leaderboards
        if leaderboard_type == 'class' and not class_id:
            return Response(
                {'success': False, 'message': 'class_id is required for class leaderboards'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Get user rank with caching
        user_rank = cached_leaderboard_manager.get_user_rank(
            user=request.user,
            leaderboard_type=leaderboard_type,
            class_id=class_id
        )
        
        if not user_rank:
            return Response({
                'success': False,
                'message': 'User not found in leaderboard. Complete some practice questions to get ranked!'
            })
        
        # Get nearby competitors with caching
        nearby_competitors = cached_leaderboard_manager.get_nearby_competitors(
            user=request.user,
            leaderboard_type=leaderboard_type,
            class_id=class_id,
            range_size=3
        )
        
        # Get user points for additional context
        try:
            user_points = UserPoints.objects.get(user=request.user)
            total_points = user_points.total_points
            completed_problems = PracticeProgress.objects.filter(
                student=request.user,
                is_completed=True
            ).count()
        except UserPoints.DoesNotExist:
            total_points = 0
            completed_problems = 0
        
        return Response({
            'success': True,
            'data': {
                'user_rank': user_rank,
                'user_points': total_points,
                'user_problems': completed_problems,
                'nearby_competitors': nearby_competitors,
                'leaderboard_type': leaderboard_type,
                'class_id': class_id if leaderboard_type == 'class' else None
            }
        })
    
    @action(detail=False, methods=['get'])
    def user_position(self, request):
        """Get current user's position in all leaderboards they participate in"""
        from .models import LeaderboardManager
        
        # Update leaderboards
        LeaderboardManager.update_leaderboards_for_user(request.user)
        
        # Get user entries from all leaderboards
        user_entries = LeaderboardEntry.objects.filter(
            user=request.user
        ).select_related('user')
        
        positions = {}
        for entry in user_entries:
            key = entry.leaderboard_type
            if entry.leaderboard_type == 'class':
                key = f"class_{entry.class_id}"
            
            positions[key] = {
                'leaderboard_type': entry.leaderboard_type,
                'class_id': str(entry.class_id) if entry.class_id else None,
                'rank': entry.rank,
                'total_points': entry.total_points,
                'completed_problems': entry.completed_problems,
                'updated_at': entry.updated_at
            }
        
        return Response({
            'success': True,
            'data': {
                'user_positions': positions,
                'user': {
                    'id': request.user.id,
                    'username': request.user.username,
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name
                }
            }
        })
    
    @action(detail=False, methods=['get'])
    def top_performers(self, request):
        """Get top performers with filtering options"""
        from .models import LeaderboardManager
        
        leaderboard_type = request.query_params.get('type', 'global')
        class_id = request.query_params.get('class_id')
        limit = int(request.query_params.get('limit', 10))
        
        # Update appropriate leaderboard
        if leaderboard_type == 'global':
            LeaderboardManager.update_global_leaderboard()
        elif class_id:
            LeaderboardManager.update_class_leaderboard(class_id)
        
        # Get top performers
        queryset = LeaderboardEntry.objects.filter(
            leaderboard_type=leaderboard_type
        ).select_related('user').order_by('rank')[:limit]
        
        if leaderboard_type == 'class' and class_id:
            queryset = queryset.filter(class_id=class_id)
        
        # Format response
        top_performers = []
        for entry in queryset:
            top_performers.append({
                'rank': entry.rank,
                'user': {
                    'id': entry.user.id,
                    'username': entry.user.username,
                    'first_name': entry.user.first_name,
                    'last_name': entry.user.last_name
                },
                'total_points': entry.total_points,
                'completed_problems': entry.completed_problems,
                'updated_at': entry.updated_at
            })
        
        return Response({
            'success': True,
            'data': {
                'top_performers': top_performers,
                'leaderboard_type': leaderboard_type,
                'class_id': class_id if leaderboard_type == 'class' else None,
                'limit': limit
            }
        })
    
    @action(detail=False, methods=['post'])
    def refresh(self, request):
        """Manually refresh leaderboards (admin/teacher only)"""
        if request.user.role not in ['teacher', 'admin']:
            return Response(
                {'success': False, 'message': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        try:
            from .models import LeaderboardManager
            
            leaderboard_type = request.data.get('type', 'global')
            class_id = request.data.get('class_id')
            
            if leaderboard_type == 'global':
                count = LeaderboardManager.update_global_leaderboard()
                message = f'Global leaderboard refreshed with {count} entries'
            elif leaderboard_type == 'class' and class_id:
                count = LeaderboardManager.update_class_leaderboard(class_id)
                message = f'Class leaderboard refreshed with {count} entries'
            else:
                return Response(
                    {'success': False, 'message': 'Invalid leaderboard type or missing class_id'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            return Response({
                'success': True,
                'message': message,
                'entries_updated': count
            })
            
        except Exception as e:
            logger.error(f"Error refreshing leaderboard: {e}")
            return Response(
                {'success': False, 'message': 'Failed to refresh leaderboard'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AnalyticsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for comprehensive analytics and statistics.
    
    Provides endpoints for:
    - Student performance analytics with comprehensive metrics
    - Class-wide analytics (for teachers) with detailed insights
    - Performance trends and concept mastery tracking
    - Real-time analytics updates and comparisons
    """
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def student_dashboard(self, request):
        """Get comprehensive student analytics for dashboard with caching"""
        from .cached_analytics_aggregator import cached_analytics_aggregator
        
        try:
            # Get comprehensive performance summary using cached analytics
            performance_summary = cached_analytics_aggregator.get_student_performance_summary(request.user)
            
            return Response({
                'success': True,
                'data': performance_summary
            })
            
        except Exception as e:
            logger.error(f"Error getting student dashboard analytics: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to load analytics'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def class_overview(self, request):
        """Get comprehensive class-wide analytics with caching (teachers only)"""
        if request.user.role not in ['teacher', 'admin']:
            return Response(
                {'success': False, 'message': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        class_id = request.query_params.get('class_id')
        if not class_id:
            return Response(
                {'success': False, 'message': 'class_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            from .cached_analytics_aggregator import cached_analytics_aggregator
            from classes.models import Class
            
            # Get class object
            try:
                # Validate UUID format first
                import uuid
                uuid.UUID(class_id)
                class_obj = Class.objects.get(id=class_id, instructor=request.user)
            except (Class.DoesNotExist, ValueError, TypeError):
                return Response(
                    {'success': False, 'message': 'Class not found or access denied'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Get comprehensive class analytics with caching
            class_analytics = cached_analytics_aggregator.get_class_analytics_summary(class_obj)
            
            return Response({
                'success': True,
                'data': class_analytics
            })
            
        except ImportError:
            return Response(
                {'success': False, 'message': 'Class analytics not available'},
                status=status.HTTP_501_NOT_IMPLEMENTED
            )
        except Exception as e:
            logger.error(f"Error getting class analytics: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to load class analytics'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def comprehensive_class_analytics(self, request):
        """Get comprehensive class analytics with advanced metrics (teachers only)"""
        if request.user.role not in ['teacher', 'admin']:
            return Response(
                {'success': False, 'message': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        class_id = request.query_params.get('class_id')
        if not class_id:
            return Response(
                {'success': False, 'message': 'class_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            from .class_analytics_service import class_analytics_service
            from classes.models import Class
            
            # Get class object
            try:
                import uuid
                uuid.UUID(class_id)
                class_obj = Class.objects.get(id=class_id, instructor=request.user)
            except (Class.DoesNotExist, ValueError, TypeError):
                return Response(
                    {'success': False, 'message': 'Class not found or access denied'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Get comprehensive analytics
            comprehensive_analytics = class_analytics_service.get_comprehensive_class_analytics(class_obj)
            
            return Response({
                'success': True,
                'data': comprehensive_analytics
            })
            
        except ImportError:
            return Response(
                {'success': False, 'message': 'Class analytics not available'},
                status=status.HTTP_501_NOT_IMPLEMENTED
            )
        except Exception as e:
            logger.error(f"Error getting comprehensive class analytics: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to load comprehensive class analytics'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def struggling_students(self, request):
        """Get detailed analysis of struggling students (teachers only)"""
        if request.user.role not in ['teacher', 'admin']:
            return Response(
                {'success': False, 'message': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        class_id = request.query_params.get('class_id')
        if not class_id:
            return Response(
                {'success': False, 'message': 'class_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            from .class_analytics_service import class_analytics_service
            from classes.models import Class
            
            # Get class object
            try:
                import uuid
                uuid.UUID(class_id)
                class_obj = Class.objects.get(id=class_id, instructor=request.user)
            except (Class.DoesNotExist, ValueError, TypeError):
                return Response(
                    {'success': False, 'message': 'Class not found or access denied'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Get comprehensive analytics and extract struggling students
            analytics = class_analytics_service.get_comprehensive_class_analytics(class_obj)
            struggling_students = analytics.get('struggling_students', [])
            
            # Add additional context
            total_students = analytics.get('class_info', {}).get('total_students', 0)
            struggle_percentage = round((len(struggling_students) / total_students) * 100, 2) if total_students > 0 else 0
            
            return Response({
                'success': True,
                'data': {
                    'struggling_students': struggling_students,
                    'summary': {
                        'total_struggling': len(struggling_students),
                        'total_students': total_students,
                        'struggle_percentage': struggle_percentage
                    },
                    'common_indicators': self._analyze_common_struggle_indicators(struggling_students)
                }
            })
            
        except ImportError:
            return Response(
                {'success': False, 'message': 'Class analytics not available'},
                status=status.HTTP_501_NOT_IMPLEMENTED
            )
        except Exception as e:
            logger.error(f"Error getting struggling students: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to identify struggling students'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def _analyze_common_struggle_indicators(self, struggling_students: List[Dict]) -> Dict[str, Any]:
        """Analyze common patterns in struggling students."""
        if not struggling_students:
            return {}
        
        # Count frequency of each struggle indicator
        indicator_counts = {}
        for student in struggling_students:
            for indicator in student.get('struggle_indicators', []):
                indicator_counts[indicator] = indicator_counts.get(indicator, 0) + 1
        
        # Sort by frequency
        sorted_indicators = sorted(indicator_counts.items(), key=lambda x: x[1], reverse=True)
        
        return {
            'most_common_indicators': sorted_indicators[:5],
            'total_indicators': len(indicator_counts),
            'avg_indicators_per_student': round(
                sum(len(s.get('struggle_indicators', [])) for s in struggling_students) / len(struggling_students), 2
            )
        }
    
    @action(detail=False, methods=['get'])
    def problem_analytics(self, request):
        """Get detailed problem-specific analytics (teachers only)"""
        if request.user.role not in ['teacher', 'admin']:
            return Response(
                {'success': False, 'message': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        class_id = request.query_params.get('class_id')
        if not class_id:
            return Response(
                {'success': False, 'message': 'class_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            from .class_analytics_service import class_analytics_service
            from classes.models import Class
            
            # Get class object
            try:
                import uuid
                uuid.UUID(class_id)
                class_obj = Class.objects.get(id=class_id, instructor=request.user)
            except (Class.DoesNotExist, ValueError, TypeError):
                return Response(
                    {'success': False, 'message': 'Class not found or access denied'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Get comprehensive analytics and extract problem analytics
            analytics = class_analytics_service.get_comprehensive_class_analytics(class_obj)
            problem_analytics = analytics.get('problem_analytics', {})
            
            return Response({
                'success': True,
                'data': problem_analytics
            })
            
        except ImportError:
            return Response(
                {'success': False, 'message': 'Class analytics not available'},
                status=status.HTTP_501_NOT_IMPLEMENTED
            )
        except Exception as e:
            logger.error(f"Error getting problem analytics: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to load problem analytics'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def export_class_report(self, request):
        """Export comprehensive class report (teachers only)"""
        if request.user.role not in ['teacher', 'admin']:
            return Response(
                {'success': False, 'message': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        class_id = request.query_params.get('class_id')
        format_type = request.query_params.get('format', 'csv').lower()
        
        if not class_id:
            return Response(
                {'success': False, 'message': 'class_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if format_type not in ['csv', 'json']:
            return Response(
                {'success': False, 'message': 'format must be csv or json'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            from .class_analytics_service import class_analytics_service
            from classes.models import Class
            
            # Get class object
            try:
                import uuid
                uuid.UUID(class_id)
                class_obj = Class.objects.get(id=class_id, instructor=request.user)
            except (Class.DoesNotExist, ValueError, TypeError):
                return Response(
                    {'success': False, 'message': 'Class not found or access denied'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Generate and return report
            return class_analytics_service.generate_class_report(class_obj, format_type)
            
        except ImportError:
            return Response(
                {'success': False, 'message': 'Class analytics not available'},
                status=status.HTTP_501_NOT_IMPLEMENTED
            )
        except Exception as e:
            logger.error(f"Error generating class report: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to generate class report'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def performance_trends(self, request):
        """Get detailed performance trends over time using AnalyticsAggregator"""
        try:
            days = int(request.query_params.get('days', 30))
        except (ValueError, TypeError):
            days = 30  # Default to 30 days if invalid parameter
        
        try:
            from .analytics_aggregator import analytics_aggregator
            
            # Update analytics to ensure fresh data
            analytics = analytics_aggregator.update_student_analytics(request.user)
            
            # Get performance trend from analytics
            performance_trend = analytics.performance_trend
            
            # Calculate summary statistics
            if performance_trend:
                total_activities = sum(day['total_activities'] for day in performance_trend)
                active_days = len([day for day in performance_trend if day['has_activity']])
                avg_score = sum(day['average_score'] for day in performance_trend if day['has_activity']) / active_days if active_days > 0 else 0
                
                summary = {
                    'total_days_analyzed': len(performance_trend),
                    'active_days': active_days,
                    'total_activities': total_activities,
                    'avg_activities_per_day': total_activities / len(performance_trend) if performance_trend else 0,
                    'avg_score': round(avg_score, 2),
                    'activity_rate': round((active_days / len(performance_trend)) * 100, 2) if performance_trend else 0
                }
            else:
                summary = {
                    'total_days_analyzed': 0,
                    'active_days': 0,
                    'total_activities': 0,
                    'avg_activities_per_day': 0,
                    'avg_score': 0,
                    'activity_rate': 0
                }
            
            return Response({
                'success': True,
                'data': {
                    'trends': performance_trend,
                    'summary': summary,
                    'date_range': {
                        'days': days,
                        'end_date': timezone.now().date().isoformat()
                    }
                }
            })
            
        except Exception as e:
            logger.error(f"Error getting performance trends: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to load performance trends'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def concept_mastery(self, request):
        """Get detailed concept mastery analysis"""
        try:
            from .analytics_aggregator import analytics_aggregator
            
            # Update analytics to ensure fresh data
            analytics = analytics_aggregator.update_student_analytics(request.user)
            
            # Get concept mastery data
            concept_mastery = analytics.concept_mastery
            
            # Calculate additional insights
            if concept_mastery:
                mastery_scores = list(concept_mastery.values())
                insights = {
                    'total_concepts': len(concept_mastery),
                    'mastered_concepts': len([score for score in mastery_scores if score >= 80]),
                    'struggling_concepts': len([score for score in mastery_scores if score < 50]),
                    'average_mastery': round(sum(mastery_scores) / len(mastery_scores), 2) if mastery_scores else 0,
                    'strongest_concept': max(concept_mastery.items(), key=lambda x: x[1]) if concept_mastery else None,
                    'weakest_concept': min(concept_mastery.items(), key=lambda x: x[1]) if concept_mastery else None
                }
            else:
                insights = {
                    'total_concepts': 0,
                    'mastered_concepts': 0,
                    'struggling_concepts': 0,
                    'average_mastery': 0,
                    'strongest_concept': None,
                    'weakest_concept': None
                }
            
            return Response({
                'success': True,
                'data': {
                    'concept_mastery': concept_mastery,
                    'insights': insights
                }
            })
            
        except Exception as e:
            logger.error(f"Error getting concept mastery: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to load concept mastery'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def student_performance(self, request):
        """
        Comprehensive student performance endpoint.
        Returns: weekly_activity, difficulty_breakdown, language_breakdown,
                 class_comparison for the authenticated student.
        Accepts ?timeframe=7d|30d|all  (default: 30d)
        """
        from django.db.models import Count, Avg, Q
        from datetime import timedelta

        timeframe = request.query_params.get('timeframe', '30d')
        if timeframe == '7d':
            days = 7
        elif timeframe == 'all':
            days = 365
        else:
            days = 30

        student = request.user
        start_date = timezone.now() - timedelta(days=days)

        try:
            # ── 1. Weekly Activity (last 4 weeks from practice + assignment) ──
            weekly_activity = []
            for week_offset in range(3, -1, -1):
                week_start = timezone.now().date() - timedelta(days=(week_offset + 1) * 7 - 1)
                week_end   = timezone.now().date() - timedelta(days=week_offset * 7)
                practice_count = PracticeSubmission.objects.filter(
                    student=student,
                    submitted_at__date__gte=week_start,
                    submitted_at__date__lte=week_end,
                    status='success'
                ).count()
                assignment_count = 0
                try:
                    from submissions.models import SubmissionAttempt
                    assignment_count = SubmissionAttempt.objects.filter(
                        student=student,
                        created_at__date__gte=week_start,
                        created_at__date__lte=week_end,
                        status='success'
                    ).count()
                except ImportError:
                    pass
                week_num = 4 - week_offset
                weekly_activity.append({
                    'week': f'Week {week_num}',
                    'week_start': week_start.isoformat(),
                    'practice': practice_count,
                    'assignments': assignment_count,
                    'total': practice_count + assignment_count,
                })

            # ── 2. Difficulty Breakdown ──
            difficulty_breakdown = []
            for diff in ['Easy', 'Medium', 'Hard']:
                qs = PracticeProgress.objects.filter(
                    student=student,
                    question__difficulty=diff
                )
                total = qs.count()
                completed = qs.filter(is_completed=True).count()
                avg_score = qs.aggregate(avg=Avg('best_score'))['avg'] or 0.0
                avg_time_sec = qs.aggregate(avg_time=Avg('time_spent'))['avg_time'] or 0
                difficulty_breakdown.append({
                    'difficulty': diff,
                    'total': total,
                    'completed': completed,
                    'avg_score': round(avg_score, 2),
                    'avg_time': int(avg_time_sec // 60),  # minutes
                })

            # ── 3. Language Breakdown ──
            lang_qs = PracticeSubmission.objects.filter(
                student=student,
                submitted_at__gte=start_date
            ).values('language').annotate(
                count=Count('id')
            ).order_by('-count')
            
            lang_map = {}
            for row in lang_qs:
                lang_name = row['language'] or 'python'
                if lang_name not in lang_map:
                    lang_map[lang_name] = {'submissions': 0, 'avg_score': 0}
                lang_map[lang_name]['submissions'] += row['count']
                
            try:
                from submissions.models import SubmissionAttempt
                assign_count = SubmissionAttempt.objects.filter(
                    student=student, created_at__gte=start_date
                ).count()
                if assign_count > 0:
                    if 'python' not in lang_map:
                        lang_map['python'] = {'submissions': 0, 'avg_score': 0}
                    lang_map['python']['submissions'] += assign_count
            except ImportError:
                pass
                
            language_breakdown = [
                {
                    'language': k,
                    'submissions': v['submissions'],
                    'avg_score': v['avg_score'],
                }
                for k, v in lang_map.items()
            ]
            language_breakdown.sort(key=lambda x: x['submissions'], reverse=True)

            # ── 4. Class Comparison (Total Points) ──
            class_avg_score = None
            try:
                from gamification.models import StudentAnalytics
                from classes.models import Class

                # Get classes the student is enrolled in
                enrolled_class_ids = Class.objects.filter(
                    enrollments__user=student,
                    enrollments__role='student'
                ).values_list('id', flat=True)

                if enrolled_class_ids.exists():
                    # student's own total points
                    student_pts = getattr(student, 'points', None)
                    student_avg = student_pts.total_points if student_pts else 0

                    # class avg points for all students in those classes
                    from django.contrib.auth import get_user_model
                    User = get_user_model()
                    classmates = User.objects.filter(
                        enrollments__class_obj_id__in=enrolled_class_ids,
                        enrollments__role='student'
                    ).distinct()

                    class_avg = UserPoints.objects.filter(
                        user__in=classmates
                    ).aggregate(avg=Avg('total_points')).get('avg') or 0

                    class_avg_score = {
                        'student_avg': int(student_avg),
                        'class_avg': int(class_avg),
                    }
            except Exception as e:
                logger.warning(f"Class comparison calculation failed: {e}")
                class_avg_score = None

            return Response({
                'success': True,
                'data': {
                    'weekly_activity': weekly_activity,
                    'difficulty_breakdown': difficulty_breakdown,
                    'language_breakdown': language_breakdown,
                    'class_comparison': class_avg_score,
                    'timeframe': timeframe,
                }
            })

        except Exception as e:
            logger.error(f"Error getting student performance data: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to load performance data'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['get'])
    def streak_analysis(self, request):
        """Get detailed streak analysis and activity patterns"""
        try:
            from .analytics_aggregator import analytics_aggregator
            
            # Update analytics to ensure fresh data
            analytics = analytics_aggregator.update_student_analytics(request.user)
            
            # Get recent activity for streak context
            recent_activity = analytics_aggregator._calculate_performance_trend(request.user, days=14)
            
            # Calculate streak insights
            active_days_last_week = len([day for day in recent_activity[-7:] if day['has_activity']])
            active_days_last_two_weeks = len([day for day in recent_activity if day['has_activity']])
            
            streak_insights = {
                'current_streak': analytics.current_streak,
                'longest_streak': analytics.longest_streak,
                'active_days_last_week': active_days_last_week,
                'active_days_last_two_weeks': active_days_last_two_weeks,
                'streak_status': 'excellent' if analytics.current_streak >= 7 else 'good' if analytics.current_streak >= 3 else 'needs_improvement',
                'days_until_milestone': max(0, 7 - analytics.current_streak) if analytics.current_streak < 7 else max(0, 30 - analytics.current_streak) if analytics.current_streak < 30 else 0
            }
            
            return Response({
                'success': True,
                'data': {
                    'streak_analysis': streak_insights,
                    'recent_activity_pattern': recent_activity
                }
            })
            
        except Exception as e:
            logger.error(f"Error getting streak analysis: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to load streak analysis'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def time_analysis(self, request):
        """Get detailed time tracking and productivity analysis"""
        try:
            from .analytics_aggregator import analytics_aggregator
            
            # Update analytics to ensure fresh data
            analytics = analytics_aggregator.update_student_analytics(request.user)
            
            # Get detailed time breakdown
            total_time_minutes = analytics.total_time_spent
            total_time_hours = total_time_minutes / 60
            
            # Get practice time breakdown
            practice_time_data = PracticeProgress.objects.filter(
                student=request.user,
                time_spent__gt=0
            ).aggregate(
                total_practice_time=Sum('time_spent'),
                avg_time_per_question=Avg('time_spent'),
                max_time_single_question=Max('time_spent')
            )
            
            practice_time_seconds = practice_time_data['total_practice_time'] or 0
            practice_time_minutes = practice_time_seconds / 60
            
            # Calculate productivity metrics
            completed_questions = analytics.total_practice_completed + analytics.total_assignments_completed
            avg_time_per_completion = (total_time_minutes / completed_questions) if completed_questions > 0 else 0
            
            time_insights = {
                'total_time_minutes': total_time_minutes,
                'total_time_hours': round(total_time_hours, 2),
                'practice_time_minutes': round(practice_time_minutes, 2),
                'estimated_assignment_time_minutes': total_time_minutes - practice_time_minutes,
                'avg_time_per_completion_minutes': round(avg_time_per_completion, 2),
                'avg_time_per_practice_minutes': round((practice_time_data['avg_time_per_question'] or 0) / 60, 2),
                'max_time_single_practice_minutes': round((practice_time_data['max_time_single_question'] or 0) / 60, 2),
                'productivity_score': min(100, max(0, 100 - (avg_time_per_completion - 15) * 2)) if avg_time_per_completion > 0 else 0
            }
            
            return Response({
                'success': True,
                'data': {
                    'time_analysis': time_insights,
                    'last_activity': analytics.last_activity
                }
            })
            
        except Exception as e:
            logger.error(f"Error getting time analysis: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to load time analysis'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def comparison_data(self, request):
        """Get data for comparing student performance with class/global averages"""
        try:
            from .analytics_aggregator import analytics_aggregator
            
            # Get student analytics
            student_analytics = analytics_aggregator.update_student_analytics(request.user)
            
            # Get global averages
            global_averages = StudentAnalytics.objects.aggregate(
                avg_practice_completed=Avg('total_practice_completed'),
                avg_assignments_completed=Avg('total_assignments_completed'),
                avg_score=Avg('average_score'),
                avg_streak=Avg('current_streak'),
                avg_time_spent=Avg('total_time_spent')
            )
            
            # Calculate percentiles
            total_students = StudentAnalytics.objects.count()
            if total_students > 0:
                practice_percentile = (StudentAnalytics.objects.filter(
                    total_practice_completed__lt=student_analytics.total_practice_completed
                ).count() / total_students) * 100
                
                score_percentile = (StudentAnalytics.objects.filter(
                    average_score__lt=student_analytics.average_score
                ).count() / total_students) * 100
                
                streak_percentile = (StudentAnalytics.objects.filter(
                    current_streak__lt=student_analytics.current_streak
                ).count() / total_students) * 100
            else:
                practice_percentile = score_percentile = streak_percentile = 0
            
            comparison_data = {
                'student_metrics': {
                    'practice_completed': student_analytics.total_practice_completed,
                    'assignments_completed': student_analytics.total_assignments_completed,
                    'average_score': student_analytics.average_score,
                    'current_streak': student_analytics.current_streak,
                    'time_spent': student_analytics.total_time_spent
                },
                'global_averages': {
                    'practice_completed': round(global_averages['avg_practice_completed'] or 0, 2),
                    'assignments_completed': round(global_averages['avg_assignments_completed'] or 0, 2),
                    'average_score': round(global_averages['avg_score'] or 0, 2),
                    'current_streak': round(global_averages['avg_streak'] or 0, 2),
                    'time_spent': round(global_averages['avg_time_spent'] or 0, 2)
                },
                'percentiles': {
                    'practice_completed': round(practice_percentile, 1),
                    'average_score': round(score_percentile, 1),
                    'current_streak': round(streak_percentile, 1)
                },
                'total_students': total_students
            }
            
            return Response({
                'success': True,
                'data': comparison_data
            })
            
        except Exception as e:
            logger.error(f"Error getting comparison data: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to load comparison data'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['post'])
    def refresh_analytics(self, request):
        """Manually refresh analytics for current user"""
        try:
            from .analytics_aggregator import analytics_aggregator
            
            # Update analytics
            updated_analytics = analytics_aggregator.update_student_analytics(request.user)
            
            return Response({
                'success': True,
                'message': 'Analytics refreshed successfully',
                'data': {
                    'updated_at': updated_analytics.updated_at,
                    'total_practice_completed': updated_analytics.total_practice_completed,
                    'total_assignments_completed': updated_analytics.total_assignments_completed,
                    'average_score': updated_analytics.average_score,
                    'current_streak': updated_analytics.current_streak
                }
            })
            
        except Exception as e:
            logger.error(f"Error refreshing analytics: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to refresh analytics'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def export_data(self, request):
        """Export comprehensive analytics data for the student"""
        try:
            from .analytics_aggregator import analytics_aggregator
            
            # Get comprehensive data
            performance_summary = analytics_aggregator.get_student_performance_summary(request.user)
            
            # Add additional export-specific data
            export_data = {
                'user_info': {
                    'username': request.user.username,
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'export_date': timezone.now().isoformat()
                },
                'analytics_summary': performance_summary,
                'detailed_submissions': []
            }
            
            # Add detailed submission history
            submissions = PracticeSubmission.objects.filter(
                student=request.user
            ).select_related('practice_question').order_by('-submitted_at')[:100]
            
            for submission in submissions:
                export_data['detailed_submissions'].append({
                    'question_title': submission.practice_question.title,
                    'difficulty': submission.practice_question.difficulty,
                    'category': submission.practice_question.category,
                    'status': submission.status,
                    'points_earned': submission.points_earned,
                    'attempt_number': submission.attempt_number,
                    'execution_time_ms': submission.execution_time_ms,
                    'submitted_at': submission.submitted_at.isoformat()
                })
            
            return Response({
                'success': True,
                'data': export_data
            })
            
        except Exception as e:
            logger.error(f"Error exporting analytics data: {e}", exc_info=True)
            return Response(
                {'success': False, 'message': 'Failed to export analytics data'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )