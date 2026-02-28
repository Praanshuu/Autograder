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

  deletePracticeLibraryEntry: async (entryId) => {
    return await api.delete(`${API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_LIBRARY}${entryId}/`);
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
  startPracticeSession: async () => {
    // Sessions are tracked automatically when students first access a question
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
  submitPracticeCode: async (questionId, payload) => {
    // Pass payload as-is: supports both coding { source_code, language }
    // and MCQ { selected_option } submission formats.
    return await api.post(`${API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_QUESTIONS}${questionId}/submit/`, payload);
  },

  // Time tracking: records cumulative seconds spent on a practice question
  updateTimeSpent: async (questionId, timeSpentSeconds) => {
    return await api.post(`${API_CONFIG.ENDPOINTS.GAMIFICATION.PRACTICE_PROGRESS}update_time/`, {
      practice_question_id: questionId,
      time_spent: timeSpentSeconds,
    });
  },
};