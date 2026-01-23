# Research: Gold Standard Schemas (LeetCode/HackerRank Style)

**Context:** Designing for 500-1000 concurrent users on a powerful local server (8x GPUs).

## 1. Core Philosophy of "Code Evaluation" Systems
Platforms like LeetCode and HackerRank differ from standard CRUD apps because **Code Execution is Asynchronous and Resource Intensive**.

### Key Architectural Patterns
1.  **Immutable Submissions (The Ledger)**:
    *   **Concept**: A submission is never "updated". If a student runs code again, it's a *new* submission (or "attempt").
    *   **Why**: Allows "Approach Analysis" (how did the student improve?), "Replay" capability, and audit trails.
    *   **Schema**:
        *   `Submission` table is "Append-Only".
        *   `LatestSubmission` (optional view/table) points to the most recent one for the UI.

2.  **Versioning of Content**:
    *   **Concept**: If a teacher modifies a test case, it shouldn't retroactively break old submissions.
    *   **Schema**: `Question` table has a `version` column. Submissions link to a specific `QuestionVersion`.

3.  **Separation of "Blob" Data**:
    *   **Problem**: Storing 10MB of `console_output` or huge `input_data` in Postgres text columns bloats the DB and slows down backups/queries.
    *   **Solution**:
        *   Small metadata in DB (`status`, `execution_time`).
        *   Large content in Object Storage (e.g., MinIO/S3) or Filesystem.
        *   *For Local Server*: We can use a dedicated `blob_storage/` directory or MinIO docker container.

4.  **Async Queue (The Buffer)**:
    *   **Flow**: User Submit -> DB `status='PENDING'` -> Redis Queue -> Worker (GPU) -> DB `status='COMPLETED'`.
    *   **Why**: Prevents the DB from locking up during execution.

---

## 2. Schema Comparison

### Entity: Submissions

| Feature | Current Autograder | Gold Standard (LeetCode/HR) |
| :--- | :--- | :--- |
| **History** | **None** (Unique constraint forces overwrite) | **Full History** (One record per run) |
| **State** | Mutable (`status` changes in place) | Immutable (New row or State Machine) |
| **Code** | Stored in `TEXT` column | Reference to Blob/File (deduplicated) |
| **Result** | Direct M2M to `TestResult` | JSONB summary + Blob for full logs |

### Entity: Questions & Assignments

| Feature | Current Autograder | Gold Standard (LeetCode/HR) |
| :--- | :--- | :--- |
| **Context** | Global (`Question` has `order`) | Contextual (`AssignmentQuestion` link has `order`) |
| **Versions** | Live editing (Destructive) | Versioned (`QuestionID`, `VerID`) |
| **Tests** | `TestCase` table | `TestCase` Versioned Bundle (Zip/JSON) |

---

## 3. High-Performance Local Server Strategy (The "IIT Bhilai" Edge)
Since we are **NOT** on limited cloud VMs but on powerful GPU servers:

1.  **PostgreSQL (Dockerized) with NVMe**:
    *   Use the fast local storage.
    *   Tune `work_mem` and `shared_buffers` aggressively since we have RAM.

2.  **Redis for "Hot State"**:
    *   **Leaderboards**: Use Redis Sorted Sets (`ZADD leaderbox <score> <user>`) for O(log N) rank updates.
    *   **Autosave**: Don't hit Postgres every 30s. Write to Redis `student:1:assignment:5:code`, then flush to DB on "Submit" or "Leave Page".

3.  **GPU Utilization**:
    *   **Not for DB**: Postgres doesn't use GPUs.
    *   **For Grading**: Start **AI Grading Agents** (LLM based) on the GPUs.
    *   **Pipeline**: The "Worker" container can load a local LLM (e.g., Llama-3-8B) to give "Code Style Hints" alongside the standard deterministic tests.

---

## 4. The "Ideal" Schema Draft (Preview)

```sql
-- The "Problem" Definition (Versioned)
CREATE TABLE problems (
    id UUID PRIMARY KEY,
    title VARCHAR,
    slug VARCHAR UNIQUE,
    current_version INT
);

CREATE TABLE problem_versions (
    id UUID PRIMARY KEY,
    problem_id UUID REFERENCES problems(id),
    version INT,
    content_markdown TEXT,
    test_cases_hash VARCHAR, -- Pointer to file/blob
    created_at TIMESTAMP
);

-- The "Context" (Course/Assignment)
CREATE TABLE assignment_problems (
    assignment_id UUID,
    problem_id UUID,
    question_order INT,
    custom_points INT, -- Override global points
    PRIMARY KEY (assignment_id, problem_id)
);

-- The "Execution" (Immutable)
CREATE TABLE submissions (
    id UUID PRIMARY KEY,
    user_id UUID,
    problem_version_id UUID,
    assignment_id UUID,
    code_blob_ref VARCHAR,
    language VARCHAR,
    status VARCHAR, -- PENDING, RUNNING, AC, RE, TLE
    runtime_ms INT,
    memory_kb INT,
    created_at TIMESTAMP
    -- No huge text fields here!
);
```

## 5. Migration Logic (For Discussion)
Moving from the current schema to this "Gold Standard" is a **Major Refactor**.
*   **Phase 1**: Break the `unique_together` constraint on Submissions (Enable History).
*   **Phase 2**: Introduce `AssignmentQuestion` link table (Fix Ordering).
*   **Phase 3**: Move autosaves to Redis (Performance).
*   **Phase 4**: Migration to Postgres.
