from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from submissions.models import SubmissionAttempt
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Cleans up submissions stuck in "processing" for more than 10 minutes.'

    def handle(self, *args, **options):
        threshold = timezone.now() - timedelta(minutes=10)
        
        stale_submissions = SubmissionAttempt.objects.filter(
            status='processing',
            created_at__lt=threshold
        )
        
        count = stale_submissions.count()
        if count > 0:
            logger.info(f"Found {count} stale submissions. Marking as error.")
            stale_submissions.update(
                status='error', 
                feedback_text="[System Recovery] Submission timed out during background processing."
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully recovered {count} stale submissions.'))
        else:
            self.stdout.write(self.style.SUCCESS('No stale submissions found.'))
