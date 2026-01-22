# Autograder Project - Complete Workflow Guide

## 🎯 Project Overview

Autograder is a Learning Management System (LMS) designed specifically for coding courses. It allows teachers to create assignments, students to submit code, and provides automated grading with instant feedback.

---

## 🏗️ Architecture

### Tech Stack

**Frontend:**
- React + Vite (Fast development)
- TailwindCSS (Styling)
- React Router (Navigation)
- Axios (API calls)

**Backend:**
- Django (Python web framework)
- Django REST Framework (API)
- SQLite (Database - development)
- JWT Authentication (djangorestframework-simplejwt)

**Structure:**
```
Autograder/
├── src/                          # React Frontend
│   ├── components/              # Reusable UI components
│   ├── pages/                   # Page components
│   │   ├── teacher/            # Teacher-specific pages
│   │   └── student/            # Student-specific pages
│   ├── services/               # API service layer
│   ├── contexts/               # React contexts (Auth, etc.)
│   └── config/                 # Configuration files
│
├── backend/                     # Django Backend
│   ├── autograder/             # Project settings
│   ├── users/                  # User management
│   ├── classes/                # Class management
│   ├── assignments/            # Assignment management
│   ├── submissions/            # Submission handling
│   └── notifications/          # Notification system
│
└── public/                      # Static assets
```

---

## 👥 User Roles & Workflows

### 1. **Teacher Workflow**

#### A. Initial Setup
1. **Register/Login**
   - Teacher creates account with role "teacher"
   - Logs in with credentials
   - Redirected to Teacher Dashboard

2. **Create a Class**
   - Click "Create Class" button
   - Fill in class details:
     - Name (e.g., "CSL100")
     - Description
     - Section, Subject, Room (optional)
   - System generates unique join code (e.g., "A9IW8U")
   - Teacher is automatically enrolled as class owner

#### B. Create Assignments
1. **Navigate to Class**
   - Select class from dashboard
   - Go to "Classwork" tab

2. **Create Assignment**
   - Click "Create Assignment"
   - Fill in details:
     - Title (e.g., "Introduction to Programming")
     - Description
     - Due date
     - Points (default: 100)
     - Allow late submissions (yes/no)

3. **Add Questions**
   - Each assignment can have multiple questions
   - For each question:
     - Title
     - Description
     - Difficulty level (Easy/Medium/Hard)
     - Time limit (milliseconds)
     - Memory limit (MB)
     - Allowed programming languages

4. **Add Test Cases**
   - For each question, add test cases:
     - Input data
     - Expected output
     - Points for this test case
     - Hidden/Visible (students see visible ones)

5. **Publish Assignment**
   - Status changes from "draft" to "published"
   - Students can now see and submit

#### C. Grade Submissions
1. **View Submissions**
   - Navigate to assignment
   - See all student submissions
   - View submission details:
     - Student name
     - Submission time
     - Code content
     - Auto-grade score (from test cases)

2. **Manual Grading**
   - Review student code
   - Add teacher feedback
   - Adjust score (manual adjustment)
   - Final score = auto_grade + manual_adjustment

3. **Publish Grades**
   - Click "Publish Grade"
   - Student receives notification
   - Grade becomes visible to student

#### D. View Gradebook
1. **Navigate to "Marks" Tab**
   - See spreadsheet-style gradebook
   - Rows: Students
   - Columns: Assignments
   - Cells: Scores
   - Can export or analyze data

---

### 2. **Student Workflow**

#### A. Initial Setup
1. **Register/Login**
   - Student creates account with role "student"
   - Logs in with credentials
   - Redirected to Student Dashboard

2. **Join a Class**
   - Click "Join Class" button
   - Enter join code (provided by teacher)
   - System enrolls student in class
   - Class appears on dashboard

#### B. View Assignments
1. **Dashboard View**
   - See all assignments across all classes
   - Filter by:
     - Class
     - Status (To Do, Submitted, Graded)
     - Search by title

2. **Assignment Details**
   - Click on assignment
   - See:
     - Description
     - Due date
     - Points
     - Questions
     - Visible test cases

#### C. Submit Code
1. **Open Workspace**
   - Click on assignment
   - Opens coding workspace with:
     - Code editor (Monaco Editor)
     - Language selector
     - Test case panel
     - Output console

2. **Write Code**
   - Write solution in editor
   - Select programming language
   - Can test code before submitting

3. **Test Code (Optional)**
   - Click "Run Tests"
   - Code runs against visible test cases
   - See output and results
   - Fix any issues

