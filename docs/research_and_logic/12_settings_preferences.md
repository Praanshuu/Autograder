# Research & Logic: Settings & Preference Architecture

**Date:** January 10, 2026
**Feature**: User Settings & Notification Granularity
**Status**: Implemented

---

## 1. The Problem: "All or Nothing" Fatigue
Most LMS platforms have terrible notification settings. It's either "Email me about everything" (which leads to spam) or "Email me nothing" (which leads to missed deadlines).
*   **Cognitive Load**: Presenting 50 checkboxes to a user is overwhelming.
*   **Hidden Dependencies**: Users often don't understand that turning off "Emails" might also turn off "Password Reset" alerts in poorly designed systems.

## 2. The Solution: Hierarchical Toggle Logic
We designed the `Settings.jsx` page with a "Cascading State" approach.

### Architecture
1.  **Master Switches**:
    *   We identified high-level categories (e.g., "Email Notifications").
    *   **Logic**: This switch controls the *visibility* and *availability* of child settings.
2.  **Conditional Rendering**:
    *   `{emailNotifications && <div className="pl-6 space-y-3">...subToggles...</div>}`
    *   **Behavior**: When the Master Switch is `OFF`, the sub-options physically disappear (or collapse). This clears the UI clutter immediately for users who opt-out.
3.  **Granularity**:
    *   We broke down alerts into specific triggers: `Comments`, `Late Submissions`, `Resubmissions`. This solves the "Spam" problem by allowing teachers to mute "Late Submissions" (low priority) while keeping "Comments" (high priority) on.

## 3. Creative Thought & UX Decisions
*   **Progressive Disclosure**: We only show complex options when the user has signaled interest (by enabling the parent toggle). This keeps the page looking simple by default.
*   **Visual Hierarchy**: We used indentation and smaller typography for sub-settings to visually imply hierarchy without needing explicit labels like "Subsection 1.2".
*   **Immediate Feedback**: Toggles use the standard "Blue = On, Grey = Off" metaphor with smooth CSS transitions (`Switch` component), providing tactile satisfaction.

## 4. Future Scope & Improvements
*   **"Quiet Hours"**: Logic to pause notifications during weekends or evenings (e.g., "Do not email me between 8 PM and 7 AM").
*   **Channel Routing**: Allow users to route specific alerts to specific channels (e.g., "Send urgent alerts to SMS, standard alerts to Email").
*   **Sync with Device**: Integration with Browser Push API to bypass email entirely for desktop users.
