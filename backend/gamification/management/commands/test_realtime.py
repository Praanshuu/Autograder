"""
Management command to test real-time functionality.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from gamification.models import UserPoints, LeaderboardManager
from gamification.realtime_service import realtime_service

User = get_user_model()


class Command(BaseCommand):
    help = 'Test real-time gamification functionality'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--test-type',
            type=str,
            default='all',
            help='Type of test to run: points, leaderboard, achievements, or all'
        )
    
    def handle(self, *args, **options):
        test_type = options['test_type']
        
        self.stdout.write(
            self.style.SUCCESS(f'Testing real-time functionality: {test_type}')
        )
        
        if test_type in ['points', 'all']:
            self.test_points_updates()
        
        if test_type in ['leaderboard', 'all']:
            self.test_leaderboard_updates()
        
        if test_type in ['achievements', 'all']:
            self.test_achievement_notifications()
        
        self.stdout.write(
            self.style.SUCCESS('Real-time testing completed successfully!')
        )
    
    def test_points_updates(self):
        """Test points update notifications."""
        self.stdout.write('Testing points updates...')
        
        # Get or create test user
        user, created = User.objects.get_or_create(
            username='realtime_test_user',
            defaults={
                'email': 'realtime@example.com',
                'password': 'testpass123'
            }
        )
        
        # Test points notification
        realtime_service.notify_points_update(
            user=user,
            old_points=100,
            new_points=150,
            source='practice'
        )
        
        self.stdout.write(
            self.style.SUCCESS('✓ Points update notification sent')
        )
    
    def test_leaderboard_updates(self):
        """Test leaderboard update broadcasts."""
        self.stdout.write('Testing leaderboard updates...')
        
        # Update global leaderboard (this will broadcast updates)
        entries_count = LeaderboardManager.update_global_leaderboard()
        
        self.stdout.write(
            self.style.SUCCESS(f'✓ Global leaderboard updated with {entries_count} entries')
        )
        
        # Test manual broadcast
        realtime_service.broadcast_leaderboard_update(
            leaderboard_type='global',
            data={'test': 'manual_broadcast'}
        )
        
        self.stdout.write(
            self.style.SUCCESS('✓ Manual leaderboard broadcast sent')
        )
    
    def test_achievement_notifications(self):
        """Test achievement notifications."""
        self.stdout.write('Testing achievement notifications...')
        
        # Get test user
        user, created = User.objects.get_or_create(
            username='realtime_test_user',
            defaults={
                'email': 'realtime@example.com',
                'password': 'testpass123'
            }
        )
        
        # Test achievement notification
        achievement_data = {
            'id': 'test-achievement-123',
            'name': 'Test Achievement',
            'description': 'A test achievement for real-time testing',
            'badge_type': 'first_completion',
            'rarity': 'common',
            'points_reward': 50
        }
        
        realtime_service.notify_achievement_earned(
            user=user,
            achievement_data=achievement_data,
            points_earned=50
        )
        
        self.stdout.write(
            self.style.SUCCESS('✓ Achievement notification sent')
        )
    
    def test_rank_changes(self):
        """Test rank change notifications."""
        self.stdout.write('Testing rank change notifications...')
        
        # Get test user
        user, created = User.objects.get_or_create(
            username='realtime_test_user',
            defaults={
                'email': 'realtime@example.com',
                'password': 'testpass123'
            }
        )
        
        # Test rank change notification
        realtime_service.notify_rank_change(
            user=user,
            old_rank=5,
            new_rank=3,
            leaderboard_type='global'
        )
        
        self.stdout.write(
            self.style.SUCCESS('✓ Rank change notification sent')
        )