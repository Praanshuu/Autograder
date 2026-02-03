"""
Tests for the LeaderboardViewSet API endpoints.

Tests cover:
- Global leaderboard API endpoints
- Class-specific leaderboard API endpoints
- User ranking and position endpoints
- Pagination functionality
- Permission restrictions
- Error handling
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from datetime import timedelta

from gamification.models import (
    LeaderboardEntry, LeaderboardManager, UserPoints, PracticeQuestion, 
    PracticeProgress
)
from classes.models import Class, Enrollment

User = get_user_model()


class LeaderboardAPITestCase(TestCase):
    """Test cases for Leaderboard API endpoints"""
    
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        
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
        
        # Create teacher
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
        
        # Enroll first 3 users in the class
        for user in self.users[:3]:
            Enrollment.objects.create(
                class_obj=self.test_class,
                user=user,
                role='student'
            )
        
        # Create practice question
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
        point_values = [500, 300, 200, 150, 100]
        for i, user in enumerate(self.users):
            UserPoints.objects.create(
                user=user,
                total_points=point_values[i],
                practice_points=point_values[i],
                assignment_points=0,
                last_updated=timezone.now() - timedelta(minutes=i)
            )
            
            # Create practice progress
            for j in range(i + 1):  # Different numbers of completed problems
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
        
        # Update leaderboards
        LeaderboardManager.update_global_leaderboard()
        LeaderboardManager.update_class_leaderboard(str(self.test_class.id))
    
    def test_global_ranking_endpoint(self):
        """Test global leaderboard ranking endpoint"""
        self.client.force_authenticate(user=self.users[0])
        
        url = reverse('leaderboard-global-ranking')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        leaderboard = response.data['data']['leaderboard']
        self.assertEqual(len(leaderboard), 5)
        
        # Check ranking order
        self.assertEqual(leaderboard[0]['rank'], 1)
        self.assertEqual(leaderboard[0]['user']['username'], 'student0')
        self.assertEqual(leaderboard[0]['total_points'], 500)
        
        # Check pagination
        pagination = response.data['data']['pagination']
        self.assertEqual(pagination['current_page'], 1)
        self.assertEqual(pagination['total_entries'], 5)
    
    def test_global_ranking_pagination(self):
        """Test global leaderboard pagination"""
        self.client.force_authenticate(user=self.users[0])
        
        url = reverse('leaderboard-global-ranking')
        response = self.client.get(url, {'page': 1, 'page_size': 2})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        leaderboard = response.data['data']['leaderboard']
        self.assertEqual(len(leaderboard), 2)
        
        pagination = response.data['data']['pagination']
        self.assertEqual(pagination['current_page'], 1)
        self.assertEqual(pagination['page_size'], 2)
        self.assertTrue(pagination['has_next'])
        self.assertFalse(pagination['has_previous'])
        
        # Test second page
        response = self.client.get(url, {'page': 2, 'page_size': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        leaderboard = response.data['data']['leaderboard']
        self.assertEqual(len(leaderboard), 2)
        
        pagination = response.data['data']['pagination']
        self.assertEqual(pagination['current_page'], 2)
        self.assertTrue(pagination['has_previous'])
    
    def test_class_ranking_endpoint(self):
        """Test class-specific leaderboard ranking endpoint"""
        self.client.force_authenticate(user=self.users[0])
        
        url = reverse('leaderboard-class-ranking')
        response = self.client.get(url, {'class_id': str(self.test_class.id)})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        leaderboard = response.data['data']['leaderboard']
        self.assertEqual(len(leaderboard), 3)  # Only 3 students in class
        
        # Check that only class students are included
        usernames = [entry['user']['username'] for entry in leaderboard]
        self.assertIn('student0', usernames)
        self.assertIn('student1', usernames)
        self.assertIn('student2', usernames)
        self.assertNotIn('student3', usernames)
        self.assertNotIn('student4', usernames)
        
        # Check class_id in response
        self.assertEqual(response.data['data']['class_id'], str(self.test_class.id))
    
    def test_class_ranking_missing_class_id(self):
        """Test class ranking endpoint without class_id parameter"""
        self.client.force_authenticate(user=self.users[0])
        
        url = reverse('leaderboard-class-ranking')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data['success'])
        self.assertIn('class_id parameter is required', response.data['message'])
    
    def test_my_rank_global(self):
        """Test user's rank in global leaderboard"""
        self.client.force_authenticate(user=self.users[2])  # 3rd place user
        
        url = reverse('leaderboard-my-rank')
        response = self.client.get(url, {'type': 'global'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        data = response.data['data']
        self.assertEqual(data['user_rank'], 3)
        self.assertEqual(data['user_points'], 200)
        self.assertEqual(data['user_problems'], 3)
        self.assertEqual(data['leaderboard_type'], 'global')
        
        # Check nearby competitors
        nearby = data['nearby_competitors']
        self.assertGreaterEqual(len(nearby), 3)  # Should have nearby competitors
        
        # Find current user in nearby competitors
        current_user_entry = next(
            (entry for entry in nearby if entry['is_current_user']),
            None
        )
        self.assertIsNotNone(current_user_entry)
        self.assertEqual(current_user_entry['rank'], 3)
    
    def test_my_rank_class(self):
        """Test user's rank in class leaderboard"""
        self.client.force_authenticate(user=self.users[1])  # 2nd place user in class
        
        url = reverse('leaderboard-my-rank')
        response = self.client.get(url, {
            'type': 'class',
            'class_id': str(self.test_class.id)
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        data = response.data['data']
        self.assertEqual(data['user_rank'], 2)
        self.assertEqual(data['leaderboard_type'], 'class')
        self.assertEqual(data['class_id'], str(self.test_class.id))
    
    def test_my_rank_class_missing_class_id(self):
        """Test my rank endpoint for class without class_id"""
        self.client.force_authenticate(user=self.users[0])
        
        url = reverse('leaderboard-my-rank')
        response = self.client.get(url, {'type': 'class'})
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data['success'])
        self.assertIn('class_id is required', response.data['message'])
    
    def test_user_position_endpoint(self):
        """Test user position in all leaderboards"""
        self.client.force_authenticate(user=self.users[0])  # Top user
        
        url = reverse('leaderboard-user-position')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        positions = response.data['data']['user_positions']
        
        # Should have global position
        self.assertIn('global', positions)
        self.assertEqual(positions['global']['rank'], 1)
        self.assertEqual(positions['global']['total_points'], 500)
        
        # Should have class position
        class_key = f"class_{self.test_class.id}"
        self.assertIn(class_key, positions)
        self.assertEqual(positions[class_key]['rank'], 1)
        
        # Check user info
        user_info = response.data['data']['user']
        self.assertEqual(user_info['username'], 'student0')
    
    def test_top_performers_global(self):
        """Test top performers endpoint for global leaderboard"""
        self.client.force_authenticate(user=self.users[0])
        
        url = reverse('leaderboard-top-performers')
        response = self.client.get(url, {'type': 'global', 'limit': 3})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        top_performers = response.data['data']['top_performers']
        self.assertEqual(len(top_performers), 3)
        
        # Check order
        self.assertEqual(top_performers[0]['rank'], 1)
        self.assertEqual(top_performers[0]['user']['username'], 'student0')
        self.assertEqual(top_performers[1]['rank'], 2)
        self.assertEqual(top_performers[1]['user']['username'], 'student1')
    
    def test_top_performers_class(self):
        """Test top performers endpoint for class leaderboard"""
        self.client.force_authenticate(user=self.users[0])
        
        url = reverse('leaderboard-top-performers')
        response = self.client.get(url, {
            'type': 'class',
            'class_id': str(self.test_class.id),
            'limit': 2
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        
        top_performers = response.data['data']['top_performers']
        self.assertEqual(len(top_performers), 2)
        
        # Should only include class students
        usernames = [p['user']['username'] for p in top_performers]
        self.assertIn('student0', usernames)
        self.assertIn('student1', usernames)
    
    def test_refresh_leaderboard_as_teacher(self):
        """Test manual leaderboard refresh as teacher"""
        self.client.force_authenticate(user=self.teacher)
        
        url = reverse('leaderboard-refresh')
        response = self.client.post(url, {'type': 'global'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertIn('Global leaderboard refreshed', response.data['message'])
        self.assertEqual(response.data['entries_updated'], 5)
    
    def test_refresh_leaderboard_as_student_forbidden(self):
        """Test that students cannot refresh leaderboards"""
        self.client.force_authenticate(user=self.users[0])
        
        url = reverse('leaderboard-refresh')
        response = self.client.post(url, {'type': 'global'})
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(response.data['success'])
        self.assertIn('Permission denied', response.data['message'])
    
    def test_refresh_class_leaderboard(self):
        """Test manual class leaderboard refresh"""
        self.client.force_authenticate(user=self.teacher)
        
        url = reverse('leaderboard-refresh')
        response = self.client.post(url, {
            'type': 'class',
            'class_id': str(self.test_class.id)
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertIn('Class leaderboard refreshed', response.data['message'])
        self.assertEqual(response.data['entries_updated'], 3)
    
    def test_unauthenticated_access_forbidden(self):
        """Test that unauthenticated users cannot access leaderboard endpoints"""
        url = reverse('leaderboard-global-ranking')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_user_not_in_leaderboard(self):
        """Test my rank endpoint for user not in leaderboard"""
        # Create user with no points
        user_no_points = User.objects.create_user(
            username='nopoints',
            email='nopoints@example.com',
            password='testpass123',
            role='student'
        )
        
        self.client.force_authenticate(user=user_no_points)
        
        url = reverse('leaderboard-my-rank')
        response = self.client.get(url, {'type': 'global'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data['success'])
        self.assertIn('User not found in leaderboard', response.data['message'])
    
    def test_leaderboard_data_consistency(self):
        """Test that leaderboard data is consistent across endpoints"""
        self.client.force_authenticate(user=self.users[0])
        
        # Get global ranking
        global_url = reverse('leaderboard-global-ranking')
        global_response = self.client.get(global_url)
        global_leaderboard = global_response.data['data']['leaderboard']
        
        # Get top performers
        top_url = reverse('leaderboard-top-performers')
        top_response = self.client.get(top_url, {'type': 'global', 'limit': 5})
        top_performers = top_response.data['data']['top_performers']
        
        # Data should be consistent
        self.assertEqual(len(global_leaderboard), len(top_performers))
        
        for i in range(len(global_leaderboard)):
            self.assertEqual(
                global_leaderboard[i]['user']['username'],
                top_performers[i]['user']['username']
            )
            self.assertEqual(
                global_leaderboard[i]['rank'],
                top_performers[i]['rank']
            )
            self.assertEqual(
                global_leaderboard[i]['total_points'],
                top_performers[i]['total_points']
            )
    
    def test_leaderboard_updates_automatically(self):
        """Test that leaderboards are updated when accessed"""
        self.client.force_authenticate(user=self.users[0])
        
        # Create new user with high points
        new_user = User.objects.create_user(
            username='newchampion',
            email='newchampion@example.com',
            password='testpass123',
            role='student'
        )
        
        UserPoints.objects.create(
            user=new_user,
            total_points=1000,  # Higher than current top user
            practice_points=1000,
            assignment_points=0
        )
        
        # Access global ranking (should trigger update)
        url = reverse('leaderboard-global-ranking')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        leaderboard = response.data['data']['leaderboard']
        
        # New user should be at the top
        self.assertEqual(leaderboard[0]['user']['username'], 'newchampion')
        self.assertEqual(leaderboard[0]['rank'], 1)
        self.assertEqual(leaderboard[0]['total_points'], 1000)
        
        # Previous top user should be rank 2
        self.assertEqual(leaderboard[1]['user']['username'], 'student0')
        self.assertEqual(leaderboard[1]['rank'], 2)