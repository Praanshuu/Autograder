from django.core.management.base import BaseCommand
from gamification.models import Achievement


class Command(BaseCommand):
    help = 'Set up default achievements for the gamification system'

    def handle(self, *args, **options):
        achievements_data = [
            {
                'name': 'First Steps',
                'description': 'Complete your first practice question',
                'icon': '🎯',
                'badge_type': 'first_completion',
                'criteria': {'type': 'first_practice_completion'},
                'rarity': 'common',
            },
            {
                'name': 'Perfect Score',
                'description': 'Get 100% on an assignment',
                'icon': '💯',
                'badge_type': 'perfect_score',
                'criteria': {'type': 'perfect_assignment_score'},
                'rarity': 'uncommon',
            },
            {
                'name': 'Speed Demon',
                'description': 'Complete a practice question in under 5 minutes',
                'icon': '⚡',
                'badge_type': 'speed',
                'criteria': {'type': 'fast_completion', 'time_limit': 300},
                'rarity': 'rare',
            },
            {
                'name': 'Streak Master',
                'description': 'Complete 5 practice questions in a row',
                'icon': '🔥',
                'badge_type': 'streak',
                'criteria': {'type': 'completion_streak', 'count': 5},
                'rarity': 'uncommon',
            },
            {
                'name': 'Century Club',
                'description': 'Earn 100 total points',
                'icon': '💰',
                'badge_type': 'milestone',
                'criteria': {'type': 'total_points'},
                'point_threshold': 100,
                'rarity': 'common',
            },
            {
                'name': 'Practice Champion',
                'description': 'Complete 10 practice questions',
                'icon': '🏆',
                'badge_type': 'milestone',
                'criteria': {'type': 'practice_completions', 'count': 10},
                'rarity': 'uncommon',
            },
            {
                'name': 'Legendary Coder',
                'description': 'Earn 1000 total points',
                'icon': '👑',
                'badge_type': 'milestone',
                'criteria': {'type': 'total_points'},
                'point_threshold': 1000,
                'rarity': 'legendary',
            },
            {
                'name': 'Problem Solver',
                'description': 'Complete practice questions in 3 different categories',
                'icon': '🧩',
                'badge_type': 'milestone',
                'criteria': {'type': 'category_diversity', 'count': 3},
                'rarity': 'rare',
            },
        ]

        created_count = 0
        for achievement_data in achievements_data:
            achievement, created = Achievement.objects.get_or_create(
                name=achievement_data['name'],
                defaults=achievement_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created achievement: {achievement.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Achievement already exists: {achievement.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new achievements')
        )