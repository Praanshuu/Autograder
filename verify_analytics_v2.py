import os
import django
import sys
import json
import time

# Setup Django
sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from submissions.services import analyze_code_structure, execute_code
from submissions.models import SubmissionAttempt, TestResult
# Import Serializer
from submissions.serializers import SubmissionAnalyticsSerializer

def verify_v2():
    print("--- Verifying Analytics V2 ---")
    
    # 1. Verify AST Analysis
    code_with_recursion = """
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

def nested():
    for i in range(10):
        for j in range(10):
            pass
"""
    print("\n[1] Testing AST Analysis...")
    keywords = analyze_code_structure(code_with_recursion)
    print(f"Detected Keywords: {keywords}")
    
    if "recursion" in keywords and "nested_loops" in keywords:
        print("✅ AST Analysis Passed: Recursion and Nested Loops detected.")
    else:
        print("❌ AST Analysis Failed.")

    # 2. Verify Execution Time
    print("\n[2] Testing Execution Time...")
    code_slow = """
import time
time.sleep(0.1)
print("done")
"""
    test_cases = [{'input': '', 'expected_output': 'done'}]
    
    results = execute_code(code_slow, 'python', test_cases)
    result = results[0]
    exec_time = result.get('execution_time', 0)
    print(f"Execution Time: {exec_time}ms")
    
    if exec_time >= 50: # Allow some buffer, typically > 100ms
        print("✅ Execution Time Verified (> 50ms).")
    else:
        print(f"❌ Execution Time Failed (too fast?): {exec_time}ms. Ensure runner is capturing time.")

    # 3. Verify Serializer
    print("\n[3] Testing Serializer...")
    
    from users.models import User
    from assignments.models import Assignment, Question, AssignmentQuestion
    from classes.models import Class, Module

    # Create dependencies
    student, _ = User.objects.get_or_create(username="verify_user", role="student")
    owner, _ = User.objects.get_or_create(username="verify_owner", role="teacher")
    
    class_obj = Class.objects.create(name="Verify Class", section="101", owner=owner)
    module = Module.objects.create(title="Verify Module", class_obj=class_obj)
    
    assignment = Assignment.objects.create(
        title="Verify Assignment", 
        module=module,
        type="assignment"
    )
    question = Question.objects.create(title="Verify Question", description="Desc", created_by=owner, slug="verify-q")
    aq = AssignmentQuestion.objects.create(assignment=assignment, question=question)

    # Create dummy attempt
    attempt = SubmissionAttempt.objects.create(
        student=student,
        assignment_question=aq,
        status='fail',
        feedback_text="Some feedback",
        detected_keywords=keywords
    )
    # Create dummy test result
    TestResult.objects.create(
        attempt=attempt,
        test_case_id="1",
        status="pass",
        actual_output="done",
        execution_time_ms=123
    )
    
    serializer = SubmissionAnalyticsSerializer(attempt)
    data = serializer.data
    
    print("Serialized Data:")
    print(json.dumps(data, indent=2))
    
    # Check execution_time_ms in test_results
    if 'test_results' in data and len(data['test_results']) > 0:
        tr = data['test_results'][0]
        if 'execution_time_ms' in tr and tr['execution_time_ms'] == 123:
            print("✅ Serializer execution_time_ms verified.")
        else:
            print("❌ Serializer execution_time_ms missing or incorrect.")
    else:
        print("❌ Test results missing in serialized data.")
        
    # Check feedback_tags
    tags = data['feedback_tags']
    if "recursion" in tags and "nested_loops" in tags:
        print("✅ Serializer feedback_tags verified (includes AST keywords).")
    else:
        print(f"❌ Serializer feedback_tags missing keywords: {tags}")

    # Cleanup
    attempt.delete()
    aq.delete()
    question.delete()
    assignment.delete()
    # student.delete() # Keep user to avoid issues if needed, or delete. Safe to leave.

if __name__ == "__main__":
    verify_v2()
