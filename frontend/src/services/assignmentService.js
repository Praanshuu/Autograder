import { api } from './apiClient.js';
import { API_CONFIG } from '../config/api.js';

export const assignmentService = {
  // Get all assignments
  getAssignments: async (params = {}) => {
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.ASSIGNMENTS.LIST}?${queryParams}` : API_CONFIG.ENDPOINTS.ASSIGNMENTS.LIST;
    return await api.get(url);
  },

  // Get assignments for a specific class
  getClassAssignments: async (classId, params = {}) => {
    const allParams = { ...params, class_id: classId };
    const queryParams = new URLSearchParams(allParams).toString();
    const url = `${API_CONFIG.ENDPOINTS.ASSIGNMENTS.LIST}?${queryParams}`;
    return await api.get(url);
  },

  // Get assignment by ID
  getAssignment: async (assignmentId) => {
    return await api.get(API_CONFIG.ENDPOINTS.ASSIGNMENTS.DETAIL(assignmentId));
  },

  // Create new assignment
  createAssignment: async (assignmentData) => {
    return await api.post(API_CONFIG.ENDPOINTS.ASSIGNMENTS.LIST, assignmentData);
  },

  // Update assignment
  updateAssignment: async (assignmentId, assignmentData) => {
    return await api.put(API_CONFIG.ENDPOINTS.ASSIGNMENTS.DETAIL(assignmentId), assignmentData);
  },

  // Delete assignment
  deleteAssignment: async (assignmentId) => {
    return await api.delete(API_CONFIG.ENDPOINTS.ASSIGNMENTS.DETAIL(assignmentId));
  },

  // Publish assignment
  publishAssignment: async (assignmentId) => {
    return await api.post(API_CONFIG.ENDPOINTS.ASSIGNMENTS.PUBLISH(assignmentId));
  },

  // Close assignment
  closeAssignment: async (assignmentId) => {
    return await api.post(API_CONFIG.ENDPOINTS.ASSIGNMENTS.CLOSE(assignmentId));
  },

  // Create Question
  createQuestion: async (questionData) => {
    return await api.post(API_CONFIG.ENDPOINTS.ASSIGNMENTS.QUESTIONS, questionData);
  },

  // Update Question
  updateQuestion: async (questionId, questionData) => {
    return await api.put(API_CONFIG.ENDPOINTS.ASSIGNMENTS.QUESTION_DETAIL(questionId), questionData);
  },
};