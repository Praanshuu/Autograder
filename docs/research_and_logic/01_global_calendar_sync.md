# Research & Logic: Global Calendar & Stream Integration

**Date:** January 10, 2026
**Feature**: Global Teacher Calendar & Class Stream Sync
**Status**: Implemented

---

## 1. The Problem: Data Isolation
In the initial architecture, the "Upcoming Work" section in the `StreamTab.jsx` component was isolated. It relied on a hardcoded array (`const upcomingWork = [...]`) defined *inside* the component. 

**Issues with this approach:**
*   **Redundancy**: A separate Calendar page would need its own copy of assignment data.
*   **Sync Failure**: Creating an assignment in the "Calendar" would not automatically reflect in the "Stream" of a class, requiring manual double-entry or complex state management.
*   **Scalability**: Adding a new class or assignment would require modifying multiple files.

## 2. The Solution: "Single Source of Truth" Pattern
We adopted a centralized data approach to ensure consistency across the application.

### Architecture
1.  **Central Database (`src/mocks/calendar.js`)**:
    *   We "lifted" the data out of the components into a shared module.
    *   This file exports `MOCK_EVENTS`, which serves as the single source of truth for all time-based items (Assignments, Exams, Quizzes).
    *   **Key Data Field**: `classId`. This acts as the foreign key linking an event to a specific class.

2.  **The Consumer (`StreamTab.jsx`)**:
    *   Instead of owning data, it now *subscribes* to the global data.
    *   **Logic**: It uses the URL parameter (`classId`) to strictly filter the global list.
    *   `const classEvents = MOCK_EVENTS.filter(event => event.classId === currentClassId)`
    *   **Benefit**: The component becomes reusable. It renders different data depending on which class route is active.

3.  **The Aggregator (`TeacherCalendar.jsx`)**:
    *   This page consumes the *entire* `MOCK_EVENTS` array without filtering.
    *   It aggregates data from all classes to provide a master view for the teacher.

## 3. Creative Thought & UX Decisions
*   **"Hub and Spoke" Syncing**: By making the `calendar.js` the hub, the "Class Stream" (spoke) and "Global Calendar" (hub view) are always in perfect sync. This reduces mental load for the teacher—they trust that if they see it in one place, it exists in the other.
*   **Contextual Filtering**: We realized that while a global view is good for planning, a class view must be focused. The strict filtering in `StreamTab` ensures students/teachers don't get distracted by "Noise" from other classes when context-switching.
*   **Visual Continuity**: We aligned the visual language (color coding for Quiz/Exam/Assignment) across both the Dashboard chips and the Calendar events to create a cohesive experience.

## 4. Future Scope & Improvements
*   **Drag-and-Drop Rescheduling**: In the future, dragging an event on the Calendar page should update its `date` in the store, which would immediately update the "Due Date" displayed on the Stream tab.
*   **Two-Way Interaction**: Clicking an event in the Stream could open the specific day on the Calendar, or vice-versa (clicking in Calendar opens the Assignment Dashboard).
*   **Backend Integration**: The `MOCK_EVENTS` array is a direct blueprint for a database table `Events` or `Assignments`. The `classId` field maps directly to a Relational Database schema.
