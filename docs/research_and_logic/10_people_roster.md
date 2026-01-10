# Research & Logic: People & Roster Management

**Date:** January 10, 2026
**Feature**: Class Roster (People Tab)
**Status**: Implemented

---

## 1. The Problem: Static Lists & Onboarding Friction
Getting students *into* a class is often the biggest hurdle at the start of a semester. Static lists without interaction make management difficult.
*   **Enrollment Chaos**: "How do I join?" is the #1 question teachers get.
*   **Role Ambiguity**: Mixing TAs, Teachers, and Students in one list confuses authority/permissions.

## 2. The Solution: Role-Segregated Management
We implemented a clean, role-defined roster view (`PeopleTab.jsx`) with integrated onboarding tools.

### Architecture
1.  **Sectioning**:
    *   We enforced a hard visual separation between **Teachers** (Top) and **Students** (Bottom).
    *   **Rationale**: Security and Authority. It must be visually obvious who has "God Mode" (Grading rights).
2.  **Invite Flow**:
    *   **Modal-Based**: Clicking "Add Student" opens a Dialog (`InviteModal`).
    *   **Dual-Method**: We support both "Email Invite" (push) and "Copy Link" (pull), covering both use cases (inviting specific people vs. posting a link on a syllabus).

## 3. Creative Thought & UX Decisions
*   **Human-Centric UI**: We used large Avatars (`AvatarImage`) and full names. In a remote learning environment, seeing faces (even placeholders) builds community better than a spreadsheet of Student IDs.
*   **Contextual Actions on Hover**: The "Remove" or "Email" buttons often clutter a list. We implemented a logical group where actions are subtle until needed, keeping the interface clean.
*   **Stats Integration**: Next to each student, we display their "Class Average". This turns the roster into a "Health Monitor" rather than just a phonebook.

## 4. Future Scope & Improvements
*   **Bulk Import**: Drag-and-drop a CSV file to invite 100 students at once.
*   **Groups/Teams**: Allow teachers to drag students into "Project Groups" directly within this interface.
*   **Permissions**: A "TA" role with limited rights (e.g., "Can grade, cannot delete class").
