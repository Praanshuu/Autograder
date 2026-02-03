/**
 * React Hook for WebSocket Integration
 * 
 * This hook provides easy WebSocket integration for React components
 * with automatic connection management and cleanup.
 */

import { useEffect, useRef, useCallback, useState } from 'react';
import websocketService from '../services/websocketService.js';

/**
 * Hook for WebSocket connection management
 * @param {string} type - Connection type ('leaderboard' or 'game')
 * @param {Object} options - Connection options
 * @returns {Object} - WebSocket connection state and methods
 */
export const useWebSocket = (type, options = {}) => {
  const [connectionStatus, setConnectionStatus] = useState('disconnected');
  const [lastMessage, setLastMessage] = useState(null);
  const [error, setError] = useState(null);
  const listenersRef = useRef(new Map());
  const optionsRef = useRef(options);

  // Update options ref when options change
  useEffect(() => {
    optionsRef.current = options;
  }, [options]);

  // Connect to WebSocket
  const connect = useCallback(async () => {
    try {
      setError(null);
      setConnectionStatus('connecting');
      
      await websocketService.connect(type, optionsRef.current);
      setConnectionStatus('connected');
    } catch (err) {
      setError(err.message);
      setConnectionStatus('disconnected');
    }
  }, [type]);

  // Disconnect from WebSocket
  const disconnect = useCallback(() => {
    websocketService.disconnect(type);
    setConnectionStatus('disconnected');
  }, [type]);

  // Send message
  const sendMessage = useCallback((message) => {
    websocketService.sendMessage(type, message);
  }, [type]);

  // Add event listener
  const addEventListener = useCallback((eventType, callback) => {
    websocketService.addEventListener(type, eventType, callback);
    
    // Store reference for cleanup
    if (!listenersRef.current.has(eventType)) {
      listenersRef.current.set(eventType, new Set());
    }
    listenersRef.current.get(eventType).add(callback);
  }, [type]);

  // Remove event listener
  const removeEventListener = useCallback((eventType, callback) => {
    websocketService.removeEventListener(type, eventType, callback);
    
    // Remove from our reference
    const listeners = listenersRef.current.get(eventType);
    if (listeners) {
      listeners.delete(callback);
    }
  }, [type]);

  // Monitor connection status
  useEffect(() => {
    const checkStatus = () => {
      const status = websocketService.getConnectionStatus(type);
      setConnectionStatus(status);
    };

    const interval = setInterval(checkStatus, 1000);
    return () => clearInterval(interval);
  }, [type]);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      // Remove all listeners we added
      for (const [eventType, callbacks] of listenersRef.current) {
        for (const callback of callbacks) {
          websocketService.removeEventListener(type, eventType, callback);
        }
      }
      listenersRef.current.clear();
    };
  }, [type]);

  return {
    connectionStatus,
    lastMessage,
    error,
    connect,
    disconnect,
    sendMessage,
    addEventListener,
    removeEventListener,
    isConnected: connectionStatus === 'connected'
  };
};

/**
 * Hook for leaderboard WebSocket connection
 * @param {Object} options - Connection options
 * @returns {Object} - Leaderboard WebSocket state and methods
 */
export const useLeaderboardWebSocket = (options = {}) => {
  const ws = useWebSocket('leaderboard', options);
  const [leaderboardData, setLeaderboardData] = useState(null);
  const [userRank, setUserRank] = useState(null);

  // Handle leaderboard-specific messages
  useEffect(() => {
    const handleLeaderboardUpdate = (data) => {
      setLeaderboardData(data.data);
    };

    const handleUserRankUpdate = (data) => {
      setUserRank(data.data);
    };

    const handleRankChange = (data) => {
      setUserRank(prev => ({
        ...prev,
        user_rank: data.new_rank,
        old_rank: data.old_rank
      }));
    };

    ws.addEventListener('leaderboard_update', handleLeaderboardUpdate);
    ws.addEventListener('initial_global_leaderboard', handleLeaderboardUpdate);
    ws.addEventListener('user_rank_data', handleUserRankUpdate);
    ws.addEventListener('initial_user_rank', handleUserRankUpdate);
    ws.addEventListener('rank_change', handleRankChange);

    return () => {
      ws.removeEventListener('leaderboard_update', handleLeaderboardUpdate);
      ws.removeEventListener('initial_global_leaderboard', handleLeaderboardUpdate);
      ws.removeEventListener('user_rank_data', handleUserRankUpdate);
      ws.removeEventListener('initial_user_rank', handleUserRankUpdate);
      ws.removeEventListener('rank_change', handleRankChange);
    };
  }, [ws]);

  // Request leaderboard data
  const requestLeaderboard = useCallback((leaderboardType = 'global', classId = null, page = 1, pageSize = 20) => {
    ws.sendMessage({
      type: 'request_leaderboard',
      leaderboard_type: leaderboardType,
      class_id: classId,
      page,
      page_size: pageSize
    });
  }, [ws]);

  // Request user rank
  const requestUserRank = useCallback((leaderboardType = 'global', classId = null) => {
    ws.sendMessage({
      type: 'request_user_rank',
      leaderboard_type: leaderboardType,
      class_id: classId
    });
  }, [ws]);

  return {
    ...ws,
    leaderboardData,
    userRank,
    requestLeaderboard,
    requestUserRank
  };
};

