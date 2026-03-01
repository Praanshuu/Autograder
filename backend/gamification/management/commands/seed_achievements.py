"""
Management command to seed default achievement badges.

Run with: python manage.py seed_achievements
"""
from django.core.management.base import BaseCommand
from gamification.models import Achievement


ACHIEVEMENTS = [
    # ── First Completion ────────────────────────────────────────────────────
    {
        'name': 'First Steps',
        'description': 'Complete your very first practice question.',
        'icon': '🎯',
        'badge_type': 'first_completion',
        'rarity': 'common',
        'criteria': {'completion_type': 'practice'},
        'point_threshold': None,
    },
    {
        'name': 'Assignment Ace',
        'description': 'Submit your first assignment successfully.',
        'icon': '📝',
        'badge_type': 'first_completion',
        'rarity': 'common',
        'criteria': {'completion_type': 'assignment'},
        'point_threshold': None,
    },

    # ── Streak ──────────────────────────────────────────────────────────────
    {
        'name': 'On Fire',
        'description': 'Maintain a 3-day submission streak.',
        'icon': '🔥',
        'badge_type': 'streak',
        'rarity': 'common',
        'criteria': {'streak_type': 'daily', 'streak_length': 3},
        'point_threshold': None,
    },
    {
        'name': 'Week Warrior',
        'description': 'Maintain a 7-day submission streak.',
        'icon': '⚔️',
        'badge_type': 'streak',
        'rarity': 'uncommon',
        'criteria': {'streak_type': 'daily', 'streak_length': 7},
        'point_threshold': None,
    },
    {
        'name': 'Unstoppable',
        'description': 'Maintain a 14-day submission streak.',
        'icon': '💪',
        'badge_type': 'streak',
        'rarity': 'rare',
        'criteria': {'streak_type': 'daily', 'streak_length': 14},
        'point_threshold': None,
    },
    {
        'name': 'Legend',
        'description': 'Maintain a 30-day submission streak.',
        'icon': '🏆',
        'badge_type': 'streak',
        'rarity': 'legendary',
        'criteria': {'streak_type': 'daily', 'streak_length': 30},
        'point_threshold': None,
    },
    {
        'name': 'Hot Streak',
        'description': 'Submit 5 successful answers in a row without failing.',
        'icon': '🌟',
        'badge_type': 'streak',
        'rarity': 'common',
        'criteria': {'streak_type': 'consecutive', 'streak_length': 5},
        'point_threshold': None,
    },

    # ── Perfect Score ────────────────────────────────────────────────────────
    {
        'name': 'Perfectionist',
        'description': 'Achieve a perfect score on 1 practice question.',
        'icon': '✨',
        'badge_type': 'perfect_score',
        'rarity': 'common',
        'criteria': {'perfect_count': 1},
        'point_threshold': None,
    },
    {
        'name': 'Flawless',
        'description': 'Achieve a perfect score on 5 practice questions.',
        'icon': '💎',
        'badge_type': 'perfect_score',
        'rarity': 'uncommon',
        'criteria': {'perfect_count': 5},
        'point_threshold': None,
    },
    {
        'name': 'Easy Master',
        'description': 'Perfect score on 3 Easy questions.',
        'icon': '🟢',
        'badge_type': 'perfect_score',
        'rarity': 'common',
        'criteria': {'perfect_count': 3, 'difficulty': 'easy'},
        'point_threshold': None,
    },
    {
        'name': 'Medium Master',
        'description': 'Perfect score on 3 Medium questions.',
        'icon': '🟡',
        'badge_type': 'perfect_score',
        'rarity': 'uncommon',
        'criteria': {'perfect_count': 3, 'difficulty': 'medium'},
        'point_threshold': None,
    },
    {
        'name': 'Hard Master',
        'description': 'Perfect score on 3 Hard questions.',
        'icon': '🔴',
        'badge_type': 'perfect_score',
        'rarity': 'rare',
        'criteria': {'perfect_count': 3, 'difficulty': 'hard'},
        'point_threshold': None,
    },

    # ── Speed ────────────────────────────────────────────────────────────────
    {
        'name': 'Speed Demon',
        'description': 'Solve any question in under 5 minutes.',
        'icon': '⚡',
        'badge_type': 'speed',
        'rarity': 'common',
        'criteria': {'max_time_seconds': 300},
        'point_threshold': None,
    },
    {
        'name': 'Lightning Fast',
        'description': 'Solve a Hard question in under 10 minutes.',
        'icon': '🌩️',
        'badge_type': 'speed',
        'rarity': 'rare',
        'criteria': {'max_time_seconds': 600, 'difficulty': 'hard'},
        'point_threshold': None,
    },

    # ── Milestone ────────────────────────────────────────────────────────────
    {
        'name': 'Point Collector',
        'description': 'Earn 100 total points.',
        'icon': '💰',
        'badge_type': 'milestone',
        'rarity': 'common',
        'criteria': {'milestone_type': 'points', 'required_value': 100},
        'point_threshold': 100,
    },
    {
        'name': 'High Scorer',
        'description': 'Earn 500 total points.',
        'icon': '🥈',
        'badge_type': 'milestone',
        'rarity': 'uncommon',
        'criteria': {'milestone_type': 'points', 'required_value': 500},
        'point_threshold': 500,
    },
    {
        'name': 'Point Machine',
        'description': 'Earn 1,000 total points.',
        'icon': '🥇',
        'badge_type': 'milestone',
        'rarity': 'rare',
        'criteria': {'milestone_type': 'points', 'required_value': 1000},
        'point_threshold': 1000,
    },
    {
        'name': 'Elite Coder',
        'description': 'Earn 5,000 total points.',
        'icon': '👑',
        'badge_type': 'milestone',
        'rarity': 'legendary',
        'criteria': {'milestone_type': 'points', 'required_value': 5000},
        'point_threshold': 5000,
    },
    {
        'name': 'Problem Solver',
        'description': 'Complete 10 practice questions.',
        'icon': '🧩',
        'badge_type': 'milestone',
        'rarity': 'common',
        'criteria': {'milestone_type': 'practice_completed', 'required_value': 10},
        'point_threshold': None,
    },
    {
        'name': 'Grinder',
        'description': 'Complete 25 practice questions.',
        'icon': '⚙️',
        'badge_type': 'milestone',
        'rarity': 'uncommon',
        'criteria': {'milestone_type': 'practice_completed', 'required_value': 25},
        'point_threshold': None,
    },
    {
        'name': 'Century Club',
        'description': 'Complete 50 practice questions.',
        'icon': '🎖️',
        'badge_type': 'milestone',
        'rarity': 'rare',
        'criteria': {'milestone_type': 'practice_completed', 'required_value': 50},
        'point_threshold': None,
    },
]


class Command(BaseCommand):
    help = 'Seed default achievement badges into the database.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset',
            action='store_true',
            help='Delete all existing achievements before seeding.',
        )

    def handle(self, *args, **options):
        if options['reset']:
            deleted, _ = Achievement.objects.all().delete()
            self.stdout.write(self.style.WARNING(f'Deleted {deleted} existing achievements.'))

        created_count = 0
        updated_count = 0

        for data in ACHIEVEMENTS:
            obj, created = Achievement.objects.update_or_create(
                name=data['name'],
                defaults={
                    'description': data['description'],
                    'icon': data['icon'],
                    'badge_type': data['badge_type'],
                    'rarity': data['rarity'],
                    'criteria': data['criteria'],
                    'point_threshold': data['point_threshold'],
                    'is_active': True,
                },
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Seeded achievements: {created_count} created, {updated_count} updated.'
            )
        )
