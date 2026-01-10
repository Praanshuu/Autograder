# Implementation Plan - Autograder Frontend

## Goal Description
Initialize and develop the frontend UI for **Autograder**, a coding-focused LMS. The focus is on a modern, minimalistic, and responsive design inspired by Google Classroom and LeetCode, tailored for Teachers, Students, and TAs.

## User Review Required
> [!IMPORTANT]
> **Project Initialization**: I plan to use **Vite** with **React** and **TailwindCSS**. This provides a fast, modern development environment perfectly matching your requirements.
> **State Management**: I will stick to **React Context + Hooks** as requested to keep it lightweight, unless you prefer a small library like **Zustand** for easier global state (e.g., user session, theme).
> **Mock Data**: Since there is no backend, I will create a dedicated `mock` directory with robust JSON data to simulate API responses for classes, assignments, and submissions.

## Proposed Changes

### Project Setup
#### [NEW] [Project Initialization]
- Initialize Vite React project in the root directory.
- Configure TailwindCSS (v3).
- Setup `react-router-dom` for routing.
- Setup `lucide-react` for icons.
- **[NEW]** Setup `shadcn/ui` for premium generic components.
- **[NEW]** Setup `framer-motion` for smooth animations.

### Component Structure
I will organize components by feature and reusability.

#### [NEW] [Directory Structure]
```text
/src
  /components
    /ui          (Reusable atoms: Button, Card, Input, Badge)
    /layout      (Sidebar, Navbar, AuthLayout, DashboardLayout)
    /features    (Feature-specific components)
      /teacher
      /student
      /editor
  /pages         (Page views)
    /teacher
    /student
    /auth
  /context       (Global state: AuthContext, ThemeContext)
  /mocks         (Mock data generators)
```

### Initial Development Tasks
1.  **Scaffolding**: Run `npm create vite@latest` and install dependencies.
2.  **Design System**: Define tailwind config for "calm, neutral colors" and typography.
3.  **Routing**: define routes in `App.jsx` for `/teacher/*`, `/student/*`.
4.  **Core Layouts**: Build the shared shell (Navbar with role-based links).
5.  **ShadCN Setup**: Initialize shadcn and add base components (Card, Button, Sheet, Dropdown).
6.  **Teacher Dashboard**: Refactor to use proper Cards and Framer Motion entrance animations.
7.  **Assignment Creation**:
    -   Create `/teacher/assignment/create` page.
    -   Implement `AssignmentForm` (Title, Instructions, Deadline).
    -   Implement `QuestionEditor` (Problem, Inputs, Test Cases).
    -   Use `Reorder` from Framer Motion for questions list.
8.  **Class Page Implementation**:
    -   **Global Layout**: Update `TeacherLayout` with Breadcrumbs, Calendar, Teaching sections.
    -   **Class Header**: Banner image, Theme color, Class Info.
    -   **Tabs Navigation**: Stream, Classwork, People, Marks.
    -   **Stream Tab**: Announcements feed, Upcoming work widget (with View All modal), Attachments UI.
    -   **Classwork Tab**: Create dropdown, Topics, Assignment list.
    -   **People Tab**: Teacher, TA, and Student lists with invite actions (Email Modal).
    -   **Marks Tab**: Gradebook table.
    -   **Archived Classes**: Refine UI with grayscale styling and read-only indicators.
    -   **Create Class**: Implement as a **Modal/Dialog** on the dashboard for better UX (preserves context).
        -   Fields: Name, Section, Subject, Room.

### Grading & Analytics System
#### [NEW] [AssignmentDashboard.jsx](file:///d:/Programming/internshipiit/Autograder_UI_Proj/autograder/src/pages/teacher/AssignmentDashboard.jsx)
*   **Route**: `/teacher/assignment/:id`
*   **Purpose**: Central hub for a specific assignment.
*   **Analytics**:
    *   **Charts**: Grade Distribution (Bar Chart), Submission Status (Pie Chart).
    *   **Stats**: Average Score, Median, Top Score, Submission Rate.
*   **Submissions List**: Filterable table (All, To Grade, Graded).
    *   Columns: Student, Status, Submission Time, Auto-Grade Score, Final Score, Action.

#### [NEW] [GradingInterface.jsx](file:///d:/Programming/internshipiit/Autograder_UI_Proj/autograder/src/pages/teacher/GradingInterface.jsx)
*   **Route**: `/teacher/grading/submission/:id`
*   **Layout**: Split Pane (Resizable?).
    *   **Left Pane**: Code Viewer (Monaco Editor or simple SyntaxHighlighter) showing student's code.
    *   **Right Pane**: Grading Tools.
        *   **Autograder Report**: Pass/Fail status of test cases, execution time, memory usage.
        *   **Rubric**: Manual criteria (e.g., Code Style, Logic) with sliders or inputs.
        *   **Feedback**: Text comments.
        *   **Score Override**: Allow teacher to adjust the final calculated grade.

#### [MODIFY] [MarksTab.jsx](file:///d:/Programming/internshipiit/Autograder_UI_Proj/autograder/src/components/features/teacher/MarksTab.jsx)
*   **Concept**: A "Master Gradebook" spreadsheet.
*   **Structure**:
    *   **Rows**: Students (sorted alphabetically).
    *   **Columns**:
        1.  **Student Info** (Name, Avatar).
        2.  **Overall Average** (Calculated percentage).
        3.  **Assignments** (Dynamic columns based on created assignments).
*   **Features**:
    *   **Visual cues**: Color-code cells (Red for missing, Green for good scores).
    *   **Interactivity**: Click a cell -> Go to `/teacher/grading/submission/:id`.
    *   **Stats**: Row at the bottom showing "Class Average" for each assignment. (e.g., "Assignment 1 Avg: 88%").


## Verification Plan

### Automated Tests
- **Linting**: Ensure `eslint` passes.
- **Build**: Run `npm run build` to verify no breaking errors.

### Manual Verification
- **Browser Preview**: I will run the dev server and use the browser tool to verify:
    - Routing works (e.g., navigating to `/teacher/dashboard` works).
    - UI aesthetics match the "Google Classroom" clean vibe.
    - Responsiveness on different viewport sizes.
#### [MODIFY] [PeopleTab.jsx](file:///d:/Programming/internshipiit/Autograder_UI_Proj/autograder/src/components/features/teacher/PeopleTab.jsx)
*   **Enhancements**:
    *   **Teachers**: List of instructors.
    *   **Students**:
        *   Full list of enrolled students.
        *   Actions: "Remove", "Email".
    *   **Invite Modal**:
        *   Triggered by `UserPlus` icon.
        *   Input field for Email Address.
        *   "Invite" button.
