# Implementation Plan: Scalable Autograder Backend

**Goal**: Transform the current SQLite prototype into a production-ready system backed by PostgreSQL, Redis, and MinIO, implementing the **v3 Unified Schema**.

## Phase 1: Infrastructure & Environment Setup (The Foundation)
**Objective**: Get the "Big Engines" running so Django can connect to them.

1.  **Dockerize the Stack**:
    *   Create a `docker-compose.yml` file in the root.
    *   **Services**:
        *   `postgres`: Version 16 (The main DB).
        *   `redis`: Version 7 (For Cache & Queue).
        *   `minio`: S3-compatible storage (For Code Blobs).
    *   **Health Checks**: Ensure services are up before Django starts.

2.  **Django Configuration (`settings.py`)**:
    *   **Database**: Switch `DATABASES` from sqlite3 to `django.db.backends.postgresql`.
    *   **Cache**: Set `CACHES` to use `django_redis`.
    *   **Storage**: Configure `django-storages` with `s3boto3` to point to local MinIO.
    *   **Env Variables**: Use `python-decouple` or `django-environ` for secrets (DB passwords).

## Phase 2: Domain Modeling (The Schema Implementation)
**Objective**: Rewrite `models.py` files to match Schema v3.

### 1. Users App (`backend/users`)
*   **Modify**: `User` model.
*   **Add**: `role` (Enum), `avatar_url`, `settings` (JSONB).

### 2. Classes App (`backend/classes`)
*   **Modify**: `Class` model (add `settings` JSONB).
*   **New Model**: `Module` (Parent: Class).
    *   *Fields*: `title`, `order_index`.

### 3. Assignments App (`backend/assignments`) - *Major Refactor*
*   **New Model**: `ContentItem` (Polymorphic Parent).
    *   *Fields*: `title`, `description`, `is_published`, `due_date`, `type`.
*   **Refactor**: `Assignment` (Inherits ContentItem).
    *   *Add*: `mode` ('practice', 'exam'), `config` (JSONB).
*   **Refactor**: `Question` (was Question/ProblemVersion).
    *   *Simplify*: Remove versioning logic. Add `slug`.
*   **New Model**: `AssignmentQuestion` (Through Table).
    *   *Fields*: `order`, `custom_points`.

### 4. Submissions App (`backend/submissions`) - *The Engine*
*   **New Model**: `AssignmentProgress` (for Autosave).
    *   *Fields*: `current_code` (Text), `time_spent`.
*   **Refactor**: `SubmissionAttempt` (was Submission).
    *   *Change*: Make immutable. Add `code_blob_ref`, `execution_time_ms`.
*   **Refactor**: `TestResult`.
    *   *Optimize*: Use lightweight fields.

### 5. Analytics App (`backend/analytics`) - *New App*
*   **New Models**: `SubmissionAnalysis`, `ProblemAnalytics`.
*   **Purpose**: Isolate heavy-read aggregates from the transaction logs.

## Phase 3: Migration Strategy
**Objective**: Switch databases cleanly.

*   **Strategy**: "Fresh Start" is recommended given the architectural shift.
    1.  Delete old SQLite `db.sqlite3`.
    2.  Delete all `migrations/` folders (except `__init__.py`).
    3.  Run `makemigrations` and `migrate` against the new Postgres container.
    4.  Create a `seed_data` script to populate initial Users and a Demo Class.

## Phase 4: API Adaptation
**Objective**: Update Views/Serializers to respect the new models.

*   **Update Serializers**: Ensure Frontend receives the correct JSON shape (e.g., `Question` details nested inside `Assignment` view).
*   **Refactor Views**:
    *   `AssignmentViewSet`: Needs to handle the "Assignment -> AssignmentQuestion -> Question" hierarchy.
    *   `SubmissionViewSet`: Needs to write to `AssignmentProgress` on autosave and `SubmissionAttempt` on final submit.

## Execution Order
1.  **Setup**: Docker & Settings.
2.  **Core Models**: User, Class, Enrollment.
3.  **Content Models**: Module, ContentItem, Assignment, Question.
4.  **Submission Models**: Progress, Attempt, Result.
5.  **Analytics Models**: Analysis, Aggregates.
6.  **Migration**: Run & Seed.
