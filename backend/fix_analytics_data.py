"""
Fix Analytics Data: Realistic per-student time distribution + TestResult records.

Model:
- Total exam: 180 minutes (3 hours), 30 questions
- Question difficulty: Derived from class-wide pass rate (harder Qs take longer)
- Student ability: Derived from their overall score (stronger students are faster)
- For each student, distribute their 180 min across 30 Qs proportionally
- Add ±15% noise for realism

Run: python fix_analytics_data.py
"""
import os, random, math
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from submissions.models import SubmissionAttempt, AssignmentProgress, TestResult
from assignments.models import AssignmentQuestion, Assignment
from django.utils import timezone
from datetime import timedelta
from collections import defaultdict

TOTAL_EXAM_MINUTES = 180  # 3 hours


def run():
    print("=" * 60)
    print("FIXING ANALYTICS DATA — REALISTIC TIME DISTRIBUTION")
    print("=" * 60)
    
    # Find assignments that have submissions
    assignment_ids = SubmissionAttempt.objects.values_list(
        'assignment_question__assignment_id', flat=True
    ).distinct()
    assignments_with_subs = Assignment.objects.filter(id__in=assignment_ids)
    
    for assignment in assignments_with_subs:
        print(f"\n{'—' * 40}")
        print(f"Assignment: {assignment.title} ({assignment.id})")
        
        aqs = list(AssignmentQuestion.objects.filter(assignment=assignment).order_by('order'))
        if not aqs:
            continue
        
        num_questions = len(aqs)
        print(f"  Questions: {num_questions}")
        
        # ─────────────────────────────────────────────
        # Step 1: Calculate question difficulty (0-1, where 1 = hardest)
        # Based on class-wide failure rate
        # ─────────────────────────────────────────────
        q_difficulty = {}
        for aq in aqs:
            subs = SubmissionAttempt.objects.filter(assignment_question=aq)
            total = subs.count()
            if total == 0:
                q_difficulty[aq.id] = 0.5  # default medium
                continue
            
            # Difficulty = 1 - (avg_score_pct / 100)
            max_pts = aq.custom_points or 6
            scores = [
                (s.manual_score / max_pts * 100) if s.manual_score is not None else 0
                for s in subs
            ]
            avg_score = sum(scores) / len(scores)
            q_difficulty[aq.id] = max(0.1, 1.0 - (avg_score / 100.0))
        
        print(f"  Difficulty range: {min(q_difficulty.values()):.2f} - {max(q_difficulty.values()):.2f}")
        
        # ─────────────────────────────────────────────
        # Step 2: Gather per-student data
        # ─────────────────────────────────────────────
        student_submissions = defaultdict(dict)  # student_id -> {aq_id: SubmissionAttempt}
        
        all_subs = list(SubmissionAttempt.objects.filter(
            assignment_question__assignment=assignment
        ).select_related('assignment_question', 'student'))
        
        for sub in all_subs:
            student_submissions[sub.student_id][sub.assignment_question_id] = sub
        
        print(f"  Students: {len(student_submissions)}")
        
        # ─────────────────────────────────────────────
        # Step 3: Calculate student ability (0-1, where 1 = strongest)
        # Based on their overall score across all questions
        # ─────────────────────────────────────────────
        student_ability = {}
        for student_id, subs_dict in student_submissions.items():
            total_score_pct = 0
            count = 0
            for aq_id, sub in subs_dict.items():
                aq = next(a for a in aqs if a.id == aq_id)
                max_pts = aq.custom_points or 6
                if sub.manual_score is not None:
                    total_score_pct += (sub.manual_score / max_pts) * 100
                count += 1
            
            avg_pct = total_score_pct / max(count, 1)
            # Ability: 0.2 (weak) to 1.0 (strong)
            student_ability[student_id] = max(0.2, avg_pct / 100.0)
        
        # ─────────────────────────────────────────────
        # Step 4: Distribute time per student
        # ─────────────────────────────────────────────
        # For each student:
        #   - Their total time varies: strong students use 60-80% of exam time,
        #     weak students use 80-100%
        #   - Time per question is proportional to difficulty, adjusted by:
        #     - High ability + easy Q → fast
        #     - Low ability + hard Q → slow (more attempts, struggling)
        #     - If score=0 on a Q → they gave up (low time, 1-4 min)
        
        # Delete existing records for this assignment's questions
        aq_ids = [aq.id for aq in aqs]
        AssignmentProgress.objects.filter(assignment_question_id__in=aq_ids).delete()
        TestResult.objects.filter(attempt__assignment_question_id__in=aq_ids).delete()
        
        progress_records = []
        test_results = []
        
        for student_id, subs_dict in student_submissions.items():
            ability = student_ability[student_id]
            
            # Total time this student spent on the exam
            # Strong students: 60-80% of exam time (they're efficient)
            # Weak students: 80-100% of exam time (they use all available time)
            time_efficiency = 0.6 + (1.0 - ability) * 0.4  # 0.6 to 1.0
            student_total_minutes = TOTAL_EXAM_MINUTES * time_efficiency
            student_total_minutes *= random.uniform(0.85, 1.15)  # ±15% noise
            student_total_minutes = min(student_total_minutes, TOTAL_EXAM_MINUTES)
            
            # Calculate raw weight for each question the student attempted
            q_weights = {}
            for aq in aqs:
                if aq.id not in subs_dict:
                    continue
                
                sub = subs_dict[aq.id]
                diff = q_difficulty[aq.id]
                
                # Score for this question
                max_pts = aq.custom_points or 6
                score_pct = (sub.manual_score / max_pts * 100) if sub.manual_score is not None else 0
                
                if score_pct == 0:
                    # Gave up early — 1-4 minutes
                    q_weights[aq.id] = random.uniform(1.0, 4.0) / student_total_minutes
                elif score_pct >= 90:
                    # Aced it — proportional to difficulty but fast
                    base_weight = diff * (1.0 / ability)
                    q_weights[aq.id] = base_weight * random.uniform(0.5, 0.8)
                else:
                    # Partial score — time increases with difficulty, decreases with ability
                    base_weight = diff * (1.0 / ability)
                    # Lower score = more time (struggling)
                    struggle_factor = 1.0 + (1.0 - score_pct / 100.0) * 0.5
                    q_weights[aq.id] = base_weight * struggle_factor * random.uniform(0.8, 1.2)
            
            # Normalize weights to sum to 1
            total_weight = sum(q_weights.values())
            if total_weight == 0:
                continue
            
            for aq_id in q_weights:
                q_weights[aq_id] /= total_weight
            
            # Assign actual minutes
            for aq in aqs:
                if aq.id not in subs_dict:
                    continue
                
                sub = subs_dict[aq.id]
                max_pts = aq.custom_points or 6
                score_pct = (sub.manual_score / max_pts * 100) if sub.manual_score is not None else 0
                
                time_minutes = q_weights.get(aq.id, 0) * student_total_minutes
                time_minutes = max(0.5, time_minutes)  # minimum 30 seconds
                time_seconds = int(time_minutes * 60)
                
                # Create AssignmentProgress
                started_at = sub.created_at - timedelta(seconds=time_seconds + random.randint(10, 120))
                
                progress_records.append(AssignmentProgress(
                    student_id=student_id,
                    assignment_question=aq,
                    current_code=(sub.source_code or '# No code')[:500],
                    time_spent=time_seconds,
                    started_at=started_at,
                ))
                
                # Create TestResult records
                num_tests = aq.custom_points or 6
                num_passing = round((score_pct / 100.0) * num_tests)
                num_passing = max(0, min(num_tests, num_passing))
                
                results = ['pass'] * num_passing + ['fail'] * (num_tests - num_passing)
                random.shuffle(results)
                
                for i in range(num_tests):
                    test_status = results[i]
                    test_results.append(TestResult(
                        attempt=sub,
                        test_case_id=f'tc_{i+1}',
                        status=test_status,
                        score=1.0 if test_status == 'pass' else 0.0,
                        actual_output='Correct' if test_status == 'pass' else 'Wrong answer',
                        error_message='' if test_status == 'pass' else 'Output mismatch'
                    ))
        
        # Bulk create
        AssignmentProgress.objects.bulk_create(progress_records, batch_size=500)
        TestResult.objects.bulk_create(test_results, batch_size=1000)
        
        print(f"  AssignmentProgress created: {len(progress_records)}")
        print(f"  TestResult created: {len(test_results)}")
        
        # Verify time distribution
        sample_student = list(student_submissions.keys())[0] if student_submissions else None
        if sample_student:
            student_progress = AssignmentProgress.objects.filter(
                student_id=sample_student,
                assignment_question__assignment=assignment
            )
            total_time = sum(p.time_spent for p in student_progress)
            print(f"  Sample student total time: {total_time/60:.1f} min (target: ~{TOTAL_EXAM_MINUTES} min)")
    
    print(f"\n{'=' * 60}")
    print("DONE!")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    run()
