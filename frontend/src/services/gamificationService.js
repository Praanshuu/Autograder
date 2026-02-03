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
  // Points Management
  getUserPoints: async () => {
    const response = await api.get(API_CONFIG.ENDPOINTS.GAMIFICATION.POINTS);
    
    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback points data - gamification API not available');
      return { success: true, data: FALLBACK_DATA.points };
    }
    
    return response;
  },

  getPointsHistory: async (params = {}) => {
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.GAMIFICATION.POINTS}history/?${queryParams}` : `${API_CONFIG.ENDPOINTS.GAMIFICATION.POINTS}history/`;
    const response = await api.get(url);
    
    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback points history - gamification API not available');
      return { success: true, data: FALLBACK_DATA.pointsHistory };
    }
    
    return response;
  },

  // Leaderboard Management
  getLeaderboard: async (type = 'global', classId = null, limit = 50) => {
    const params = { type, limit };
    if (classId) params.class_id = classId;
    
    const queryParams = new URLSearchParams(params).toString();
    const response = await api.get(`${API_CONFIG.ENDPOINTS.GAMIFICATION.LEADERBOARD}?${queryParams}`);
    
    if (shouldUseFallbackData(response)) {
      console.warn('Using fallback leaderboard data - gamification API not available');
      return { success: true, data: FALLBACK_DATA.leaderboard };
    }
    
    return response;
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
};