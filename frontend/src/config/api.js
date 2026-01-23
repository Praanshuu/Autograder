// API Configuration
export const API_CONFIG = {
  BASE_URL: import.meta.env.VITE_API_BASE_URL || '/api',
  TIMEOUT: 10000, // 10 seconds
  ENDPOINTS: {
    // Authentication
    AUTH: {
      REGISTER: '/users/register/',
      LOGIN: '/auth/simple-login/',  // Use working function-based view
      ME: '/users/me/',  // Use working function-based view
      UPDATE_ME: '/users/update_me/',
      SETTINGS: '/users/settings/',
      REQUEST_PASSWORD_RESET: '/users/request_password_reset/',
      RESET_PASSWORD_CONFIRM: '/users/reset_password_confirm/',
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
      QUESTIONS: '/assignments/questions/',
    },
    // Submissions
    SUBMISSIONS: {
      LIST: '/submissions/attempts/',
      DETAIL: (id) => `/submissions/attempts/${id}/`,
      RUN_CODE: '/submissions/attempts/run/',
      GRADE: (id) => `/submissions/attempts/${id}/grade/`,
      PUBLISH: (id) => `/submissions/attempts/${id}/publish/`,
      RUN_AUTOGRADER: '/submissions/grading/run-autograder/',
      SAMPLE_QUESTIONS: '/submissions/sample-questions/',
      SYSTEM_STATUS: '/submissions/system-status/',
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