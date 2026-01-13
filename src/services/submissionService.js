import { api } from './apiClient.js';
import { API_CONFIG } from '../config/api.js';

export const submissionService = {
  // Get all submissions
  getSubmissions: async (params = {}) => {
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.SUBMISSIONS.LIST}?${queryParams}` : API_CONFIG.ENDPOINTS.SUBMISSIONS.LIST;
    return await api.get(url);
  },

  // Get submissions for a specific assignment
  getAssignmentSubmissions: async (assignmentId, params = {}) => {
    const allParams = { ...params, assignment_id: assignmentId };
    const queryParams = new URLSearchParams(allParams).toString();
    const url = `${API_CONFIG.ENDPOINTS.SUBMISSIONS.LIST}?${queryParams}`;
    return await api.get(url);
  },

  // Get submission by ID
  getSubmission: async (submissionId) => {
    return await api.get(API_CONFIG.ENDPOINTS.SUBMISSIONS.DETAIL(submissionId));
  },

  // Create/submit code
  submitCode: async (submissionData) => {
    return await api.post(API_CONFIG.ENDPOINTS.SUBMISSIONS.LIST, submissionData);
  },

  // Run code without submitting (for testing)
  runCode: async (codeData) => {
    return await api.post(API_CONFIG.ENDPOINTS.SUBMISSIONS.RUN_CODE, codeData);
  },

  // Grade a submission (Teacher/TA only)
  gradeSubmission: async (submissionId, gradeData) => {
    return await api.put(API_CONFIG.ENDPOINTS.SUBMISSIONS.GRADE(submissionId), gradeData);
  },

  // Publish grade to student (Teacher/Admin only)
  publishGrade: async (submissionId) => {
    return await api.post(API_CONFIG.ENDPOINTS.SUBMISSIONS.PUBLISH(submissionId));
  },

  // Run autograder on all submissions for an assignment
  runAutograder: async (assignmentId) => {
    return await api.post(API_CONFIG.ENDPOINTS.SUBMISSIONS.RUN_AUTOGRADER, { assignment_id: assignmentId });
  },
};