4. **Submit**
   - Click "Submit"
   - Code is saved
   - Auto-grader runs all test cases
   - Receives immediate feedback on visible tests
   - Status changes to "Submitted"

#### D. View Results
1. **Check Grades**
   - Navigate to assignment
   - See:
     - Auto-grade score
     - Test case results
     - Teacher feedback (if graded)
     - Final score (if published)

2. **Resubmit (if allowed)**
   - Can resubmit before deadline
   - Latest submission counts

---

## 🔄 Data Flow

### Authentication Flow
```
1. User enters credentials
   ↓
2. Frontend → POST /api/auth/simple-login/
   ↓
3. Backend validates credentials
   ↓
4. Backend generates JWT tokens (access + refresh)
   ↓
5. Frontend stores tokens in localStorage
   ↓
6. Frontend includes token in all API requests
   ↓
7. Backend validates token for protected routes
```

### Assignment Creation Flow
```
1. Teacher fills form
   ↓
2. Frontend → POST /api/assignments/
   {
     class_obj: 1,
     title: "Assignment 1",
     description: "...",
     due_date: "2024-01-20",
     points: 100,
     status: "draft"
   }
   ↓
3. Backend creates Assignment record
   ↓
4. Teacher adds questions
   ↓
5. Frontend → POST /api/assignments/questions/
   ↓
6. Backend creates Question records
   ↓
7. Teacher adds test cases
   ↓
8. Frontend → POST /api/assignments/test-cases/
   ↓
9. Backend creates TestCase records
   ↓
10. Teacher publishes
    ↓
11. Frontend → POST /api/assignments/{id}/publish/
    ↓
12. Backend updates status to "published"
```

### Submission Flow
```
1. Student writes code in editor
   ↓
2. Student clicks "Submit"
   ↓
3. Frontend → POST /api/submissions/submissions/
   {
     assignment: 1,
     question: 1,
     code_content: "function solve() {...}",
     language: "javascript"
   }
   ↓
4. Backend creates Submission record
   ↓
5. Backend runs auto-grader (future: AI grading)
   ↓
6. Backend calculates score from test cases
   ↓
7. Backend saves auto_grade_score
   ↓
8. Frontend receives response with score
   ↓
9. Student sees immediate feedback
```

### Grading Flow
```
1. Teacher views submission
   ↓
2. Frontend → GET /api/submissions/submissions/{id}/
   ↓
3. Backend returns submission with code
   ↓
4. Teacher reviews and adds feedback
   ↓
5. Frontend → PUT /api/submissions/submissions/{id}/grade/
   {
     final_score: 95,
     teacher_feedback: "Great work!",
     manual_adjustment: 5
   }
   ↓
6. Backend updates submission
   ↓
7. Teacher publishes grade
   ↓
8. Frontend → POST /api/submissions/submissions/{id}/publish/
   ↓
9. Backend sets is_published = true
   ↓
10. Backend creates notification for student
    ↓
11. Student sees grade and feedback
```

---

## 📊 Database Schema

### Key Models

**User**
- id, username, email, password (hashed)
- first_name, last_name
- role (student/teacher/ta/admin)
- avatar_url, settings
- is_active, date_joined

**Class**
- id, name, description
- owner (FK → User)
- join_code (unique, 6 chars)
- section, subject, room
- is_archived
- created_at, updated_at

**Enrollment**
- id
- user (FK → User)
- class_obj (FK → Class)
- role (student/teacher/ta)
- status (active/inactive)
- joined_at

**Assignment**
- id, title, description
- class_obj (FK → Class)
- created_by (FK → User)
- due_date, points
- status (draft/published/closed)
- allow_late_submission
- created_at, updated_at

**Question**
- id, title, description
- difficulty (Easy/Medium/Hard)
- time_limit, memory_limit
- allowed_languages (JSON array)
- order

**TestCase**
- id
- input, expected_output
- is_hidden (boolean)
- points

**Submission**
- id
- assignment (FK → Assignment)
- question (FK → Question)
- student (FK → User)
- code_content, language
- status (submitted/graded/late)
- auto_grade_score
- manual_adjustment
- final_score
- teacher_feedback
- is_graded, is_published
- submitted_at

---

## 🔐 Security & Permissions

### Authentication
- JWT tokens (access + refresh)
- Access token expires in 7 days
- Refresh token expires in 30 days
- Tokens stored in localStorage

### Authorization Rules

**Students can:**
- View published assignments in enrolled classes
- Submit code for assignments
- View their own submissions
- View published grades

