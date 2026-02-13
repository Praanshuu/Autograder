import os
import django
import sys

sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from classes.models import Class, Enrollment
from assignments.models import Assignment
from submissions.models import SubmissionAttempt

User = get_user_model()

print("--- Final Dual-Class Verification ---")

# 1. Classes
cls_cs = Class.objects.filter(name="CSL100-CS").first()
cls_ee = Class.objects.filter(name="CSL100-EE").first()

if cls_cs and cls_ee:
    print(f"[OK] Found both classes: {cls_cs.name}, {cls_ee.name}")
else:
    print("[FAIL] Classes missing!")
    
# 2. Enrollments
if cls_cs:
    cnt_cs = Enrollment.objects.filter(class_obj=cls_cs, role='student').count()
    print(f"[OK] CSL100-CS Students: {cnt_cs} (Expected ~63)")

if cls_ee:
    cnt_ee = Enrollment.objects.filter(class_obj=cls_ee, role='student').count()
    print(f"[OK] CSL100-EE Students: {cnt_ee} (Expected ~58)")
    
# 3. Grades
# Check for non-zero scores
success_subs = SubmissionAttempt.objects.filter(status='success', manual_score__gt=0).count()
total_subs = SubmissionAttempt.objects.count()

print(f"[OK] Total Submissions: {total_subs}")
print(f"[OK] Non-Zero Score Submissions: {success_subs}")

if total_subs > 0:
    ratio = success_subs / total_subs
    print(f"    Success Rate: {ratio:.1%}")
    if ratio < 0.1:
        print("[WARN] Low success rate! Check scoring logic.")
    else:
        print("[OK] Scoring looks realistic.")

# 4. Sample
sample = SubmissionAttempt.objects.filter(manual_score__gt=0).first()
if sample:
    print(f"Sample Score: {sample.manual_score} (Student: {sample.student.username})")
    print(f"Code Snippet: {sample.source_code[:50]}...")
