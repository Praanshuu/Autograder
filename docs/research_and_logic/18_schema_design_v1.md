# Unified Database Schema Design (v1)

**Context:** Local Server Deployment (8x GPUs), 500-1000 Concurrent Users.
**Goal:** Scalability, Data Integrity, and Advanced Analytics Support.

## 1. Core Content Hierarchy (The "Skeleton")

We are moving from a flat list to a structured "Module" based system.

### **Table: Class** (Existing, kept mostly same)
- `id`: UUID
- `owner_id`: UUID (Teacher)
- `join_code`: VARCHAR(6) [Unique]
- `settings`: JSONB (Theme, configurations)

### **Table: Module** (New)
*Grouping unit for content (e.g., "Week 1: Recursion").*
- `id`: UUID
- `class_id`: UUID [FK -> Class]
- `title`: VARCHAR
- `order_index`: INT
- `status`: ENUM ('active', 'archived')

### **Table: ContentItem** (New - Polymorphic)
*Abstracts Assignments, Quizzes, and Materials.*
- `id`: UUID
- `module_id`: UUID [FK -> Module]
- `content_type`: ENUM ('assignment', 'quiz', 'resource')
- `title`: VARCHAR
- `order_index`: INT
- `is_published`: BOOLEAN

### **Table: Assignment** (Refactored)
*Specifics for coding tasks.*
- `id`: UUID [FK -> ContentItem.id] (One-to-One with ContentItem)
- `instructions_markdown`: TEXT
- `difficulty`: ENUM
- `points_total`: INT
- `allowed_languages`: ARRAY<VARCHAR> (Postgres Array)
- `config`: JSONB (Time limits, memory limits)

### **Table: AssignmentProblem** (New - The "Through Model")
*Links reusable Problems to Assignments with context.*
- `id`: UUID
- `assignment_id`: UUID [FK]
- `problem_id`: UUID [FK -> ProblemVersion]
- `order_index`: INT
- `custom_points`: INT (Override default)

---

## 2. Submission Engine (The "Ledger")

We enforce **Immutable History**. Every "Run" is a new record.

### **Table: SubmissionAttempt**
- `id`: UUID
- `student_id`: UUID [FK]
- `assignment_problem_id`: UUID [FK]
- `attempt_number`: INT
- `code_content`: TEXT (Or Blob Reference)
- `language`: VARCHAR
- `status`: ENUM ('queued', 'processing', 'completed', 'error')
- `created_at`: TIMESTAMP
- `execution_time_ms`: INT
- `memory_usage_kb`: INT

### **Table: SubmissionResult**
*Stores the outcome of an attempt.*
- `id`: UUID
- `attempt_id`: UUID [FK]
- `score`: FLOAT
- `passed_test_cases`: INT
- `total_test_cases`: INT
- `feedback_markdown`: TEXT (Teacher/AI feedback)

### **Table: TestResult** (High Volume)
*Individual test case outcomes.*
- `id`: UUID
- `attempt_id`: UUID [FK]
- `test_case_id`: UUID [FK]
- `status`: ENUM ('pass', 'fail', 'timeout', 'runtime_error')
- `stdout`: TEXT (Truncated)
- `stderr`: TEXT

---

## 3. Analytics & "AI" Layers (The "Brain")

Pre-computed tables to serve the Dashboards fast without scanning millions of rows.

### **Table: StudentProgress** (Snapshot)
*Serving: Performance Matrix & Trajectory Graphs.*
- `student_id`: UUID
- `assignment_id`: UUID
- `current_score`: FLOAT
- `attempts_count`: INT
- `time_spent_seconds`: INT (Accumulated by frontend heartbeats)
- `last_activity`: TIMESTAMP
- `status`: ENUM ('started', 'submitted', 'graded')

### **Table: ProblemAnalytics** (Snapshot)
*Serving: Error Heatmaps.*
- `assignment_problem_id`: UUID
- `test_case_id`: UUID
- `pass_count`: INT
- `fail_count`: INT
- `common_error_type`: VARCHAR (e.g., "Timeout", "LogicError")
- `last_updated`: TIMESTAMP

### **Table: SubmissionAnalysis** (AI Data)
*Serving: UMAP Clusters & Word Clouds.*
- `attempt_id`: UUID [FK]
- `umap_x`: FLOAT
- `umap_y`: FLOAT
- `cluster_label`: VARCHAR (e.g., "Recursive Approach")
- `detected_keywords`: ARRAY<VARCHAR> (Normalized tags for Word Cloud)
- `ai_critique_summary`: TEXT

---

## 4. Calendar & Scheduling

### **Table: CalendarEvent**
- `id`: UUID
- `class_id`: UUID [FK] (Nullable - for personal events)
- `owner_id`: UUID [FK]
- `title`: VARCHAR
- `start_time`: TIMESTAMP
- `end_time`: TIMESTAMP
- `event_type`: ENUM ('assignment_due', 'exam', 'quiz', 'reminder')
- `reference_id`: UUID (Nullable - link to Assignment ID)

---

## 5. Technology Stack Recommendations (Local Server)

1.  **Database**: PostgreSQL 16+
    *   Extensions: `pg_trgm` (Search), `vector` (Optional for embeddings).
2.  **Cache/Queue**: Redis
    *   Queue for Grading Jobs.
    *   Cache for `StudentProgress` leaderboards.
3.  **Blob Storage**: MinIO (Docker) or Local Filesystem
    *   Store large code files and full logs here, not in PG `TEXT` columns.

## 6. Migration Notes
*   **Step 1**: Create new tables alongside old ones (`v2_submissions`).
*   **Step 2**: Dual-write to both during transition.
*   **Step 3**: Backfill `SubmissionAttempt` from existing `Submission` (creating "Attempt #1" for all).
