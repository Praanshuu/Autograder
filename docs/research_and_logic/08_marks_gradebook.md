# Research & Logic: Master Gradebook (Marks Tab)

**Date:** January 10, 2026
**Feature**: High-Density Gradebook Spreadsheet
**Status**: Implemented

---

## 1. The Problem: Data Density vs. Readability
Grading is a data-heavy task. A typical teacher with 30 students and 10 assignments manages 300+ data points.
*   **List Failure**: A list of "Recent Submissions" doesn't show the big picture. "Did Alice fail because she didn't study, or did *everyone* fail because the test was too hard?"
*   **Scroll Fatigue**: Navigating student-by-student to see grades is inefficient for broad analysis.

## 2. The Solution: 2D Grid with "Heatmap" Visualization
We implemented a spreadsheet-style interface (`MarksTab.jsx`) that prioritizes density without sacrificing clarity.

### Architecture
1.  **Grid Layout**:
    *   **X-Axis**: Assignments (Chronological).
    *   **Y-Axis**: Students (Alphabetical).
    *   **Z-Axis (Value)**: The Score.
2.  **Heatmap Logic**:
    *   We added a Toggle (`Switch`) to enable "Heatmap Mode".
    *   **Algorithm**: `Score / TotalPoints`.
        *   < 50%: Red Background (Critical).
        *   50-75%: Yellow (Warning).
        *   > 75%: Green/Transparent (Good).
3.  **Sticky Columns**: The Student Name column is stuck (`position: sticky`) to the left, ensuring context is never lost while scrolling horizontally through assignments.

## 3. Creative Thought & UX Decisions
*   **Instant Pattern Recognition**: The heatmap isn't just aesthetic; it's a diagnostic tool. A **Vertical Red Stripe** means a bad assignment (Teacher's fault?). A **Horizontal Red Stripe** means a struggling student (Intervention needed?).
*   **Safe Interaction**: Each cell is a button. Clicking it doesn't just "show a number"; it takes you directly to that student's submission for that specific assignment. It connects "Analysis" to "Action".
*   **Summary Cards**: We placed aggregated stats (Class Average, Highest Score) *above* the grid. This follows the "Dashboards First" principle—give the summary before the raw data.

## 4. Future Scope & Improvements
*   **Excel Export**: Essential for administrative reporting. `CSV` export logic needs to be added.
*   **Curve Grading**: A tool to "Add +5 to all" or "Normalize to Bell Curve" directly in the column header.
*   **Keyboard Navigation**: Power users should be able to navigate the grid with Arrow Keys and hit Enter to grade, just like in Excel.
