# Real-time Notification System

This document describes the WebSocket-based real-time notification system implemented for the gamified autograder.

## Overview

The system provides real-time updates for:
- Leaderboard changes
- Achievement notifications
- Points updates
- Practice question completions
- Assignment submissions

## Architecture

### Backend Components

1. **WebSocket Consumers** (`consumers.py`)
   - `LeaderboardConsumer`: Handles leaderboard updates and rank changes
   - `GameConsumer`: Handles general gamification events (achievements, points, etc.)

2. **Authentication Middleware** (`middleware.py`)
   - `JWTAuthMiddleware`: Authenticates WebSocket connections using JWT tokens
   - Extracts tokens from query parameters: `ws://localhost:8000/ws/game/?token=<jwt_token>`

3. **Real-time Service** (`realtime_service.py`)
   - Centralized service for broadcasting WebSocket messages
   - Handles different types of notifications (achievements, points, leaderboard updates)

4. **Signal Handlers** (`signals.py`)
   - Automatically trigger real-time notifications when database events occur
   - Integrated with existing submission processing workflow

### Frontend Components

1. **WebSocket Service** (`frontend/src/services/websocketService.js`)
   - Manages WebSocket connections with authentication
   - Handles reconnection logic and error handling
   - Provides event-based API for components

2. **React Hooks** (`frontend/src/hooks/useWebSocket.js`)
   - `useWebSocket`: Basic WebSocket connection management
   - `useLeaderboardWebSocket`: Specialized hook for leaderboard updates
   - `useGameWebSocket`: Specialized hook for game events
   - `useAuthenticatedWebSocket`: Authentication-aware connection management

3. **Notification Components** (`frontend/src/components/features/gamification/NotificationToast.jsx`)
   - Toast notifications for achievements, points, etc.
   - Animated notification container with stacking

4. **Gamification Context** (`frontend/src/contexts/GamificationContext.jsx`)
   - Centralized state management for gamification features
   - Global notification handling

## WebSocket Endpoints

### `/ws/leaderboard/`
Handles leaderboard-related real-time updates.

**Incoming Messages:**
```json
{
  "type": "request_leaderboard",
  "leaderboard_type": "global|class",
  "class_id": "optional-class-id",
  "page": 1,
  "page_size": 20
}
```

```json
{
  "type": "request_user_rank",
  "leaderboard_type": "global|class",
  "class_id": "optional-class-id"
}
```

**Outgoing Messages:**
```json
{
  "type": "leaderboard_update",
  "leaderboard_type": "global|class",
  "class_id": "optional-class-id",
  "data": { /* leaderboard data */ }
}
```

```json
{
  "type": "rank_change",
  "old_rank": 5,
  "new_rank": 3,
  "leaderboard_type": "global|class",
  "class_id": "optional-class-id"
}
```

### `/ws/game/`
Handles general gamification events.

**Outgoing Messages:**
```json
{
  "type": "achievement_earned",
  "achievement": {
    "id": "1",
    "name": "First Steps",
    "description": "Complete your first practice question",
    "badge_type": "first_completion",
    "rarity": "common"
  },
  "points_earned": 50
}
```

```json
{
  "type": "points_update",
  "old_points": 100,
  "new_points": 200,
  "points_earned": 100,
  "source": "practice|assignment"
}
```

```json
{
  "type": "practice_completed",
  "question_title": "Array Basics",
  "points_earned": 100,
  "attempt_number": 1
}
```

## Authentication

WebSocket connections require JWT authentication via query parameters:

```javascript
const token = localStorage.getItem('access_token');
const wsUrl = `ws://localhost:8000/ws/game/?token=${token}`;
const ws = new WebSocket(wsUrl);
```

## Usage Examples

### Frontend Integration

```javascript
import { useGameWebSocket } from '../hooks/useWebSocket';

function MyComponent() {
  const {
    isConnected,
    achievements,
    points,
    notifications,
    clearNotification
  } = useGameWebSocket();

  return (
    <div>
      <div>Connection: {isConnected ? 'Connected' : 'Disconnected'}</div>
      <div>Recent achievements: {achievements.length}</div>
      <div>Current points: {points?.new_points || 0}</div>
    </div>
  );
}
```

### Backend Notification Triggering

```python
from gamification.realtime_service import realtime_service

# Notify achievement earned
realtime_service.notify_achievement_earned(
    user=student,
    achievement_data={
        'id': '1',
        'name': 'First Steps',
        'description': 'Complete your first practice question',
        'badge_type': 'first_completion',
        'rarity': 'common'
    },
    points_earned=50
)

# Notify points update
realtime_service.notify_points_update(
    user=student,
    old_points=100,
    new_points=200,
    source='practice'
)
```

## Configuration

### Django Settings

```python
# Channel Layers Configuration
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}

# ASGI Application
ASGI_APPLICATION = 'autograder.asgi.application'
```

### Frontend Configuration

```javascript
// API Configuration
export const API_CONFIG = {
  WS_BASE_URL: 'ws://127.0.0.1:8000',
  // ... other config
};
```

## Error Handling

### Backend
- Invalid JWT tokens result in connection rejection
- Database errors are logged but don't crash the WebSocket connection
- Graceful handling of missing user data

### Frontend
- Automatic reconnection with exponential backoff
- Fallback to REST API polling when WebSocket unavailable
- Error boundaries prevent crashes from WebSocket errors

## Testing

Run WebSocket tests:
```bash
cd backend
python -m pytest gamification/test_websockets.py -v
```

## Deployment Considerations

1. **Redis**: Required for Django Channels message passing
2. **WebSocket Support**: Ensure your deployment supports WebSocket connections
3. **Load Balancing**: Use sticky sessions if load balancing WebSocket connections
4. **Security**: Use WSS (WebSocket Secure) in production
5. **Monitoring**: Monitor WebSocket connection counts and message throughput

## Troubleshooting

### Common Issues

1. **Connection Refused**: Check Redis is running and accessible
2. **Authentication Failed**: Verify JWT token is valid and not expired
3. **Messages Not Received**: Check signal handlers are properly connected
4. **High Memory Usage**: Monitor Redis memory usage and connection counts

### Debug Mode

Enable WebSocket debugging in Django settings:
```python
LOGGING = {
    'loggers': {
        'gamification.consumers': {
            'level': 'DEBUG',
        },
        'gamification.realtime_service': {
            'level': 'DEBUG',
        },
    }
}
```