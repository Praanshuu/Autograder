import { api } from './apiClient.js';
import { API_CONFIG } from '../config/api.js';

// Helper function to check if we should use fallback data
const shouldUseFallbackData = (response) => {
  return !response.success && (
    response.status === 404 ||
    response.status === 500 ||
    response.message?.includes('Failed to fetch') ||
    response.message?.includes('Network Error')
  );
};

// Minimal fallback data for when API is unavailable
const FALLBACK_DATA = {
  points: { total_points: 0, practice_points: 0, assignment_points: 0 },
  leaderboard: [],
  userRank: { rank: 0, total_points: 0 },
  achievements: [],
  pointsHistory: []
};

export const gamificationService = {
  getUserPoints: async () => {
    // Call the specific DRF @action that builds the PointsCalculator summary
    const response = await api.get(`${API_CONFIG.ENDPOINTS.GAMIFICATION.POINTS}my_points/`);

    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback points data - gamification API not available');
      return { success: true, data: FALLBACK_DATA.points };
    }

    // `my_points` returns { user: {...}, points: { total_points, ... } }
    // We return data.points so PointsDisplay.jsx can read newPoints.total_points
    return {
      success: response.success,
      data: response.data?.points || FALLBACK_DATA.points,
    };
  },

  getPointsHistory: async (params = {}) => {
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.GAMIFICATION.POINTS}point_history/?${queryParams}` : `${API_CONFIG.ENDPOINTS.GAMIFICATION.POINTS}point_history/`;
    const response = await api.get(url);

    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback points history - gamification API not available');
      return { success: true, data: FALLBACK_DATA.pointsHistory };
    }

    return response;
  },

  // Leaderboard Management
  // Uses the /points/leaderboard/ endpoint which reads UserPoints directly
  // (the /leaderboard/ endpoint uses LeaderboardEntry which is a stale cache table)
  getLeaderboard: async (type = 'global', classId = null, limit = 50) => {
    const params = { limit };
    const queryParams = new URLSearchParams(params).toString();
    const response = await api.get(`${API_CONFIG.ENDPOINTS.GAMIFICATION.POINTS}leaderboard/?${queryParams}`);

    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback leaderboard data - gamification API not available');
      return { success: true, data: { leaderboard: [] } };
    }

    // The points/leaderboard/ endpoint returns { leaderboard: [{user, rank, total_points, ...}], ... }
    // Normalise each entry to have a nested user object (same shape as LeaderboardWidget expects)
    const raw = response.data?.leaderboard || [];
    const normalised = raw.map(entry => ({
      rank: entry.rank,
      total_points: entry.total_points ?? entry.points?.total_points ?? 0,
      completed_problems: entry.completed_problems ?? 0,
      user: entry.user ?? { id: null, username: entry.username, first_name: entry.first_name ?? entry.username, last_name: entry.last_name ?? '' },
    }));

    return { success: true, data: { leaderboard: normalised }, status: response.status };
  },

  getUserRank: async (type = 'global', classId = null) => {
    const params = { type };
    if (classId) params.class_id = classId;

    const queryParams = new URLSearchParams(params).toString();
    const response = await api.get(`${API_CONFIG.ENDPOINTS.GAMIFICATION.LEADERBOARD}my_rank/?${queryParams}`);

    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback user rank - gamification API not available');
      return { success: true, data: FALLBACK_DATA.userRank };
    }

    return response;
  },

  // Achievements Management
  getUserAchievements: async () => {
    const response = await api.get(`${API_CONFIG.ENDPOINTS.GAMIFICATION.ACHIEVEMENTS}earned/`);

    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback achievements data - gamification API not available');
      return { success: true, data: FALLBACK_DATA.achievements };
    }

    return response;
  },

  getAvailableAchievements: async () => {
    const response = await api.get(`${API_CONFIG.ENDPOINTS.GAMIFICATION.ACHIEVEMENTS}available/`);

    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback available achievements - gamification API not available');
      return { success: true, data: FALLBACK_DATA.achievements };
    }

    return response;
  },

  getAllAchievements: async () => {
    const response = await api.get(API_CONFIG.ENDPOINTS.GAMIFICATION.ACHIEVEMENTS);

    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback all achievements - gamification API not available');
      return { success: true, data: FALLBACK_DATA.achievements };
    }

    return response;
  },

  // Analytics
  getStudentAnalytics: async () => {
    const response = await api.get(`${API_CONFIG.ENDPOINTS.GAMIFICATION.ANALYTICS}student_dashboard/`);

    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback analytics data - gamification API not available');
      return { success: true, data: { message: 'Analytics not available yet' } };
    }

    return response;
  },

  getClassAnalytics: async (classId) => {
    const params = classId ? { class_id: classId } : {};
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.GAMIFICATION.ANALYTICS}class_overview/?${queryParams}` : `${API_CONFIG.ENDPOINTS.GAMIFICATION.ANALYTICS}class_overview/`;
    const response = await api.get(url);

    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback class analytics - gamification API not available');
      return { success: true, data: { message: 'Class analytics not available yet' } };
    }

    return response;
  },

  getPerformanceTrends: async (days = 30) => {
    const params = { days };
    const queryParams = new URLSearchParams(params).toString();
    const response = await api.get(`${API_CONFIG.ENDPOINTS.GAMIFICATION.ANALYTICS}performance_trends/?${queryParams}`);

    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback performance trends - gamification API not available');
      return { success: true, data: { message: 'Performance trends not available yet' } };
    }

    return response;
  },

  // Comprehensive student performance (weekly activity, difficulty, language breakdown)
  getStudentPerformance: async (timeframe = '30d') => {
    const response = await api.get(`${API_CONFIG.ENDPOINTS.GAMIFICATION.ANALYTICS}student_performance/?timeframe=${timeframe}`);
    if (shouldUseFallbackData(response)) {
      return { success: false, data: null };
    }
    return response;
  },

  // Point earning history
  getPointHistory: async (days = 30) => {
    const response = await api.get(`${API_CONFIG.ENDPOINTS.GAMIFICATION.POINTS}point_history/?days=${days}`);
    if (shouldUseFallbackData(response)) {
      return { success: true, data: { history: [] } };
    }
    return response;
  },
};