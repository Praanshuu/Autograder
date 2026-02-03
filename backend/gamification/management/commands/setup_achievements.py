"""
Management command to set up default achievements for the gamified autograder system.

This command creates a set of common achievements that students can earn:
- First completion achievements
- Streak achievements  
- Perfect score achievements
- Speed achievements
- Milestone achievements
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from gamification.models import Achievement


class Command(BaseCommand):
    help = 'Set up default achievements for the gamified autograder system'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing achievements before creating new ones'
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be created without making changes'
        )
    
    def handle(self, *args, **options):
        if options['clear']:
            if options['dry_run']:
                self.stdout.write("DRY RUN: Would clear existing achievements")
            else:
                Achievement.objects.all().delete()
                self.stdout.write("Cleared existing achievements")
        
        achievements_to_create = self.get_default_achievements()
        
        if options['dry_run']:
            self.stdout.write(f"DRY RUN: Would create {len(achievements_to_create)} achievements:")
            for achievement in achievements_to_create:
                self.stdout.write(f"  - {achievement['name']} ({achievement['badge_type']})")
            return
        
        created_count = 0
        updated_count = 0
        
        with transaction.atomic():
            for achievement_data in achievements_to_create:
                achievement, created = Achievement.objects.get_or_create(
                    name=achievement_data['name'],
                    defaults=achievement_data
                )
                
                if created:
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f"Created achievement: {achievement.name}")
                    )
                else:
                    # Update existing achievement
                    for key, value in achievement_data.items():
                        setattr(achievement, key, value)
                    achievement.save()
                    updated_count += 1
                    self.stdout.write(
                        self.style.WARNING(f"Updated achievement: {achievement.name}")
                    )
        
        self.stdout.write(
            self.style.SUCCESS(
                f"Setup complete! Created {created_count} new achievements, "
                f"updated {updated_count} existing achievements."
            )
        )
    
    def get_default_achievements(self):
        """Define the default achievements to create"""
        return [
            # First Completion Achievements
            {
                'name': 'First Steps',
                'description': 'Complete your first practice question',
                'icon': '🎯',
                'badge_type': 'first_completion',
                'criteria': {
                    'completion_type': 'practice'
                },
                'point_threshold': None,
                'rarity': 'common',
                'is_active': True
            },
            
            # Streak Achievements
            {
                'name': 'On Fire',
                'description': 'Submit successful solutions for 3 days in a row',
                'icon': '🔥',
                'badge_type': 'streak',
                'criteria': {
                    'streak_type': 'daily',
                    'streak_length': 3
                },
                'point_threshold': None,
                'rarity': 'uncommon',
                'is_active': True
            },
            {
                'name': 'Unstoppable',
                'description': 'Submit successful solutions for 7 days in a row',
                'icon': '⚡',
                'badge_type': 'streak',
                'criteria': {
                    'streak_type': 'daily',
                    'streak_length': 7
                },
                'point_threshold': None,
                'rarity': 'rare',
                'is_active': True
            },
            {
                'name': 'Perfect Streak',
                'description': 'Get 5 consecutive successful submissions',
                'icon': '✨',
                'badge_type': 'streak',
                'criteria': {
                    'streak_type': 'consecutive',
                    'streak_length': 5
                },
                'point_threshold': None,
                'rarity': 'uncommon',
                'is_active': True
            },
            
            # Perfect Score Achievements
            {
                'name': 'Perfectionist',
                'description': 'Get perfect scores on 5 practice questions',
                'icon': '💯',
                'badge_type': 'perfect_score',
                'criteria': {
                    'perfect_count': 5
                },
                'point_threshold': None,
                'rarity': 'uncommon',
                'is_active': True
            },
            {
                'name': 'Easy Mastery',
                'description': 'Get perfect scores on 10 easy practice questions',
                'icon': '🟢',
                'badge_type': 'perfect_score',
                'criteria': {
                    'perfect_count': 10,
                    'difficulty': 'easy'
                },
                'point_threshold': None,
                'rarity': 'common',
                'is_active': True
            },
            {
                'name': 'Hard Conqueror',
                'description': 'Get perfect scores on 5 hard practice questions',
                'icon': '🔴',
                'badge_type': 'perfect_score',
                'criteria': {
                    'perfect_count': 5,
                    'difficulty': 'hard'
                },
                'point_threshold': None,
                'rarity': 'rare',
                'is_active': True
            },
            
            # Speed Achievements
            {
                'name': 'Speed Demon',
                'description': 'Complete a practice question in under 2 minutes',
                'icon': '💨',
                'badge_type': 'speed',
                'criteria': {
                    'max_time_seconds': 120
                },
                'point_threshold': None,
                'rarity': 'uncommon',
                'is_active': True
            },
            {
                'name': 'Lightning Fast',
                'description': 'Complete an easy question in under 1 minute',
                'icon': '⚡',
                'badge_type': 'speed',
                'criteria': {
                    'max_time_seconds': 60,
                    'difficulty': 'easy'
                },
                'point_threshold': None,
                'rarity': 'rare',
                'is_active': True
            },
            
            # Milestone Achievements - Points
            {
                'name': 'Point Collector',
                'description': 'Earn your first 100 points',
                'icon': '🏆',
                'badge_type': 'milestone',
                'criteria': {
                    'milestone_type': 'points',
                    'required_value': 100
                },
                'point_threshold': 100,
                'rarity': 'common',
                'is_active': True
            },
            {
                'name': 'Rising Star',
                'description': 'Earn 500 points',
                'icon': '⭐',
                'badge_type': 'milestone',
                'criteria': {
                    'milestone_type': 'points',
                    'required_value': 500
                },
                'point_threshold': 500,
                'rarity': 'uncommon',
                'is_active': True
            },
            {
                'name': 'Champion',
                'description': 'Earn 1000 points',
                'icon': '👑',
                'badge_type': 'milestone',
                'criteria': {
                    'milestone_type': 'points',
                    'required_value': 1000
                },
                'point_threshold': 1000,
                'rarity': 'rare',
                'is_active': True
            },
            {
                'name': 'Legend',
                'description': 'Earn 2500 points',
                'icon': '🌟',
                'badge_type': 'milestone',
                'criteria': {
                    'milestone_type': 'points',
                    'required_value': 2500
                },
                'point_threshold': 2500,
                'rarity': 'legendary',
                'is_active': True
            },
            
            # Milestone Achievements - Practice Completed
            {
                'name': 'Getting Started',
                'description': 'Complete 5 practice questions',
                'icon': '📚',
                'badge_type': 'milestone',
                'criteria': {
                    'milestone_type': 'practice_completed',
                    'required_value': 5
                },
                'point_threshold': None,
                'rarity': 'common',
                'is_active': True
            },
            {
                'name': 'Dedicated Learner',
                'description': 'Complete 25 practice questions',
                'icon': '📖',
                'badge_type': 'milestone',
                'criteria': {
                    'milestone_type': 'practice_completed',
                    'required_value': 25
                },
                'point_threshold': None,
                'rarity': 'uncommon',
                'is_active': True
            },
            {
                'name': 'Practice Master',
                'description': 'Complete 50 practice questions',
                'icon': '🎓',
                'badge_type': 'milestone',
                'criteria': {
                    'milestone_type': 'practice_completed',
                    'required_value': 50
                },
                'point_threshold': None,
                'rarity': 'rare',
                'is_active': True
            },
            
            # Milestone Achievements - Categories
            {
                'name': 'Well Rounded',
                'description': 'Complete questions in 3 different categories',
                'icon': '🎯',
                'badge_type': 'milestone',
                'criteria': {
                    'milestone_type': 'categories_mastered',
                    'required_value': 3
                },
                'point_threshold': None,
                'rarity': 'uncommon',
                'is_active': True
            },
            {
                'name': 'Versatile Coder',
                'description': 'Complete questions in 5 different categories',
                'icon': '🔧',
                'badge_type': 'milestone',
                'criteria': {
                    'milestone_type': 'categories_mastered',
                    'required_value': 5
                },
                'point_threshold': None,
                'rarity': 'rare',
                'is_active': True
            }
        ]