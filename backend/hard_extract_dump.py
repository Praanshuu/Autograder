#!/usr/bin/env python3
import os
import sys
import django
import json
import datetime
from django.utils import timezone
from dateutil.parser import parse as parse_date

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import transaction

# Import all other models
from classes.models import Class, Enrollment
from assignments.models import Assignment, Question, TestCase
from submissions.models import Submission

User = get_user_model()

def clean_datetime(dt_str):
    if not dt_str:
        return None
    try:
        return parse_date(dt_str)
    except:
        return timezone.now()

def hard_extract_dump():
    print("Starting hard extraction from db_dump.json...")
    
    try:
        with open('db_dump.json', 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        print("db_dump.json not found.")
        return
    
    # Try to parse the JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"JSON error at position {e.pos}, attempting to recover valid prefix...")
        content = content[:e.pos]
        content = content.rstrip().rstrip(',') + '\n]'
        try:
            data = json.loads(content)
        except:
            print("CRITICAL: Could not recover any valid JSON list.")
            return

    print(f"Successfully parsed {len(data)} objects from dump.")

    # Separation by model
    model_data = {
        'users.user': [],
        'classes.class': [],
        'classes.enrollment': [],
        'assignments.assignment': [],
        'assignments.question': [],
        'assignments.testcase': [],
        'submissions.submission': []
    }

    for item in data:
        m = item.get('model')
        if m in model_data:
            model_data[m].append(item)
    
    print("\n--- Data Summary by Model ---")
    for m, items in model_data.items():
        print(f"{m}: {len(items)} records")
    print("-----------------------------\n")

    # ID Mappings: Dump ID -> Created Object
    id_map = {
        'users.user': {},
        'classes.class': {},
        'assignments.assignment': {},
        'assignments.question': {},
        'assignments.testcase': {}
    }

    with transaction.atomic():
        # 1. Users
        print("Processing Users...")
        count = 0
        for item in model_data['users.user']:
            fields = item['fields']
            pk = item['pk']
            try:
                user, created = User.objects.update_or_create(
                    username=fields['username'],
                    defaults={
                        'email': fields.get('email', ''),
                        'first_name': fields.get('first_name', ''),
                        'last_name': fields.get('last_name', ''),
                        'is_active': fields.get('is_active', True),
                        'is_staff': fields.get('is_staff', False),
                        'is_superuser': fields.get('is_superuser', False),
                        'date_joined': clean_datetime(fields.get('date_joined')),
                    }
                )
                if 'password' in fields:
                    user.password = fields['password']
                    user.save()
                id_map['users.user'][pk] = user
                count += 1
            except Exception as e:
                print(f"Error processing user {fields.get('username')}: {e}")
        print(f"Processed {count} users.")

        # 2. Classes
        print("\nProcessing Classes...")
        count = 0
        for item in model_data['classes.class']:
            fields = item['fields']
            pk = item['pk']
            try:
                owner_pk = fields.get('owner') 
                owner = id_map['users.user'].get(owner_pk)
                
                if not owner:
                     # Fallback so we don't lose class data if owner missing
                     owner = User.objects.filter(is_superuser=True).first()
                if not owner:
                     print(f"Skipping class {fields.get('name')} - No valid owner.")
                     continue

                cls_obj, created = Class.objects.update_or_create(
                    pk=pk, # Preserve PK
                    defaults={
                        'name': fields.get('name', 'Untitled'),
                        'section': fields.get('section', ''),
                        'description': fields.get('description', ''),
                        'owner': owner,
                        'theme_color': fields.get('theme_color', '#6366f1'),
                        'join_code': fields.get('join_code'),
                    }
                )
                id_map['classes.class'][pk] = cls_obj
                count += 1
            except Exception as e:
                print(f"Error processing class {pk}: {e}")
        print(f"Processed {count} classes.")

        # 3. M2M Helper: Enrollments
        print("\nProcessing Enrollments...")
        count = 0
        for item in model_data['classes.enrollment']:
            fields = item['fields']
            try:
                user_pk = fields.get('user')
                class_pk = fields.get('class_obj')
                
                user = id_map['users.user'].get(user_pk)
                cls_obj = id_map['classes.class'].get(class_pk)
                
                if user and cls_obj:
                    Enrollment.objects.get_or_create(
                        user=user,
                        class_obj=cls_obj,
                        defaults={
                            'role': fields.get('role', 'student'),
                            'status': fields.get('status', 'active')
                        }
                    )
                    count += 1
            except Exception as e:
                pass
        print(f"Processed {count} enrollments.")

        # 4. TestCases (Independent or linked to Question?)
        # Verified: TestCase has no FK to Question. Question has M2M to TestCase.
        # So Create TestCases first.
        print("\nProcessing TestCases...")
        count = 0
        for item in model_data['assignments.testcase']:
            fields = item['fields']
            pk = item['pk']
            try:
                tc, created = TestCase.objects.update_or_create(
                    pk=pk,
                    defaults={
                        'input': fields.get('input', ''),
                        'expected_output': fields.get('expected_output', ''),
                        'is_hidden': fields.get('is_hidden', False),
                        'points': fields.get('points', 0)
                    }
                )
                id_map['assignments.testcase'][pk] = tc
                count += 1
            except Exception as e:
                print(f"Error testcase {pk}: {e}")
        print(f"Processed {count} test cases.")

        # 5. Questions (Link to TestCases)
        print("\nProcessing Questions...")
        count = 0
        for item in model_data['assignments.question']:
            fields = item['fields']
            pk = item['pk']
            try:
                q, created = Question.objects.update_or_create(
                    pk=pk,
                    defaults={
                        'title': fields.get('title', 'Untitled Question'),
                        'description': fields.get('description', ''),
                        'difficulty': fields.get('difficulty', 'Medium'),
                         # Add others if needed: time_limit, etc.
                    }
                )
                
                # Link TestCases
                if 'test_cases' in fields:
                    tc_pks = fields['test_cases']
                    for tc_pk in tc_pks:
                        tc_obj = id_map['assignments.testcase'].get(tc_pk)
                        if tc_obj:
                            q.test_cases.add(tc_obj)

                id_map['assignments.question'][pk] = q
                count += 1
            except Exception as e:
                print(f"Error processing question {pk}: {e}")
        print(f"Processed {count} questions.")

        # 6. Assignments (depends on Class, link to Questions)
        print("\nProcessing Assignments...")
        count = 0
        for item in model_data['assignments.assignment']:
            fields = item['fields']
            pk = item['pk']
            try:
                class_pk = fields.get('class_obj') 
                cls_obj = id_map['classes.class'].get(class_pk)
                
                # Creator
                creator_pk = fields.get('created_by')
                creator = id_map['users.user'].get(creator_pk)
                if not creator:
                    creator = User.objects.filter(is_superuser=True).first()

                if not cls_obj: 
                    print(f"Skipping assignment {fields.get('title')} - Class {class_pk} not found.")
                    continue

                assign, created = Assignment.objects.update_or_create(
                    pk=pk,
                    defaults={
                        'title': fields.get('title'),
                        'description': fields.get('description', ''),
                        'due_date': clean_datetime(fields.get('due_date')),
                        'points': fields.get('points', 100),
                        'class_obj': cls_obj,
                        'created_by': creator
                    }
                )
                
                # Handle M2M Questions
                if 'questions' in fields:
                    q_pks = fields['questions']
                    for q_pk in q_pks:
                        q_obj = id_map['assignments.question'].get(q_pk)
                        if q_obj:
                            assign.questions.add(q_obj)
                            
                id_map['assignments.assignment'][pk] = assign
                count += 1
            except Exception as e:
                print(f"Error processing assignment {pk}: {e}")
        print(f"Processed {count} assignments.")

        # 7. Submissions
        print("\nProcessing Submissions...")
        count = 0
        for item in model_data['submissions.submission']:
            fields = item['fields']
            pk = item['pk']
            try:
                assign_pk = fields.get('assignment')
                question_pk = fields.get('question')
                student_pk = fields.get('student')
                
                assign = id_map['assignments.assignment'].get(assign_pk)
                question = id_map['assignments.question'].get(question_pk)
                student = id_map['users.user'].get(student_pk)
                
                if assign and student and question:
                    sub, created = Submission.objects.update_or_create(
                        assignment=assign,
                        question=question,
                        student=student,
                        defaults={
                            'code_content': fields.get('code_content', ''),
                            'submitted_at': clean_datetime(fields.get('submitted_at')),
                            'final_score': fields.get('final_score', 0), # field name mismatch? Dump said 'final_score'?
                            # Step 85 output: 'final_score', 'auto_grade_score'. Correct.
                            'auto_grade_score': fields.get('auto_grade_score', 0),
                            'teacher_feedback': fields.get('teacher_feedback', ''),
                            'language': fields.get('language', 'python')
                        }
                    )
                    count += 1
            except Exception as e:
                print(f"Error submission {pk}: {e}")
        print(f"Processed {count} submissions.")

    print("\nExtraction and Load Complete!")

if __name__ == '__main__':
    hard_extract_dump()
