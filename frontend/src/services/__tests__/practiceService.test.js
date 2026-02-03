import { describe, it, expect, vi, beforeEach } from 'vitest';
import { practiceService } from '../practiceService';
import { api } from '../apiClient';

// Mock the API client
vi.mock('../apiClient', () => ({
  api: {
    get: vi.fn(),
    post: vi.fn(),
    put: vi.fn(),
    delete: vi.fn(),
  }
}));

describe('practiceService', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('getPracticeQuestions', () => {
    it('should fetch practice questions without parameters', async () => {
      const mockResponse = { data: { results: [] } };
      api.get.mockResolvedValue(mockResponse);

      const result = await practiceService.getPracticeQuestions();

      expect(api.get).toHaveBeenCalledWith('/gamification/practice-questions/');
      expect(result).toBe(mockResponse);
    });

    it('should fetch practice questions with parameters', async () => {
      const mockResponse = { data: { results: [] } };
      api.get.mockResolvedValue(mockResponse);

      const params = { difficulty: 'easy', category: 'Arrays' };
      const result = await practiceService.getPracticeQuestions(params);

      expect(api.get).toHaveBeenCalledWith('/gamification/practice-questions/?difficulty=easy&category=Arrays');
      expect(result).toBe(mockResponse);
    });
  });

  describe('createPracticeQuestion', () => {
    it('should create a new practice question', async () => {
      const mockResponse = { data: { id: 1, title: 'Test Question' } };
      api.post.mockResolvedValue(mockResponse);

      const questionData = {
        title: 'Test Question',
        description: 'A test question',
        difficulty: 'easy',
        category: 'Arrays',
        point_value: 100,
        test_cases: []
      };

      const result = await practiceService.createPracticeQuestion(questionData);

      expect(api.post).toHaveBeenCalledWith('/gamification/practice-questions/', questionData);
      expect(result).toBe(mockResponse);
    });
  });

  describe('updatePracticeQuestion', () => {
    it('should update an existing practice question', async () => {
      const mockResponse = { data: { id: 1, title: 'Updated Question' } };
      api.put.mockResolvedValue(mockResponse);

      const questionId = '123';
      const questionData = {
        title: 'Updated Question',
        description: 'An updated question',
        difficulty: 'medium'
      };

      const result = await practiceService.updatePracticeQuestion(questionId, questionData);

      expect(api.put).toHaveBeenCalledWith('/gamification/practice-questions/123/', questionData);
      expect(result).toBe(mockResponse);
    });
  });

  describe('deletePracticeQuestion', () => {
    it('should delete a practice question', async () => {
      const mockResponse = { status: 204 };
      api.delete.mockResolvedValue(mockResponse);

      const questionId = '123';
      const result = await practiceService.deletePracticeQuestion(questionId);

      expect(api.delete).toHaveBeenCalledWith('/gamification/practice-questions/123/');
      expect(result).toBe(mockResponse);
    });
  });

  describe('getPracticeLibrary', () => {
    it('should fetch practice library questions', async () => {
      const mockResponse = { data: { results: [] } };
      api.get.mockResolvedValue(mockResponse);

      const result = await practiceService.getPracticeLibrary();

      expect(api.get).toHaveBeenCalledWith('/gamification/practice-library/');
      expect(result).toBe(mockResponse);
    });
  });
});