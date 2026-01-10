# Research & Logic: Assignment Creation Workflow

**Date:** January 10, 2026
**Feature:** Assignment Configuration & Test Case Manager
**Status:** Implemented (UI)

---

## 1. The Problem: The "Config" Wall
Setting up an autograded coding assignment is traditionally terrifying. Usage of YAML files, Dockerfile configurations, or proprietary scripting languages (like in Moodle/VPL) creates a high barrier to entry. Teacher's just want to say: *"Here is the problem, here are the inputs, here are the outputs."*

## 2. The Solution: "No-Code" Test Case Manager
We built `CreateAssignment.jsx` to hide the complexity of the grading engine behind a friendly form.

### A. Visual Test Case Editor
*   **Logic**: Instead of writing a script, the teacher adds "Cases".
    *   `Input`: The arguments passed to the function.
    *   `Expected Output`: The exact return value required.
    *   `Hidden?`: A toggle to determine if students can see this case or if it's a "Secret" marking case.
*   **Benefit**: This creates a structured JSON object (`testCases array`) that the backend runner can simply parse and iterate over. No Docker knowledge required for the teacher.

### B. Drag-and-Drop Organization
*   **Interaction**: We typically use libraries like `dnd-kit` (implied in design) or simple arrow buttons to reorder questions.
*   **Why**: Curating the "Flow" of an assignment (Easy -> Hard) is a pedagogical choice. UI friction shouldn't prevent a teacher from reordering questions.

## 3. UX Decisions
*   **Review Step**: We broke the process into steps (Details -> Questions -> Settings -> Review).
    *   *Reasoning*: "Wizard" style forms reduce cognitive load. You don't see the complex settings (timeouts, memory limits) until you've finished the creative part (writing the question).
*   **Validation**: The UI prevents publishing if a question has 0 test cases. This prevents the "Broken Assignment" scenario where students submit but nothing gets graded.

## 4. Future Scope
*   **AI Generator**: Integrate an LLM to "Generate Test Cases". Teacher types "Function to add two numbers", AI auto-populates 5 test cases covering edge cases (negatives, zeros, large numbers).
*   **Language Specifics**: Currently generic. We need dropdowns for specific language templates (e.g., `public static void main` for Java vs `def solution():` for Python).
*   **Reference Solution**: Allow teachers to write a "Correct Solution" and run the test cases against it immediately to verify they are valid *before* publishing.
