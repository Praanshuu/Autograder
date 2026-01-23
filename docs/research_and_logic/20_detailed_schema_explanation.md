# Deep Dive: Understanding the "vFinal" Schema

You asked for a **critical judgment** of the schema—how the tables connect, who uses what, and why we designed it this way.

This document breaks the `19_complete_unified_schema.md` down into plain English and "Data Flows".

---

## 1. The Big Picture (Entity Map)

This diagram shows the **High-Traffic Highway** (Student Submissions) vs. the **Static Map** (Class Structure).

```mermaid
erDiagram
    %% CORE USERS & CLASSES
    User ||--o{ Enrollment : joins
    Class ||--o{ Enrollment : has
    Class ||--o{ Module : contains
    Module ||--o{ ContentItem : organizes

    %% ASSIGNMENTS & CONTENT
    ContentItem ||--|| Assignment : "is a"
    Assignment ||--o{ AssignmentProblem : "includes"
    ProblemVersion ||--o{ AssignmentProblem : "is used in"

    %% THE SUBMISSION ENGINE (High Traffic)
    User ||--o{ AssignmentProgress : "drafts"
    AssignmentProblem ||--o{ AssignmentProgress : "has draft"
    
    User ||--o{ SubmissionAttempt : "submits"
    AssignmentProblem ||--o{ SubmissionAttempt : "attempted for"
    SubmissionAttempt ||--o{ TestResult : "generates"
    SubmissionAttempt ||--|| SubmissionAnalysis : "analyzed by AI"

    %% GRADES
    User ||--o{ GradebookEntry : "gets grade"
    ContentItem ||--o{ GradebookEntry : "graded for"
```

---

## 2. The Student's Journey (Table Usage)

Here is exactly which tables are touched when a Student interacts with the system.

### **Phase 1: "What do I have to do?" (Dashboard)**
*   **User Action**: Logs in and looks at "Up Next".
*   **Tables Query**:
    1.  `Enrollment`: "Which classes is Student X in?" -> Returns `class_id`s.
    2.  `ContentItem`: "Find items with `due_date > NOW()` linked to those classes."
    3.  `GradebookEntry`: "Filter out items where `status = 'graded'` or `score = 100`."
*   **Critical Logic**: We needed `due_date` on the parent `ContentItem` table so we don't have to join 5 different tables (Assignment, Quiz, etc.) just to sort by date.

### **Phase 2: "Working on the Problem" (The Workspace)**
*   **User Action**: Typos code, runs test cases, autosaves.
*   **Tables Query**:
    1.  **READ**: `AssignmentProblem` + `ProblemVersion` (Gets the Description, Starter Code).
    2.  **WRITE (Autosave)**: `AssignmentProgress`. 
        *   *Why separate?* This table is **Mutable** (we overwrite it constantly). It stays small. It prevents locking the massive history table.
        *   *Key Constraint*: `Unique(student_id, assignment_problem_id)`. One draft per problem.

### **Phase 3: "Submit!" (The Heavy Lift)**
*   **User Action**: Clicks "Submit" (Final Grading).
*   **Tables Query**:
    1.  **WRITE**: `SubmissionAttempt`.
        *   *The Magic*: This is **Immutable** (Append-Only). We never update this row. This preserves the history for the "Performance Trajectory" graph.
    2.  **WRITE**: `TestResult` (e.g., 10 rows for 10 test cases).
    3.  **WRITE**: `GradebookEntry`. We update the student's final score for the *Assignment* (parent) based on this attempt.

---

## 3. The Teacher's Journey (Analysis)

### **Scenario: "How is my class doing?" (Heatmap & Analytics)**
You asked how we fetch "Better Data". Here is the specific join strategy:

**1. The "Error Heatmap"**
*   **Goal**: Show which test case is failing the most.
*   **The Join**:
    `AssignmentProblem` (The Context)
    -> **JOIN** `ProblemAnalytics` (The Aggregated Stats)
*   **Why it's smart**: We don't verify 10,000 `TestResult` rows every time you load the page. We update `ProblemAnalytics` in the background. The dashboard loads instantly.

**2. The "Word Cloud" (Common Mistakes)**
*   **Goal**: See that 50% of students have "Infinite Loop" errors.
*   **The Join**:
    `SubmissionAttempt` (Filter by Assignment)
    -> **JOIN** `SubmissionAnalysis` (Select `detected_keywords`)
*   **Why it's smart**: `detected_keywords` is a Postgres Array. We can quickly count frequency: `SELECT keyword, count(*) FROM ... UNNEST(detected_keywords)`.

---

## 4. Critical Judgment: Why this Schema?

### **Critique 1: Why split `ContentItem` and `Assignment`?**
*   **The Problem**: If we just had an `Assignment` table, adding "Quizzes" or "PDF Resources" later would be messy. We'd need separate "Up Next" queries for each.
*   **The Solution**: **Polymorphism**. `ContentItem` holds the shared stuff (Title, Order, Due Date). `Assignment` holds the code-specific stuff (Time Limit, Languages).
*   **Trade-off**: It costs 1 extra JOIN to get the details.
*   **Verdict**: Worth it for a unified Calendar.

### **Critique 2: Why `AssignmentProblem` (Through Table)?**
*   **The Problem**: A `ProblemVersion` (e.g., "Two Sum") is global.
    *   In "Week 1 Homework", it might be worth 10 points.
    *   In "Final Exam", it might be worth 50 points.
*   **The Solution**: `AssignmentProblem` acts as the "Context". It says "Use 'Two Sum', but make it worth 50 points *for this specific exam*."
*   **Foreign Keys**: 
    *   `assignment_id` (FK to Assignment)
    *   `problem_id` (FK to ProblemVersion)

### **Critique 3: Handling Scale (1000 Users)**
*   **The Risk**: `TestResult` table will contain millions of rows (1000 users * 10 problems * 10 tests = 100k rows *per assignment*).
*   **The Defense**: 
    1.  **Composite Index**: We index `(attempt_id, status)`.
    2.  **Archiving**: We only need "Live" data for the current semester. Old `TestResults` can be moved to cold storage (CSV/Parquet) while keeping the `SubmissionAttempt` summary.

## 5. Summary of Relational Keys

| Table | Primary Key | Critical Foreign Keys | Why? |
| :--- | :--- | :--- | :--- |
| **SubmissionAttempt** | `id` (UUID) | `student_id`, `assignment_problem_id` | Links a specific run to a specific student context. |
| **AssignmentProgress** | `id` (UUID) | `student_id` | Allows "Resuming" work from where they left off. |
| **GradebookEntry** | `id` (UUID) | `student_id`, `content_item_id` | The "Report Card" view. Detached from individual code runs. |
