# Autograder UI - Comprehensive Feature Documentation

This document serves as the master record of all features implemented in the Autograder UI. It details the functionality, design choices, and workflow integrations for the teacher's experience.

---

## 1. Global Navigation & Layout
**Component**: `TeacherLayout` | **Sidebar**: Persistent

The application uses a persistent sidebar layout for seamless navigation, ensuring teachers can jump between high-level management and specific class contexts without losing their place.

*   **Sidebar Links**:
    *   **Dashboard**: The home base.
    *   **Calendar**: (Placeholder) Schedule view.
    *   **All Assignments**: Global task list.
    *   **Archived Classes**: Read-only view of past courses.
    *   **Settings**: Global user preferences.
*   **Top Bar**:
    *   **Search**: Global search (Students, Classes, Assignments).
    *   **Notifications**: Real-time alerts via the **Bell Icon**.
        *   **Dropdown UI**: Shows detailed list of alerts (New Submissions, Comments, Deadlines).
        *   **Visual Indicators**: Red dot for unread, specialized icons (Check, Message, Clock) for context.
    *   **User Menu**: Profile management and logout.

---

## 2. Teacher Dashboard
**Location**: `/teacher/dashboard`

The landing page for teachers, providing a high-level overview of their active courses.

*   **Class Cards**:
    *   **Dynamic Visuals**: Color-coded patterns for quick visual distinction.
    *   **Key Stats**: Student count and active assignment count.
    *   **"Grading Pending" Indicator**: A pulsing amber indicator alerts teachers if a class has ungraded submissions, driving immediate action.
*   **Create Class**: Modal dialog to provision new courses.

---

## 3. Class Management (The Class Page)
**Location**: `/teacher/class/:classId`

The core workspace for a specific course, organized into four main tabs:

### A. Stream Tab
The social hub of the class.
*   **Announcements**: Rich-text input with attachment support (documents, links).
*   **Upcoming Work Card**: specialized "To-Do" widget showing immediate deadlines.
    *   **"View All" Modal**: A dialog showing the complete schedule of upcoming assignments.
*   **Comments**: Threaded discussions on posts.

### B. Classwork Tab
The curriculum organizer.
*   **Modules/Units**: Grouping of assignments and materials.
*   **Assignment List**: Status indicators (Active, Draft, Scheduled).

### C. People Tab
Roster management.
*   **Role Separation**: Distinct lists for Teachers and Students.
*   **Invite Modals**:
    *   **Invite Students**: Input email or copy invite link.
    *   **Invite Teachers**: Co-teacher collaboration invites.
*   **User Stats**: Displays class averages per student.

### D. Marks Tab (Gradebook)
High-density data view for grading performance.
*   **Heatmap Visualization**: Color-coded cells (Green -> Red) to instantly spot at-risk students or difficult assignments.
*   **Summary Cards**:
    *   **Class Average**: Overall performance metric.
    *   **Highest Average**: Top performing student.
    *   **Submissions Needed**: Count of pending grades.
*   **Grid Layout**: Scrollable grid mapping Students (rows) to Assignments (columns).

---

## 4. Assignment Workflow

### Creation & Editing
**Location**: `/teacher/assignments/create`
*   **Drag-and-Drop Question Manager**: Reorder questions simply by dragging.
*   **Question Editor Dialog**:
    *   **Test Case Definition**: Define input/output pairs for the autograder.
    *   **Difficulty tagging**: Easy/Medium/Hard tags.
*   **Rich Text Instructions**: Markdown support for assignment descriptions.

### The Grading Interface
**Location**: `/teacher/grading/submission/:submissionId`
Designed for speed and fairness.
*   **Split-Pane Layout**:
    *   **Left (Code)**: Read-only view of student's submission with syntax highlighting.
    *   **Right (Tools)**: Tabbed interface for Autograder Results and Manual Rubric.
*   **Autograder Feedback**:
    *   **Test Suite Results**: Line-by-line pass/fail status for test cases.
    *   **Console Output**: Raw execution logs for debugging.
*   **Manual Override**:
    *   **Score Adjustment**: Teachers can override the calculated score (e.g., awarding partial credit).
    *   **Feedback**: Text area for qualitative feedback.

---

## 5. Global Tools

### All Assignments (Review Center)
**Location**: `/teacher/assignments`
A "Command Center" for grading, aggregating work from **all** active classes into one list.
*   **"To Review" Tab**: Assignments with ungraded submissions. Shows "To Grade" vs "Turned In" counts.
*   **"Reviewed" Tab**: Historical view of completed assignments.

### Settings Page
**Location**: `/teacher/settings`
Fine-grained control over the application experience.
*   **Profile**: Avatar and name management.
*   **Notification Toggles**:
    *   **Global Email Toggle**: Master switch.
    *   **Granular Controls**: Specific toggles for Comments, Late Submissions, Resubmissions, and Co-teach invites.
    *   **Visual Logic**: Sub-settings disappear when the master Email switch is disabled (Conditional Rendering).

---

## 6. Advanced Analytics
**Context**: Deep insights for teachers.
*   **Performance Matrix**: Scatter plot (Time Spent vs. Score) to identify "Strugglers" vs "High Performers".
*   **Error Heatmap**: Grid view of test case failures. Red/Yellow/Green tiering helps spot common misconceptions.
*   **Code Similarity (UMAP)**: AI-driven clustering to group students by solution strategy (e.g., "Recursive" vs "Iterative").
*   **Learning Trajectory**:
    *   **Micro-View**: Line chart showing an individual student's performance trend across assignments.
    *   **Access**: Available in `GradingInterface` (History Tab) and `ClassPage` (Marks Tab -> Click Student).

## 7. Global Calendar
**Location**: `/teacher/calendar`
*   **Monthly View**: Visualizes all assignments, quizzes, and exams across **all** classes.
*   **Sync Logic**: Acts as the "Single Source of Truth". Events created here are automatically filtered and displayed in the appropriate **Class Stream**.
*   **Upcoming Events**: Sidebar list for quick scanning of immediate deadlines.

## 8. UI/UX Refinements
*   **Consistent Design System**: Usage of `ShadCN/UI` components (Cards, Badges, Dialogs, Switches) for a professional look.
*   **Visual Feedback**:
    *   **Hover Effects**: On cards and list items.
    *   **Micro-interactions**: Framer Motion animations on page loads.
*   **Accessibility**:
    *   **Contrast**: High-contrast text (e.g., Green text on dark console backgrounds).
    *   **Readable Modals**: Solid backgrounds for dialogs to prevent text bleeding.
*   **State Indication**:
    *   **Switches**: Blue for Active, Grey for Inactive.
    *   **Badges**: Color-coded status badges (Green for Success, Yellow for Pending).