**Students cannot:**
- View other students' submissions
- View unpublished assignments
- Modify assignments
- Grade submissions

**Teachers can:**
- Create/edit/delete assignments in their classes
- View all submissions in their classes
- Grade submissions
- Publish grades
- View gradebook

**Teachers cannot:**
- View/modify other teachers' classes (unless enrolled)
- Access admin functions

---

## 🚀 API Endpoints Summary

### Authentication
- `POST /api/auth/simple-login/` - Login
- `POST /api/users/register/` - Register
- `GET /api/users/me/` - Get current user

### Classes
- `GET /api/classes/` - List user's classes
- `POST /api/classes/` - Create class
- `GET /api/classes/{id}/` - Get class details
- `POST /api/classes/join-by-code/` - Join class
- `GET /api/classes/{id}/people/` - Get roster
- `GET /api/classes/{id}/grades/` - Get gradebook

### Assignments
- `GET /api/assignments/` - List assignments
- `GET /api/assignments/?class_id={id}` - Filter by class
- `POST /api/assignments/` - Create assignment
- `GET /api/assignments/{id}/` - Get details
- `POST /api/assignments/{id}/publish/` - Publish

### Submissions
- `GET /api/submissions/submissions/` - List submissions
- `POST /api/submissions/submissions/` - Submit code
- `GET /api/submissions/submissions/{id}/` - Get details
- `PUT /api/submissions/submissions/{id}/grade/` - Grade
- `POST /api/submissions/submissions/{id}/publish/` - Publish grade

---

## 🎨 Frontend Components

### Layout Components
- `StudentLayout` - Sidebar navigation for students
- `TeacherLayout` - Sidebar navigation for teachers

### Feature Components
- `CreateClassDialog` - Modal for creating classes
- `JoinClassDialog` - Modal for joining classes
- `StreamTab` - Class announcements/stream
- `ClassworkTab` - Assignments list
- `MarksTab` - Gradebook view
- `PeopleTab` - Class roster

### Page Components
- `TeacherDashboard` - Teacher home page
- `StudentDashboard` - Student home page
- `ClassPage` - Class details with tabs
- `AssignmentDashboard` - Assignment details
- `StudentWorkspace` - Code editor for submissions
- `GradingInterface` - Teacher grading view

---

## 🔧 Development Workflow

### Setup
1. Clone repository
2. Install dependencies:
   ```bash
   npm install
   cd backend && pip3 install -r requirements.txt
   ```
3. Setup database:
   ```bash
   cd backend
   python3 setup_database.py
   ```

### Running
1. Start backend:
   ```bash
   cd backend
   python3 manage.py runserver
   ```
2. Start frontend:
   ```bash
   npm run dev
   ```

### Testing
- Backend: `python3 manage.py test`
- Frontend: `npm test`

### Database Management
- Backup: `python3 backend/backup_database.py`
- Restore: `python3 backend/setup_database.py`
- Migrations: `python3 manage.py migrate`

---

## 📝 Key Features

### Current Features ✅
- User authentication (JWT)
- Role-based access control
- Class creation and management
- Join classes with codes
- Assignment creation with questions
- Test case management
- Code submission
- Auto-grading (test cases)
- Manual grading
- Gradebook view
- Notifications

### Future Features 🚧
- AI-powered code review
- Plagiarism detection
- Real-time collaboration
- Video tutorials
- Discussion forums
- Analytics dashboard
- Mobile app
- Integration with GitHub

---

## 🐛 Common Issues & Solutions

### Issue: Can't see assignments
**Solution:** Make sure:
1. You're enrolled in the class
2. Assignments are published
3. You're logged in with correct role

### Issue: Registration fails
**Solution:** Check:
1. Password is strong enough (8+ chars)
2. Passwords match
3. Email is valid
4. Username is unique

### Issue: Can't join class
**Solution:** Verify:
1. Join code is correct (case-sensitive)
2. Class is not archived
3. You're logged in as student

---

## 📚 Additional Resources

- **API Documentation**: See `backend/README.md`
- **Architecture**: See `backend/ARCHITECTURE.md`
- **Setup Guide**: See `SETUP.md`
- **Quick Start**: See `QUICK_START.md`

---

## 🎓 Learning Path

### For Students:
1. Register → Join Class → View Assignments → Submit Code → Check Grades

### For Teachers:
1. Register → Create Class → Share Join Code → Create Assignment → Grade Submissions → View Gradebook

---

This is your complete Autograder workflow! The system is designed to make coding education easier for both teachers and students. 🚀
