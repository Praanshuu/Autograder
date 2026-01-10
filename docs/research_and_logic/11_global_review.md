# Research & Logic: Global Assignment Review (All Assignments)

**Date:** January 10, 2026
**Feature**: Cross-Class Review Center
**Status**: Implemented

---

## 1. The Problem: Tunnel Vision
When a teacher manages 5 classes, they have 5 separate "Inbox" buckets.
*   **Missed Grading**: It's easy to forget that "Class A" had an assignment due yesterday if you are busy working on "Class B".
*   **Workflow Friction**: Navigating In/Out of every class just to check for submissions is tedious.

## 2. The Solution: The "To-Do" Aggregator
We built a global "All Assignments" page (`AllAssignments.jsx`) that acts as a unified Inbox for grading.

### Architecture
1.  **Data Aggregation**:
    *   The page fetches assignments from *all* active classes.
    *   **Filtering Logic**:
        *   **"To Review"**: `submissions.length > graded.length`. (Validation: If unprocessed work exists).
        *   **"Reviewed"**: `submissions.length == graded.length`.
2.  **Visual Queues**:
    *   We show the **Class Name** prominently on the card. This provides context ("Oh, this is for Calculus, not Algebra").
    *   **Progress Bar**: A visual indicator of "Graded vs. Total" (e.g., "15/20 graded") gives a sense of completion.

## 3. Creative Thought & UX Decisions
*   **Gamification of Work**: By treating grading like a "To-Do" list that can be cleared to zero ("Inbox Zero"), we provide a psychological reward structure for the teacher.
*   **Direct Access**: Clicking an item here bypasses the "Class Dashboard" and "Assignment Details" pages, dropping the teacher directly into the `GradingInterface`. This saves ~3 clicks per session.
*   **Separation of Concerns**: We explicitly separated "To Review" (Active) from "Reviewed" (Done). This prevents the "Done" pile from cluttering the workspace.

## 4. Future Scope & Improvements
*   **Smart Sorting**: Sort by "Oldest Submission First" to ensure no student waits too long for feedback.
*   **Batch Actions**: "Mark All as Graded" for participation-based assignments.
*   **Calendar Overlay**: See a timeline of "Grading Load" to help teachers realize "I shouldn't schedule 3 exams on the same day next month."
