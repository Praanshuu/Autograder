# Backend Data Models & API Requirements
*Inferred from Frontend Implementation*

This document outlines the data structures and API contracts required to support the current Autograder UI. Use this as a blueprint for database schema design (SQL/NoSQL) and API endpoints.

## 1. User & Authentication
**Context**: Global state, Settings page, Profile.

```typescript
interface User {
  id: string;
  name: string;
  email: string; // Used for "Invite" logic
  avatar_url: string;
  role: "teacher" | "student" | "admin";
  settings: {
    notifications: {
      email_alerts: boolean;
      comments: boolean;
      class_invites: boolean;
      late_submissions: boolean;
    };
  };
}
```

## 2. Class Management
**Context**: Dashboard, Class Page (Header), Settings.

```typescript
interface Class {
  id: string;
  name: string; // e.g., "Advanced Algorithms"
  section: string; // e.g., "CS-401"
  subject: string;
  room: string;
  theme_color: string; // Hex code or predefined theme ID
  owner_id: string; // Teacher ID
  is_archived: boolean;
}

interface Enrollment {
  class_id: string;
  user_id: string;
  role: "TEACHER" | "STUDENT"; // Support for co-teachers
  joined_at: timestamp;
}
```

## 3. Stream & Communication
**Context**: Stream Tab, Announcements.

```typescript
interface StreamPost {
  id: string;
  class_id: string;
  author_id: string;
  content: string; // Rich text / Markdown
  created_at: timestamp;
  updated_at: timestamp;
  type: "ANNOUNCEMENT" | "MATERIAL";
  attachments: Attachment[]; // Links, Files
}

interface Comment {
  id: string;
  post_id: string; // Parent post
  author_id: string;
  content: string;
  created_at: timestamp;
}
```

## 4. Assignments & Grading
**Context**: Assignments Tab, Grading Interface, Marks Tab.

```typescript
interface Assignment {
  id: string;
  class_id: string;
  title: string;
  description: string; // Markdown
  due_date: timestamp;
  points: number;
  status: "DRAFT" | "PUBLISHED" | "SCHEDULED";
  questions: Question[];
}

interface Question {
  id: string;
  title: string;
  description: string;
  difficulty: "EASY" | "MEDIUM" | "HARD";
  test_cases: TestCase[];
}

interface TestCase {
  input: string;
  expected_output: string;
  is_hidden: boolean; // For "submit" vs "run"
}
```

## 5. Submissions & Results
**Context**: Grading Interface, Student View.

```typescript
interface Submission {
  id: string;
  assignment_id: string;
  student_id: string;
  submitted_at: timestamp;
  code_content: string;
  language: string; // e.g., "python", "cpp"
  status: "SUBMITTED" | "LATE" | "MISSING";
  
  // Grading
  auto_grade_score: number; // Calculated from passed test cases
  manual_adjustment: number; // Teacher override
  final_score: number; // Derived
  teacher_feedback: string;
  is_graded: boolean; // "Returned" to student
}

interface TestResult {
  submission_id: string;
  test_case_id: string;
  status: "PASS" | "FAIL" | "ERROR";
  execution_time: number;
  memory_usage: number;
  console_output: string;
}
```

## 6. Notifications
**Context**: Topbar Bell Icon.

```typescript
interface Notification {
  id: string;
  user_id: string;
  type: "SUBMISSION" | "COMMENT" | "ALERT" | "INVITE";
  title: string;
  message: string;
  reference_link: string; // Internal Deep Link (e.g. /teacher/grading/123)
  is_read: boolean;
  created_at: timestamp;
}
```

## Critical API Endpoints Needed

### Teacher Operations
*   `POST /api/classes`: Create a new class.
*   `POST /api/assignments`: Publish/Save assignment.
*   `GET /api/classes/:id/people`: Get roster.
*   `POST /api/invites`: Send email invites.
*   `PUT /api/submissions/:id/grade`: Update score and feedback.

### Dashboards
*   `GET /api/dashboard/summary`: Aggregated stats (Active assignments, grading pending counts).
*   `GET /api/notifications`: Fetch user alerts.

### Autograder Service
*   `POST /api/run`: Execute code against test cases (Stateless).
    *   Input: Code, Language, TestCases.
    *   Output: Pass/Fail results, Stdout/Stderr.
