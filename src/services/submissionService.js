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

  // Run code without submitting (for testing) - Enhanced with better error handling
  runCode: async (data) => {
    try {
      const response = await api.post(API_CONFIG.ENDPOINTS.SUBMISSIONS.RUN_CODE, data);
      return response;
    } catch (error) {
      // Handle different types of errors
      if (error.response?.status === 429) {
        throw new Error('Rate limit exceeded. Please wait before running code again.');
      } else if (error.response?.status === 400) {
        throw new Error(error.response.data.message || 'Invalid request');
      } else if (error.response?.status >= 500) {
        throw new Error('Server error. Please try again later.');
      } else {
        throw new Error(error.response?.data?.message || 'Failed to run code');
      }
    }
  },

  // Get sample questions for testing
  getSampleQuestions: async () => {
    try {
      const response = await api.get(API_CONFIG.ENDPOINTS.SUBMISSIONS.SAMPLE_QUESTIONS);
      return response;
    } catch (error) {
      throw new Error('Failed to load sample questions');
    }
  },

  // Get system status (for monitoring)
  getSystemStatus: async () => {
    try {
      const response = await api.get(API_CONFIG.ENDPOINTS.SUBMISSIONS.SYSTEM_STATUS);
      return response;
    } catch (error) {
      throw new Error('Failed to get system status');
    }
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
  
  // Timer tracking methods
  startTimer: async (assignmentId, questionId) => {
    return await api.post('/submissions/start-timer/', {
      assignment_id: assignmentId,
      question_id: questionId
    });
  },
  
  updateTimer: async (assignmentId, questionId, timeSpent) => {
    return await api.post('/submissions/update-timer/', {
      assignment_id: assignmentId,
      question_id: questionId,
      time_spent: timeSpent
    });
  },
  
  getTimer: async (assignmentId, questionId) => {
    return await api.get(`/submissions/get-timer/?assignment_id=${assignmentId}&question_id=${questionId}`);
  },
};