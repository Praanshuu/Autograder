# Analytics Backend Specification

This document outlines the data structures, aggregation logic, and service requirements needed to power the **Teacher Analytics Dashboard**.

## 1. Feature: Performance Matrix (The "Effort Chart")

**UI Goal**: Visualize Student Score vs. Time Spent to identify struggling students vs. rapid performers.

### Data Requirements
**Per Submission:**
- `time_spent`: (Integer, Seconds/Minutes) Total active time the student spent on the interface before final submission.
- `attempts`: (Integer) Number of code runs/attempts before success.
- `score`: (Float) Final auto-graded score (0-100).

### Backend Logic
1.  **Time Tracking**: The backend must track the "session duration" for a specific question.
    *   *Start*: When student opens the editor for Question X.
    *   *Accumulate*: Heartbeat/Active check every min.
    *   *End*: Final submission.
2.  **API Response**:
    ```json
    {
      "student_id": "123",
      "time_spent_mins": 45,
      "score": 80
      // ...other details
    }
    ```

---

## 2. Feature: Error Heatmap (The "Correction Tool")

**UI Goal**: Show failure rates for specific test cases (e.g., "Negative Numbers") to highlight class-wide misconceptions.

### Data Requirements
**Test Case Definition (Teacher Side):**
- `test_case_id`: Unique ID.
- `description`: Human-readable label (e.g., "Negative Input Handling"). **Crucial**: This is what appears on the heatmap, not just "Test Case 3".

**Submission Results (Student Side):**
- A table linking `submission_id` -> `test_case_id` -> `passed` (Boolean).

### Backend Logic (Aggregation)
The API must return the aggregated pass rates **per question**:

```sql
-- Conceptual Logic
SELECT 
    test_case_id, 
    test_case.description,
    COUNT(CASE WHEN passed = TRUE THEN 1 END) as pass_count,
    COUNT(*) as total_attempts,
    (pass_count / total_attempts) * 100 as pass_rate_percentage
FROM submission_test_cases
WHERE assignment_id = '{id}'
GROUP BY test_case_id;
```

**Frontend Color Logic (Implemented):**
- **Green (>85%)**: Concept mastered.
- **Yellow (50-85%)**: Slight confusion.
- **Red (<50%)**: Critical misconception.

---

## 3. Feature: Approach Clusters (UMAP Strategy View)

**UI Goal**: Group students by their *code logic* (e.g., Recursive vs. Iterative) rather than just score.

### Data Requirements
**Per Submission:**
- `umap_x`: (Float) Coordinate X.
- `umap_y`: (Float) Coordinate Y.
- `cluster_label`: (String) Semantic name of the approach (e.g., "Recursive Solution", "Brute Force").

### Backend Logic (ML Pipeline)
**This requires an asynchronous ML Worker.**
1.  **Trigger**: When the assignment due date passes OR on-demand "Analyze" button.
2.  **Processing**:
    *   Fetch all successful submissions for Question X.
    *   **Preprocessing**: Abstract Syntax Tree (AST) conversion to normalize variable names (so `var a = 1` and `var b = 1` are treated as identical logic).
    *   **Embedding**: Convert code to vectors (CodeBERT or TF-IDF on AST tokens).
    *   **Dimensionality Reduction**: Run UMAP (Uniform Manifold Approximation and Projection) to reduce vectors to 2D (x, y).
    *   **Clustering**: Run DBSCAN or K-Means to find groups.
    *   **Labeling**: (Optional/Advanced) Use LLM to generate a summary name for the cluster (e.g., "Iterative").
3.  **Storage**: Save `{x, y, label}` back to the generic `Submission` record.

---

## 4. API Structure Proposal (Dashboard Data)

**GET /api/teacher/assignments/{id}/analytics**

This aggregated endpoint should return everything needed for the dashboard to avoid N+1 queries.

```json
{
  "assignment_id": "a1",
  "questions": [
    {
      "id": "q1",
      "title": "Palindrome Check",
      "avg_score": 78,
      "test_cases_analytics": [
        { "id": "tc1", "name": "Negative Inputs", "pass_rate": 28 },
        { "id": "tc2", "name": "Standard Palindrome", "pass_rate": 95 }
      ],
      "submissions_analytics": [
        {
          "student_id": "s1",
          "time_spent": 30,
          "score": 100,
          "umap_x": 0.5,
          "umap_y": -1.2,
          "cluster": "String Reversal Method"
        }
        // ... all students
      ]
    }
  ]
}
```
