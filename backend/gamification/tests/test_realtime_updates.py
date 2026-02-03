"""
Tests for real-time leaderboard and gamification updates.
"""

import json
from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.contrib.auth import get_user_model
from channels.testing import WebsocketCommunicator
from channels.db import database_sync_to_async

from ..consumers import LeaderboardConsumer, GameConsumer
from ..models import UserPoints, PracticeQuestion, PracticeSubmission, LeaderboardEntry
from ..realtime_service import RealtimeService
from classes.models import Class, Enrollment

User = get_user_model()


class RealtimeServiceTest(TestCase):
    """Test the RealtimeService for broadcasting updates."""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.service = RealtimeService()
    
    @patch('gamification.realtime_service.get_channel_layer')
    def test_broadcast_leaderboard_update_global(self, mock_get_channel_layer):
        """Test broadcasting global leaderboard updates."""
        mock_channel_layer = MagicMock()
        mock_get_channel_layer.return_value = mock_channel_layer
        
        # Create new service instance to use mocked channel layer
        service = RealtimeService()
        
        test_data = {'test': 'data'}
        service.broadcast_leaderboard_update('global', data=test_data)
        
        # Verify the correct group and message were sent
        mock_channel_layer.group_send.assert_called_once()
        args, kwargs = mock_channel_layer.group_send.call_args
        
        self.assertEqual(args[0], 'leaderboard_global')
        self.assertEqual(args[1]['type'], 'leaderboard_update')
        self.assertEqual(args[1]['leaderboard_type'], 'global')
        self.assertEqual(args[1]['data'], test_data)
    
    @patch('gamification.realtime_service.get_channel_layer')
    def test_broadcast_leaderboard_update_class(self, mock_get_channel_layer):
        """Test broadcasting class leaderboard updates."""
        mock_channel_layer = MagicMock()
        mock_get_channel_layer.return_value = mock_channel_layer
        
        service = RealtimeService()
        
        class_id = 'test-class-123'
        test_data = {'test': 'data'}
        service.broadcast_leaderboard_update('class', class_id=class_id, data=test_data)
        
        # Verify the correct group and message were sent
        mock_channel_layer.group_send.assert_called_once()
        args, kwargs = mock_channel_layer.group_send.call_args
        
        self.assertEqual(args[0], f'leaderboard_class_{class_id}')
        self.assertEqual(args[1]['type'], 'leaderboard_update')
        self.assertEqual(args[1]['leaderboard_type'], 'class')
        self.assertEqual(args[1]['class_id'], class_id)
        self.assertEqual(args[1]['data'], test_data)
    
    @patch('gamification.realtime_service.get_channel_layer')
    def test_notify_rank_change(self, mock_get_channel_layer):
        """Test notifying users of rank changes."""
        mock_channel_layer = MagicMock()
        mock_get_channel_layer.return_value = mock_channel_layer
        
        service = RealtimeService()
        
        service.notify_rank_change(
            user=self.user,
            old_rank=5,
            new_rank=3,
            leaderboard_type='global'
        )
        
        # Verify the correct user group and message were sent
        mock_channel_layer.group_send.assert_called_once()
        args, kwargs = mock_channel_layer.group_send.call_args
        
        self.assertEqual(args[0], f'user_{self.user.id}')
        self.assertEqual(args[1]['type'], 'rank_change')
        self.assertEqual(args[1]['old_rank'], 5)
        self.assertEqual(args[1]['new_rank'], 3)
        self.assertEqual(args[1]['leaderboard_type'], 'global')
    
    @patch('gamification.realtime_service.get_channel_layer')
    def test_notify_achievement_earned(self, mock_get_channel_layer):
        """Test notifying users of earned achievements."""
        mock_channel_layer = MagicMock()
        mock_get_channel_layer.return_value = mock_channel_layer
        
        service = RealtimeService()
        
        achievement_data = {
            'name': 'First Steps',
            'description': 'Complete your first practice question',
            'badge_type': 'first_completion'
        }
        
        service.notify_achievement_earned(
            user=self.user,
            achievement_data=achievement_data,
            points_earned=50
        )
        
        # Verify the correct user group and message were sent
        mock_channel_layer.group_send.assert_called_once()
        args, kwargs = mock_channel_layer.group_send.call_args
        
        self.assertEqual(args[0], f'user_{self.user.id}')
        self.assertEqual(args[1]['type'], 'achievement_earned')
        self.assertEqual(args[1]['achievement'], achievement_data)
        self.assertEqual(args[1]['points_earned'], 50)
    
    @patch('gamification.realtime_service.get_channel_layer')
    def test_notify_points_update(self, mock_get_channel_layer):
        """Test notifying users of points updates."""
        mock_channel_layer = MagicMock()
        mock_get_channel_layer.return_value = mock_channel_layer
        
        service = RealtimeService()
        
        service.notify_points_update(
            user=self.user,
            old_points=100,
            new_points=150,
            source='practice'
        )
        
        # Verify the correct user group and message were sent
        mock_channel_layer.group_send.assert_called_once()
        args, kwargs = mock_channel_layer.group_send.call_args
        
        self.assertEqual(args[0], f'user_{self.user.id}')
        self.assertEqual(args[1]['type'], 'points_update')
        self.assertEqual(args[1]['old_points'], 100)
        self.assertEqual(args[1]['new_points'], 150)
        self.assertEqual(args[1]['points_earned'], 50)
        self.assertEqual(args[1]['source'], 'practice')
    
    def test_no_channel_layer_graceful_handling(self):
        """Test that service handles missing channel layer gracefully."""
        with patch('gamification.realtime_service.get_channel_layer', return_value=None):
            service = RealtimeService()
            
            # These should not raise exceptions
            service.broadcast_leaderboard_update('global')
            service.notify_rank_change(self.user, 1, 2, 'global')
            service.notify_achievement_earned(self.user, {}, 0)
            service.notify_points_update(self.user, 0, 10, 'test')


