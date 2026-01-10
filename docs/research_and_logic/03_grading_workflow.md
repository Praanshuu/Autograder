# Research & Logic: High-Velocity Grading Interface

**Date:** January 10, 2026
**Feature:** Grading Interface & Feedback Loop
**Status:** Implemented

---

## 1. The Problem: The "Context Switch" Tax
Grading coding assignments typically involves opening a file, reading logic, running it (mentally or locally), checking the rubric, and then writing feedback.
*   **Friction**: Switching between a code editor (VS Code), a browser (LMS), and a terminal breaks flow.
*   **Memory Loss**: By the time you navigate to the grade box, you might forget the specific line of code that was inefficient.
*   **Lack of Context**: Grading "Submission 4" in isolation makes it hard to know if this is an improvement or a regression for that student.

## 2. The Solution: Code-Centric Split View
We designed a `GradingInterface.jsx` that effectively acts as a specialized IDE for teachers.

### A. The Layout (Split Pane)
*   **Left Pane (The Evidence)**: Read-only code editor with syntax highlighting. It stays static while the teacher works.
*   **Right Pane (The Tools)**: A tabbed interface for "Rubric", "Autograder Results", and "History".
*   **Reasoning**: This mimics a developer's environment (Code + Inspector). The teacher never loses sight of the student's work while entering grades.

### B. "Contextual" History Tab
*   **Innovation**: We embedded the **Learning Trajectory** chart *inside* the grading sidebar.
*   **Logic**: When grading "Alice", the system fetches her history array.
*   **Benefit**: The teacher sees a trend line (e.g., "Declining Scores"). This changes the feedback from "You failed this loop" to "I noticed you've been struggling with iteration for two weeks—let's meet." It makes feedback **longitudinal** rather than **transactional**.

### C. Autograder "Console" View
*   **Design**: We don't just show "Pass/Fail". We render a mock terminal output.
*   **Why**: Teachers need to see the *runtime error* or the *stdout* to understand the student's thought process. A "Fail" badge tells you nothing; a `IndexOutOfBoundsException` tells you everything.

## 3. UX Decisions
*   **Manual Overrides**: We deliberately allowed teachers to change the "Autograde Score".
    *   *Why?* Automated tests are brittle. A student might fail a test because of a typo but get the logic 100% right. The UI empowers the teacher to award partial credit, reinforcing that **logic matters more than syntax**.
*   **Visual cues**: The usage of `CheckCircle2` (Green) and `XCircle` (Red) provides immediate cognition of test statuses without reading text.

## 4. Future Scope
*   **Inline Comments**: Like GitHub PR reviews, teachers should be able to click line 42 and leave a comment connected to that specific line.
*   **Diff View**: For resubmissions, show a "Diff" view against the student's *previous* submission to see exactly what they fixed.
*   **Snippets Library**: A clickable library of common feedback comments (e.g., "Check indentation", "Use variable naming conventions") to speed up typing.
