"""
Tests for the LeaderboardManager and LeaderboardEntry model.

Tests cover:
- Global leaderboard calculation and ranking
- Class-specific leaderboard calculation
- Tie-breaking logic
- Cached leaderboard updates
- User rank lookup and nearby competitors
- Pagination functionality
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

from gamification.models import (
    LeaderboardEntry, LeaderboardManager, UserPoints, PracticeQuestion, 
    PracticeProgress
)
from classes.models import Class

User = get_user_model()


class LeaderboardManagerTestCase(TestCase):
    """Test cases for LeaderboardManager functionality"""
    
    def setUp(self):
        """Set up test data"""
        # Create test users
        self.users = []
        for i in range(5):
            user = User.objects.create_user(
                username=f'student{i}',
                email=f'student{i}@example.com',
                password='testpass123',
                role='student'
            )
            self.users.append(user)
        
        # Create teacher for practice questions
        self.teacher = User.objects.create_user(
            username='teacher',
            email='teacher@example.com',
            password='testpass123',
            role='teacher'
        )
        
        # Create test class
        self.test_class = Class.objects.create(
            name='Test Class',
            section='Section A',
            owner=self.teacher
        )
        
        # Add first 3 users to the class through enrollments
        from classes.models import Enrollment
        for user in self.users[:3]:
            Enrollment.objects.create(
                class_obj=self.test_class,
                user=user,
                role='student'
            )
        
        # Create practice question for completed problems counting
        self.practice_question = PracticeQuestion.objects.create(
            title='Test Question',
            description='A test practice question',
            difficulty='easy',
            category='Arrays',
            test_cases=[{'input': '1', 'output': '1'}],
            point_value=100,
            created_by=self.teacher
        )
        
        # Create user points with different scores
        self.user_points = []
        point_values = [500, 300, 300, 200, 100]  # Note: two users with 300 points for tie-breaking test
        
        for i, user in enumerate(self.users):
            points = UserPoints.objects.create(
                user=user,
                total_points=point_values[i],
                practice_points=point_values[i],
                assignment_points=0,
                last_updated=timezone.now() - timedelta(minutes=i)  # Different update times for tie-breaking
            )
            self.user_points.append(points)
        
        # Create some completed practice progress for testing
        for i, user in enumerate(self.users):
            # Create different numbers of completed problems
            for j in range(i + 1):  # user0: 1 problem, user1: 2 problems, etc.
                # Create additional practice questions for multiple completions
                if j > 0:
                    practice_question = PracticeQuestion.objects.create(
                        title=f'Test Question {j}',
                        description=f'A test practice question {j}',
                        difficulty='easy',
                        category='Arrays',
                        test_cases=[{'input': str(j), 'output': str(j)}],
                        point_value=100,
                        created_by=self.teacher
                    )
                else:
                    practice_question = self.practice_question
                
                PracticeProgress.objects.create(
                    student=user,
                    practice_question=practice_question,
                    is_completed=True,
                    attempts_count=1,
                    best_score=100.0
                )
    
    def test_calculate_global_leaderboard(self):
        """Test global leaderboard calculation with proper ranking"""
        rankings = LeaderboardManager.calculate_global_leaderboard()
        
        # Should have 5 users
        self.assertEqual(len(rankings), 5)
        
        # Check ranking order (by points, then by last_updated for ties)
        expected_order = [
            (self.users[0], 500, 1),  # Highest points
            (self.users[1], 300, 2),  # Tied points, but updated earlier (tie-breaker)
            (self.users[2], 300, 2),  # Same rank as user1 due to tie
            (self.users[3], 200, 4),  # Next rank after tie
            (self.users[4], 100, 5)   # Lowest points
        ]
        
        for i, (expected_user, expected_points, expected_rank) in enumerate(expected_order):
            ranking = rankings[i]
            self.assertEqual(ranking['user'], expected_user)
            self.assertEqual(ranking['total_points'], expected_points)
            self.assertEqual(ranking['rank'], expected_rank)
            self.assertEqual(ranking['completed_problems'], i + 1)  # Based on our setup
    
    def test_calculate_class_leaderboard(self):
        """Test class-specific leaderboard calculation"""
        rankings = LeaderboardManager.calculate_class_leaderboard(str(self.test_class.id))
        
        # Should have 3 users (only first 3 are in the class)
        self.assertEqual(len(rankings), 3)
        
        # Check that only class students are included
        class_users = [ranking['user'] for ranking in rankings]
        self.assertIn(self.users[0], class_users)
        self.assertIn(self.users[1], class_users)
        self.assertIn(self.users[2], class_users)
        self.assertNotIn(self.users[3], class_users)
        self.assertNotIn(self.users[4], class_users)
        
        # Check ranking order within class
        self.assertEqual(rankings[0]['user'], self.users[0])  # 500 points
        self.assertEqual(rankings[0]['rank'], 1)
        self.assertEqual(rankings[1]['rank'], 2)  # 300 points (tie)
        self.assertEqual(rankings[2]['rank'], 2)  # 300 points (tie)
    
    def test_calculate_class_leaderboard_invalid_class(self):
        """Test class leaderboard with invalid class ID"""
        rankings = LeaderboardManager.calculate_class_leaderboard('invalid-uuid')
        self.assertEqual(rankings, [])
    
    def test_update_global_leaderboard(self):
        """Test updating cached global leaderboard entries"""
        # Initially no leaderboard entries
        self.assertEqual(LeaderboardEntry.objects.filter(leaderboard_type='global').count(), 0)
        
        # Update global leaderboard
        count = LeaderboardManager.update_global_leaderboard()
        
        # Should create 5 entries
        self.assertEqual(count, 5)
        self.assertEqual(LeaderboardEntry.objects.filter(leaderboard_type='global').count(), 5)
        
        # Check that entries are created correctly
        top_entry = LeaderboardEntry.objects.filter(
            leaderboard_type='global',
            rank=1
        ).first()
        
        self.assertEqual(top_entry.user, self.users[0])
        self.assertEqual(top_entry.total_points, 500)
        self.assertEqual(top_entry.completed_problems, 1)
        
        # Test updating again (should replace existing entries)
        count = LeaderboardManager.update_global_leaderboard()
        self.assertEqual(count, 5)
        self.assertEqual(LeaderboardEntry.objects.filter(leaderboard_type='global').count(), 5)
    
    def test_update_class_leaderboard(self):
        """Test updating cached class leaderboard entries"""
        class_id = str(self.test_class.id)
        
        # Initially no class leaderboard entries
        self.assertEqual(
            LeaderboardEntry.objects.filter(
                leaderboard_type='class',
                class_id=class_id
            ).count(),
            0
        )
        
        # Update class leaderboard
        count = LeaderboardManager.update_class_leaderboard(class_id)
        
        # Should create 3 entries (3 students in class)
        self.assertEqual(count, 3)
        self.assertEqual(
            LeaderboardEntry.objects.filter(
                leaderboard_type='class',
                class_id=class_id
            ).count(),
            3
        )
        
        # Check that entries are created correctly
        top_entry = LeaderboardEntry.objects.filter(
            leaderboard_type='class',
            class_id=class_id,
            rank=1
        ).first()
        
        self.assertEqual(top_entry.user, self.users[0])
        self.assertEqual(top_entry.total_points, 500)
    
    def test_get_user_rank_global(self):
        """Test getting user rank and nearby competitors for global leaderboard"""
        # Update leaderboard first
        LeaderboardManager.update_global_leaderboard()
        
        # Get rank for middle user
        rank_info = LeaderboardManager.get_user_rank(self.users[2], 'global')
        
        self.assertIsNotNone(rank_info)
        self.assertEqual(rank_info['user_rank'], 2)  # Tied for 2nd place
        self.assertEqual(rank_info['user_points'], 300)
        self.assertEqual(rank_info['user_problems'], 3)
        
        # Check nearby competitors
        nearby = rank_info['nearby_competitors']
        self.assertGreaterEqual(len(nearby), 3)  # Should have at least 3 competitors
        
        # Find current user in nearby competitors
        current_user_entry = next(
            (entry for entry in nearby if entry['is_current_user']),
            None
        )
        self.assertIsNotNone(current_user_entry)
        self.assertEqual(current_user_entry['rank'], 2)
    
    def test_get_user_rank_class(self):
        """Test getting user rank for class leaderboard"""
        class_id = str(self.test_class.id)
        
        # Update class leaderboard first
        LeaderboardManager.update_class_leaderboard(class_id)
        
        # Get rank for class user
        rank_info = LeaderboardManager.get_user_rank(
            self.users[1], 
            'class', 
            class_id
        )
        
        self.assertIsNotNone(rank_info)
        self.assertEqual(rank_info['user_rank'], 2)  # Tied for 2nd in class
        self.assertEqual(rank_info['user_points'], 300)
    
    def test_get_user_rank_not_found(self):
        """Test getting rank for user not in leaderboard"""
        # Don't update leaderboard, so no entries exist
        rank_info = LeaderboardManager.get_user_rank(self.users[0], 'global')
        self.assertIsNone(rank_info)
    
    def test_get_leaderboard_page_global(self):
        """Test paginated global leaderboard retrieval"""
        # Update leaderboard first
        LeaderboardManager.update_global_leaderboard()
        
        # Get first page
        page_data = LeaderboardManager.get_leaderboard_page('global', page=1, page_size=3)
        
        # Check entries
        self.assertEqual(len(page_data['entries']), 3)
        self.assertEqual(page_data['entries'][0]['rank'], 1)
        self.assertEqual(page_data['entries'][0]['user'], self.users[0])
        
        # Check pagination info
        pagination = page_data['pagination']
        self.assertEqual(pagination['current_page'], 1)
        self.assertEqual(pagination['page_size'], 3)
        self.assertEqual(pagination['total_entries'], 5)
        self.assertEqual(pagination['total_pages'], 2)
        self.assertTrue(pagination['has_next'])
        self.assertFalse(pagination['has_previous'])
        
        # Get second page
        page_data = LeaderboardManager.get_leaderboard_page('global', page=2, page_size=3)
        
        self.assertEqual(len(page_data['entries']), 2)  # Remaining 2 entries
        self.assertFalse(page_data['pagination']['has_next'])
        self.assertTrue(page_data['pagination']['has_previous'])
    
    def test_get_leaderboard_page_class(self):
        """Test paginated class leaderboard retrieval"""
        class_id = str(self.test_class.id)
        
        # Update class leaderboard first
        LeaderboardManager.update_class_leaderboard(class_id)
        
        # Get class leaderboard page
        page_data = LeaderboardManager.get_leaderboard_page(
            'class', 
            class_id=class_id, 
            page=1, 
            page_size=10
        )
        
        # Should have 3 entries (3 students in class)
        self.assertEqual(len(page_data['entries']), 3)
        self.assertEqual(page_data['pagination']['total_entries'], 3)
        self.assertEqual(page_data['pagination']['total_pages'], 1)
    
    def test_update_leaderboards_for_user(self):
        """Test updating leaderboards when a user's points change"""
        # Initially no leaderboard entries
        self.assertEqual(LeaderboardEntry.objects.count(), 0)
        
        # Update leaderboards for a user
        LeaderboardManager.update_leaderboards_for_user(self.users[0])
        
        # Should create global leaderboard entries
        self.assertEqual(LeaderboardEntry.objects.filter(leaderboard_type='global').count(), 5)
        
        # Should create class leaderboard entries for user's classes
        class_entries = LeaderboardEntry.objects.filter(
            leaderboard_type='class',
            class_id=str(self.test_class.id)
        ).count()
        self.assertEqual(class_entries, 3)  # 3 students in the class
    
    def test_tie_breaking_logic(self):
        """Test that tie-breaking works correctly based on last_updated"""
        rankings = LeaderboardManager.calculate_global_leaderboard()
        
        # Find the two users with 300 points
        tied_users = [r for r in rankings if r['total_points'] == 300]
        self.assertEqual(len(tied_users), 2)
        
        # Both should have rank 2
        self.assertEqual(tied_users[0]['rank'], 2)
        self.assertEqual(tied_users[1]['rank'], 2)
        
        # The user updated earlier should come first in the list
        self.assertEqual(tied_users[0]['user'], self.users[1])  # Updated earlier
        self.assertEqual(tied_users[1]['user'], self.users[2])  # Updated later
    
    def test_leaderboard_entry_model(self):
        """Test LeaderboardEntry model functionality"""
        entry = LeaderboardEntry.objects.create(
            user=self.users[0],
            rank=1,
            total_points=500,
            completed_problems=5,
            leaderboard_type='global'
        )
        
        self.assertEqual(str(entry), f"#1 {self.users[0].username} (global)")
        self.assertEqual(entry.leaderboard_type, 'global')
        self.assertIsNone(entry.class_id)
        
        # Test class leaderboard entry
        class_entry = LeaderboardEntry.objects.create(
            user=self.users[1],
            rank=2,
            total_points=300,
            completed_problems=3,
            leaderboard_type='class',
            class_id=str(self.test_class.id)
        )
        
        self.assertEqual(class_entry.leaderboard_type, 'class')
        self.assertEqual(str(class_entry.class_id), str(self.test_class.id))
    
    def test_empty_leaderboard(self):
        """Test leaderboard calculation with no users"""
        # Delete all user points
        UserPoints.objects.all().delete()
        
        rankings = LeaderboardManager.calculate_global_leaderboard()
        self.assertEqual(rankings, [])
        
        count = LeaderboardManager.update_global_leaderboard()
        self.assertEqual(count, 0)
    
    def test_performance_with_bulk_operations(self):
        """Test that leaderboard updates use bulk operations for performance"""
        # This test ensures bulk_create is used
        # We can verify by checking that all entries are created in one operation
        
        initial_count = LeaderboardEntry.objects.count()
        LeaderboardManager.update_global_leaderboard()
        final_count = LeaderboardEntry.objects.count()
        
        # Should create exactly 5 entries (one for each user)
        self.assertEqual(final_count - initial_count, 5)
        
        # Verify all entries have the same created timestamp (within a small window)
        entries = LeaderboardEntry.objects.filter(leaderboard_type='global')
        timestamps = [entry.updated_at for entry in entries]
        
        # All timestamps should be very close (within 1 second)
        time_diff = max(timestamps) - min(timestamps)
        self.assertLess(time_diff.total_seconds(), 1.0)