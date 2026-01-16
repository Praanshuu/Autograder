#!/usr/bin/env python3
"""
Populate Test Data Script
Creates assignments, submissions, and grades for testing
"""
import os
import sys
import django
import random
from datetime import timedelta
from django.utils import timezone

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from django.contrib.auth import get_user_model
from classes.models import Class, Enrollment
from assignments.models import Assignment, Question, TestCase
from submissions.models import Submission

User = get_user_model()

def create_assignments_for_class(class_obj, teacher, num_assignments=5):
    """Create assignments for a class"""
    print(f"\n📝 Creating {num_assignments} assignments for {class_obj.name}...")
    
    assignment_titles = [
        "Introduction to Programming",
        "Data Structures - Arrays",
        "Control Flow and Loops",
        "Functions and Recursion",
        "Object-Oriented Programming",
        "File I/O Operations",
        "Error Handling",
        "Algorithm Design",
        "Final Project",
        "Midterm Exam"
    ]
    
    assignments = []
    for i in range(num_assignments):
        title = assignment_titles[i % len(assignment_titles)]
        if i >= len(assignment_titles):
            title = f"{title} - Part {i // len(assignment_titles) + 1}"
        
        # Create assignment
        assignment = Assignment.objects.create(
            class_obj=class_obj,
            title=title,
            description=f"Complete the {title.lower()} assignment. Submit your code and ensure all test cases pass.",
            points=100,
            status='published',
            created_by=teacher,
            due_date=timezone.now() + timedelta(days=7 * (i + 1)),
            allow_late_submission=True
        )
        
        # Create a question for this assignment
        question = Question.objects.create(
            title=f"{title} - Main Task",
            description=f"Implement the solution for {title.lower()}.",
            difficulty='Medium',
            time_limit=5000,
            memory_limit=256,
            order=1
        )
        
        assignment.questions.add(question)
        
        # Create test cases
        for j in range(3):
            test_case = TestCase.objects.create(
                input=f"test_input_{j+1}",
                expected_output=f"expected_output_{j+1}",
                is_hidden=j > 0,  # First test case is visible
                points=100 // 3
            )
            question.test_cases.add(test_case)
        
        assignments.append(assignment)
        print(f"  ✓ Created: {title}")
    
    return assignments

def create_submissions_for_students(assignment, students):
    """Create submissions for students"""
    question = assignment.questions.first()
    if not question:
        return
    
    submission_count = 0
    for student in students:
        # 80% of students submit
        if random.random() < 0.8:
            # Random score between 60-100
            score = random.randint(60, 100)
            
            # Random status
            statuses = ['submitted', 'graded']
            status_choice = random.choice(statuses)
            
            Submission.objects.create(
                assignment=assignment,
                question=question,
                student=student,
                code_content=f"// Sample code submission for {assignment.title}\nfunction solve() {{\n  // Implementation here\n  return result;\n}}",
                language='javascript',
                status=status_choice,
                final_score=score,
                auto_grade_score=score,
                is_graded=True,
                is_published=True,
                teacher_feedback=f"Good work! Score: {score}/100" if score >= 80 else "Needs improvement. Review the concepts."
            )
            submission_count += 1
    
    return submission_count

def main():
    print("=" * 60)
    print("  Populating Test Data")
    print("=" * 60)
    
    # Get CSL100 class (the one with most students)
    try:
        csl100 = Class.objects.get(name="CSL100")
    except Class.DoesNotExist:
        print("❌ CSL100 class not found!")
        return 1
    
    # Get teacher
    teacher = User.objects.filter(role='teacher').first()
    if not teacher:
        print("❌ No teacher found!")
        return 1
    
    print(f"\n📚 Class: {csl100.name}")
    print(f"👨‍🏫 Teacher: {teacher.username}")
    
    # Get enrolled students
    students = User.objects.filter(
        enrollments__class_obj=csl100,
        enrollments__role='student',
        enrollments__status='active'
    ).distinct()
    
    print(f"👥 Students: {students.count()}")
    
    # Create assignments
    assignments = create_assignments_for_class(csl100, teacher, num_assignments=8)
    
    # Create submissions for each assignment
    print(f"\n📄 Creating submissions...")
    total_submissions = 0
    for assignment in assignments:
        count = create_submissions_for_students(assignment, students)
        total_submissions += count
        print(f"  ✓ {assignment.title}: {count} submissions")
    
    # Summary
    print(f"\n" + "=" * 60)
    print(f"✅ Data Population Complete!")
    print(f"=" * 60)
    print(f"  Classes: {Class.objects.count()}")
    print(f"  Assignments: {Assignment.objects.count()}")
    print(f"  Questions: {Question.objects.count()}")
    print(f"  Test Cases: {TestCase.objects.count()}")
    print(f"  Submissions: {Submission.objects.count()}")
    print(f"  Students with submissions: ~{int(students.count() * 0.8)}")
    print(f"\n🎉 You can now view assignments and grades in the UI!")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
