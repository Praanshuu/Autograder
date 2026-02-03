"""
Management command to recalculate points for all users.

This command is useful for:
- Fixing point inconsistencies
- Updating points after algorithm changes
- Initial point calculation for existing users
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction, models
from gamification.points_calculator import PointsCalculator
from gamification.models import UserPoints, PracticeSubmission
import logging

logger = logging.getLogger(__name__)
User = get_user_model()


class Command(BaseCommand):
    help = 'Recalculate points for all users or specific users'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--user',
            type=str,
            help='Username to recalculate points for (if not provided, recalculates for all users)'
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be changed without making actual changes'
        )
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Show detailed output for each user'
        )
    
    def handle(self, *args, **options):
        calculator = PointsCalculator()
        
        # Determine which users to process
        if options['user']:
            try:
                users = [User.objects.get(username=options['user'])]
                self.stdout.write(f"Recalculating points for user: {options['user']}")
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"User '{options['user']}' not found")
                )
                return
        else:
            users = User.objects.filter(role='student')
            self.stdout.write(f"Recalculating points for {users.count()} users")
        
        total_updated = 0
        total_points_changed = 0
        
        for user in users:
            try:
                # Get current points
                try:
                    current_points = UserPoints.objects.get(user=user)
                    old_total = current_points.total_points
                    old_practice = current_points.practice_points
                    old_assignment = current_points.assignment_points
                except UserPoints.DoesNotExist:
                    old_total = old_practice = old_assignment = 0
                
                if not options['dry_run']:
                    # Recalculate points
                    updated_summary = calculator.recalculate_user_points(user)
                    new_total = updated_summary['total_points']
                    new_practice = updated_summary['practice_points']
                    new_assignment = updated_summary['assignment_points']
                else:
                    # Dry run - calculate what would change
                    practice_points = PracticeSubmission.objects.filter(
                        student=user,
                        status='success'
                    ).aggregate(
                        total=models.Sum('points_earned')
                    )['total'] or 0
                    
                    new_practice = practice_points
                    new_assignment = old_assignment  # Not recalculating assignments in dry run
                    new_total = new_practice + new_assignment
                
                # Check if points changed
                points_changed = (
                    old_total != new_total or 
                    old_practice != new_practice or 
                    old_assignment != new_assignment
                )
                
                if points_changed:
                    total_updated += 1
                    total_points_changed += abs(new_total - old_total)
                    
                    status_style = self.style.SUCCESS if new_total >= old_total else self.style.WARNING
                    
                    if options['verbose'] or points_changed:
                        self.stdout.write(
                            status_style(
                                f"{'[DRY RUN] ' if options['dry_run'] else ''}"
                                f"{user.username}: "
                                f"Total {old_total} -> {new_total} "
                                f"(Practice: {old_practice} -> {new_practice}, "
                                f"Assignment: {old_assignment} -> {new_assignment})"
                            )
                        )
                elif options['verbose']:
                    self.stdout.write(f"{user.username}: No changes needed")
                    
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Error processing {user.username}: {e}"
                    )
                )
                logger.error(f"Error recalculating points for {user.username}: {e}", exc_info=True)
        
        # Summary
        self.stdout.write("\n" + "="*50)
        if options['dry_run']:
            self.stdout.write(
                self.style.SUCCESS(
                    f"DRY RUN COMPLETE: {total_updated} users would be updated"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"RECALCULATION COMPLETE: Updated {total_updated} users"
                )
            )
        
        self.stdout.write(f"Total point changes: {total_points_changed}")
        
        if not options['dry_run'] and total_updated > 0:
            self.stdout.write("Consider running 'update_leaderboard' command to refresh leaderboard cache")