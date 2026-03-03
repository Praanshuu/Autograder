# Testing Guide: Hide Test Questions Feature

## How to Test

### Step 1: Create an Exam with Questions
1. Go to your admin panel or API
2. Create an Assignment with:
   - `mode = 'exam'`
   - `due_date` = some future datetime
   - Add questions to it via `question_ids`

### Step 2: Verify Questions are Hidden
1. Browse the PracticeQuestionLibrary API endpoint
2. Verify exam questions are NOT visible
3. Example API call:
   ```bash
   curl -H "Authorization: Bearer <token>" \
   http://localhost:8000/api/practice-library/
   ```
   Expected: Exam questions should not appear in the list

### Step 3: Expire the Exam
1. Update the exam's `due_date` to a past datetime
2. Run the periodic task manually:
   ```bash
   python manage.py shell
   from assignments.tasks import release_expired_exam_questions
   result = release_expired_exam_questions()
   print(result)  # Should show questions released
   ```

### Step 4: Verify Questions are Unhidden
1. Browse the PracticeQuestionLibrary again
2. Verify exam questions NOW appear in the list
3. The same API call should now include the questions

## Database Queries for Testing

### Find hidden questions
```sql
SELECT * FROM practice_question_library 
WHERE is_hidden = true;
```

### Find questions with an associated exam
```sql
SELECT q.title, a.title as exam_title, pql.is_hidden
FROM practice_question_library pql
JOIN questions q ON pql.question_id = q.id
JOIN assignments a ON pql.source_assignment_id = a.id
WHERE a.mode = 'exam';
```

### Check which exams have released their questions
```sql
SELECT id, title, due_date, questions_released
FROM assignments
WHERE mode = 'exam'
ORDER BY due_date DESC;
```

## Manual Task Testing

```python
# Django shell
python manage.py shell

from assignments.tasks import release_expired_exam_questions
from datetime import timedelta
from django.utils import timezone

# Run the task
result = release_expired_exam_questions()
print(f"Exams processed: {result['exams_processed']}")
print(f"Questions released: {result['questions_released']}")
```

## Example: Create Test Scenario

```python
from django.utils import timezone
from datetime import timedelta
from assignments.models import Assignment, ContentItem, Question, AssignmentQuestion
from classes.models import Module, Class
from gamification.models import PracticeQuestionLibrary

# Assuming you have a class and module
module = Module.objects.first()

# Create an exam that expired 1 hour ago
exam = ContentItem.objects.create(
    module=module,
    type='assignment',
    title='Final Exam - Expired',
    is_published=True,
    due_date=timezone.now() - timedelta(hours=1)
)

assignment = Assignment.objects.create(
    id=exam.id,
    module=module,
    type='assignment',
    title=exam.title,
    mode='exam',
    is_published=True,
    due_date=timezone.now() - timedelta(hours=1)
)

# Add a question to it
question = Question.objects.first()  # Get any existing question
AssignmentQuestion.objects.create(
    assignment=assignment,
    question=question,
    order=1
)

# Check if it's hidden
pql = PracticeQuestionLibrary.objects.filter(question=question).first()
print(f"Question hidden: {pql.is_hidden}")  # Should be True

# Run the task
from assignments.tasks import release_expired_exam_questions
release_expired_exam_questions()

# Check again
pql.refresh_from_db()
print(f"Question hidden after task: {pql.is_hidden}")  # Should be False
```

## Expected Behavior Timeline

| Time | Status | Visible in Library |
|------|--------|-------------------|
| Before exam | Exam created | ❌ No (hidden) |
| During exam | Exam ongoing | ❌ No (hidden) |
| At due_date | Exam ends | ❌ No (still hidden) |
| +1 min | Task runs | ✅ Yes (unhidden) |

## Troubleshooting

### Questions still hidden after due date
1. Check if Celery Beat is running: `celery -A myproject beat`
2. Check Celery logs for task execution
3. Run the task manually to test

### AssignmentQuestion doesn't have expected questions
1. Verify `AssignmentQuestion.objects.filter(assignment=exam_id)` has entries
2. Check if the assignment ID matches the ContentItem ID

### API still doesn't show questions
1. Make sure to refresh the page/clear cache
2. Check the database directly with SQL queries above
3. Verify `is_hidden=False` and `hide_until` is in the past
