"""
Tests for the LeaderboardManager class.

Tests cover:
- Global and class-specific leaderboard calculation
- Ranking with tie-breaking logic
- Cached leaderboard data management
- User position updates
- Performance optimization
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

from gamification.models import (
    LeaderboardEntry, UserPoints, PracticeQuestion, PracticeProgress, 
    StudentAnalytics
)
from gamification.leaderboard_manager import LeaderboardManager, update_global_leaderboard
from classes.models import Class

User = get_user_model()


class LeaderboardManagerTestCase(TestCase):
    """Test cases for LeaderboardManager functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.manager = LeaderboardManager()
        
        # Create test teacher
        self.teacher = User.objects.create_user(
            username='teacher',
            email='teacher@example.com',
            password='testpass123',
            role='teacher'
        )
        
        # Create test students
        self.student1 = User.objects.create_user(
            username='student1',
            email='student1@example.com',
            password='testpass123',
            role='student'
        )
        
        self.student2 = User.objects.create_user(
            username='student2',
            email='student2@example.com',
            password='testpass123',
            role='student'
        )
        
        self.student3 = User.objects.create_user(
            username='student3',
            email='student3@example.com',
            password='testpass123',
            role='student'
        )
        
        # Create test class
        self.test_class = Class.objects.create(
            name='Test Class',
            owner=self.teacher,
            section='A'
        )
        
        # Enroll students in the class
        from classes.models import Enrollment
        Enrollment.objects.create(
            class_obj=self.test_class,
            user=self.student1,
            role='student'
        )
        Enrollment.objects.create(
            class_obj=self.test_class,
            user=self.student2,
            role='student'
        )
        
        # Create user points with different scores
        UserPoints.objects.create(
            user=self.student1,
            total_points=300,
            practice_points=300,
            assignment_points=0
        )
        
        UserPoints.objects.create(
            user=self.student2,
            total_points=200,
            practice_points=200,
            assignment_points=0
        )
        
        UserPoints.objects.create(
            user=self.student3,
            total_points=250,
            practice_points=250,
            assignment_points=0
        )
        
        # Create practice question for testing
        self.practice_question = PracticeQuestion.objects.create(
            title='Test Question',
            description='A test practice question',
            difficulty='easy',
            category='Arrays',
            test_cases=[{'input': '1', 'output': '1'}],
            point_value=100,
            created_by=self.teacher
        )
        
        # Create practice progress with different completion counts
        PracticeProgress.objects.create(
            student=self.student1,
            practice_question=self.practice_question,
            is_completed=True,
            attempts_count=1,
            best_score=100.0
        )
        
        # Create analytics data
        StudentAnalytics.objects.create(
            student=self.student1,
            total_practice_completed=1,
            last_activity=timezone.now()
        )
        
        StudentAnalytics.objects.create(
            student=self.student2,
            total_practice_completed=0,
            last_activity=timezone.now() - timedelta(hours=1)
        )
        
        StudentAnalytics.objects.create(
            student=self.student3,
            total_practice_completed=0,
            last_activity=timezone.now() - timedelta(minutes=30)
        )
    
    def test_update_global_leaderboard(self):
        """Test global leaderboard calculation and ranking"""
        # Update global leaderboard
        updated_count = self.manager.update_global_leaderboard()
        
        # Should have updated 3 students
        self.assertEqual(updated_count, 3)
        
        # Check rankings are correct
        entries = LeaderboardEntry.objects.filter(
            leaderboard_type='global',
            class_id__isnull=True
        ).order_by('rank')
        
        self.assertEqual(len(entries), 3)
        
        # Student1 should be rank 1 (300 points, 1 completed problem)
        self.assertEqual(entries[0].user, self.student1)
        self.assertEqual(entries[0].rank, 1)
        self.assertEqual(entries[0].total_points, 300)
        self.assertEqual(entries[0].completed_problems, 1)
        
        # Student3 should be rank 2 (250 points, 0 completed problems)
        self.assertEqual(entries[1].user, self.student3)
        self.assertEqual(entries[1].rank, 2)
        self.assertEqual(entries[1].total_points, 250)
        
        # Student2 should be rank 3 (200 points, 0 completed problems)
        self.assertEqual(entries[2].user, self.student2)
        self.assertEqual(entries[2].rank, 3)
        self.assertEqual(entries[2].total_points, 200)
    
    def test_update_class_leaderboard(self):
        """Test class-specific leaderboard calculation"""
        # Update class leaderboard
        updated_count = self.manager.update_class_leaderboard(str(self.test_class.id))
        
        # Should have updated 2 students (only class members)
        self.assertEqual(updated_count, 2)
        
        # Check rankings are correct
        entries = LeaderboardEntry.objects.filter(
            leaderboard_type='class',
            class_id=str(self.test_class.id)
        ).order_by('rank')
        
        self.assertEqual(len(entries), 2)
        
        # Student1 should be rank 1
        self.assertEqual(entries[0].user, self.student1)
        self.assertEqual(entries[0].rank, 1)
        
        # Student2 should be rank 2
        self.assertEqual(entries[1].user, self.student2)
        self.assertEqual(entries[1].rank, 2)
        
        # Student3 should not be in class leaderboard
        self.assertFalse(
            LeaderboardEntry.objects.filter(
                user=self.student3,
                leaderboard_type='class',
                class_id=str(self.test_class.id)
            ).exists()
        )
    
    def test_tie_breaking_logic(self):
        """Test tie-breaking logic when users have same points"""
        # Create two users with same points but different completion counts
        student4 = User.objects.create_user(
            username='student4',
            email='student4@example.com',
            password='testpass123',
            role='student'
        )
        
        student5 = User.objects.create_user(
            username='student5',
            email='student5@example.com',
            password='testpass123',
            role='student'
        )
        
        # Both have 200 points (same as student2)
        UserPoints.objects.create(
            user=student4,
            total_points=200,
            practice_points=200,
            assignment_points=0
        )
        
        UserPoints.objects.create(
            user=student5,
            total_points=200,
            practice_points=200,
            assignment_points=0
        )
        
        # Student4 has completed 1 problem, student5 has 0
        second_question = PracticeQuestion.objects.create(
            title='Second Question',
            description='Another test question',
            difficulty='medium',
            category='Algorithms',
            test_cases=[{'input': '2', 'output': '4'}],
            point_value=150,
            created_by=self.teacher
        )
        
        PracticeProgress.objects.create(
            student=student4,
            practice_question=second_question,
            is_completed=True,
            attempts_count=1,
            best_score=100.0
        )
        
        # Create analytics
        StudentAnalytics.objects.create(
            student=student4,
            total_practice_completed=1,
            last_activity=timezone.now()
        )
        
        StudentAnalytics.objects.create(
            student=student5,
            total_practice_completed=0,
            last_activity=timezone.now()
        )
        
        # Update leaderboard
        self.manager.update_global_leaderboard(force_refresh=True)
        
        # Check tie-breaking: student4 should rank higher than student2 and student5
        # due to more completed problems
        student4_entry = LeaderboardEntry.objects.get(
            user=student4,
            leaderboard_type='global'
        )
        student2_entry = LeaderboardEntry.objects.get(
            user=self.student2,
            leaderboard_type='global'
        )
        student5_entry = LeaderboardEntry.objects.get(
            user=student5,
            leaderboard_type='global'
        )
        
        # Student4 should rank higher than student2 and student5
        self.assertLess(student4_entry.rank, student2_entry.rank)
        self.assertLess(student4_entry.rank, student5_entry.rank)
    
    def test_get_user_rank(self):
        """Test getting a user's current rank"""
        # Update leaderboard first
        self.manager.update_global_leaderboard()
        
        # Test global rank
        rank1 = self.manager.get_user_rank(self.student1, 'global')
        rank2 = self.manager.get_user_rank(self.student2, 'global')
        rank3 = self.manager.get_user_rank(self.student3, 'global')
        
        self.assertEqual(rank1, 1)
        self.assertEqual(rank3, 2)
        self.assertEqual(rank2, 3)
        
        # Test class rank
        self.manager.update_class_leaderboard(str(self.test_class.id))
        
        class_rank1 = self.manager.get_user_rank(
            self.student1, 'class', str(self.test_class.id)
        )
        class_rank2 = self.manager.get_user_rank(
            self.student2, 'class', str(self.test_class.id)
        )
        
        self.assertEqual(class_rank1, 1)
        self.assertEqual(class_rank2, 2)
        
        # Student3 should not have a class rank
        class_rank3 = self.manager.get_user_rank(
            self.student3, 'class', str(self.test_class.id)
        )
        self.assertIsNone(class_rank3)
    
    def test_get_leaderboard_with_pagination(self):
        """Test getting leaderboard with pagination"""
        # Update leaderboard
        self.manager.update_global_leaderboard()
        
        # Get first 2 entries
        leaderboard = self.manager.get_leaderboard(
            leaderboard_type='global',
            limit=2,
            offset=0
        )
        
        self.assertEqual(len(leaderboard), 2)
        self.assertEqual(leaderboard[0]['rank'], 1)
        self.assertEqual(leaderboard[0]['user']['username'], 'student1')
        self.assertEqual(leaderboard[1]['rank'], 2)
        self.assertEqual(leaderboard[1]['user']['username'], 'student3')
        
        # Get next entry
        leaderboard_page2 = self.manager.get_leaderboard(
            leaderboard_type='global',
            limit=2,
            offset=2
        )
        
        self.assertEqual(len(leaderboard_page2), 1)
        self.assertEqual(leaderboard_page2[0]['rank'], 3)
        self.assertEqual(leaderboard_page2[0]['user']['username'], 'student2')
    
    def test_get_nearby_competitors(self):
        """Test getting users ranked near a specific user"""
        # Update leaderboard
        self.manager.update_global_leaderboard()
        
        # Get nearby competitors for student3 (rank 2)
        nearby = self.manager.get_nearby_competitors(
            self.student3,
            leaderboard_type='global',
            range_size=1
        )
        
        # Should include ranks 1, 2, 3 (student3 ± 1)
        self.assertEqual(len(nearby), 3)
        
        # Check that current user is marked
        student3_entry = next(
            entry for entry in nearby 
            if entry['user']['username'] == 'student3'
        )
        self.assertTrue(student3_entry['is_current_user'])
        
        # Check other users are not marked as current
        other_entries = [
            entry for entry in nearby 
            if entry['user']['username'] != 'student3'
        ]
        for entry in other_entries:
            self.assertFalse(entry['is_current_user'])
    
    def test_update_user_leaderboard_position(self):
        """Test updating a specific user's leaderboard position"""
        # Initial leaderboard update
        self.manager.update_global_leaderboard()
        
        # Verify initial rank
        initial_rank = self.manager.get_user_rank(self.student2, 'global')
        self.assertEqual(initial_rank, 3)
        
        # Update student2's points to make them rank higher
        student2_points = UserPoints.objects.get(user=self.student2)
        student2_points.total_points = 350
        student2_points.save()
        
        # Update their leaderboard position
        self.manager.update_user_leaderboard_position(self.student2)
        
        # Check new rank
        new_rank = self.manager.get_user_rank(self.student2, 'global')
        self.assertEqual(new_rank, 1)  # Should now be rank 1
    
    def test_get_leaderboard_stats(self):
        """Test getting leaderboard statistics"""
        # Update leaderboard
        self.manager.update_global_leaderboard()
        
        # Get global stats
        stats = self.manager.get_leaderboard_stats('global')
        
        self.assertEqual(stats['total_participants'], 3)
        self.assertEqual(stats['max_points'], 300)
        self.assertEqual(stats['total_problems_solved'], 1)
        self.assertGreater(stats['average_points'], 0)
        
        # Get class stats
        self.manager.update_class_leaderboard(str(self.test_class.id))
        class_stats = self.manager.get_leaderboard_stats('class', str(self.test_class.id))
        
        self.assertEqual(class_stats['total_participants'], 2)
        self.assertEqual(class_stats['max_points'], 300)
    
    def test_force_refresh_leaderboard(self):
        """Test force refresh functionality"""
        # Create initial leaderboard
        self.manager.update_global_leaderboard()
        
        # Verify entries exist
        initial_count = LeaderboardEntry.objects.filter(
            leaderboard_type='global'
        ).count()
        self.assertEqual(initial_count, 3)
        
        # Force refresh should recreate all entries
        updated_count = self.manager.update_global_leaderboard(force_refresh=True)
        self.assertEqual(updated_count, 3)
        
        # Should still have same number of entries
        final_count = LeaderboardEntry.objects.filter(
            leaderboard_type='global'
        ).count()
        self.assertEqual(final_count, 3)
    
    def test_convenience_functions(self):
        """Test the convenience functions"""
        # Test global leaderboard update function
        updated_count = update_global_leaderboard()
        self.assertEqual(updated_count, 3)
        
        # Test update_user_leaderboard_position function
        from gamification.leaderboard_manager import update_user_leaderboard_position
        
        # This should not raise an exception
        update_user_leaderboard_position(self.student1)
        
        # Verify user still has a rank
        rank = self.manager.get_user_rank(self.student1, 'global')
        self.assertIsNotNone(rank)
    
    def test_error_handling(self):
        """Test error handling in leaderboard manager"""
        # Test with non-existent class
        result = self.manager.update_class_leaderboard('non-existent-class-id')
        self.assertEqual(result, 0)
        
        # Test getting rank for non-existent user entry
        new_user = User.objects.create_user(
            username='newuser',
            email='new@example.com',
            password='testpass123',
            role='student'
        )
        
        rank = self.manager.get_user_rank(new_user, 'global')
        self.assertIsNone(rank)
        
        # Test getting leaderboard for non-existent class
        leaderboard = self.manager.get_leaderboard('class', 'non-existent-class')
        self.assertEqual(len(leaderboard), 0)
    
    def test_username_tie_breaking(self):
        """Test final tie-breaking by username"""
        # Create two users with identical stats
        student_a = User.objects.create_user(
            username='a_student',  # Should rank higher alphabetically
            email='a@example.com',
            password='testpass123',
            role='student'
        )
        
        student_z = User.objects.create_user(
            username='z_student',  # Should rank lower alphabetically
            email='z@example.com',
            password='testpass123',
            role='student'
        )
        
        # Give them identical points and completion stats
        UserPoints.objects.create(
            user=student_a,
            total_points=100,
            practice_points=100,
            assignment_points=0
        )
        
        UserPoints.objects.create(
            user=student_z,
            total_points=100,
            practice_points=100,
            assignment_points=0
        )
        
        # Create identical analytics
        StudentAnalytics.objects.create(
            student=student_a,
            total_practice_completed=0,
            last_activity=timezone.now()
        )
        
        StudentAnalytics.objects.create(
            student=student_z,
            total_practice_completed=0,
            last_activity=timezone.now()
        )
        
        # Update leaderboard
        self.manager.update_global_leaderboard(force_refresh=True)
        
        # Check that username tie-breaking works
        student_a_rank = self.manager.get_user_rank(student_a, 'global')
        student_z_rank = self.manager.get_user_rank(student_z, 'global')
        
        # student_a should rank higher than student_z due to alphabetical order
        self.assertLess(student_a_rank, student_z_rank)