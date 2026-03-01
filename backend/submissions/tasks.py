import logging
import os
import json
import shutil
import subprocess
from pathlib import Path

from celery import shared_task
from django.db.models import F
from django.utils import timezone

from .models import SubmissionAttempt, TestResult
from .services import (
    execute_code,
    update_gradebook,
    award_assignment_points,
    SubmissionConfigGenerator,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helper: resolve the Autograder_plus python binary (prefers venv)
# ---------------------------------------------------------------------------

def _resolve_python_bin(autograder_plus_root: Path) -> str:
    """
    Return the python executable to use for Autograder_plus.
    Priority:
      1. venv at <root>/newgrade/bin/python
      2. system python3
    A quick --version probe ensures the interpreter actually works.
    """
    venv_python = autograder_plus_root / "newgrade" / "bin" / "python"
    candidate = str(venv_python) if venv_python.exists() else "python3"

    try:
        subprocess.run(
            [candidate, "--version"],
            capture_output=True,
            timeout=5,
            check=True,
        )
        return candidate
    except (OSError, subprocess.TimeoutExpired, subprocess.CalledProcessError) as exc:
        logger.warning(
            f"Autograder_plus venv python failed ({exc}), falling back to python3. "
            "Recreate the venv: cd Autograder_plus && python3 -m venv newgrade && "
            "newgrade/bin/pip install -r requirements.txt"
        )
        return "python3"


# ---------------------------------------------------------------------------
# Regular code-execution task (unchanged logic, kept here for completeness)
# ---------------------------------------------------------------------------

@shared_task
def execute_submission_task(attempt_id, language="python"):
    """
    Background task to execute student code.
    Ensures terminal status updates via robust try/except/finally block.
    """
    attempt = None
    try:
        attempt = SubmissionAttempt.objects.get(id=attempt_id)
        attempt.status = "processing"
        attempt.save(update_fields=["status"])

        logger.info(f"--- [TASK START] Submission {attempt_id} for {attempt.student.username} ---")

        aq = attempt.assignment_question
        question = aq.question
        config = question.config or {}
        test_cases = question.test_cases or []
        code = attempt.source_code

        logger.info(f"[{attempt_id}] Executing {language} code in sandbox...")
        results = execute_code(code, language, test_cases, config=config)
        logger.info(f"[{attempt_id}] Sandbox execution finished.")

        passed_count = 0
        test_results_data = []
        attempt.test_results.all().delete()

        for idx, res in enumerate(results):
            status_res = res.get("status", "fail")
            if status_res == "pass":
                passed_count += 1

            test_result = TestResult.objects.create(
                attempt=attempt,
                test_case_id=str(idx),
                status=status_res,
                score=1 if status_res == "pass" else 0,
                actual_output=res.get("console_output", ""),
                error_message=res.get("error_message", ""),
                execution_time_ms=res.get("execution_time", 0),
            )
            test_results_data.append({"status": status_res, "score": test_result.score})

        attempt.status = "success" if results and passed_count == len(results) else "fail"

        try:
            award_assignment_points(attempt, test_results_data)
        except Exception as exc:
            logger.error(f"[{attempt_id}] Points failed: {exc}")

        try:
            artifact_path = SubmissionConfigGenerator.save_artifacts(attempt, language)
            attempt.code_blob_ref = artifact_path
        except Exception as exc:
            logger.error(f"[{attempt_id}] Artifacts failed: {exc}")

        try:
            update_gradebook(attempt.student, aq.assignment)
        except Exception as exc:
            logger.error(f"[{attempt_id}] Gradebook failed: {exc}")

        return attempt.status

    except SubmissionAttempt.DoesNotExist:
        logger.error(f"SubmissionAttempt {attempt_id} not found in DB")
        return "not_found"
    except Exception as exc:
        logger.error(f"--- [TASK CRASHED] {attempt_id}: {exc} ---", exc_info=True)
        if attempt:
            attempt.status = "error"
        return "error"
    finally:
        if attempt:
            attempt.save()
            logger.info(f"--- [TASK END] {attempt_id}: status={attempt.status} ---")


# ---------------------------------------------------------------------------
# MASTER TASK — splits work per-question and spawns one worker per question
# ---------------------------------------------------------------------------

@shared_task(bind=True)
def analyze_assignment_ai_task(self, assignment_id, ai_task_id):
    """
    MASTER TASK: For each question in the assignment, collects the latest
    submission from every student and dispatches a single `analyze_question_ai_task`
    worker.  One worker = one question = one pipeline run (the heavy model is
    loaded only once per question batch).
    """
    from django.conf import settings
    from assignments.models import Assignment
    from .models import AIAnalysisTask

    try:
        assignment = Assignment.objects.get(id=assignment_id)
        ai_task = AIAnalysisTask.objects.get(id=ai_task_id)
        ai_task.status = "running"
        ai_task.save(update_fields=["status"])

        logger.info(f"[MASTER] Starting for assignment: {assignment.title} ({assignment_id})")

        autograder_plus_root = Path(settings.BASE_DIR).parent.parent / "Autograder_plus"
        main_script = str(autograder_plus_root / "main.py")
        python_bin = _resolve_python_bin(autograder_plus_root)

        question_task_ids = []
        total_questions = 0

        for aq in assignment.assignmentquestion_set.select_related("question"):
            question = aq.question

            # Latest attempt per student for this question
            attempt_ids = list(
                SubmissionAttempt.objects
                .filter(assignment_question=aq)
                .order_by("student_id", "-created_at")
                .distinct("student_id")
                .values_list("id", flat=True)
            )

            if not attempt_ids:
                logger.info(f"[MASTER] No submissions for question '{question.slug}', skipping.")
                continue

            # Build the config that Autograder_plus expects — use question.config directly.
            # We only add the extra fields that the pipeline *actually* reads.
            q_config = question.config or {}
            pipeline_config = {
                # Fields the Ingestor / pipeline uses:
                "assignment_id": f"{assignment_id}_{question.slug}",
                "language": q_config.get("language", "python").lower(),
                "question": question.description,
                "test_cases": question.test_cases or [],
                # Keep every field from question.config as-is (entry_point, execution_mode, etc.)
                **q_config,
            }

            staging_dir = str(
                Path(settings.MEDIA_ROOT) / "ai_staging" / str(assignment_id) / question.slug
            )

            task = analyze_question_ai_task.apply_async(
                kwargs=dict(
                    assignment_id=str(assignment_id),
                    ai_task_id=str(ai_task_id),
                    attempt_ids=[str(x) for x in attempt_ids],
                    pipeline_config=pipeline_config,
                    staging_dir=staging_dir,
                    python_bin=python_bin,
                    main_script=main_script,
                    question_slug=question.slug,
                ),
                queue="ai_analysis",  # dedicated queue — ignored by old zombie workers
            )
            question_task_ids.append(task.id)
            total_questions += 1

        # Update task record with totals
        ai_task.task_ids = question_task_ids
        ai_task.total_batches = total_questions          # 1 batch = 1 question
        ai_task.total_submissions = SubmissionAttempt.objects.filter(
            assignment_question__assignment_id=assignment_id
        ).count()
        ai_task.save(update_fields=["task_ids", "total_batches", "total_submissions"])

        if total_questions == 0:
            ai_task.status = "completed"
            ai_task.save(update_fields=["status"])
            logger.info(f"[MASTER] No questions with submissions — marked completed immediately.")
        else:
            logger.info(f"[MASTER] Spawned {total_questions} question workers for {assignment_id}.")

        return f"Spawned {total_questions} question workers"

    except Exception as exc:
        logger.error(f"[MASTER] Failed for {assignment_id}: {exc}", exc_info=True)
        try:
            ai_task = AIAnalysisTask.objects.get(id=ai_task_id)
            ai_task.status = "failed"
            ai_task.error_message = str(exc)
            ai_task.save(update_fields=["status", "error_message"])
        except Exception:
            pass
        return "failed"


# ---------------------------------------------------------------------------
# QUESTION WORKER — stages files, runs pipeline once, persists results
# ---------------------------------------------------------------------------

@shared_task
def analyze_question_ai_task(
    assignment_id,
    ai_task_id,
    attempt_ids,
    pipeline_config,
    staging_dir,
    python_bin,
    main_script,
    question_slug,
):
    """
    WORKER TASK: Runs the Autograder+ pipeline for all submissions of ONE question.
    - Stages student files under <staging_dir>/submissions/<username>/
    - Writes a single config.json (built directly from the DB question config)
    - Invokes Autograder+ once (with the newgrade venv python)
    - Reads results.json and bulk-updates SubmissionAttempt.ai_analysis_data
    """
    from .models import AIAnalysisTask

    staging_path = Path(staging_dir)
    log_lines = []  # collected for the admin UI

    def _log(msg: str):
        """Log to Django logger AND accumulate for DB."""
        logger.info(msg)
        log_lines.append(msg)

    try:
        # ── Cancellation guard ─────────────────────────────────────────────
        ai_task = AIAnalysisTask.objects.get(id=ai_task_id)
        if ai_task.status == "cancelled":
            _log(f"[{question_slug}] Skipped — task was cancelled.")
            return "cancelled"

        # ── Language / file naming ─────────────────────────────────────────
        language = pipeline_config.get("language", "python").lower()
        ext_map = {"python": ".py", "c": ".c", "java": ".java"}
        target_ext = ext_map.get(language, ".py")
        target_filename = "Main.java" if language == "java" else f"main{target_ext}"

        # ── Set up clean staging directory ─────────────────────────────────
        if staging_path.exists():
            shutil.rmtree(staging_path, ignore_errors=True)
        staging_path.mkdir(parents=True, exist_ok=True)
        submissions_dir = staging_path / "submissions"
        submissions_dir.mkdir()

        # ── Write student submission files ─────────────────────────────────
        attempts = (
            SubmissionAttempt.objects
            .filter(id__in=attempt_ids)
            .select_related("student")
        )
        id_to_attempt = {str(a.id): a for a in attempts}

        for attempt_id in attempt_ids:
            attempt = id_to_attempt.get(attempt_id)
            if not attempt:
                continue
            student_dir = submissions_dir / attempt.student.username
            student_dir.mkdir(exist_ok=True)
            (student_dir / target_filename).write_text(attempt.source_code or "")

        staged_count = len([a for a in id_to_attempt.values()])
        _log(f"[{question_slug}] Staged {staged_count} submissions.")

        # ── Write config.json (from DB — no manual re-mapping) ────────────
        config_path = staging_path / "config.json"
        config_path.write_text(json.dumps(pipeline_config, indent=2))

        # ── Build and run the pipeline subprocess ─────────────────────────
        output_dir = staging_path / "reports"
        output_dir.mkdir(exist_ok=True)

        ai_timeout = int(os.environ.get("AI_TIMEOUT_SECONDS", "900"))

        # Memory limit (optional, default off)
        mem_limit_mb = int(os.environ.get("AI_MEMORY_LIMIT_MB", "0"))

        def _limit_memory():
            if mem_limit_mb > 0:
                import resource
                limit = mem_limit_mb * 1024 * 1024
                resource.setrlimit(resource.RLIMIT_AS, (limit, limit))

        cmd = [
            python_bin, main_script, "grade",
            "--assignment-config", str(config_path),
            "--submissions-dir", str(submissions_dir),
            "--output-dir", str(output_dir),
            "--level", "full",
        ]

        _log(f"[{question_slug}] Running: {' '.join(cmd)}")

        # Build a clean env for the subprocess:
        # - PYTORCH_CUDA_ALLOC_CONF: prevents OOM by enabling PyTorch's expandable
        #   segment allocator — instead of crashing, it reuses fragmented GPU memory.
        subprocess_env = os.environ.copy()
        subprocess_env["PYTORCH_CUDA_ALLOC_CONF"] = os.environ.get(
            "PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True"
        )

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=ai_timeout,
                preexec_fn=_limit_memory if mem_limit_mb > 0 else None,
                cwd=str(Path(main_script).parent),  # run from Autograder_plus root
                env=subprocess_env,
            )
        except subprocess.TimeoutExpired:
            _log(
                f"[{question_slug}] TIMEOUT — exceeded {ai_timeout}s. "
                "Increase AI_TIMEOUT_SECONDS or reduce question batch size."
            )
            result = None
        except OSError as oserr:
            _log(
                f"[{question_slug}] OSError launching subprocess: {oserr}. "
                "If 'bad interpreter' — recreate venv: cd Autograder_plus && "
                "python3 -m venv newgrade && newgrade/bin/pip install -r requirements.txt"
            )
            result = None

        # ── Parse and persist results ──────────────────────────────────────
        saved_count = 0
        if result is not None:
            if result.returncode != 0:
                _log(
                    f"[{question_slug}] Pipeline exited with code {result.returncode}. "
                    f"stderr: {result.stderr[:800]}"
                )
            else:
                # Capture pipeline stdout for admin viewer
                if result.stdout:
                    for line in result.stdout.splitlines():
                        _log(f"  {line}")

                results_file = output_dir / "results.json"
                if results_file.exists():
                    results_data = json.loads(results_file.read_text())

                    # Bulk update using a mapping for efficiency
                    update_map = {
                        item["student_id"]: item.get("analysis", {})
                        for item in results_data
                        if item.get("student_id")
                    }
                    if item_error := {
                        item["student_id"]: item["error_processing"]
                        for item in results_data
                        if item.get("error_processing") and item.get("student_id")
                    }:
                        for sid, err in item_error.items():
                            if sid in update_map:
                                update_map[sid]["error"] = err

                    for attempt in attempts:
                        uname = attempt.student.username
                        if uname in update_map:
                            attempt.ai_analysis_data = update_map[uname]
                            attempt.save(update_fields=["ai_analysis_data"])
                            saved_count += 1

                    _log(f"[{question_slug}] Saved {saved_count}/{len(attempt_ids)} results to DB.")
                else:
                    _log(
                        f"[{question_slug}] results.json not found in {output_dir}. "
                        "Pipeline ran but produced no output — check Autograder_plus logs."
                    )

                # Persist the interactive UMAP HTML plot if generated
                try:
                    from django.conf import settings
                    from django.utils.text import slugify
                    from assignments.models import AssignmentQuestion, Assignment

                    assignment = Assignment.objects.get(id=assignment_id)
                    assignment_slug = f"{slugify(assignment.title)}-{str(assignment.id)[:8]}"

                    html_files = list(output_dir.glob("interactive_embeddings_*.html"))
                    if html_files:
                        html_src = html_files[0]
                        # Target location: MEDIA_ROOT/ai_reports/<assignment_slug>/<question_slug>_umap.html
                        reports_dir = Path(settings.MEDIA_ROOT) / "ai_reports" / assignment_slug
                        reports_dir.mkdir(parents=True, exist_ok=True)
                        html_dest = reports_dir / f"{question_slug}_umap.html"
                        shutil.copy2(html_src, html_dest)
                        
                        relative_url = f"/media/ai_reports/{assignment_slug}/{html_dest.name}"
                        _log(f"[{question_slug}] Saved interactive map to {relative_url}")
                        
                        AssignmentQuestion.objects.filter(
                            assignment_id=assignment_id,
                            question__slug=question_slug
                        ).update(umap_url=relative_url)
                except Exception as eval_exc:
                    _log(f"[{question_slug}] WARNING: Failed to copy interactive map: {eval_exc}")

        if saved_count == 0 and result is not None and result.returncode == 0:
            _log(f"[{question_slug}] WARNING: saved_count=0 despite successful run.")

    except Exception as exc:
        logger.error(f"[{question_slug}] Worker crashed: {exc}", exc_info=True)
        _log(f"[{question_slug}] CRASH: {exc}")
    finally:
        # ── Always update progress + append logs ──────────────────────────
        try:
            AIAnalysisTask.objects.filter(id=ai_task_id).update(
                completed_batches=F("completed_batches") + 1,
                analyzed=F("analyzed") + saved_count,
            )

            # Append logs to the JSONField so admin UI can display them
            _append_logs_to_task(ai_task_id, log_lines)

            # Check if all question workers have finished
            ai_task.refresh_from_db()
            if (
                ai_task.completed_batches >= ai_task.total_batches
                and ai_task.status == "running"
            ):
                ai_task.status = "completed"
                ai_task.save(update_fields=["status"])
                logger.info(f"[{question_slug}] All question workers done — marked completed.")

        except Exception as db_exc:
            logger.error(f"[{question_slug}] DB update in finally block failed: {db_exc}")

        # ── Clean up staging directory ─────────────────────────────────────
        shutil.rmtree(staging_path, ignore_errors=True)


# ---------------------------------------------------------------------------
# Helper: append log lines atomically using a PostgreSQL array append
# ---------------------------------------------------------------------------

def _append_logs_to_task(ai_task_id: str, lines: list[str]):
    """
    Appends log_lines to AIAnalysisTask.log_output using a PostgreSQL
    JSONField array concat so concurrent workers don't overwrite each other.
    Falls back to a read-modify-write if the DB doesn't support the shorthand.
    """
    from .models import AIAnalysisTask
    from django.db.models.expressions import RawSQL

    if not lines:
        return

    try:
        # PostgreSQL-specific: concatenate arrays at DB level
        AIAnalysisTask.objects.filter(id=ai_task_id).update(
            log_output=RawSQL(
                "log_output || %s::jsonb",
                [json.dumps(lines)],
            )
        )
    except Exception:
        # Fallback for non-Postgres or any error
        try:
            task = AIAnalysisTask.objects.get(id=ai_task_id)
            task.log_output = (task.log_output or []) + lines
            task.save(update_fields=["log_output"])
        except Exception as exc:
            logger.warning(f"Could not append logs to task {ai_task_id}: {exc}")
