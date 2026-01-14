import { api } from './apiClient.js';
import { API_CONFIG } from '../config/api.js';

export const classService = {
  // Get all classes for current user
  getClasses: async (params = {}) => {
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.CLASSES.LIST}?${queryParams}` : API_CONFIG.ENDPOINTS.CLASSES.LIST;
    return await api.get(url);
  },

  // Get archived classes
  getArchivedClasses: async () => {
    return await api.get(`${API_CONFIG.ENDPOINTS.CLASSES.LIST}?archived=true`);
  },

  // Get class by ID
  getClass: async (classId) => {
    return await api.get(API_CONFIG.ENDPOINTS.CLASSES.DETAIL(classId));
  },

  // Create new class
  createClass: async (classData) => {
    return await api.post(API_CONFIG.ENDPOINTS.CLASSES.LIST, classData);
  },

  // Update class
  updateClass: async (classId, classData) => {
    return await api.put(API_CONFIG.ENDPOINTS.CLASSES.DETAIL(classId), classData);
  },

  // Delete class
  deleteClass: async (classId) => {
    return await api.delete(API_CONFIG.ENDPOINTS.CLASSES.DETAIL(classId));
  },

  // Join class with join code (via ID)
  joinClass: async (classId, joinCode) => {
    return await api.post(API_CONFIG.ENDPOINTS.CLASSES.JOIN(classId), { join_code: joinCode });
  },

  // Join class by code only (no ID needed)
  joinClassByCode: async (joinCode) => {
    return await api.post(`${API_CONFIG.ENDPOINTS.CLASSES.LIST}join-by-code/`, { join_code: joinCode });
  },

  // Archive/unarchive class
  archiveClass: async (classId) => {
    return await api.post(API_CONFIG.ENDPOINTS.CLASSES.ARCHIVE(classId));
  },

  // Get class people/roster
  getClassPeople: async (classId) => {
    return await api.get(API_CONFIG.ENDPOINTS.CLASSES.PEOPLE(classId));
  },

  // Get gradebook data
  getClassGrades: async (classId) => {
    return await api.get(`${API_CONFIG.ENDPOINTS.CLASSES.DETAIL(classId)}grades/`);
  },
};