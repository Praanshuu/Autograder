import { api } from './apiClient.js';
import { API_CONFIG } from '../config/api.js';

export const notificationService = {
  // Get all notifications for current user
  getNotifications: async (params = {}) => {
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.NOTIFICATIONS.LIST}?${queryParams}` : API_CONFIG.ENDPOINTS.NOTIFICATIONS.LIST;
    return await api.get(url);
  },

  // Get unread notifications only
  getUnreadNotifications: async () => {
    return await api.get(`${API_CONFIG.ENDPOINTS.NOTIFICATIONS.LIST}?unread_only=true`);
  },

  // Get notification by ID
  getNotification: async (notificationId) => {
    return await api.get(API_CONFIG.ENDPOINTS.NOTIFICATIONS.DETAIL(notificationId));
  },

  // Mark notification as read
  markAsRead: async (notificationId) => {
    return await api.put(API_CONFIG.ENDPOINTS.NOTIFICATIONS.MARK_READ(notificationId));
  },

  // Mark all notifications as read
  markAllAsRead: async () => {
    return await api.put(API_CONFIG.ENDPOINTS.NOTIFICATIONS.MARK_ALL_READ);
  },

  // Create notification (if needed)
  createNotification: async (notificationData) => {
    return await api.post(API_CONFIG.ENDPOINTS.NOTIFICATIONS.LIST, notificationData);
  },
};