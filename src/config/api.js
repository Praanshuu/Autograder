// API Configuration
export const API_CONFIG = {
  BASE_URL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api',
  TIMEOUT: 10000, // 10 seconds
  ENDPOINTS: {
    // Authentication
    AUTH: {
      REGISTER: '/auth/register/',
      LOGIN: '/auth/login/',
      ME: '/users/me/',
      UPDATE_ME: '/users/update_me/',
      SETTINGS: '/users/settings/',
    },
    // Classes
    CLASSES: {
      LIST: '/classes/',
      DETAIL: (id) => `/classes/${id}/`,
      JOIN: (id) => `/classes/${id}/join/`,
      ARCHIVE: (id) => `/classes/${id}/archive/`,
      PEOPLE: (id) => `/classes/${id}/people/`,
    },
    // Assignments
    ASSIGNMENTS: {
      LIST: '/assignments/',
      DETAIL: (id) => `/assignments/${id}/`,
      PUBLISH: (id) => `/assignments/${id}/publish/`,
      CLOSE: (id) => `/assignments/${id}/close/`,
    },
    // Submissions
    SUBMISSIONS: {
      LIST: '/submissions/submissions/',
      DETAIL: (id) => `/submissions/submissions/${id}/`,
      RUN_CODE: '/code/run/',
      GRADE: (id) => `/submissions/submissions/${id}/grade/`,
      PUBLISH: (id) => `/submissions/submissions/${id}/publish/`,
      RUN_AUTOGRADER: '/grading/run-autograder/',
    },
    // Notifications
    NOTIFICATIONS: {
      LIST: '/notifications/',
      DETAIL: (id) => `/notifications/${id}/`,
      MARK_READ: (id) => `/notifications/${id}/mark_read/`,
      MARK_ALL_READ: '/notifications/mark_all_read/',
    },
  },
};