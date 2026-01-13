# Research & Logic: Advanced Analytics (Box Plots & Word Clouds)

**Date:** January 12, 2026
**Feature**: Assignment Analytics Enhancement
**Status**: Planned

---

## 1. The Problem: "Average" isn't enough
A simple "Class Average" (e.g., 75%) hides the distribution of understanding.
*   **The "Bi-Modal" Problem**: In CS classes, it's common to have half the class get 100% and half get 0%. The average is 50%, but *nobody* actually understands 50% of the material.
*   **Pattern Blindness**: Knowing "students are struggling" is vague. Teachers need to know *what specific concepts* (e.g., Recursion, Memory Management) are causing the struggle.

## 2. The Solution: Statistical & Semantic Visualization

### A. Box Plot (The "Fairness" Check)
*   **Metric**: Grade Distribution.
*   **Visualization**: A standard statistical Box-and-Whisker plot.
    *   **Box**: The Interquartile Range (middle 50% of students).
    *   **Line**: The Median (replaces "Average" as the better metric).
    *   **Whiskers**: The range of "normal" scores.
    *   **Dots**: Outliers (Students who need immediate help or extra challenge).
*   **Goal**: If the box is tiny and high, the assignment was too easy. If the box is huge, the instructions were likely unclear.

### B. Word Cloud (Feedback Aggregator)
*   **Metric**: Frequency of phrases in Autograder Feedback.
*   **Data Source**: 
    1.  **Aggregated Feedback**: parsing the `feedback` or `stdout` logs from all student submissions.
    2.  **Tokens**: Identifying common phrases like "Index out of bounds", "Variable not defined", "Test case 3 failed".
*   **Visualization**: Size = Frequency. Color = Severity.
*   **Goal**: To let teachers see the "Voice of the Autograder" at scale. If 50% of feedback says "Memory Limit Exceeded", the teacher knows to optimize their solution or increase limits.

## 3. Creative Thought & UX Decisions
*   **Interactive Filtering**: Clicking "Timeout" in the Word Cloud should filter the Submission List below to show *only* students who got Timeouts. This connects "Analysis" to "Action".
*   **Contextual Tooltips**: Box plots are confusing to non-statisticians. We will add hover tooltips explaining "This means 50% of students scored between X and Y".

## 4. Future Scope
*   **Historical Trend**: A "Moving Box Plot" to see if the class spread is tightening (getting more consistent) over the semester.
*   **AI Summary**: "Based on the Word Cloud, it seems students are struggling with Loop Termination conditions."