class LeaderboardConsumerTest(TestCase):
    """Test the LeaderboardConsumer WebSocket functionality."""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Create some test data
        UserPoints.objects.create(
            user=self.user,
            total_points=100,
            practice_points=60,
            assignment_points=40
        )
    
    async def test_consumer_connect_authenticated(self):
        """Test that authenticated users can connect to the consumer."""
        communicator = WebsocketCommunicator(LeaderboardConsumer.as_asgi(), "/ws/leaderboard/")
        communicator.scope["user"] = self.user
        
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        await communicator.disconnect()
    
    async def test_consumer_reject_anonymous(self):
        """Test that anonymous users are rejected."""
        from django.contrib.auth.models import AnonymousUser
        
        communicator = WebsocketCommunicator(LeaderboardConsumer.as_asgi(), "/ws/leaderboard/")
        communicator.scope["user"] = AnonymousUser()
        
        connected, subprotocol = await communicator.connect()
        self.assertFalse(connected)
    
    async def test_consumer_leaderboard_request(self):
        """Test requesting leaderboard data through WebSocket."""
        communicator = WebsocketCommunicator(LeaderboardConsumer.as_asgi(), "/ws/leaderboard/")
        communicator.scope["user"] = self.user
        
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Send leaderboard request
        await communicator.send_json_to({
            'type': 'request_leaderboard',
            'leaderboard_type': 'global',
            'page': 1,
            'page_size': 10
        })
        
        # Receive response
        response = await communicator.receive_json_from()
        
        self.assertEqual(response['type'], 'leaderboard_data')
        self.assertEqual(response['leaderboard_type'], 'global')
        self.assertIn('data', response)
        
        await communicator.disconnect()
    
    async def test_consumer_user_rank_request(self):
        """Test requesting user rank data through WebSocket."""
        communicator = WebsocketCommunicator(LeaderboardConsumer.as_asgi(), "/ws/leaderboard/")
        communicator.scope["user"] = self.user
        
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Send user rank request
        await communicator.send_json_to({
            'type': 'request_user_rank',
            'leaderboard_type': 'global'
        })
        
        # Receive response
        response = await communicator.receive_json_from()
        
        self.assertEqual(response['type'], 'user_rank_data')
        self.assertEqual(response['leaderboard_type'], 'global')
        self.assertIn('data', response)
        
        await communicator.disconnect()
    
    async def test_consumer_invalid_message(self):
        """Test handling of invalid messages."""
        communicator = WebsocketCommunicator(LeaderboardConsumer.as_asgi(), "/ws/leaderboard/")
        communicator.scope["user"] = self.user
        
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Send invalid message
        await communicator.send_json_to({
            'type': 'invalid_type'
        })
        
        # Receive error response
        response = await communicator.receive_json_from()
        
        self.assertEqual(response['type'], 'error')
        self.assertIn('Unknown message type', response['message'])
        
        await communicator.disconnect()


