# Student Coding Environment Features

## Overview
Implemented a complete coding environment for students with code submission tracking, hints display, and an intelligent timer system.

## Features Implemented

### 1. Timer System ⏱️

#### Frontend Timer
- **Auto-start**: Timer starts automatically when student opens a question
- **Pause/Resume**: Students can manually pause and resume the timer
- **Auto-pause**: Timer pauses when student leaves the page (component unmount)
- **Auto-resume**: Timer resumes when student returns to the question
- **Display**: Shows elapsed time in MM:SS or HH:MM:SS format
- **Auto-save**: Timer state is saved to backend every 30 seconds
- **Persistent**: Timer state is loaded from backend when reopening a question

#### Backend Timer Tracking
- **New Fields in Submission Model**:
  - `time_spent`: Total time spent in seconds
  - `started_at`: When student first opened the question
  - `last_activity_at`: Last time student was active

- **New API Endpoints**:
  - `POST /api/submissions/submissions/start-timer/` - Start/resume timer
  - `POST /api/submissions/submissions/update-timer/` - Update time spent
  - `GET /api/submissions/submissions/get-timer/` - Get current timer state

### 2. Hints Display 💡

#### Question Model Updates
- Added `hint` field to Question model
- Added `starter_code` field to Question model

#### Frontend Hint Display
- Collapsible hint section below question description
- "Show Hint" / "Hide Hint" toggle button
- Styled with amber/yellow theme to stand out
- Animated expand/collapse transition
- Icon indicator (lightbulb) for visual clarity

### 3. Code Submission Tracking 📝

#### Submission Flow
1. Student writes code in the editor
2. Code is auto-saved with timer updates every 30 seconds
3. When student submits:
   - Final timer state is saved
   - Code content is saved
   - Time spent is recorded
   - Submission is created/updated in database

#### Teacher View
- Teachers can see:
  - Student's submitted code
  - Time spent on each question
  - Submission timestamp
  - Grades and feedback

### 4. Code Persistence 💾

- Student's code is saved to backend periodically
- When reopening a question, previous code is loaded
- Timer state is restored from last session
- No work is lost when navigating away

## Database Changes

### Migrations Applied
1. `assignments/migrations/0004_question_hint_question_starter_code.py`
   - Added `hint` field to Question
   - Added `starter_code` field to Question

2. `submissions/migrations/0004_submission_last_activity_at_submission_started_at_and_more.py`
   - Added `started_at` field to Submission
   - Added `last_activity_at` field to Submission
   - Changed `time_spent` from minutes to seconds

### Data Population
- All 39 existing questions updated with:
  - Sample hints
  - Python starter code template

## Files Modified

### Backend
1. `backend/assignments/models.py` - Added hint and starter_code fields
2. `backend/submissions/models.py` - Added timer tracking fields
3. `backend/submissions/views.py` - Added timer API endpoints
4. `backend/add_hints_to_questions.py` - Script to populate hints

### Frontend
1. `src/pages/student/StudentWorkspace.jsx` - Added timer and hints UI
2. `src/services/submissionService.js` - Added timer API methods

## How It Works

### Timer Flow
```
1. Student opens question
   ↓
2. Frontend calls startTimer() API
   ↓
3. Backend creates/updates Submission with started_at
   ↓
4. Frontend starts local timer interval (1 second)
   ↓
5. Every 30 seconds: updateTimer() API saves current time
   ↓
6. Student leaves page: pauseTimer() saves final time
   ↓
7. Student returns: getTimer() loads previous state
   ↓
8. Timer resumes from saved time
```

### Hint Flow
```
1. Question loads with hint data
   ↓
2. "Show Hint" button appears if hint exists
   ↓
3. Student clicks button
   ↓
4. Hint expands with animation
   ↓
5. Student can hide hint again
```

### Submission Flow
```
1. Student writes code
   ↓
2. Code auto-saves every 30 seconds with timer
   ↓
3. Student clicks "Submit"
   ↓
4. Final timer update sent to backend
   ↓
5. Submission created/updated with:
   - code_content
   - time_spent
   - submitted_at
   ↓
6. Timer stops
   ↓
7. Success modal shown
```

## Testing

### Test Timer Functionality
1. Login as student (`student_315` / `password`)
2. Go to Assignments
3. Click on any assignment
4. Observe timer starts automatically
5. Click pause button - timer stops
6. Click play button - timer resumes
7. Navigate away and come back - timer state persists

### Test Hints
1. Open any question in workspace
2. Scroll down in description panel
3. Click "Show Hint" button
4. Hint expands with animation
5. Click "Hide Hint" to collapse

### Test Code Submission
1. Write some code in the editor
2. Click "Submit" button
3. Code and timer are saved
4. Success modal appears
5. Check teacher dashboard - submission appears with time spent

## API Endpoints

### Timer Endpoints
```
POST /api/submissions/submissions/start-timer/
Body: { assignment_id, question_id }
Response: { success, data: { started_at, time_spent, last_activity_at } }

POST /api/submissions/submissions/update-timer/
Body: { assignment_id, question_id, time_spent }
Response: { success, data: { time_spent, last_activity_at } }

GET /api/submissions/submissions/get-timer/?assignment_id=X&question_id=Y
Response: { success, data: { started_at, time_spent, last_activity_at, code_content } }
```

## Future Enhancements

1. **Timer Analytics**
   - Show average time spent per question
   - Compare student time vs class average
   - Time-based insights for teachers

2. **Hint System**
   - Multiple hints per question (progressive hints)
   - Hint usage tracking
   - Penalty for using hints (optional)

3. **Code Autosave**
   - More frequent autosave (every 10 seconds)
   - Version history
   - Restore previous versions

4. **Timer Features**
   - Time limit warnings
   - Recommended time per question
   - Time-based achievements

## Notes

- Timer uses seconds for precision (not minutes)
- Timer state is saved even if student doesn't submit
- Hints are optional - questions without hints won't show the button
- Code editor supports Python syntax highlighting
- All timer operations are async and non-blocking
