# Research & Logic: Class Management & Gradebook Architecture

**Date:** January 10, 2026
**Feature:** Class Page & Marks Tab
**Status:** Implemented

---

## 1. The Problem: Information Overload
A "Management System" for a class involves four distinct domains:
1.  **Communication** (Announcements, Chat)
2.  **Tasks** (Assignments, Materials)
3.  **People** (Roster, Roles)
4.  **Performance** (Grades, Analytics)

Jamming these into one dashboard creates cognitive clutter. Teachers spend too much time hunting for "Where do I add a student?" vs "Where do I post a message?".

## 2. The Solution: Tabbed Separation of Concerns
We adopted a rigid 4-tab architecture (`Stream`, `Classwork`, `People`, `Marks`) inspired by Google Classroom but enhanced with analytics.

### A. The "Marks" Tab (Gradebook 2.0)
The standard spreadsheet gradebook is boring and hard to parse. We upgraded it:
*   **Heatmap Toggling**: We added an "Eye" icon to toggle a heatmap mode.
    *   *Logic*: Conditional CSS classes (`bg-red-100`, `bg-green-100`) based on score thresholds (60, 70, 80, 90).
    *   *Benefit*: A teacher can squint at the screen and instantly see "Red Columns" (Hard assignments) or "Red Rows" (Struggling students) without reading a single number.
*   **Integrated Analytics Modal**:
    *   *Feature*: Clicking a student's name opens their **Learning Trajectory** graph.
    *   *Logic*: We reused the `LearningTrajectory` component but placed it in a Dialog overlay.
    *   *Why?* It prevents navigating away from the gradebook. You can check Alice's trend, close it, and move to Bob immediately.

### B. The "Stream" Tab (Dynamic Hub)
*   **Design**: A social-media style feed.
*   **Integration**: As detailed in `01_global_calendar_sync.md`, the "Upcoming Work" sidebar is a filtered view of global data.
*   **Purpose**: Keeps the "Business" of the class (deadlines) visible while facilitating the "Community" (discussion).

## 3. UX Decisions
*   **Sticky Columns**: In the `MarksTab`, the "Student Name" column is sticky (CSS `sticky left-0`).
    *   *Reasoning*: Gradebooks get wide. Teachers need to scroll horizontally to see Assignment #10, but they must not lose track of which row belongs to "Alice". This mimics Excel functionality in the web UI.
*   **Empty States**: We designed careful empty states (e.g., "All caught up!" in Assignment lists) to celebrate zero-inbox moments rather than showing blank screens.

## 4. Future Scope
*   **Export flexibility**: Currently we have a "Download CSV" button. Future versions should support specific formats (Excel, PDF, integrations with SIS like PowerSchool).
*   **Bulk Actions**: In the `People` tab, adding checkboxes to "Email Selected" or "Drop Selected" would improve administrative efficiency.
*   **Weighted Grading**: The current `gradebook.js` logic is simple averaging. Real classes use weights (e.g., Exams 40%, Homework 20%). The frontend logic needs to support a "Weighted" toggle in the calculation function.
