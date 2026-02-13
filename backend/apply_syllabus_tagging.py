import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()

from assignments.models import Question

# Syllabus Mapping
syllabus = {
    "Python Basics & Control Flow": ["Q1", "Q4", "Q5", "Q6", "Q10"],
    "Strings & String Operations": ["Q2", "Q3", "Q12", "Q19"],
    "Lists & List Operations": ["Q7", "Q8", "Q15", "Q28"],
    "Functions & Advanced Parameters": ["Q10", "Q11"],
    "Recursion": ["Q9", "Q16", "Q18"],
    "Dictionaries": ["Q11", "Q12", "Q14", "Q26", "Q27"],
    "Sets": ["Q7", "Q13"],
    "List Comprehension": ["Q15"],
    "Nested Data Structures": ["Q16", "Q17", "Q30"],
    "Algorithmic Problem Solving": ["Q18", "Q19", "Q28", "Q29"],
    "Validation Problems": ["Q20"],
    "Object-Oriented Programming (OOP)": ["Q21", "Q22", "Q23", "Q24", "Q25"]
}

# Invert to map Q_num -> [Tags]
q_to_tags = {}
for topic, q_list in syllabus.items():
    for q_code in q_list:
        if q_code not in q_to_tags:
            q_to_tags[q_code] = []
        q_to_tags[q_code].append(topic)

print("Mapping Plan:")
for q, tags in q_to_tags.items():
    print(f"{q}: {tags}")

print("\nApplying Tags...")

questions = Question.objects.all()
updated_count = 0

for q in questions:
    # Match title "Q1." or "Q1 " or just "Q1" if exact
    # My DB check showed titles like "Q1. FizzBuzz".
    # extracting prefix
    title = q.title.strip()
    q_code = None
    
    # Try to find Q code in title
    import re
    match = re.search(r"Q(\d+)", title)
    if match:
        q_num = match.group(1)
        q_code = f"Q{q_num}"
    
    if q_code and q_code in q_to_tags:
        new_tags = q_to_tags[q_code]
        # Merge with existing tags if any, ensuring uniqueness
        current_tags = q.tags or []
        # if tags is list of strings
        combined_tags = list(set(current_tags + new_tags))
        
        q.tags = combined_tags
        q.save()
        print(f"Updated {title} with tags: {combined_tags}")
        updated_count += 1
    else:
        # print(f"Skipped {title} (No matching Q code found)")
        pass

print(f"\nTotal Questions Updated: {updated_count}")
