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
        
        # Ensure 'type' is set to 'assignment'
        if 'type' not in request.data:
            request.data['type'] = 'assignment'

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
        
        # Ensure 'type' is set
        if 'type' not in request.data:
            request.data['type'] = 'assignment'

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



    @action(detail=True, methods=['get'], url_path='analysis-progress')
    def analysis_progress(self, request, pk=None):
        """
        Returns how many submissions for this assignment have been AI-analyzed.
        Computes from DB so no Celery task tracking dependency.
        """
        from submissions.models import SubmissionAttempt
        total = SubmissionAttempt.objects.filter(
            assignment_question__assignment_id=pk
        ).count()
        analyzed = SubmissionAttempt.objects.filter(
            assignment_question__assignment_id=pk,
            ai_analysis_data__isnull=False
        ).count()
        percent = round((analyzed / total) * 100) if total > 0 else 0
        return Response({'total': total, 'analyzed': analyzed, 'percent': percent})

    @action(detail=True, methods=['get'], url_path='word-cloud')
    def generate_word_cloud(self, request, pk=None):
        """
        Generate and return a base64 word cloud image.
        Runs entirely in-process — no subprocess, no temp files, no display required.
        """
        import re
        import base64
        from io import BytesIO
        from collections import Counter

        # --- CRITICAL: set non-interactive backend before ANY matplotlib/wordcloud import ---
        import matplotlib
        matplotlib.use('Agg')
        try:
            from wordcloud import WordCloud
        except ImportError:
            return Response({'message': 'wordcloud library not installed. Run: pip install wordcloud'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            from submissions.models import SubmissionAttempt
            attempts = SubmissionAttempt.objects.filter(
                assignment_question__assignment_id=pk,
                ai_analysis_data__isnull=False
            )

            STOPWORDS = {
                'a','an','the','and','or','but','in','on','at','to','for','of','with',
                'is','are','was','were','be','been','being','have','has','had','do','does',
                'did','will','would','shall','should','may','might','must','can','could',
                'not','no','nor','so','yet','both','either','neither','as','if','then',
                'than','though','because','while','since','up','out','by','from','this',
                'that','these','those','it','its','i','you','he','she','we','they','them',
                'their','what','which','who','how','when','where','why','all','each','any',
                'more','also','very','just','about','into','through','during','before',
                'after','above','below','between','use','using','make','makes','made',
                'function','line','code','python','variable','value','return','print',
                'string','list','int','type','none','true','false','error','warning',
                'however','therefore','thus','given','provides','overall','solution',
                'implement','implementation','approach','provides','demonstrates','given',
                's','t','re','ve','ll','d','m','one','two','three','four','five',
            }

            all_tokens = []
            for attempt in attempts:
                ai = attempt.ai_analysis_data
                if not isinstance(ai, dict):
                    continue
                # Old format: tags list
                for t in ai.get('tags', []):
                    if t: all_tokens.append(str(t).lower())
                # New format: ai.feedback.*
                fb = ai.get('feedback', {})
                if isinstance(fb, dict):
                    for field in ('technical_summary', 'error_explanation', 'summarized_construct'):
                        val = fb.get(field)
                        if val and isinstance(val, str):
                            all_tokens.extend(re.findall(r"[a-zA-Z][a-zA-Z0-9']{2,}", val.lower()))
                    for c in fb.get('identified_concepts', []):
                        if c: all_tokens.append(str(c).lower())
                # Static constructs
                static = ai.get('static', {})
                if isinstance(static, dict):
                    for c in static.get('constructs_found', []):
                        if isinstance(c, str):
                            all_tokens.extend(re.findall(r"[a-zA-Z][a-zA-Z0-9']{2,}", c.lower()))
                # Detected keywords fallback
                kw = getattr(attempt, 'detected_keywords', None)
                if kw:
                    items = kw if isinstance(kw, list) else [x.strip() for x in kw.split(',') if x.strip()]
                    all_tokens.extend([str(k).lower() for k in items])

            filtered = [t for t in all_tokens if t and t not in STOPWORDS and len(t) > 2 and not t.isdigit()]
            if not filtered:
                return Response({'message': 'No AI analysis data found. Run Autograder+ first.'}, status=status.HTTP_404_NOT_FOUND)

            freq = dict(Counter(filtered).most_common(150))

            # Generate word cloud entirely in-process — PIL Image, no display needed
            wc = WordCloud(
                width=900,
                height=450,
                background_color='white',
                colormap='plasma',
                max_words=120,
                prefer_horizontal=0.8,
                min_font_size=10,
            )
            wc.generate_from_frequencies(freq)

            buf = BytesIO()
            wc.to_image().save(buf, format='PNG')
            img_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')

            return Response({
                'image_base64': img_b64,
                'top_words': list(freq.items())[:20],
            })

        except Exception as e:
            logger.error(f"Error generating word cloud: {e}", exc_info=True)
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    @action(detail=True, methods=['post'], url_path='analyze-ai')
    def analyze_ai(self, request, pk=None):
        """
        Trigger Bulk AI Analysis for this assignment.
        """
        from submissions.tasks import analyze_assignment_ai_task
        
        assignment = self.get_object()
        
        # Check permissions (Teachers/Admins only)
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
            
        # Trigger Celery Task
        task = analyze_assignment_ai_task.delay(assignment.id)
        
        return Response({
            'success': True,
            'task_id': task.id,
            'message': 'AI Analysis started in background.'
        })

    @action(detail=True, methods=['get'], url_path='analysis-progress')
    def analysis_progress(self, request, pk=None):
        """
        Get progress of AI analysis for the latest submissions of this assignment.
        """
        from submissions.models import SubmissionAttempt
        
        # Filter for this assignment
        qs = SubmissionAttempt.objects.filter(assignment_question__assignment_id=pk)
        
        # Get latest attempts only (matching the task logic)
        latest_attempts = qs.order_by('student_id', 'assignment_question_id', '-created_at').distinct('student_id', 'assignment_question_id')
        
        total = latest_attempts.count()
        
        # Count how many of these *latest* attempts have AI data
        # We can't easily filter the distinct QuerySet directly for a property without losing distinct in some DBs or versions,
        # but in Postgres with Django distinct(), we can chaining filter? 
        # Actually, filter() after distinct() is tricky. 
        # Let's count in python for safety if list is small, or use a subquery.
        # Given potential scale, subquery is better.
        
        latest_ids = latest_attempts.values_list('id', flat=True)
        analyzed = SubmissionAttempt.objects.filter(id__in=latest_ids, ai_analysis_data__isnull=False).count()
        
        return Response({
            'total': total,
            'analyzed': analyzed,
            'percent': round((analyzed / total * 100), 1) if total > 0 else 0
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

    def perform_update(self, serializer):
        question = serializer.save()
        try:
            from .services import ConfigGenerator
            ConfigGenerator.generate_question_config(question)
        except Exception as e:
            print(f"Warning: Failed to generate config for question {question.id}: {e}")
