"""
Test WebSocket functionality for real-time notifications.

This module contains tests for the WebSocket consumers and real-time
notification system.
"""

import json
import pytest
from channels.testing import WebsocketCommunicator
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.test import TransactionTestCase
from rest_framework_simplejwt.tokens import AccessToken

from .consumers import LeaderboardConsumer, GameConsumer
from .models import UserPoints, PracticeQuestion, PracticeSubmission

User = get_user_model()


class WebSocketTestCase(TransactionTestCase):
    """Base test case for WebSocket tests"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            role='student'
        )
        
        # Create access token for authentication
        self.token = AccessToken.for_user(self.user)
        self.token_string = str(self.token)
    
    async def create_communicator(self, consumer_class, token=None):
        """Create a WebSocket communicator with authentication"""
        if token is None:
            token = self.token_string
        
        # Add token as query parameter
        communicator = WebsocketCommunicator(
            consumer_class.as_asgi(),
            f"/ws/test/?token={token}"
        )
        
        return communicator


class LeaderboardConsumerTestCase(WebSocketTestCase):
    """Test cases for LeaderboardConsumer"""
    
    @pytest.mark.asyncio
    async def test_leaderboard_connection(self):
        """Test WebSocket connection to leaderboard consumer"""
        communicator = await self.create_communicator(LeaderboardConsumer)
        
        # Test connection
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Test disconnection
        await communicator.disconnect()
    
    @pytest.mark.asyncio
    async def test_leaderboard_authentication_required(self):
        """Test that authentication is required for leaderboard connection"""
        # Try to connect without token
        communicator = WebsocketCommunicator(
            LeaderboardConsumer.as_asgi(),
            "/ws/test/"
        )
        
        connected, subprotocol = await communicator.connect()
        self.assertFalse(connected)
    
    @pytest.mark.asyncio
    async def test_leaderboard_request(self):
        """Test requesting leaderboard data"""
        communicator = await self.create_communicator(LeaderboardConsumer)
        
        # Connect
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Request leaderboard data
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
    
    @pytest.mark.asyncio
    async def test_user_rank_request(self):
        """Test requesting user rank data"""
        communicator = await self.create_communicator(LeaderboardConsumer)
        
        # Connect
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Request user rank
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


class GameConsumerTestCase(WebSocketTestCase):
    """Test cases for GameConsumer"""
    
    @pytest.mark.asyncio
    async def test_game_connection(self):
        """Test WebSocket connection to game consumer"""
        communicator = await self.create_communicator(GameConsumer)
        
        # Test connection
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Test disconnection
        await communicator.disconnect()
    
    @pytest.mark.asyncio
    async def test_game_authentication_required(self):
        """Test that authentication is required for game connection"""
        # Try to connect without token
        communicator = WebsocketCommunicator(
            GameConsumer.as_asgi(),
            "/ws/test/"
        )
        
        connected, subprotocol = await communicator.connect()
        self.assertFalse(connected)
    
    @pytest.mark.asyncio
    async def test_echo_message(self):
        """Test echo functionality"""
        communicator = await self.create_communicator(GameConsumer)
        
        # Connect
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Send test message
        await communicator.send_json_to({
            'type': 'test_message',
            'data': 'hello'
        })
        
        # Receive echo response
        response = await communicator.receive_json_from()
        self.assertEqual(response['type'], 'echo')
        self.assertIn('test_message', response['message'])
        
        await communicator.disconnect()


class RealTimeNotificationTestCase(WebSocketTestCase):
    """Test cases for real-time notifications"""
    
    def setUp(self):
        super().setUp()
        
        # Create test practice question
        self.practice_question = PracticeQuestion.objects.create(
            title='Test Question',
            description='Test description',
            difficulty='easy',
            category='test',
            test_cases=[{'input': '1', 'expected_output': '1'}],
            point_value=100,
            created_by=self.user
        )
    
    @pytest.mark.asyncio
    async def test_achievement_notification(self):
        """Test achievement earned notification"""
        communicator = await self.create_communicator(GameConsumer)
        
        # Connect
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Simulate achievement earned (this would normally be triggered by signals)
        from .realtime_service import realtime_service
        
        achievement_data = {
            'id': '1',
            'name': 'First Steps',
            'description': 'Complete your first practice question',
            'badge_type': 'first_completion',
            'rarity': 'common'
        }
        
        # Send achievement notification
        await database_sync_to_async(realtime_service.notify_achievement_earned)(
            user=self.user,
            achievement_data=achievement_data,
            points_earned=50
        )
        
        # Should receive achievement notification
        response = await communicator.receive_json_from()
        self.assertEqual(response['type'], 'achievement_earned')
        self.assertEqual(response['achievement']['name'], 'First Steps')
        self.assertEqual(response['points_earned'], 50)
        
        await communicator.disconnect()
    
    @pytest.mark.asyncio
    async def test_points_update_notification(self):
        """Test points update notification"""
        communicator = await self.create_communicator(GameConsumer)
        
        # Connect
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Simulate points update
        from .realtime_service import realtime_service
        
        await database_sync_to_async(realtime_service.notify_points_update)(
            user=self.user,
            old_points=0,
            new_points=100,
            source='practice'
        )
        
        # Should receive points update notification
        response = await communicator.receive_json_from()
        self.assertEqual(response['type'], 'points_update')
        self.assertEqual(response['old_points'], 0)
        self.assertEqual(response['new_points'], 100)
        self.assertEqual(response['points_earned'], 100)
        self.assertEqual(response['source'], 'practice')
        
        await communicator.disconnect()
    
    @pytest.mark.asyncio
    async def test_practice_completion_notification(self):
        """Test practice completion notification"""
        communicator = await self.create_communicator(GameConsumer)
        
        # Connect
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        
        # Simulate practice completion
        from .realtime_service import realtime_service
        
        await database_sync_to_async(realtime_service.notify_practice_completed)(
            user=self.user,
            question_title='Test Question',
            points_earned=100,
            attempt_number=1
        )
        
        # Should receive practice completion notification
        response = await communicator.receive_json_from()
        self.assertEqual(response['type'], 'practice_completed')
        self.assertEqual(response['question_title'], 'Test Question')
        self.assertEqual(response['points_earned'], 100)
        self.assertEqual(response['attempt_number'], 1)
        
        await communicator.disconnect()


# Integration test to verify the complete flow
class WebSocketIntegrationTestCase(WebSocketTestCase):
    """Integration tests for WebSocket functionality"""
    
    @pytest.mark.asyncio
    async def test_complete_notification_flow(self):
        """Test complete flow from submission to notification"""
        # This test would require more complex setup with actual submission processing
        # For now, we'll test the individual components
        pass


if __name__ == '__main__':
    # Run tests with pytest
    pytest.main([__file__])