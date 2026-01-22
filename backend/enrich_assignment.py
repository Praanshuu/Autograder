import os
import django
import random
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from assignments.models import Assignment, Question, TestCase
from submissions.models import Submission, TestResult

User = get_user_model()

def enrich_data():
    print("Enriching Assignment ID 1...")
    
    try:
        assignment = Assignment.objects.get(id=1)
    except Assignment.DoesNotExist:
        print("Assignment ID 1 not found.")
        return

    # 1. Update Assignment Details
    assignment.title = "Introduction to Programming"
    assignment.description = "A series of basic programming challenges to test your understanding of variables, loops, and functions."
    assignment.points = 300
    assignment.due_date = timezone.now() + timedelta(days=7)
    assignment.status = 'published'
    assignment.save()
    print("Assignment updated.")

    # 2. Update Student Names (Indian Names)
    indian_first_names = [
        "Aarav", "Vihaan", "Aditya", "Sai", "Arjun", "Reyansh", "Muhammad", "Aryan",
        "Ishaan", "Dhruv", "Kabir", "Ananya", "Diya", "Saanvi", "Aadhya", "Pari",
        "Fatima", "Zara", "Myra", "Riya", "Krishna", "Rahul", "Rohan", "Vikram"
    ]
    indian_last_names = [
        "Patel", "Sharma", "Singh", "Kumar", "Gupta", "Verma", "Reddy", "Rao", 
        "Jain", "Mehta", "Malhotra", "Khan", "Shah", "Desai", "Joshi", "Das"
    ]
    
    students = list(User.objects.filter(role='student'))
    print(f"Updating names for {len(students)} students...")
    for student in students:
        student.first_name = random.choice(indian_first_names)
        student.last_name = random.choice(indian_last_names)
        student.save()

    # 3. Create Realistic Questions
    questions_data = [
        {
            "title": "Hello World",
            "description": "Write a function that returns the string 'Hello, World!'.",
            "difficulty": "Easy",
            "points": 50,
            "test_cases": [
                {"input": "", "expected_output": "Hello, World!", "points": 50, "is_hidden": False}
            ]
        },
        {
            "title": "Sum of Two Numbers",
            "description": "Write a function `sum(a, b)` that takes two integers and returns their sum.",
            "difficulty": "Easy",
            "points": 100,
            "test_cases": [
                {"input": "1 2", "expected_output": "3", "points": 50, "is_hidden": False},
                {"input": "-1 5", "expected_output": "4", "points": 50, "is_hidden": True}
            ]
        },
        {
            "title": "Factorial",
            "description": "Write a function `factorial(n)` that returns the factorial of n. Return -1 for negative numbers.",
            "difficulty": "Medium",
            "points": 150,
            "test_cases": [
                {"input": "5", "expected_output": "120", "points": 50, "is_hidden": False},
                {"input": "0", "expected_output": "1", "points": 50, "is_hidden": False},
                {"input": "-5", "expected_output": "-1", "points": 50, "is_hidden": True}
            ]
        }
    ]

    # Clear existing to rebuild
    assignment.questions.clear() 
    
    created_questions = []
    for idx, q_data in enumerate(questions_data):
        q, _ = Question.objects.get_or_create(
            title=q_data['title'],
            defaults={
                'description': q_data['description'],
                'difficulty': q_data['difficulty'],
                'order': idx
            }
        )
        q.description = q_data['description']
        q.save()
        assignment.questions.add(q)
        created_questions.append(q)

        q.test_cases.clear()
        for tc_data in q_data['test_cases']:
            tc = TestCase.objects.create(
                input=tc_data['input'],
                expected_output=tc_data['expected_output'],
                points=tc_data['points'],
                is_hidden=tc_data['is_hidden']
            )
            q.test_cases.add(tc)

    # 4. Generate Submissions
    
    # Keyword pools for word cloud
    positive_tags = ["Optimal Solution", "Clean Code", "Efficient", "Good Logic", "Well Documented"]
    negative_tags = ["Syntax Error", "Logic Error", "Time Limit Exceeded", "Memory Limit", "Edge Case Failure", "Indentation Error", "Redundant Code"]
    
    print(f"Generating submissions...")

    Submission.objects.filter(assignment=assignment).delete() 

    # We want ~120 submissions total across 3 questions
    target_students = random.sample(students, min(len(students), 60))

    for student in target_students:
        for question in created_questions:
            if random.random() > 0.85: continue # 15% skip rate
            
            # User profile (Smart, Average, Struggling)
            profile = random.choices(['smart', 'average', 'struggling'], weights=[0.2, 0.5, 0.3])[0]
            
            if profile == 'smart':
                score_pct = random.uniform(0.9, 1.0)
                tags = random.sample(positive_tags, k=random.randint(1, 3))
            elif profile == 'average':
                score_pct = random.uniform(0.4, 0.85)
                # Mix of tags
                tags = random.sample(positive_tags + negative_tags, k=random.randint(1, 3))
            else:
                score_pct = random.uniform(0.0, 0.4)
                tags = random.sample(negative_tags, k=random.randint(1, 4))
                
            # Create Submission
            submitted_at = timezone.now() - timedelta(days=random.randint(0, 6), hours=random.randint(0, 23))
            
            sub = Submission.objects.create(
                assignment=assignment,
                question=question,
                student=student,
                code_content="# Sample code...",
                language="python",
                submitted_at=submitted_at,
                status='submitted',
                feedback_tags = ", ".join(tags)
            )

            # Generate Test Result details based on score_pct
            total_points = 0
            tcs = list(question.test_cases.all())
            total_possible = sum(tc.points for tc in tcs)
            
            target_score = int(total_possible * score_pct)
            current_score = 0
            
            for tc in tcs:
                # Decide if pass based on remaining needed score
                if current_score < target_score:
                     passed = True
                     current_score += tc.points
                else:
                     passed = False
                
                tr = TestResult.objects.create(
                    test_case=tc,
                    status='pass' if passed else 'fail',
                    execution_time=random.randint(10, 100),
                    memory_usage=random.randint(5, 50),
                    points_earned=tc.points if passed else 0,
                    console_output="Pass" if passed else "Fail",
                    error_message="" if passed else f"Failed test case {tc.id}"
                )
                sub.test_results.add(tr)
            
            sub.auto_grade_score = current_score
            sub.final_score = current_score # Store raw score? Or percentage? 
            # Frontend: "sub.final_score !== null ? `${sub.final_score}%`"
            # It expects percentage usually for grade display, 
            # BUT BoxPlot uses values. 
            # Step 89 Model: final_score = models.IntegerField(default=0)
            # Step 212 Dashboard: scores.reduce...
            # Usually Autograders store RAW points, but frontend treats as % if out of 100?
            # Question points: 50, 100, 150 = 300 total.
            # If dashboard shows %, it divides?
            # Dashboard line 289: `${sub.final_score}%`
            # This implies the stored value IS percentage (0-100).
            # Okay, I will normalize the score to 0-100 for `final_score`.
            
            sub.final_score = int((current_score / total_possible) * 100) if total_possible > 0 else 0
            sub.save()
            
    print("Deep Enrichment Complete!")

if __name__ == '__main__':
    enrich_data()
