import logging
from celery import shared_task
from django.utils import timezone
from .models import SubmissionAttempt, TestResult
from .services import (
    execute_code,
    update_gradebook,
    award_assignment_points,
    SubmissionConfigGenerator
)

import os

logger = logging.getLogger(__name__)

# Configurable block size (submissions per task) — defaults to 50
BATCH_SIZE = int(os.environ.get('AI_BATCH_SIZE', '50'))


@shared_task
def execute_submission_task(attempt_id, language='python'):
    """
    Background task to execute student code.
    Ensures terminal status updates via robust try/except/finally block.
    """
    attempt = None
    try:
        attempt = SubmissionAttempt.objects.get(id=attempt_id)
        attempt.status = 'processing'
        attempt.save(update_fields=['status'])

        logger.info(f"--- [TASK START] Submission {attempt_id} for {attempt.student.username} ---")

        aq = attempt.assignment_question
        question = aq.question
        config = question.config or {}
        test_cases = question.test_cases or []
        code = attempt.source_code

        # Log sub-process start
        logger.info(f"[{attempt_id}] Executing {language} code in sandbox...")
        results = execute_code(code, language, test_cases, config=config)
        logger.info(f"[{attempt_id}] Sandbox execution finished.")

        passed_count = 0
        test_results_data = []
        attempt.test_results.all().delete()

        for idx, res in enumerate(results):
            status_res = res.get('status', 'fail')
            if status_res == 'pass':
                passed_count += 1

            test_result = TestResult.objects.create(
                attempt=attempt,
                test_case_id=str(idx),
                status=status_res,
                score=1 if status_res == 'pass' else 0,
                actual_output=res.get('console_output', ''),
                error_message=res.get('error_message', ''),
                execution_time_ms=res.get('execution_time', 0)
            )
            test_results_data.append({'status': status_res, 'score': test_result.score})

        # Calculate final status
        if results and passed_count == len(results):
            attempt.status = 'success'
        else:
            attempt.status = 'fail'

        # Optional: AI/Gamification/Artifacts (non-critical, fail gracefully)
        try:
            award_assignment_points(attempt, test_results_data)
        except Exception as e:
            logger.error(f"[{attempt_id}] Points failed: {e}")

        try:
            artifact_path = SubmissionConfigGenerator.save_artifacts(attempt, language)
            attempt.code_blob_ref = artifact_path
        except Exception as e:
            logger.error(f"[{attempt_id}] Artifacts failed: {e}")

        try:
            update_gradebook(attempt.student, aq.assignment)
        except Exception as e:
            logger.error(f"[{attempt_id}] Gradebook failed: {e}")

        return attempt.status

    except SubmissionAttempt.DoesNotExist:
        logger.error(f"SubmissionAttempt {attempt_id} not found in DB")
        return "not_found"
    except Exception as e:
        logger.error(f"--- [TASK CRASHED] {attempt_id}: {e} ---", exc_info=True)
        if attempt:
            attempt.status = 'error'
        return "error"
    finally:
        if attempt:
            # The critical save. Status is now guaranteed to be 'success', 'fail', or 'error'.
            attempt.save()
            logger.info(f"--- [TASK END] {attempt_id}: status={attempt.status} ---")