/**
 * Hook for game WebSocket connection (achievements, points, etc.)
 * @param {Object} options - Connection options
 * @returns {Object} - Game WebSocket state and methods
 */
export const useGameWebSocket = (options = {}) => {
  const ws = useWebSocket('game', options);
  const [achievements, setAchievements] = useState([]);
  const [points, setPoints] = useState(null);
  const [notifications, setNotifications] = useState([]);

  // Handle game-specific messages
  useEffect(() => {
    const handleAchievementEarned = (data) => {
      const newAchievement = {
        ...data.achievement,
        points_earned: data.points_earned,
        timestamp: new Date()
      };
      
      setAchievements(prev => [newAchievement, ...prev]);
      setNotifications(prev => [...prev, {
        type: 'achievement',
        data: newAchievement,
        id: Date.now()
      }]);
    };

    const handlePointsUpdate = (data) => {
      setPoints({
        old_points: data.old_points,
        new_points: data.new_points,
        points_earned: data.points_earned,
        source: data.source
      });
      
      setNotifications(prev => [...prev, {
        type: 'points',
        data,
        id: Date.now()
      }]);
    };

    const handlePracticeCompleted = (data) => {
      setNotifications(prev => [...prev, {
        type: 'practice_completed',
        data,
        id: Date.now()
      }]);
    };

    const handleAssignmentSubmitted = (data) => {
      setNotifications(prev => [...prev, {
        type: 'assignment_submitted',
        data,
        id: Date.now()
      }]);
    };

    const handleStreakUpdate = (data) => {
      setNotifications(prev => [...prev, {
        type: 'streak_update',
        data,
        id: Date.now()
      }]);
    };

    ws.addEventListener('achievement_earned', handleAchievementEarned);
    ws.addEventListener('points_update', handlePointsUpdate);
    ws.addEventListener('practice_completed', handlePracticeCompleted);
    ws.addEventListener('assignment_submitted', handleAssignmentSubmitted);
    ws.addEventListener('streak_update', handleStreakUpdate);

    return () => {
      ws.removeEventListener('achievement_earned', handleAchievementEarned);
      ws.removeEventListener('points_update', handlePointsUpdate);
      ws.removeEventListener('practice_completed', handlePracticeCompleted);
      ws.removeEventListener('assignment_submitted', handleAssignmentSubmitted);
      ws.removeEventListener('streak_update', handleStreakUpdate);
    };
  }, [ws]);

  // Clear notification
  const clearNotification = useCallback((notificationId) => {
    setNotifications(prev => prev.filter(n => n.id !== notificationId));
  }, []);

  // Clear all notifications
  const clearAllNotifications = useCallback(() => {
    setNotifications([]);
  }, []);

  return {
    ...ws,
    achievements,
    points,
    notifications,
    clearNotification,
    clearAllNotifications
  };
};

/**
 * Hook for authentication-aware WebSocket connections
 * Automatically manages authentication token and reconnection
 */
export const useAuthenticatedWebSocket = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Set authentication token
  const setAuthToken = useCallback((token) => {
    websocketService.setAuthToken(token);
    setIsAuthenticated(!!token);
  }, []);

  // Clear authentication
  const clearAuth = useCallback(() => {
    websocketService.clearAuth();
    setIsAuthenticated(false);
  }, []);

  // Auto-connect when authenticated
  const autoConnect = useCallback(async (types = ['leaderboard', 'game']) => {
    if (!isAuthenticated) return;

    const connections = [];
    for (const type of types) {
      try {
        await websocketService.connect(type);
        connections.push(type);
      } catch (error) {
        console.warn(`Failed to connect to ${type} WebSocket:`, error);
      }
    }
    
    return connections;
  }, [isAuthenticated]);

  return {
    isAuthenticated,
    setAuthToken,
    clearAuth,
    autoConnect
  };
};