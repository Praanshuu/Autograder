import { api } from './apiClient.js';
import { API_CONFIG } from '../config/api.js';

export const practiceService = {
  // Practice Questions Management
  getPracticeQuestions: async (params = {}) => {
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_QUESTIONS}?${queryParams}` : API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_QUESTIONS;
    return await api.get(url);
  },

  getPracticeQuestion: async (questionId) => {
    return await api.get(API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_QUESTION_DETAIL(questionId));
  },

  createPracticeQuestion: async (questionData) => {
    return await api.post(API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_QUESTIONS, questionData);
  },

  updatePracticeQuestion: async (questionId, questionData) => {
    return await api.put(API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_QUESTION_DETAIL(questionId), questionData);
  },

  deletePracticeQuestion: async (questionId) => {
    return await api.delete(API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_QUESTION_DETAIL(questionId));
  },

  // Practice Question Library
  getPracticeLibrary: async (params = {}) => {
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_LIBRARY}?${queryParams}` : API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_LIBRARY;
    return await api.get(url);
  },

  // Practice Submissions (for teachers to view)
  getPracticeSubmissions: async (params = {}) => {
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_SUBMISSIONS}?${queryParams}` : API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_SUBMISSIONS;
    return await api.get(url);
  },

  // Practice Progress (for teachers to view)
  getPracticeProgress: async (params = {}) => {
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_PROGRESS}?${queryParams}` : API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_PROGRESS;
    return await api.get(url);
  },

  // Practice Analytics
  getPracticeAnalytics: async (endpoint = 'summary', params = {}) => {
    const queryParams = new URLSearchParams(params).toString();
    const url = queryParams ? `${API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_ANALYTICS}${endpoint}/?${queryParams}` : `${API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_ANALYTICS}${endpoint}/`;
    return await api.get(url);
  },

  // Practice Session Management
  startPracticeSession: async (questionId) => {
    // This is a placeholder - in practice mode, sessions are tracked automatically
    // when students first access a question. No explicit API call needed.
    return Promise.resolve({ success: true });
  },

  // Code Execution for Practice
  runPracticeCode: async (questionId, codeData) => {
    return await api.post(`${API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_QUESTIONS}${questionId}/run_code/`, {
      source_code: codeData.code,
      language: codeData.language
    });
  },

  // Practice Code Submission
  submitPracticeCode: async (questionId, codeData) => {
    return await api.post(`${API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_QUESTIONS}${questionId}/submit/`, {
      source_code: codeData.code,
      language: codeData.language
    });
  },
};