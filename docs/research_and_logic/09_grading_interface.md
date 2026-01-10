# Research & Logic: Grading Interface & Autograder

**Date:** January 10, 2026
**Feature**: Split-Pane Grading Environment
**Status**: Implemented

---

## 1. The Problem: "Alt-Tab" Grading
In traditional environments, grading coding assignments involves three disconnected contexts:
1.  **Reading Code**: Viewing the file.
2.  **Running Code**: Executing it locally or in a terminal.
3.  **Entering Grades**: Going to the LMS to type "90/100".
This context switching is slow and error-prone.

## 2. The Solution: Integrated Split-Pane Environment
We built a unified interface (`GradingInterface.jsx`) that brings Code, Execution, and Evaluation into one screen.

### Architecture
1.  **Visual Layout**:
    *   **Left Pane (60%)**: Code Viewer. We use a syntax-highlighted block (simulating Monaco Editor) to show the student's submission.
    *   **Right Pane (40%)**: Grading Tools. This is tabbed to separate "Automated Results" from "Manual Feedback".
2.  **Autograder Logic**:
    *   **Results Visualization**: Instead of raw logs, we parse the results into a structured list of Test Cases.
    *   `Map`: `testCases.map(case => <Badge>{case.status}</Badge>)`.
    *   **Green/Red Indicators**: Immediate visual feedback on how much the code works.

## 3. Creative Thought & UX Decisions
*   **"Trust but Verify"**: The Autograder provides a "Suggested Score" based on passed tests, but the UI explicitly allows a **Manual Override**. This respects the teacher's authority to give partial credit for logic even if a semicolon was missing.
*   **Scoped Scrolling**: The left (code) and right (tools) panes scroll independently. This allows a teacher to read line 100 of the code while keeping the "Submit Grade" button visible on the right.
*   **Student History**: We added a "History" tab to show the student's learning trajectory. Knowing if a student *usually* does well vs. is *suddenly* failing helps the teacher write better feedback.

## 4. Future Scope & Improvements
*   **Inline Comments**: Allow teachers to highlight a specific line of code and attach a comment (`Line 23: Potential overflow here`).
*   **Diff View**: For resubmissions, show a side-by-side diff of "Version 1 vs Version 2" to see what changed.
*   **Plagiarism Detection**: Integrate a "Similarity Score" indicator in the header, linking to a detailed report if high.
