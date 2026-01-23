# Technology Stack Explanation
**Why we need more than just SQLite.**

You asked about **PostgreSQL vs. SQLite**, **Redis**, and **MinIO**. Here is the breakdown of why we chose them for your **500-User Local Server**.

---

## 1. The Database: SQLite vs. PostgreSQL

| Feature | SQLite (Current) | PostgreSQL (Target) | Why it matters to YOU |
| :--- | :--- | :--- | :--- |
| **Concurrency** | **Serial** (1 writer at a time) | **Parallel** (Unlimited writers) | With 500 students, SQLite will crash with `Database Locked` errors during an exam. Postgres handles thousands of simultaneous submissions. |
| **Data Types** | Basic (Text, Int, Real) | **Advanced** (JSONB, Arrays) | We need `JSONB` to store "Test Cases" efficiently and `Arrays` for "Word Cloud Keywords" (`SubmissionAnalysis`). |
| **Connecting** | File-based access | Network Server | Allows your "Background Grader" (Python Worker) to calculate grades without blocking the Website. |

**Verdict**: SQLite is for phones and prototypes. PostgreSQL is for Production Servers.

---

## 2. The Speed Layer: Redis

**What is it?**
An in-memory database. It doesn't store data on the hard drive; it stores it in RAM. It is instant.

**What will we use it for?**
1.  **The Job Queue**: When a student clicks "Run", we don't freeze their browser. We put a generic "Ticket" in Redis. Your Python Worker picks up the ticket, runs the code, and puts the result back.
2.  **Live Leaderboards**: Redis has a data structure called `Sorted Sets`. It can rank 1,000 students by score + time in *0.001 milliseconds*. Postgres is too slow for real-time ranking.
3.  **Autosave**: Saving a draft every 30 seconds for 500 users = 16 writes/second. Redis handles this easily without touching the main disk.

---

## 3. The File Locker: MinIO

**What is it?**
A local version of "AWS S3" (Google Drive for code). It stores files.

**The "Blob" Problem:**
*   **Without MinIO**: You store 10,000 python files inside PostgreSQL `TEXT` columns. Your database backup becomes 10GB. Queries get slow.
*   **With MinIO**: You store the file in MinIO. You save a tiny string `path/to/file.py` in PostgreSQL.
*   **Benefit**: Your database stays tiny and fast. Your code files are safe on the hard drive.

---

## Summary Architecture

1.  **Frontend (React)**: "Here is my code!"
2.  **Redis**: "I'll hold this job ticket."
3.  **Worker (Python)**: "I grabbed the ticket from Redis. I'll execute the code."
4.  **MinIO**: "I'll save the code file."
5.  **PostgreSQL**: "I'll save the Grade and Analytics."
