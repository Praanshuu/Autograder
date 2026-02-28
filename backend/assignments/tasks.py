import logging
from celery import shared_task
from django.utils import timezone

logger = logging.getLogger(__name__)


@shared_task
def release_expired_exam_questions():
    """
    Periodic task: checks for exam assignments whose due_date has passed,
    and automatically links their questions into the PracticeQuestionLibrary.

    This task is idempotent — it uses `questions_released` to ensure it only
    processes each expired exam once.
    """
    from .models import Assignment
    from gamification.models import PracticeQuestionLibrary

    now = timezone.now()

    # Find published exams that have expired and haven't had their questions released yet
    expired_exams = Assignment.objects.filter(
        mode='exam',
        is_published=True,
        due_date__lt=now,
        questions_released=False,
    ).prefetch_related('assignmentquestion_set__question')

    total_released = 0
    exams_processed = 0

    for exam in expired_exams:
        questions = [aq.question for aq in exam.assignmentquestion_set.all()]
        released_for_this_exam = 0

        for question in questions:
            try:
                _, created = PracticeQuestionLibrary.objects.get_or_create(
                    question=question,
                    defaults={
                        'is_public': True,
                        'tags': question.tags,
                    }
                )
                if created:
                    released_for_this_exam += 1
                    logger.info(
                        f"[release_expired_exam_questions] Released question '{question.title}' "
                        f"(ID: {question.id}) from expired exam '{exam.title}' (ID: {exam.id})."
                    )
            except Exception as e:
                logger.error(
                    f"[release_expired_exam_questions] Failed to release question '{question.id}': {e}"
                )

        # Mark the exam so we never process it again
        exam.questions_released = True
        exam.save(update_fields=['questions_released'])

        total_released += released_for_this_exam
        exams_processed += 1
        logger.info(
            f"[release_expired_exam_questions] Processed exam '{exam.title}': "
            f"released {released_for_this_exam} new question(s) to the Practice Library."
        )

    if exams_processed > 0:
        logger.info(
            f"[release_expired_exam_questions] Done. {exams_processed} exam(s) processed, "
            f"{total_released} question(s) newly released."
        )
    else:
        logger.debug("[release_expired_exam_questions] No expired exams found — nothing to do.")

    return {
        'exams_processed': exams_processed,
        'questions_released': total_released,
    }