@shared_task(bind=True)
def analyze_assignment_ai_task(self, assignment_id, ai_task_id):
    """
    MASTER TASK: Splits submissions into batches and dispatches analyze_batch_task
    for each one in parallel. Updates AIAnalysisTask progress record.
    """
    import json
    import os
    import shutil
    from pathlib import Path
    from django.conf import settings
    from assignments.models import Assignment
    from .models import AIAnalysisTask

    try:
        assignment = Assignment.objects.get(id=assignment_id)
        ai_task = AIAnalysisTask.objects.get(id=ai_task_id)
        ai_task.status = 'running'
        ai_task.save(update_fields=['status'])

        logger.info(f"Master task starting for Assignment: {assignment.title} ({assignment_id})")

        autograder_plus_root = Path(settings.BASE_DIR).parent.parent / "Autograder_plus"
        main_script = str(autograder_plus_root / "main.py")
        venv_python = autograder_plus_root / "newgrade" / "bin" / "python"
        python_bin = str(venv_python) if venv_python.exists() else "python3"
        # If venv was created on another machine (bad interpreter), fall back to system python
        import subprocess as _sp
        try:
            _sp.run([python_bin, "--version"], capture_output=True, timeout=5, check=True)
        except (OSError, _sp.TimeoutExpired, _sp.CalledProcessError) as _e:
            logger.warning(
                f"Autograder_plus venv python failed ({_e}), using python3. "
                "Recreate the venv in Autograder_plus with: python3 -m venv newgrade"
            )
            python_bin = "python3"

        batch_task_ids = []
        total_batches = 0

        for aq in assignment.assignmentquestion_set.all():
            question = aq.question
            q_slug = question.slug

            # Get latest attempt per student for this question
            attempt_ids = list(
                SubmissionAttempt.objects
                .filter(assignment_question=aq)
                .order_by('student_id', '-created_at')
                .distinct('student_id')
                .values_list('id', flat=True)
            )

            if not attempt_ids:
                logger.info(f"No submissions for question {q_slug}, skipping.")
                continue

            # Split into batches
            batches = [attempt_ids[i:i + BATCH_SIZE] for i in range(0, len(attempt_ids), BATCH_SIZE)]

            # Prepare config for this question (shared across all its batches)
            q_config = question.config or {}
            language = q_config.get('language', 'python').lower()
            config_data = {
                "assignment_name": f"{assignment.title} - {question.title}",
                "language": language,
                "execution_mode": q_config.get('execution_mode', {'type': 'program'}),
                "test_cases": question.test_cases or [],
                "entry_point": q_config.get('entry_point'),
                "input_types": q_config.get('input_types'),
                "points": aq.custom_points if aq.custom_points is not None else question.point_value,
                "description": question.description,
            }

            staging_base = Path(settings.MEDIA_ROOT) / "ai_staging" / str(assignment_id) / q_slug

            for batch_num, batch_ids in enumerate(batches):
                batch_staging = str(staging_base / f"batch_{batch_num}")

                task = analyze_batch_task.delay(
                    assignment_id=str(assignment_id),
                    ai_task_id=str(ai_task_id),
                    attempt_ids=[str(x) for x in batch_ids],
                    config_data=config_data,
                    staging_dir=batch_staging,
                    python_bin=python_bin,
                    main_script=main_script,
                )
                batch_task_ids.append(task.id)
                total_batches += 1

        # Update record with all spawned task IDs and total batch count
        ai_task.task_ids = batch_task_ids
        ai_task.total_batches = total_batches
        ai_task.total_submissions = SubmissionAttempt.objects.filter(
            assignment_question__assignment_id=assignment_id
        ).count()
        ai_task.save(update_fields=['task_ids', 'total_batches', 'total_submissions'])

        # If no batches (no submissions), mark completed immediately
        if total_batches == 0:
            ai_task.status = 'completed'
            ai_task.save(update_fields=['status'])
            logger.info(f"Master task done: no submissions for {assignment_id}, marked completed.")
        else:
            logger.info(f"Master task done: spawned {total_batches} batch tasks for {assignment_id}")
        return f"Spawned {total_batches} batches"

    except Exception as e:
        logger.error(f"Master task failed for {assignment_id}: {e}", exc_info=True)
        try:
            ai_task = AIAnalysisTask.objects.get(id=ai_task_id)
            ai_task.status = 'failed'
            ai_task.error_message = str(e)
            ai_task.save(update_fields=['status', 'error_message'])
        except Exception:
            pass
        return "failed"


