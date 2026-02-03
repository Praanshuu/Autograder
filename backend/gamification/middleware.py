"""
WebSocket authentication middleware for JWT tokens.

This middleware handles JWT authentication for WebSocket connections,
allowing authenticated users to connect to real-time gamification features.
"""

import logging
from urllib.parse import parse_qs
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

logger = logging.getLogger(__name__)
User = get_user_model()


@database_sync_to_async
def get_user_from_token(token_string):
    """
    Get user from JWT token string.
    
    Args:
        token_string: JWT token string
        
    Returns:
        User instance or AnonymousUser if invalid
    """
    try:
        # Validate and decode the token
        token = AccessToken(token_string)
        user_id = token.payload.get('user_id')
        
        if not user_id:
            return AnonymousUser()
        
        # Get user from database
        user = User.objects.get(id=user_id)
        return user
        
    except (InvalidToken, TokenError) as e:
        logger.warning(f"Invalid WebSocket authentication token: {e}")
        return AnonymousUser()
    except User.DoesNotExist as e:
        logger.warning(f"User not found: {e}")
        return AnonymousUser()
    except Exception as e:
        logger.error(f"Error authenticating WebSocket user: {e}")
        return AnonymousUser()


class JWTAuthMiddleware(BaseMiddleware):
    """
    JWT authentication middleware for WebSocket connections.
    
    This middleware extracts JWT tokens from WebSocket query parameters
    and authenticates users for real-time features.
    
    Usage:
        Add token as query parameter: ws://localhost:8000/ws/game/?token=<jwt_token>
    """
    
    async def __call__(self, scope, receive, send):
        """
        Authenticate WebSocket connection using JWT token.
        
        Args:
            scope: ASGI scope dictionary
            receive: ASGI receive callable
            send: ASGI send callable
        """
        # Close old database connections to prevent usage of timed out connections
        close_old_connections()
        
        # Extract token from query parameters
        query_params = parse_qs(scope.get("query_string", b"").decode())
        token_list = query_params.get("token", [])
        
        if token_list:
            token_string = token_list[0]
            scope["user"] = await get_user_from_token(token_string)
        else:
            # No token provided, set as anonymous user
            scope["user"] = AnonymousUser()
        
        # Continue with the WebSocket connection
        return await super().__call__(scope, receive, send)


def JWTAuthMiddlewareStack(inner):
    """
    Convenience function to create JWT auth middleware stack.
    
    Args:
        inner: Inner ASGI application
        
    Returns:
        Middleware stack with JWT authentication
    """
    return JWTAuthMiddleware(inner)