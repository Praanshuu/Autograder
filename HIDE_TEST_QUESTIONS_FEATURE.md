# Hide Test Questions Feature Implementation

## Overview
This feature hides exam/test questions from the PracticeQuestionLibrary while the test is ongoing, and automatically displays them after the test ends.

## Changes Made

### 1. **PracticeQuestionLibrary Model** (`gamification/models.py`)
Added three new fields to track exam questions:
- `source_assignment`: ForeignKey to track which assignment (exam) the question belongs to
- `is_hidden`: Boolean flag to mark if a question is currently hidden
- `hide_until`: DateTimeField to store when the question should be unhidden (typically the exam due_date)

```python
source_assignment = models.ForeignKey('assignments.Assignment', on_delete=models.SET_NULL, 
                                      null=True, blank=True, related_name='library_questions')
is_hidden = models.BooleanField(default=False)  # Hide test/exam questions until test ends
hide_until = models.DateTimeField(null=True, blank=True)  # When to unhide
```

### 2. **PracticeQuestionLibraryViewSet** (`gamification/views.py`)
Updated the `get_queryset()` method to filter out hidden questions:

```python
def get_queryset(self):
    """Return public library questions that are not hidden or whose hide period has expired"""
    from django.utils import timezone
    now = timezone.now()
    
    return PracticeQuestionLibrary.objects.filter(
        is_public=True,
        question__is_active=True
    ).filter(
        # Include questions that are not hidden, or whose hide period has expired
        Q(is_hidden=False) | Q(hide_until__lte=now)
    ).select_related('question', 'question__created_by')
```

### 3. **Assignment Creation/Update Logic** (`assignments/views.py`)
Modified `perform_create()` and `perform_update()` in AssignmentViewSet:

**Before:**
- Deleted exam questions from PracticeQuestionLibrary entirely

**After:**
- Creates/updates PracticeQuestionLibrary entries with `is_hidden=True`
- Sets `hide_until` to the assignment's `due_date` (or 1 year in future if no due date)
- Tracks the `source_assignment` for reference

```python
# Get or create library entries and mark them as hidden
for q_id in q_ids:
    pql, _ = PracticeQuestionLibrary.objects.get_or_create(
        question_id=q_id,
        defaults={'is_public': True}
    )
    # Mark as hidden and set unhide date to assignment due date
    pql.is_hidden = True
    pql.source_assignment = assignment
    pql.hide_until = assignment.due_date if assignment.due_date else timezone.now() + timezone.timedelta(days=365)
    pql.save()
```

### 4. **Automatic Unhiding Task** (`assignments/tasks.py`)
Updated the existing Celery task `release_expired_exam_questions()` to:
- Check for exams whose `due_date` has passed
- Unhide their questions by setting `is_hidden=False` and clearing `hide_until`
- Mark the exam as processed to avoid re-processing

This task runs periodically (via Celery Beat) and automatically reveals exam questions after the test ends.

### 5. **Database Migration**
Created migration `0008_practicequestionlibrary_hide_until_and_more.py` that adds:
- `is_hidden` field with index
- `hide_until` field with index
- `source_assignment` ForeignKey field

## How It Works

1. **When an Exam is Created:**
   - Questions are automatically added to PracticeQuestionLibrary with `is_hidden=True`
   - `hide_until` is set to the exam's due_date
   - `source_assignment` tracks the exam

2. **While Exam is Active:**
   - Questions are NOT visible in PracticeQuestionLibrary when students browse
   - Filtering in `get_queryset()` excludes hidden questions

3. **After Exam Ends:**
   - Celery periodic task `release_expired_exam_questions()` runs
   - Finds all exams with `due_date` in the past and `questions_released=False`
   - Unhides their questions by setting `is_hidden=False`
   - Questions become visible in PracticeQuestionLibrary for practice

## Configuration

The periodic task is configured in your Celery Beat schedule. Ensure it's running:

```python
# celery.py configuration
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'release-expired-exam-questions': {
        'task': 'assignments.tasks.release_expired_exam_questions',
        'schedule': crontab(minute=0),  # Run every hour
    },
    # ... other scheduled tasks
}
```

## Benefits

- ✅ Prevents exam questions from being visible during the test
- ✅ Automatically shows questions after exam ends for practice
- ✅ No manual intervention required
- ✅ Database tracks relationship between questions and source exams
- ✅ Backward compatible (handles exams without due dates)

## Notes

- If an exam has no `due_date`, questions are hidden for 1 year by default
- The `questions_released` field on Assignment ensures the unhiding task is only processed once
- Existing exam questions in the library are not affected until an exam is created/updated
