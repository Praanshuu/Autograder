"""
Management command to update student analytics.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from gamification.analytics_aggregator import analytics_aggregator

User = get_user_model()


class Command(BaseCommand):
    help = 'Update student analytics for all users or specific user'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--user',
            type=str,
            help='Username to update analytics for (if not provided, updates all users)'
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force update even if analytics were recently updated'
        )
    
    def handle(self, *args, **options):
        username = options.get('user')
        force_update = options.get('force', False)
        
        if username:
            # Update specific user
            try:
                user = User.objects.get(username=username)
                self.stdout.write(f'Updating analytics for user: {username}')
                
                analytics = analytics_aggregator.update_student_analytics(user)
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✓ Updated analytics for {username}:\n'
                        f'  - Practice completed: {analytics.total_practice_completed}\n'
                        f'  - Assignments completed: {analytics.total_assignments_completed}\n'
                        f'  - Average score: {analytics.average_score}%\n'
                        f'  - Current streak: {analytics.current_streak} days\n'
                        f'  - Total time: {analytics.total_time_spent} minutes'
                    )
                )
                
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'User "{username}" not found')
                )
                return
        else:
            # Update all users
            users = User.objects.all()
            total_users = users.count()
            
            self.stdout.write(f'Updating analytics for {total_users} users...')
            
            updated_count = 0
            for i, user in enumerate(users, 1):
                try:
                    analytics_aggregator.update_student_analytics(user)
                    updated_count += 1
                    
                    if i % 10 == 0:  # Progress update every 10 users
                        self.stdout.write(f'Progress: {i}/{total_users} users processed')
                        
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(
                            f'Failed to update analytics for {user.username}: {e}'
                        )
                    )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'✓ Successfully updated analytics for {updated_count}/{total_users} users'
                )
            )
        
        # Show summary statistics
        self.show_analytics_summary()
    
    def show_analytics_summary(self):
        """Show overall analytics summary."""
        from gamification.models import StudentAnalytics
        from django.db.models import Avg, Max, Min, Count, Q
        
        self.stdout.write('\n' + '='*50)
        self.stdout.write('ANALYTICS SUMMARY')
        self.stdout.write('='*50)
        
        total_analytics = StudentAnalytics.objects.count()
        
        if total_analytics == 0:
            self.stdout.write('No analytics data available.')
            return
        
        # Calculate summary statistics
        summary = StudentAnalytics.objects.aggregate(
            avg_practice=Avg('total_practice_completed'),
            avg_assignments=Avg('total_assignments_completed'),
            avg_score=Avg('average_score'),
            avg_streak=Avg('current_streak'),
            max_streak=Max('longest_streak'),
            avg_time=Avg('total_time_spent'),
            active_users=Count('id', filter=Q(last_activity__isnull=False))
        )
        
        self.stdout.write(f'Total students with analytics: {total_analytics}')
        self.stdout.write(f'Active students: {summary["active_users"]}')
        self.stdout.write(f'Average practice completed: {summary["avg_practice"]:.1f}')
        self.stdout.write(f'Average assignments completed: {summary["avg_assignments"]:.1f}')
        self.stdout.write(f'Average score: {summary["avg_score"]:.1f}%')
        self.stdout.write(f'Average current streak: {summary["avg_streak"]:.1f} days')
        self.stdout.write(f'Longest streak recorded: {summary["max_streak"]} days')
        self.stdout.write(f'Average time spent: {summary["avg_time"]:.0f} minutes')
        
        # Show top performers
        top_performers = StudentAnalytics.objects.order_by('-average_score')[:5]
        
        if top_performers:
            self.stdout.write('\nTop 5 Performers:')
            for i, analytics in enumerate(top_performers, 1):
                self.stdout.write(
                    f'  {i}. {analytics.student.username}: {analytics.average_score:.1f}% '
                    f'({analytics.total_practice_completed + analytics.total_assignments_completed} completed)'
                )
        
        self.stdout.write('='*50)