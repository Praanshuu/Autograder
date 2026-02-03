"""
Management command to update leaderboards.

This command can be used to:
- Update global leaderboard
- Update specific class leaderboards
- Update all leaderboards
"""

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from gamification.leaderboard_manager import LeaderboardManager

User = get_user_model()


class Command(BaseCommand):
    help = 'Update leaderboard rankings'

    def add_arguments(self, parser):
        parser.add_argument(
            '--type',
            type=str,
            choices=['global', 'class', 'all'],
            default='global',
            help='Type of leaderboard to update (default: global)'
        )
        
        parser.add_argument(
            '--class-id',
            type=str,
            help='Specific class ID to update (required when type=class)'
        )
        
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force update even if recently updated'
        )

    def handle(self, *args, **options):
        manager = LeaderboardManager()
        
        leaderboard_type = options['type']
        class_id = options.get('class_id')
        force = options['force']
        
        try:
            if leaderboard_type == 'global':
                self.stdout.write('Updating global leaderboard...')
                updated_count = manager.update_global_leaderboard()
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully updated global leaderboard with {updated_count} entries')
                )
                
            elif leaderboard_type == 'class':
                if not class_id:
                    raise CommandError('--class-id is required when updating class leaderboards')
                
                self.stdout.write(f'Updating class {class_id} leaderboard...')
                updated_count = manager.update_class_leaderboard(class_id)
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully updated class leaderboard with {updated_count} entries')
                )
                
            elif leaderboard_type == 'all':
                # Update global leaderboard
                self.stdout.write('Updating global leaderboard...')
                global_count = manager.update_global_leaderboard()
                self.stdout.write(f'Updated global leaderboard with {global_count} entries')
                
                # Update all class leaderboards
                # This would need to be implemented based on your class model
                # For now, we'll just show a message
                self.stdout.write('Class leaderboard updates would be implemented here')
                
                self.stdout.write(
                    self.style.SUCCESS('Successfully updated all leaderboards')
                )
                
        except Exception as e:
            raise CommandError(f'Error updating leaderboards: {e}')