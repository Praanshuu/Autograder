🔥 MASTER PROMPT — AUTOGRADER LMS UI (React.js)

---

## Context & Goal

You are designing the **complete frontend UI** for a **coding-focused Learning Management System (LMS)** named **Autograder**.

This platform is inspired by:

* **Google Classroom** → class & assignment flow, clarity, simplicity
* **LeetCode** → coding environment, problem layout, editor UX

The goal is to build a **lightweight, modern, minimalistic, and intelligent UI** using **React.js**, prioritizing **ease of use**, **clarity**, and **teacher control**.

This is **NOT** a feature-heavy LMS.
This is a **focused coding LMS with delayed AI grading**.

---

## Tech Requirements

* **Framework:** React.js (functional components)
* **Routing:** React Router
* **Styling:** TailwindCSS (preferred) OR clean CSS modules
* **State:** Local state / Context (no heavy state libs)
* **Design Style:** Modern, minimal, neutral colors, intelligent spacing
* **Responsiveness:** Desktop-first, responsive layouts

---

## Core Product Philosophy

* Class → Assignment → Question → Submission is the main hierarchy
* No unnecessary analytics or dashboards
* AI (Autograder) is **teacher-triggered only**
* Students do NOT see AI feedback until teacher publishes results
* UI should feel calm, structured, and intentional

---

## USER ROLES

There are **4 roles**:

1. Admin
2. Teacher
3. Teaching Assistant (TA)
4. Student

Each role sees **only what they need**.

---

# 🧑‍🏫 TEACHER UI (MOST IMPORTANT)

Design Teacher UI first-class.

---

## Teacher Pages & Components

---

### 1. Teacher Dashboard (`/teacher/dashboard`)

**Purpose:** Entry point showing teaching workload

**UI Elements:**

* List of **Classes**
* Each Class Card shows:

  * Class name
  * Student count
  * Active assignments count
  * Pending grading indicator
* Primary CTA: `Create Class`

**Design Notes:**

* Clean cards (Google Classroom style)
* No charts, no graphs

---

### 2. Class Page (`/teacher/class/:classId`)

**Purpose:** Everything related to ONE class

#### Class Header

* Class name
* Description
* Join link (copy button)
* Semester / duration (optional)

#### Tabs inside Class Page

##### Tab 1: Assignments (Default)

* Assignment list:

  * Name
  * Deadline
  * Status (Draft / Active / Closed)
  * Submissions (X / Y)
* Actions:

  * Create Assignment
  * Edit (if not closed)

##### Tab 2: Students

* Student list:

  * Name
  * Email / ID
  * Submission summary
* Actions:

  * Remove student

##### Tab 3: TAs

* TA list
* Add / remove TA
* Permission indicator (read-only / review-only)

---

### 3. Create / Edit Assignment (`/teacher/assignment/create`)

**Purpose:** Define assignment rules

**Sections:**

* Assignment Info

  * Title
  * Instructions (Markdown)
  * Deadline
  * Late submission toggle
* Questions Section

  * List of questions
  * Add / reorder questions
* Controls:

  * Save Draft
  * Publish Assignment

---

### 4. Question Editor (`/teacher/question/create`)

**Purpose:** Create coding problems

**Sections:**

* Problem Statement
* Input / Output format
* Constraints
* Sample test cases
* Test Cases

  * Public test cases
  * Hidden test cases
* Execution rules:

  * Time limit
  * Memory limit
  * Allowed languages

---

### 5. Assignment Overview (`/teacher/assignment/:assignmentId`)

**Purpose:** Monitor assignment progress

**Displays:**

* Assignment details
* Deadline status
* Submission progress bar

**Primary Action (after deadline):**

* `Run Autograder` (Teacher-only)

---

### 6. Submissions Review Page (`/teacher/assignment/:id/submissions`)

**Purpose:** Review & grade students

**Layout:**

* Left panel:

  * Student list
  * Submission status filter
* Right panel:

  * Read-only code viewer
  * Test case summary
  * Autograder feedback (if run)
  * Manual feedback input
  * Grade input

**Actions:**

* Save feedback
* Navigate next student
* Publish results

---

### 7. Teacher Settings

* Default language
* Grading preferences
* Editor preferences

---

# 🧑‍🎓 STUDENT UI

---

### 1. Student Dashboard (`/student/dashboard`)

* Joined classes
* Active assignments
* Upcoming deadlines
* Submission status

---

### 2. Assignment Page (`/student/assignment/:id`)

* Assignment instructions
* Questions list
* Deadline
* Submission status

---

### 3. Coding Environment (`/student/code/:questionId`)

**Inspired by LeetCode**

**Layout:**

* Left:

  * Problem description
  * Constraints
* Right:

  * Code editor
  * Language selector
  * Run button
  * Submit button
* Bottom:

  * Test case output
  * Error logs

**Important:**

* NO AI feedback here
* Only test case results

---

### 4. Results Page (`/student/results/:assignmentId`)

(Visible only after teacher publishes)

* Score
* Test case summary
* Autograder feedback
* Teacher comments

---

### 5. Progress Page

* Assignments completed
* Average score
* Pending assignments

---

# 🧑‍💼 TA UI

TA uses **same pages as Teacher**, but with restrictions:

* Can view submissions
* Can add comments
* Cannot:

  * Run autograder
  * Publish grades
  * Edit assignments

No separate TA UI needed.

---

# 🛠 ADMIN UI (MINIMAL)

---

### Admin Dashboard

* User list
* Assign roles
* Create teachers

No learning flow involvement.

---

## UI / UX PRINCIPLES TO FOLLOW

* Inspired by **Google Classroom**:

  * Calm colors
  * Clear hierarchy
  * Card-based layouts
* Inspired by **LeetCode**:

  * Split-pane editor
  * Clear problem layout
* Minimal animations
* No clutter
* Strong typography
* Intelligent spacing
* Accessibility-friendly

---

## Output Expectations

* Generate:

  * Full React component structure
  * Page-wise components
  * Clean routing setup
  * Reusable UI components (Card, Tabs, Editor layout)
* Use **mock data**
* No backend logic required
* Focus on **UI correctness & flow**

---

## Final Instruction

Design this as a **production-ready frontend UI**, optimized for:

* Teachers
* Coding education
* Focused workflows
* Long-term scalability

---

