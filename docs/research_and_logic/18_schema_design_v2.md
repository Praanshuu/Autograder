# Unified Database Schema Design (v2)

**Context:** Local Server Deployment (8x GPUs), 500-1000 Concurrent Users.
**Goal:** Scalability, Data Integrity, and Advanced Analytics Support.

---

## 1. Analytics Data Mapping (The "Why")

We designed these tables specifically to power your requested plots:

| Requested Plot / Feature | Powered By Table | Columns / Logic |
| :--- | :--- | :--- |
| **Marks vs Time** (Progress) | `SubmissionAttempt` | `created_at` records for every run (history). |
| **Performance Trajectory** | `StudentProgress` | Snapshot of `current_score` over sequence of assignments. |
| **Error Heatmaps** | `ProblemAnalytics` | Pre-aggregated `fail_count` by `test_case_id`. |
| **Word Cloud** | `SubmissionAnalysis` | `detected_keywords` (e.g. ['syntax_error', 'infinity_loop']). |
| **UMAP Logic Cluster** | `SubmissionAnalysis` | `umap_x`, `umap_y`, `cluster_label`. |
| **Marks Schema** (Gradebook) | `GradebookEntry` | Normalized score per student per assessment. |

---

## 2. Core Hierarchy: Modules & Content

We support **Practice Sets** vs **Tests** via `AssignmentType`.

### **Table: Class**
- `id`: UUID (PK)
- `owner_id`: FK -> User
- `name`: VARCHAR
- `join_code`: VARCHAR(6) [Unique]
- `settings`: JSONB

### **Table: Module**
*Grouping unit (e.g., "Week 1", "Graph Theory").*
- `id`: UUID (PK)
- `class_id`: FK -> Class
- `title`: VARCHAR
- `order_index`: INT
- `is_published`: BOOLEAN

### **Table: ContentItem** (Polymorphic Parent)
- `id`: UUID (PK)
- `module_id`: FK -> Module
- `type`: ENUM ('assignment', 'quiz', 'material')
- `title`: VARCHAR
- `description`: TEXT
- `order_index`: INT
- `is_published`: BOOLEAN
- `due_date`: TIMESTAMP (Critical for Calendar/Sorting)

### **Table: Assignment** (Extends ContentItem)
- `id`: FK -> ContentItem.id (PK)
- `mode`: ENUM ('practice', 'exam', 'homework')
- `points_total`: INT
- `difficulty`: ENUM ('easy', 'medium', 'hard')
- `config`: JSONB (Time limits, languages, max_retries)

### **Table: AssignmentProblem** (Through Table)
*Links reusable Problems to Assignments with specific context.*
- `id`: UUID (PK)
### **Table: ProblemVersion** (Reusable Question)
*The core problem definition.*
- `id`: UUID (PK)
- `title`: VARCHAR
- `slug`: VARCHAR (Unique)
- `description_markdown`: TEXT
- `starter_code`: TEXT
- `reference_solution`: TEXT
- `hint`: TEXT (UI Toggle)
- `test_cases`: JSONB (Or link to TestCase table)
- `created_at`: TIMESTAMP

---

## 3. Submission Engine (Immutable History)

### **Table: SubmissionAttempt**
*One record for EVERY time a student hits "Run" or "Submit".*
- `id`: UUID (PK)
- `type`: ENUM ('test_run', 'final_submission') -- UI distinguishes "Run" vs "Submit"
- `student_id`: FK -> User
- `assignment_problem_id`: FK -> AssignmentProblem
- `attempt_number`: INT
- `code_blob_ref`: VARCHAR (Path to MinIO/File)
- `language`: VARCHAR
- `status`: ENUM ('queued', 'processing', 'completed', 'error')
- `created_at`: TIMESTAMP
- `execution_time_ms`: INT (Runtime duration)
- `time_focused_seconds`: INT (Timer value from UI)
- `memory_usage_kb`: INT

### **Table: TestResult** (High Volume)
- `id`: UUID (PK)
- `attempt_id`: FK -> SubmissionAttempt
- `test_case_id`: FK -> TestCase
- `status`: ENUM ('pass', 'fail', 'timeout', 'runtime_error')
- `score`: FLOAT

---

## 4. Advanced Analytics & AI Layers

### **Table: SubmissionAnalysis** (AI Data)
*Serves Word Cloud & UMAP.*
- `id`: UUID (PK)
- `attempt_id`: FK -> SubmissionAttempt
- `umap_x`: FLOAT
- `umap_y`: FLOAT
- `cluster_label`: VARCHAR
- `ai_feedback_summary`: TEXT
- `detected_keywords`: ARRAY<VARCHAR> (Indexed for fast Word Cloud generation)

### **Table: ProblemAnalytics** (Aggregated View)
*Serves Error Heatmaps.*
- `assignment_problem_id`: FK
- `test_case_id`: FK
- `pass_count`: INT
- `fail_count`: INT
- `common_error_msg`: VARCHAR
- `last_updated`: TIMESTAMP

### **Table: GradebookEntry** (Marks Schema)
*Serves Student Marks Grid & Trajectory.*
- `student_id`: FK -> User
- `content_item_id`: FK -> ContentItem
- `score_obtained`: FLOAT
- `max_score`: FLOAT
- `grade_letter`: VARCHAR
- `manual_feedback`: TEXT (Visible to student)
- `private_notes`: TEXT (Teacher only)
- `submitted_at`: TIMESTAMP
- `status`: ENUM ('graded', 'pending', 'missing')

### **Table: AssignmentProgress** (UI Draft State)
*Handles Autosave & Timer State before submission.*
- `id`: UUID (PK)
- `student_id`: FK -> User
- `assignment_problem_id`: FK -> AssignmentProblem
- `current_code`: TEXT (Draft content)
- `current_language`: VARCHAR
- `time_spent_seconds`: INT (Accumulated timer)
- `last_updated`: TIMESTAMP

---

## 5. Calendar

### **Table: CalendarEvent**
- `id`: UUID (PK)
- `owner_id`: FK -> User
- `class_id`: FK -> Class (Nullable)
- `title`: VARCHAR
- `start_time`: TIMESTAMP
- `end_time`: TIMESTAMP
- `type`: ENUM
- `reference_id`: UUID (Link to Assignment/Quiz)

---

## 6. Notifications

### **Table: Notification**
- `id`: UUID (PK)
- `recipient_id`: FK -> User
- `type`: ENUM
- `title`: VARCHAR
- `payload`: JSONB (Deep links, metadata)
- `is_read`: BOOLEAN
- `created_at`: TIMESTAMP

---

## 7. Tech Stack Strategy (Local GPU Server)

1.  **PostgreSQL**: Primary Store.
2.  **Redis**:
    *   **Hot Queue**: For grading jobs.
    *   **Leaderboard**: Sorted Sets for fast rank retrieval.
3.  **MinIO (Local)**:
    *   Store `code_blob_ref` files here.
    *   Avoids bloating Postgres with huge text blocks.
4.  **Local LLM Worker (Python)**:
    *   Reads from Redis Queue.
    *   Runs Test Cases.
    *   Invokes Local LLM (Llama-3) for `SubmissionAnalysis`.
    *   Writes back to Postgres.