class GameConsumerTest(TestCase):
    """Test the GameConsumer WebSocket functionality."""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    async def test_game_consumer_connect(self):
        """Test that authenticated users can connect to the game consumer."""
        communicator = WebsocketCommunicator(GameConsumer.as_asgi(), "/ws/game/")
        communicator.scope["user"] = self.user
        
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        await communicator.disconnect()
    
    async def test_game_consumer_echo(self):
        """Test echo functionality of game consumer."""
        communicator = WebsocketCommunicator(GameConsumer.as_asgi(), "/ws/game/")
        communicator.scope["user"] = self.user
        
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Send test message
        await communicator.send_json_to({
            'type': 'test_message'
        })
        
        # Receive echo response
        response = await communicator.receive_json_from()
        
        self.assertEqual(response['type'], 'echo')
        self.assertIn('test_message', response['message'])
        
        await communicator.disconnect()


class IntegrationTest(TestCase):
    """Integration tests for real-time updates with actual models."""
    
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@example.com',
            password='testpass123'
        )
        
        # Create practice question
        self.practice_question = PracticeQuestion.objects.create(
            title='Test Question',
            description='A test question',
            difficulty='easy',
            category='algorithms',
            starter_code='def solution():\n    pass',
            point_value=100,
            test_cases=[{'input': '', 'expected': 'test'}],
            created_by=self.user1
        )
    
    @patch('gamification.realtime_service.get_channel_layer')
    def test_points_update_triggers_realtime_notifications(self, mock_get_channel_layer):
        """Test that points updates trigger real-time notifications."""
        mock_channel_layer = MagicMock()
        mock_get_channel_layer.return_value = mock_channel_layer
        
        from ..points_calculator import PointsCalculator
        
        calculator = PointsCalculator()
        
        # Award points to user
        total_points, points_added = calculator.update_user_points(
            user=self.user1,
            points_to_add=100,
            point_type='practice'
        )
        
        # Verify real-time notifications were sent
        self.assertTrue(mock_channel_layer.group_send.called)
        
        # Check that both points update and leaderboard update were sent
        call_args_list = mock_channel_layer.group_send.call_args_list
        
        # Should have at least points update notification
        points_notification_found = False
        for call_args in call_args_list:
            args, kwargs = call_args
            if args[1].get('type') == 'points_update':
                points_notification_found = True
                self.assertEqual(args[1]['new_points'], 100)
                self.assertEqual(args[1]['points_earned'], 100)
                self.assertEqual(args[1]['source'], 'practice')
                break
        
        self.assertTrue(points_notification_found, "Points update notification not found")
    
    def test_leaderboard_manager_integration(self):
        """Test that LeaderboardManager correctly updates with real-time notifications."""
        from ..models import LeaderboardManager
        
        # Create user points
        UserPoints.objects.create(
            user=self.user1,
            total_points=200,
            practice_points=200,
            assignment_points=0
        )
        UserPoints.objects.create(
            user=self.user2,
            total_points=100,
            practice_points=100,
            assignment_points=0
        )
        
        with patch('gamification.realtime_service.get_channel_layer') as mock_get_channel_layer:
            mock_channel_layer = MagicMock()
            mock_get_channel_layer.return_value = mock_channel_layer
            
            # Update global leaderboard
            LeaderboardManager.update_global_leaderboard()
            
            # Verify leaderboard entries were created
            entries = LeaderboardEntry.objects.filter(leaderboard_type='global').order_by('rank')
            self.assertEqual(len(entries), 2)
            self.assertEqual(entries[0].user, self.user1)  # Higher points = rank 1
            self.assertEqual(entries[0].rank, 1)
            self.assertEqual(entries[1].user, self.user2)  # Lower points = rank 2
            self.assertEqual(entries[1].rank, 2)
            
            # Verify real-time broadcast was sent
            self.assertTrue(mock_channel_layer.group_send.called)