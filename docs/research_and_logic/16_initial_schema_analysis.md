# Deep Database Schema Analysis

**Date:** 2026-01-22
**Context:** Evaluation of current Autograder schema for 500–1000 concurrent users.

---

## 1. Summary of System Intent (Inferred)
The system is an **Autograding LMS** requiring:
*   **High-Frequency Writes**: Students saving code (autosave) and submitting (burst traffic).
*   **Complex Analytics**: "Time spent", "Error Heatmaps", and "Approach Clusters" (requires preserving history).
*   **Flexible Content**: reuse of questions across assignments.

---

## 2. Validation of Existing Schema Analysis
**Verdict: Partially Correct**

*   **Correct Identified Structure**: The relationship mapping (User 1-to-M Enrollment) is correct.
*   **Critical Miss - "Reusable Questions"**: The previous analysis claimed "Reusable questions across assignments" is a feature. While technically true via M2M, the current implementation is **broken**. The `order` field exists on the `Question` model, not the relationship.
    *   *Result*: If Question A is #1 in Assignment X, it MUST be #1 in Assignment Y. This breaks reuse flexibility.
*   **Critical Miss - "One submission per student"**: The analysis listed `unique_together: (assignment, question, student)` as a feature.
    *   *Result*: This is a **severe limitation**. It forces overwriting previous attempts, making "Improvement Analytics" and "Error Trends" impossible. You cannot graph a student's progress if you delete their past mistakes.

---

## 3. Strengths of Current Schema
*   **Clean Auth Separation**: Extending `AbstractUser` is standard and correctly implemented.
*   **Modular App Structure**: Splitting `users`, `classes`, `assignments` is good for code organization.
*   **Join Codes**: Simple, effective logic for enrollment.

---

## 4. Weaknesses & Design Smells

### 🚨 Critical Logic Flaws
1.  **M2M Context Missing (The "Order" Bug)**:
    *   *Issue*: `Question` has `order` and `points` (via `TestCase` aggregation).
    *   *Flaw*: You cannot assign different point values or orders to the *same* question in different assignments.
    *   *Fix*: Need an explicit "Through Model" (`AssignmentQuestion`) to store `order`, `points_override`, and `config` specific to that assignment context.

2.  **Destructive Submissions**:
    *   *Issue*: `Submission` has `unique_together`.
    *   *Flaw*: Autosaves and retries overwrite data.
    *   *Impact*: You lose the "User Journey". You can't detect "Brute Force" vs "Thoughtful" behavior if you only keep the final state.

3.  **Global Test Case Mutation**:
    *   *Issue*: `TestCases` are M2M with `Questions`.
    *   *Flaw*: If a teacher edits a test case to fix a typo for their class, it changes for **every other teacher** using that question.
    *   *Fix*: Test cases should largely be immutable or versioned once published.

### ⚠️ Performance Smells
1.  **JSONField Overuse**: `User.settings` and `Question.allowed_languages` as JSON are fine for now, but querying "Find all users with email_notifications=true" will be slow without specific JSONB indexes (Postgres specific).

---

## 5. Scalability & Concurrency Risks (500-1000 Users)

### 🔴 The SQLite Bottleneck
*   **Status**: **Will Fail immediately.**
*   *Why*: SQLite locks the entire file on write. 500 students submitting within 1 minute = ~8 requests/sec. Each grading operation might update `Submission`, `TestResult` (multiple rows). SQLite will throw `OperationalError: database is locked`.
*   *Requirement*: Must migrate to **PostgreSQL** for production.

### 🔴 The `TestResult` Explosion
*   *Math*: 1000 students × 5 assignments × 5 questions × 10 test cases = **250,000 records**.
*   *Risk*: This table grows fastest.
*   *Mitigation*: The table is necessary, but we need **Composite Indexes** `(submission, status)` or `(test_case, status)` for the "Error Heatmap" to load fast.

### 🟡 Autosave Contention
*   *Issue*: Frontend autosaves every 30s.
*   *Risk*: If 1000 users are active, that's 33 writes/sec. Updating the *same* `Submission` row repeatedly can cause row-level locking issues.
*   *Recommendation*: Use a specialized lightweight store (Redis) for "Drafts/Autosave" and only hit the main DB on "Run/Submit".

---

## 6. Missing or Incorrect Components

| Component | Status | Missing Logic |
| :--- | :--- | :--- |
| **AssignmentQuestion** | ❌ Missing | Stores specific `order`, `max_score` for a question *in a specific assignment*. |
| **SubmissionHistory** | ❌ Missing | Stores snapshots of code/results for every attempt. |
| **Rubrics** | ❌ Missing | Current grading is just a single integer `manual_adjustment`. Need structured criteria. |
| **Audit Log** | ❌ Missing | "Who changed this grade?" "Who edited this question?" |
| **Course Modules** | ❌ Missing | `Class -> Assignment` is too flat. Need `Class -> Module -> Assignment/Material`. |
