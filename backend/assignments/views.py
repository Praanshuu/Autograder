from rest_framework import viewsets, status
import logging
import json
import subprocess
import os
import sys
import tempfile
logger = logging.getLogger(__name__)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Assignment, Question
from .serializers import AssignmentSerializer, QuestionSerializer
from classes.models import Enrollment


class AssignmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'list':
            from .serializers import StreamAssignmentSerializer
            return StreamAssignmentSerializer
        return AssignmentSerializer
    
    def get_queryset(self):
        user = self.request.user
        class_id = self.request.query_params.get('class_id', None)
        
        # Select related module -> class for filtering
        from django.db.models import Count
        queryset = Assignment.objects.select_related('module__class_obj').annotate(
            comments_count=Count('class_comments', distinct=True)
        )
        
        # Only prefetch questions if NOT listing (detailed view needs them)
        if self.action != 'list':
            queryset = queryset.prefetch_related('questions')
        
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
        
        # Handle type and mode
        req_type = request.data.get('type', 'assignment')
        req_mode = request.data.get('mode', 'practice')
        
        # Validate type
        valid_types = [t[0] for t in Assignment.TYPE_CHOICES]
        if req_type not in valid_types:
            req_type = 'assignment'
            
        # Validate mode
        valid_modes = [m[0] for m in Assignment.MODE_CHOICES]
        if req_mode not in valid_modes:
            req_mode = 'practice'
            
        request.data['type'] = req_type
        request.data['mode'] = req_mode

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Handle 'class_obj_id' from frontend -> 'module' for backend
        class_id = request.data.get('class_obj_id')
        if class_id and 'module' not in request.data:
            from classes.models import Module, Class
            try:
                class_obj = Class.objects.get(id=class_id)
                module, _ = Module.objects.get_or_create(
                    class_obj=class_obj,
                    defaults={'title': 'Assignments', 'order_index': 0}
                )
                request.data['module'] = module.id
            except Class.DoesNotExist:
                return Response(
                    {'message': 'Invalid Class ID'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        # Handle type and mode
        if 'type' in request.data:
            req_type = request.data.get('type')
            valid_types = [t[0] for t in Assignment.TYPE_CHOICES]
            if req_type not in valid_types:
                request.data['type'] = 'assignment'
                
        if 'mode' in request.data:
            req_mode = request.data.get('mode')
            valid_modes = [m[0] for m in Assignment.MODE_CHOICES]
            if req_mode not in valid_modes:
                request.data['mode'] = 'practice'

        return super().update(request, *args, **kwargs)

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

        # Ensure exam questions are NOT in the Practice Library
        if assignment.mode == 'exam':
            try:
                from gamification.models import PracticeQuestionLibrary
                from .models import AssignmentQuestion
                q_ids = AssignmentQuestion.objects.filter(assignment=assignment).values_list('question_id', flat=True)
                PracticeQuestionLibrary.objects.filter(question_id__in=q_ids).delete()
            except Exception as e:
                logger.warning(f"Could not remove exam questions from Practice Library: {e}")

    def perform_update(self, serializer):
        user = self.request.user
        instance = serializer.instance
        
        # Check if is_published is being changed by a non-teacher
        if 'is_published' in serializer.validated_data:
            new_status = serializer.validated_data['is_published']
            
            if new_status != instance.is_published:
                # Verify permissions
                class_owner = instance.module.class_obj.owner
                is_owner = class_owner == user
                is_teacher = Enrollment.objects.filter(
                    class_obj=instance.module.class_obj, 
                    user=user, 
                    role='teacher'
                ).exists()
                is_admin = user.role == 'admin'
                
                if not (is_owner or is_teacher or is_admin):
                    # Revert to original status
                    serializer.validated_data['is_published'] = instance.is_published

        assignment = serializer.save()
        
        # Handle question_ids linkage update
        # Check explicit None vs empty list if we want to support clearing, 
        # but frontend sends [] if empty.
        # We only update if 'question_ids' key is present in request.
        if 'question_ids' in self.request.data:
            question_ids = self.request.data.get('question_ids', [])
            from .models import AssignmentQuestion, Question
            
            # Clear existing questions
            AssignmentQuestion.objects.filter(assignment=assignment).delete()
            
            # Re-link new questions
            for index, q_id in enumerate(question_ids):
                try:
                    question = Question.objects.get(id=q_id)
                    AssignmentQuestion.objects.create(
                        assignment=assignment,
                        question=question,
                        order=index
                    )
                except Question.DoesNotExist:
                    pass
                    
        # Ensure exam questions are NOT in the Practice Library
        if assignment.mode == 'exam':
            try:
                from gamification.models import PracticeQuestionLibrary
                from .models import AssignmentQuestion
                q_ids = AssignmentQuestion.objects.filter(assignment=assignment).values_list('question_id', flat=True)
                PracticeQuestionLibrary.objects.filter(question_id__in=q_ids).delete()
            except Exception as e:
                logger.warning(f"Could not remove exam questions from Practice Library: {e}")
    
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        """Publish an assignment"""
        assignment = self.get_object()
        
        # Check authorization relative to class owner/teacher
        # TAs (role='ta') cannot publish. Only 'teacher' or 'admin' or class owner.
        class_owner = assignment.module.class_obj.owner
        
        # Check credentials
        is_owner = class_owner == request.user
        is_teacher = Enrollment.objects.filter(
            class_obj=assignment.module.class_obj, 
            user=request.user, 
            role='teacher'
        ).exists()
        is_admin = request.user.role == 'admin'
        
        if not (is_owner or is_teacher or is_admin):
             return Response(
                {'message': 'Not authorized. Only Teachers can publish.'},
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
        """Close an assignment (unpublish)"""
        assignment = self.get_object()
        
        class_owner = assignment.module.class_obj.owner
        is_owner = class_owner == request.user
        is_teacher = Enrollment.objects.filter(
            class_obj=assignment.module.class_obj, 
            user=request.user, 
            role='teacher'
        ).exists()
        is_admin = request.user.role == 'admin'
        
        if not (is_owner or is_teacher or is_admin):
            return Response(
                {'message': 'Not authorized. Only Teachers can close assignments.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        assignment.is_published = False
        assignment.save()
        
        return Response({
            'success': True,
            'data': AssignmentSerializer(assignment).data
        })




    @action(detail=True, methods=['get'], url_path='word-cloud')
    def generate_word_cloud(self, request, pk=None):
        """
        Generate per-question word clouds split by score tier.

        Query params:
            question_id  (required) – the Question PK to scope to.

        Response:
            {
              "full":    { "image_base64": "...", "top_words": [...], "count": N },
              "partial": { "image_base64": "...", "top_words": [...], "count": N },
            }
        Both keys are always present; image_base64 is null when there is no data
        for that tier.
        """
        import re
        import base64
        from io import BytesIO
        from collections import Counter

        import matplotlib
        matplotlib.use('Agg')
        try:
            from wordcloud import WordCloud
        except ImportError:
            return Response(
                {'message': 'wordcloud library not installed. Run: pip install wordcloud'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        question_id = request.query_params.get('question_id')
        if not question_id:
            return Response({'message': 'question_id query param is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # ------------------------------------------------------------------ #
        # Extended stop-word list — remove generic / non-insightful tokens    #
        # ------------------------------------------------------------------ #
        STOPWORDS = {
            # Articles / prepositions / conjunctions
            'a','an','the','and','or','but','in','on','at','to','for','of','with',
            'is','are','was','were','be','been','being','have','has','had','do','does',
            'did','will','would','shall','should','may','might','must','can','could',
            'not','no','nor','so','yet','both','either','neither','as','if','then',
            'than','though','because','while','since','up','out','by','from','this',
            'that','these','those','it','its','they','them','their',
            'what','which','who','how','when','where','why','all','each','any',
            'more','also','very','just','about','into','through','during','before',
            'after','above','below','between',
            # Generic programming / filler verbs
            'use','used','using','make','makes','made','takes','take','taken',
            'get','gets','got','set','sets','let','lets','call','calls','called',
            'check','checks','return','returns','print','prints',
            'function','line','code','python','variable','value','output','input',
            'string','list','dict','int','float','bool','type','none','true','false',
            'error','warning','result','results','based','given','provide','provides',
            'provided','overall','solution','attempt','attempts','student','students',
            'implement','implementation','approach','demonstrates','given',
            'however','therefore','thus','hence','also','additionally','furthermore',
            'correct','correctly','incorrect','incorrect','wrong','right','well',
            'good','better','best','issue','issues','problem','problems','note','notes',
            'show','shows','shown','see','seen','need','needs','needed',
            'work','works','worked','working','run','runs','running','ran',
            # Short noise
            's','t','re','ve','ll','d','m','one','two','three','four','five',
            'six','seven','eight','nine','ten',
        }

        def _extract_tokens(attempt, include_errors=False):
            """Extract only technical/conceptual tokens from ai_analysis_data."""
            tokens = []
            ai = attempt.ai_analysis_data
            if not isinstance(ai, dict):
                return tokens

            fb = ai.get('feedback', {})
            if isinstance(fb, dict):
                # Technical concepts / approach descriptions
                for field in ('technical_summary', 'summarized_construct'):
                    val = fb.get(field)
                    if val and isinstance(val, str):
                        tokens.extend(re.findall(r'[a-zA-Z][a-zA-Z0-9_]{3,}', val.lower()))
                # Error explanations — only for partial/incorrect tier
                if include_errors:
                    val = fb.get('error_explanation')
                    if val and isinstance(val, str):
                        tokens.extend(re.findall(r'[a-zA-Z][a-zA-Z0-9_]{3,}', val.lower()))
                # Identified concepts are always useful
                for c in fb.get('identified_concepts', []):
                    if c and isinstance(c, str):
                        tokens.extend(re.findall(r'[a-zA-Z][a-zA-Z0-9_]{3,}', str(c).lower()))

            # Static constructs (always technical)
            static = ai.get('static', {})
            if isinstance(static, dict):
                for c in static.get('constructs_found', []):
                    if isinstance(c, str):
                        tokens.extend(re.findall(r'[a-zA-Z][a-zA-Z0-9_]{3,}', c.lower()))

            # Tags (short labels from old format or pipeline)
            for tag in ai.get('tags', []):
                if tag and isinstance(tag, str) and len(tag) >= 4:
                    tokens.append(tag.lower().strip())

            # Filter stop-words, digits, short tokens
            return [
                t for t in tokens
                if t not in STOPWORDS and not t.isdigit() and len(t) >= 4
            ]

        def _build_cloud(tokens, colormap):
            """Build a WordCloud PIL image from token list; returns base64 string or None."""
            if not tokens:
                return None, []
            freq = Counter(tokens)
            top = freq.most_common(120)
            freq_dict = dict(top)
            wc = WordCloud(
                width=900,
                height=420,
                background_color='white',
                colormap=colormap,
                max_words=100,
                prefer_horizontal=0.75,
                min_font_size=10,
                collocations=False,
            )
            wc.generate_from_frequencies(freq_dict)
            buf = BytesIO()
            wc.to_image().save(buf, format='PNG')
            img_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            return img_b64, [(w, c) for w, c in top[:20]]

        try:
            from submissions.models import SubmissionAttempt
            from assignments.models import AssignmentQuestion

            # Resolve the AssignmentQuestion to get max_score
            try:
                aq = AssignmentQuestion.objects.select_related('question').get(
                    assignment_id=pk,
                    question_id=question_id
                )
            except AssignmentQuestion.DoesNotExist:
                return Response(
                    {'message': 'Question not found in this assignment.'},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Max score = number of test cases (each worth 1 point)
            test_cases = aq.question.test_cases or []
            max_score = len(test_cases) if isinstance(test_cases, list) else 1

            # Fetch all attempts for this specific question that have AI data
            attempts = SubmissionAttempt.objects.filter(
                assignment_question=aq,
                ai_analysis_data__isnull=False
            ).only('ai_analysis_data', 'manual_score', 'status')

            if not attempts.exists():
                return Response(
                    {'message': 'No AI analysis data found for this question. Run Autograder+ first.'},
                    status=status.HTTP_404_NOT_FOUND
                )

            full_tokens = []
            partial_tokens = []

            for attempt in attempts:
                score = attempt.manual_score
                # Full tier: score equals max (all test cases passed)
                is_full = (
                    score is not None
                    and max_score > 0
                    and score >= max_score
                ) or attempt.status == 'success'

                if is_full:
                    full_tokens.extend(_extract_tokens(attempt, include_errors=False))
                else:
                    partial_tokens.extend(_extract_tokens(attempt, include_errors=True))

            full_img, full_top = _build_cloud(full_tokens, colormap='YlGn')
            partial_img, partial_top = _build_cloud(partial_tokens, colormap='YlOrRd')

            if full_img is None and partial_img is None:
                return Response(
                    {'message': 'Not enough meaningful tokens found. Try running more AI analysis first.'},
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response({
                'full': {
                    'image_base64': full_img,
                    'top_words': full_top,
                    'count': len(full_tokens),
                },
                'partial': {
                    'image_base64': partial_img,
                    'top_words': partial_top,
                    'count': len(partial_tokens),
                },
            })

        except Exception as e:
            logger.error(f"Error generating word cloud: {e}", exc_info=True)
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    @action(detail=True, methods=['post'], url_path='analyze-ai')
    def analyze_ai(self, request, pk=None):
        """
        Trigger Bulk AI Analysis for this assignment (batched, parallel Celery tasks).
        """
        from submissions.tasks import analyze_assignment_ai_task
        from submissions.models import AIAnalysisTask

        assignment = self.get_object()

        # Permissions: owner / teacher / admin only
        class_owner = assignment.module.class_obj.owner
        is_owner = class_owner == request.user
        is_teacher = Enrollment.objects.filter(
            class_obj=assignment.module.class_obj,
            user=request.user,
            role='teacher'
        ).exists()
        is_admin = request.user.role == 'admin'

        if not (is_owner or is_teacher or is_admin):
            return Response(
                {'message': 'Not authorized. Only Teachers can trigger AI analysis.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Removed global guard to allow concurrent AI analyses and rely on Celery for queue management.

        # Block duplicate runs FOR THIS ASSIGNMENT — reject if already pending or running
        # unless 'force=true' is passed OR the task is clearly stale.
        force_restart = str(request.data.get('force', '')).lower() == 'true'
        from django.utils import timezone
        from datetime import timedelta

        active_task = AIAnalysisTask.objects.filter(
            assignment=assignment, status__in=['pending', 'running']
        ).order_by('-created_at').first()

        if active_task:
            is_stale = (timezone.now() - active_task.created_at) > timedelta(minutes=30)
            
            if force_restart or (is_stale and active_task.status == 'pending'):
                logger.info(f"Overriding {'stale ' if is_stale else ''}AI task {active_task.id} for assignment {pk}")
                active_task.status = 'cancelled'
                active_task.save(update_fields=['status'])
                active_task = None # Allow creation of new task below
            else:
                # Tell the frontend about the existing task so it can resume polling
                return Response({
                    'success': False,
                    'already_running': True,
                    'task_id': str(active_task.id),
                    'completed_batches': active_task.completed_batches,
                    'total_batches': active_task.total_batches,
                    'analyzed': active_task.analyzed,
                    'total': active_task.total_submissions or assignment.assignmentquestion_set.count(),
                    'message': f'An AI analysis is already in progress (status: {active_task.status}). '
                               f'Batch {active_task.completed_batches}/{active_task.total_batches}. '
                               f'Cancel it first before starting a new one.',
                }, status=status.HTTP_409_CONFLICT)

        # Create a tracking record first (so progress endpoint works immediately)
        ai_task = AIAnalysisTask.objects.create(
            assignment=assignment,
            status='pending',
        )

        # Dispatch master task
        celery_task = analyze_assignment_ai_task.delay(
            str(assignment.id),
            str(ai_task.id)
        )

        return Response({
            'success': True,
            'task_id': str(ai_task.id),
            'celery_task_id': celery_task.id,
            'message': 'AI Analysis started in background.',
        })

    @action(detail=True, methods=['post'], url_path='cancel-ai')
    def cancel_ai_analysis(self, request, pk=None):
        """
        Cancel the currently running AI analysis for this assignment.
        Revokes all pending Celery batch tasks.
        """
        from celery import current_app
        from submissions.models import AIAnalysisTask

        ai_task = AIAnalysisTask.objects.filter(
            assignment_id=pk, status__in=['pending', 'running']
        ).first()

        if not ai_task:
            return Response({'message': 'No active analysis to cancel.'}, status=status.HTTP_404_NOT_FOUND)

        # Revoke all spawned batch tasks
        for task_id in ai_task.task_ids:
            try:
                current_app.control.revoke(task_id, terminate=True)
            except Exception as e:
                logger.warning(f"Could not revoke task {task_id}: {e}")

        ai_task.status = 'cancelled'
        ai_task.save(update_fields=['status'])

        return Response({'success': True, 'message': 'Analysis cancelled.'})

    @action(detail=False, methods=['get'], url_path='ai-analysis-tasks')
    def list_ai_analysis_tasks(self, request):
        """List active (pending/running) AI analysis tasks. Admin: all; teacher/ta: only their assignments."""
        from submissions.models import AIAnalysisTask
        tasks_qs = AIAnalysisTask.objects.filter(
            status__in=['pending', 'running']
        ).select_related('assignment__module__class_obj')
        if getattr(request.user, 'role', None) != 'admin':
            # Teacher/TA: only assignments in classes they own or teach
            allowed_classes = set()
            from classes.models import Class
            owned = Class.objects.filter(owner=request.user).values_list('id', flat=True)
            allowed_classes.update(owned)
            taught = Enrollment.objects.filter(user=request.user, role='teacher').values_list('class_obj_id', flat=True)
            allowed_classes.update(taught)
            tasks_qs = tasks_qs.filter(assignment__module__class_obj_id__in=allowed_classes)
        tasks = tasks_qs.order_by('-created_at')
        data = [{
            'task_id': str(t.id),
            'assignment_id': str(t.assignment_id),
            'assignment_title': t.assignment.title,
            'status': t.status,
            'completed_batches': t.completed_batches,
            'total_batches': t.total_batches,
            'analyzed': t.analyzed,
            'total_submissions': t.total_submissions,
            'log_output': t.log_output or [],
        } for t in tasks]
        return Response(data)

    @action(detail=True, methods=['get'], url_path='analysis-progress')
    def analysis_progress(self, request, pk=None):
        """
        Returns real-time batch progress from the AIAnalysisTask model.
        Falls back to counting DB records if no task record exists or hasn't been
        populated yet (race condition window right after task is created).
        """
        from submissions.models import AIAnalysisTask, SubmissionAttempt

        ai_task = AIAnalysisTask.objects.filter(assignment_id=pk).first()

        if ai_task:
            # If the master task hasn't populated total yet, get a real count from DB
            total = ai_task.total_submissions
            if total == 0:
                total = SubmissionAttempt.objects.filter(
                    assignment_question__assignment_id=pk
                ).values('student_id', 'assignment_question_id').distinct().count()

            analyzed = ai_task.analyzed
            percent = round(analyzed / total * 100) if total > 0 else 0

            return Response({
                'status':            ai_task.status,
                'total_batches':     ai_task.total_batches,
                'completed_batches': ai_task.completed_batches,
                'total':             total,
                'analyzed':          analyzed,
                'percent':           percent,
            })

        # No task record at all — count directly from DB
        total    = SubmissionAttempt.objects.filter(
            assignment_question__assignment_id=pk
        ).values('student_id', 'assignment_question_id').distinct().count()
        analyzed = SubmissionAttempt.objects.filter(
            assignment_question__assignment_id=pk,
            ai_analysis_data__isnull=False
        ).count()
        return Response({
            'status':  'unknown',
            'total':   total,
            'analyzed': analyzed,
            'percent': round(analyzed / total * 100, 1) if total > 0 else 0,
        })


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        question = serializer.save()
        try:
            from .services import ConfigGenerator
            ConfigGenerator.generate_question_config(question)
        except Exception as e:
            print(f"Warning: Failed to generate config for question {question.id}: {e}")
            
        # Automatically add the new question to the Practice Question Library
        try:
            from gamification.models import PracticeQuestionLibrary
            PracticeQuestionLibrary.objects.get_or_create(
                question=question,
                defaults={
                    'is_public': True,
                    'tags': question.tags
                }
            )
        except Exception as e:
            print(f"Warning: Failed to add question {question.id} to Practice Library: {e}")

    def perform_update(self, serializer):
        question = serializer.save()
        try:
            from .services import ConfigGenerator
            ConfigGenerator.generate_question_config(question)
        except Exception as e:
            print(f"Warning: Failed to generate config for question {question.id}: {e}")
