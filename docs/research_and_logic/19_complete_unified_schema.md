# Final Unified Database Schema Reference (vFinal)

**Date:** 2026-01-23
**Status:** Ready for Implementation
**Infrastructure:** Local Server (8x GPUs, PostgreSQL, Redis, MinIO)

---

## 1. Schema Overview & Core Hierarchy

This schema supports a **3-tier hierarchy**: `Class -> Module -> ContentItem`.
It uses **Polymorphism** for content items to support Assignments, Quizzes, and Materials uniformly in the Calendar and Gradebook.

### **Table: User** (Extends `auth.User`)
*Standard Django Authentication + Profile fields.*
- `id`: UUID (PK)
- `username`, `email`, `password_hash`: (Standard Auth)
- `role`: ENUM ('student', 'teacher', 'admin', 'ta')
- `avatar_url`: VARCHAR
- `settings`: JSONB (Notifications, Theme preferences)
- `created_at`: TIMESTAMP

### **Table: Class**
*Academic Course container.*
- `id`: UUID (PK)
- `owner_id`: FK -> User (Teacher)
- `name`: VARCHAR
- `section`: VARCHAR (e.g., "Fall 2025")
- `join_code`: VARCHAR(6) [Unique, Indexed]
- `is_archived`: BOOLEAN
- `settings`: JSONB (Grade weights, visibility)

### **Table: Enrollment** (Junction)
- `id`: UUID (PK)
- `user_id`: FK -> User
- `class_id`: FK -> Class
- `role`: ENUM ('student', 'ta', 'teacher')
- `joined_at`: TIMESTAMP
- `status`: ENUM ('active', 'dropped')
- *Unique Constraint: (user_id, class_id)*

### **Table: Module**
*Grouping unit (e.g., "Week 1", "Graph Theory").*
- `id`: UUID (PK)
- `class_id`: FK -> Class
- `title`: VARCHAR
- `description`: TEXT
- `order_index`: INT
- `is_published`: BOOLEAN

---

## 2. Content & Assignments

### **Table: ContentItem** (Polymorphic Parent)
*Base table for anything that appears in the course stream/calendar.*
- `id`: UUID (PK)
- `module_id`: FK -> Module
- `content_type`: ENUM ('assignment', 'quiz', 'material', 'announcement')
- `title`: VARCHAR
- `description`: TEXT
- `order_index`: INT
- `is_published`: BOOLEAN
- `due_date`: TIMESTAMP (Critical for Calendar & "Up Next")
- `release_date`: TIMESTAMP

### **Table: Assignment** (Extends ContentItem)
*Specific configuration for coding tasks.*
- `id`: FK -> ContentItem.id (PK)
- `mode`: ENUM ('practice', 'exam', 'homework')
    *   *Practice*: Unlimited retries, immediate hints/feedback.
    *   *Exam*: Timer enforced, hidden test cases, strict lock.
- `points_total`: INT
- `difficulty`: ENUM ('easy', 'medium', 'hard')
- `config`: JSONB
    *   `allowed_languages`: ["python", "cpp"]
    *   `time_limit_mins`: 60
    *   `max_attempts`: null (unlimited)

### **Table: ProblemVersion** (Reusable Question Library)
*The system-wide library of coding problems.*
- `id`: UUID (PK)
- `title`: VARCHAR
- `slug`: VARCHAR (Unique)
- `description_markdown`: TEXT
- `starter_code`: TEXT
- `reference_solution`: TEXT (Teacher solution)
- `hint`: TEXT (Revealable in UI)
- `test_cases`: JSONB (or FK to separate table for massive suites)
    *   Array of `{ input: string, output: string, hidden: bool, points: number }`
- `created_at`: TIMESTAMP

