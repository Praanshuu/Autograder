# Research & Logic: The Student Experience (Metacognitive Approach)

**Date:** January 11, 2026
**Topic:** Student View Architecture
**Status:** In Design

---

## 1. The Philosophy: "Thinking about Thinking"
The user explicitly rejected shallow gamification (points, streaks) in favor of **metacognition**. The goal is not to drive addiction, but to drive **understanding**.
*   **Old Model**: "You failed. Try again for points."
*   **New Model**: "Your logic diverged here. What assumption led you to this path?"

## 2. The Solution: An Interface for Inquiry
The UI must shift the student's focus from "Getting the green checkmark" to "Understanding the problem space".

### A. The Dashboard: "Concept Mastery"
Instead of a "Urgency Queue" or "Streak", we show a unique view of their **Mental Model**.
*   **Knowledge Map**: A visual graph (Node-based) showing concepts (e.g., "Loops", "Arrays", "Recursion").
    *   *State*: Nodes light up as they prove mastery. 
    *   *Feedback*: "You are strong in *Logic* but your *Edge Case Handling* needs work."
*   **"Unresolved Questions"**: A list of problems they attempted but didn't solve, framed as "Open Inquiries" rather than "Failures".

### B. The IDE: "The Debugging Partner"
The coding environment shouldn't just run code; it should help visualize execution.
*   **Visual Diffing**: If the student returns `[1, 2]` but expected `[2, 1]`, don't just say "Fail". Show the array indices visually so they *see* the sorting error.
*   **The "Rubber Duck" AI (Socratic Method)**:
    *   *Trigger*: When a test fails.
    *   *Interaction*: The system DOES NOT give the answer.
    *   *Prompt*: "It looks like your loop runs `n` times. What happens if `n` is 0? Walk me through it."
    *   *Goal*: Force the student to simulate the computer's logic in their head.

### C. The Feedback Loop: "Reflection, Not Correction"
*   **Self-Reflection Prompt**: Before revealing the solution or final grade, ask: "Where do you think you got stuck?"
    1.  "I didn't understand the question."
    2.  "I couldn't translate my idea to code."
    3.  "I missed an edge case."
    *   *Why*: This data helps the teacher diagnose *types* of failure (Conceptual vs Implementation).
*   **Logic Tracing**: Allow the student to "Step Through" execution (like a debugger) to see exactly where variable state changed unexpectedly.

## 3. Creative Features (Deep Learning)
*   **"Explain It To Me"**: A button where the student has to explain their OWN code to the AI. If the AI understands it, they pass a "Clarity Check".
*   **Counter-Example Generator**: If a student's logic is "Strings are always length > 0", the system generates a counter-example `""` (empty string) and asks "Does your code handle this?"

## 4. Technical Approach
*   **Monaco Editor**: Essential for professional feel.
*   **Client-Side Execution (Pyodide/WebAssembly)**: Run code in the browser to allow instant "Step-Through" debugging without server latency. This empowers the "Logic Tracing" feature.

## 5. Summary
The Student View should answer the question: **"What exactly is wrong with how I’m thinking?"**
It transforms the computer from a "Grader" into a "Mirror" for their own logic.
