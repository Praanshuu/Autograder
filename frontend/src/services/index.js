// Main services export
export { api } from './apiClient.js';
export { authService } from './authService.js';
export { classService } from './classService.js';
export { assignmentService } from './assignmentService.js';
export { submissionService } from './submissionService.js';
export { notificationService } from './notificationService.js';
export { practiceService } from './practiceService.js';
export { gamificationService } from './gamificationService.js';

// Re-export utilities
export { tokenManager } from '../utils/tokenManager.js';
export { API_CONFIG } from '../config/api.js';