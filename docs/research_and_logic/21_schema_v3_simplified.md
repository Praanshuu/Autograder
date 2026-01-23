# Unified Database Schema (v3 - Simplified)

**Status:** Finalizing for Implementation
**Key Decisions:**
1.  **No Complex Versioning**: Teachers edit drafts; published assignments are static.
2.  **Analytics Strategy**: "Practice Sets" power the Learning Trajectory; "Exams" are single-attempt.
3.  **Blob Data**: Code stored in file storage (`code_blob_ref`) for performance.

---

## 1. Core Users & Classes

### **Table: User**
*Standard Django AbstractUser.*
- `id`: UUID (PK)
- `username`, `email`, `role`, `avatar_url`

### **Table: Class**
- `id`: UUID (PK)
- `owner_id`: FK -> User
- `name`, `section`, `join_code`, `settings` (JSONB)

### **Table: Enrollment** (Junction)
- `user_id`, `class_id`, `role`

---

## 2. Content Structure (Simplified)

We removed the `ProblemVersion` complexity. Questions are now simple resources.

### **Table: Module**
*Grouping unit (e.g., "Week 1").*
- `id`: UUID (PK)
- `class_id`: FK -> Class
- `title`, `order_index`

### **Table: ContentItem** (Polymorphic Parent)
*Anything in the stream (Assignment, Quiz, Material).*
- `id`: UUID (PK)
- `module_id`: FK -> Module
- `type`: ENUM ('assignment', 'quiz', 'material')
- `title`, `description`, `is_published`
- `due_date`: TIMESTAMP

### **Table: Assignment** (Extends ContentItem)
- `id`: FK -> ContentItem
- `mode`: ENUM ('practice', 'exam')
    *   **Practice**: Allows multiple `SubmissionAttempts` (Powers Analytics).
    *   **Exam**: Application Logic restricts to 1 `SubmissionAttempt`.
- `points_total`: INT
- `difficulty`: ENUM
- `config`: JSONB (languages, time_limit)

### **Table: Question** (Was ProblemVersion)
*A reusable coding problem.*
- `id`: UUID (PK)
- `title`: VARCHAR
- `slug`: VARCHAR (Unique)
- `description`: TEXT
- `starter_code`: TEXT
- `reference_solution`: TEXT
- `test_cases`: JSONB (Input/Output/Hidden/Points)
- `created_by`: FK -> User (Teacher)

### **Table: AssignmentQuestion** (Link Table)
*Orders questions within an assignment.*
- `assignment_id`: FK -> Assignment
- `question_id`: FK -> Question
- `order`: INT
- `custom_points`: INT (Optional override)

---

## 3. Submission & Grading (The Engine)

### **Table: AssignmentProgress** (Autosave/Draft)
*Mutable. Overwritten every 30s.*
- `id`: UUID (PK)
- `student_id`: FK
- `assignment_question_id`: FK
- `current_code`: TEXT
- `time_spent`: INT

### **Table: SubmissionAttempt** (The Log)
*Immutable.*
*For **Exam**: Only 1 row allowed per student/question.*
*For **Practice**: Multiple rows allowed (This data feeds the Learning Graphs).*
- `id`: UUID (PK)
- `student_id`: FK
- `assignment_question_id`: FK
- `attempt_number`: INT
- `code_blob_ref`: VARCHAR (Path to file)
- `execution_time_ms`: INT
- `status`: ENUM ('queued', 'success', 'fail')
- `created_at`: TIMESTAMP

### **Table: TestResult** (Details)
- `attempt_id`: FK
- `test_case_id`: VARCHAR
- `status`: ENUM
- `score`: FLOAT

### **Table: GradebookEntry** (The Scorecard)
*Summary for the Gradebook UI.*
- `student_id`: FK
- `content_item_id`: FK
- `final_score`: FLOAT
- `status`: ENUM ('graded', 'submitted')

---

## 4. Analytics (Aggregated)

### **Table: SubmissionAnalysis** (AI)
- `attempt_id`: FK
- `detected_keywords`: ARRAY<VARCHAR> (Word Cloud)
- `umap_x`, `umap_y`: FLOAT (Cluster Map)
- `ai_feedback`: TEXT

### **Table: ProblemAnalytics**
*Pre-calculated stats for Heatmaps.*
- `question_id`: FK
- `test_case_id`: VARCHAR
- `pass_count`, `fail_count`