### **Table: AssignmentProblem** (Through Table)
*Links a specific Problem to an Assignment with local overrides.*
- `id`: UUID (PK)
- `assignment_id`: FK -> Assignment
- `problem_id`: FK -> ProblemVersion
- `order_index`: INT (Problem #1, #2...)
- `custom_points`: INT (Override default points)

---

## 3. Submission Engine & Immutable History

### **Table: AssignmentProgress** (Drafts & Autosave)
*Mutable state. Updated every 30s by UI.*
- `id`: UUID (PK)
- `student_id`: FK -> User
- `assignment_problem_id`: FK -> AssignmentProblem
- `current_code`: TEXT
- `current_language`: VARCHAR
- `time_spent_seconds`: INT (Accumulated focus time)
- `last_updated`: TIMESTAMP

### **Table: SubmissionAttempt** (Immutable History)
*Created on "Run" or "Submit". NEVER Updated.*
- `id`: UUID (PK)
- `type`: ENUM ('test_run', 'final_submission')
- `student_id`: FK -> User
- `assignment_problem_id`: FK -> AssignmentProblem
- `attempt_number`: INT (Auto-increment per student/problem)
- `code_blob_ref`: VARCHAR (Path to MinIO/File Storage)
- `language`: VARCHAR
- `status`: ENUM ('queued', 'processing', 'completed', 'error')
- `created_at`: TIMESTAMP
- `execution_time_ms`: INT (Server execution time)
- `time_focused_seconds`: INT (Snapshot of timer at submission)
- `memory_usage_kb`: INT

### **Table: TestResult** (Execution Details)
- `id`: UUID (PK)
- `attempt_id`: FK -> SubmissionAttempt
- `test_case_id`: VARCHAR (ID within the JSONB or FK)
- `status`: ENUM ('pass', 'fail', 'timeout', 'runtime_error')
- `stdout`: TEXT (Truncated to 10kb)
- `stderr`: TEXT
- `score`: FLOAT

---

## 4. Analytics & AI Layers

### **Table: SubmissionAnalysis** (AI & Clusters)
*Populated by background AI worker.*
- `id`: UUID (PK)
- `attempt_id`: FK -> SubmissionAttempt
- `umap_x`: FLOAT (For Logic Cluster Map)
- `umap_y`: FLOAT
- `cluster_label`: VARCHAR
- `ai_feedback_summary`: TEXT
- `detected_keywords`: ARRAY<VARCHAR> (For Word Cloud)

### **Table: ProblemAnalytics** (Aggregated Stats)
*For Heatmaps. Updated periodically or on-write.*
- `assignment_problem_id`: FK
- `test_case_id`: VARCHAR
- `pass_count`: INT
- `fail_count`: INT
- `common_error_msg`: VARCHAR
- `last_updated`: TIMESTAMP

---

## 5. Grading & Calendar

### **Table: GradebookEntry**
*Normalized View for "My Grades" and Teacher Gradebook.*
- `id`: UUID (PK)
- `student_id`: FK -> User
- `content_item_id`: FK -> ContentItem
- `score_obtained`: FLOAT
- `max_score`: FLOAT
- `grade_letter`: VARCHAR
- `manual_feedback`: TEXT
- `private_notes`: TEXT
- `submitted_at`: TIMESTAMP
- `status`: ENUM ('graded', 'pending', 'missing', 'excused')

### **Table: CalendarEvent**
- `id`: UUID (PK)
- `owner_id`: FK -> User
- `class_id`: FK -> Class (Nullable)
- `title`: VARCHAR
- `start_time`: TIMESTAMP
- `end_time`: TIMESTAMP
- `type`: ENUM ('class', 'assignment_due', 'exam', 'personal')
- `reference_id`: UUID (Nullable link to ContentItem)

### **Table: Notification**
- `id`: UUID (PK)
- `recipient_id`: FK -> User
- `type`: ENUM ('grade_posted', 'due_soon', 'announcement')
- `title`: VARCHAR
- `payload`: JSONB (Deep links)
- `is_read`: BOOLEAN
- `created_at`: TIMESTAMP

---

## 6. Implementation Notes
*   **Storage**: Access `code_blob_ref` via MinIO or disk mount, do not SELECT `TEXT` columns in list views.
*   **Indexing**: Add indices on `submission_attempt(student_id, assignment_problem_id)` and `content_item(due_date)`.
*   **Concurrency**: Use Redis for job queues (`celery`) to process `SubmissionAttempt` rows.