@shared_task
def analyze_batch_task(assignment_id, ai_task_id, attempt_ids, config_data,
                       staging_dir, python_bin, main_script):
    """
    WORKER TASK: Processes one batch of submissions.
    Stages files, runs Autograder+ pipeline, parses results, updates DB.
    """
    import subprocess
    import json
    import shutil
    from pathlib import Path
    from .models import AIAnalysisTask

    staging_path = Path(staging_dir)

    try:
        # Check if cancelled before starting
        ai_task = AIAnalysisTask.objects.get(id=ai_task_id)
        if ai_task.status == 'cancelled':
            logger.info(f"Batch skipped — task {ai_task_id} was cancelled")
            return "cancelled"

        language = config_data.get('language', 'python')
        ext_map = {'python': '.py', 'c': '.c', 'java': '.java'}
        target_ext = ext_map.get(language, '.py')
        target_filename = "Main.java" if language == 'java' else f"main{target_ext}"

        # Set up staging directory (ignore permission errors on leftover dirs from other runs)
        if staging_path.exists():
            shutil.rmtree(staging_path, ignore_errors=True)
        staging_path.mkdir(parents=True, exist_ok=True)
        submissions_dir = staging_path / "submissions"
        submissions_dir.mkdir()

        # Write submission files
        attempts = SubmissionAttempt.objects.filter(id__in=attempt_ids).select_related('student')
        id_to_attempt = {str(a.id): a for a in attempts}

        for attempt_id in attempt_ids:
            attempt = id_to_attempt.get(attempt_id)
            if not attempt:
                continue
            student_dir = submissions_dir / attempt.student.username
            student_dir.mkdir(exist_ok=True)
            with open(student_dir / target_filename, 'w') as f:
                f.write(attempt.source_code or '')

        # Write config
        config_path = staging_path / "config.json"
        with open(config_path, 'w') as f:
            json.dump(config_data, f, indent=2)

        output_dir = staging_path / "reports"
        cmd = [
            python_bin, main_script, "grade",
            "--assignment-config", str(config_path),
            "--submissions-dir", str(submissions_dir),
            "--output-dir", str(output_dir),
            "--level", "full",
        ]

        logger.info(f"Running pipeline for batch {staging_path.name}")

        # Limit the subprocess virtual address space.
        # Configurable via AI_MEMORY_LIMIT_MB env var (default: 0 = No Limit).
        # If main.py exceeds this limit it receives SIGKILL — only the subprocess
        # dies; Daphne and Celery workers are completely unaffected.
        _mem_limit_mb = int(os.environ.get('AI_MEMORY_LIMIT_MB', '0'))
        
        if _mem_limit_mb > 0:
            logger.info(f"[{staging_path.name}] Memory limit: {_mem_limit_mb} MB (set AI_MEMORY_LIMIT_MB to 0 to disable)")
        else:
            logger.info(f"[{staging_path.name}] Memory limit: DISABLED (Using full system RAM. Set AI_MEMORY_LIMIT_MB to enable)")

        def _limit_memory():
            if _mem_limit_mb > 0:
                import resource
                _mem_limit_bytes = _mem_limit_mb * 1024 * 1024
                resource.setrlimit(resource.RLIMIT_AS, (_mem_limit_bytes, _mem_limit_bytes))

        # Configurable timeout
        ai_timeout = int(os.environ.get('AI_TIMEOUT_SECONDS', '900'))  # Default 15 minutes per batch

        sub_result = None
        try:
            sub_result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=ai_timeout,
                preexec_fn=_limit_memory if _mem_limit_mb > 0 else None,
            )
        except subprocess.TimeoutExpired:
            logger.error(
                f"[{staging_path.name}] TIMEOUT — batch exceeded {ai_timeout}s hard limit. "
                f"Increase AI_TIMEOUT_SECONDS or reduce AI_BATCH_SIZE."
            )
        except OSError as os_err:
            logger.error(
                f"[{staging_path.name}] Subprocess failed to run. "
                f"Error: {os_err}. "
                f"If you see 'bad interpreter', recreate Autograder_plus venv: cd Autograder_plus && python3 -m venv newgrade && newgrade/bin/pip install -r requirements.txt"
            )

        saved_count = 0
        if sub_result is not None:
            if sub_result.returncode != 0:
                logger.error(
                    f"[{staging_path.name}] PIPELINE FAILED — exit code {sub_result.returncode}. "
                    f"stderr: {sub_result.stderr[:800]}"
                )
            else:
                # Parse results and save to DB
                results_file = output_dir / "results.json"
                if results_file.exists():
                    with open(results_file, 'r') as f:
                        results_data = json.load(f)

                    for item in results_data:
                        student_username = item.get("student_id")
                        if not student_username:
                            continue
                        try:
                            attempt = next(
                                a for a in attempts if a.student.username == student_username
                            )
                            analysis_data = item.get("analysis", {})
                            if item.get("error_processing"):
                                analysis_data["error"] = item["error_processing"]
                            attempt.ai_analysis_data = analysis_data
                            attempt.save(update_fields=['ai_analysis_data'])
                            saved_count += 1
                        except StopIteration:
                            logger.warning(
                                f"[{staging_path.name}] No attempt found for student '{student_username}' — skipping."
                            )
                else:
                    logger.error(
                        f"[{staging_path.name}] MISSING results.json — pipeline ran but produced no output. "
                        f"Check {output_dir} for partial files."
                    )

        if saved_count == 0:
            logger.warning(
                f"[{staging_path.name}] saved_count=0 — no submissions were written to DB for this batch. "
                f"Possible causes: subprocess OOM/timeout, empty results.json, or all student IDs unmatched."
            )
        else:
            logger.info(f"[{staging_path.name}] Saved {saved_count}/{len(attempt_ids)} submissions to DB.")

        # Atomically increment completed_batches.
        # Use saved_count (actual DB saves) so the analyzed counter stays accurate.
        from django.db.models import F
        AIAnalysisTask.objects.filter(id=ai_task_id).update(
            completed_batches=F('completed_batches') + 1,
            analyzed=F('analyzed') + saved_count,
        )

        # Check if all batches done → mark completed
        ai_task.refresh_from_db()
        if ai_task.completed_batches >= ai_task.total_batches and ai_task.status == 'running':
            ai_task.status = 'completed'
            ai_task.save(update_fields=['status'])
            logger.info(f"All batches done for ai_task {ai_task_id}")

        # Clean up staging
        shutil.rmtree(staging_path, ignore_errors=True)
        return "success"

    except Exception as e:
        logger.error(f"Batch task failed ({staging_dir}): {e}", exc_info=True)
        from django.db.models import F
        AIAnalysisTask.objects.filter(id=ai_task_id).update(
            completed_batches=F('completed_batches') + 1,
        )
        
        # Ensure task completion check runs even if this batch errored out!
        # Otherwise, if the last batch throws, the task stays 'running' forever.
        try:
            ai_task.refresh_from_db()
            if ai_task.completed_batches >= ai_task.total_batches and ai_task.status == 'running':
                ai_task.status = 'completed'
                ai_task.save(update_fields=['status'])
                logger.info(f"All batches done (with some errors) for ai_task {ai_task_id}")
        except Exception as db_err:
            logger.error(f"Failed to update task status on batch error: {db_err}")

        shutil.rmtree(staging_path, ignore_errors=True)
        return "error"
