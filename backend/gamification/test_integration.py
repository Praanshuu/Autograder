from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import PracticeQuestion, PracticeQuestionLibrary

User = get_user_model()


class PracticeQuestionIntegrationTestCase(TestCase):
    """Integration tests for the complete practice question workflow"""
    
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        
        # Create test users
        self.teacher = User.objects.create_user(
            username='teacher1',
            email='teacher@test.com',
            password='testpass123',
            role='teacher'
        )
        
        self.student = User.objects.create_user(
            username='student1',
            email='student@test.com',
            password='testpass123',
            role='student'
        )
    
    def test_complete_practice_question_workflow(self):
        """Test the complete workflow from creation to submission"""
        
        # 1. Teacher creates a practice question
        self.client.force_authenticate(user=self.teacher)
        create_url = reverse('practice-questions-list')
        
        question_data = {
            'title': 'Sum Two Numbers',
            'description': 'Write a function that returns the sum of two numbers',
            'difficulty': 'easy',
            'category': 'Basic Math',
            'test_cases': [
                {
                    'input': '2, 3',
                    'expected_output': '5'
                },
                {
                    'input': '10, 15',
                    'expected_output': '25'
                }
            ],
            'starter_code': 'def sum_two_numbers(a, b):\n    # Your code here\n    pass',
            'point_value': 100
        }
        
        response = self.client.post(create_url, question_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        question_id = response.data['id']
        
        # 2. Teacher adds question to library
        library_url = reverse('practice-library-list')
        library_data = {
            'question_id': question_id,
            'is_public': True,
            'tags': ['beginner', 'math']
        }
        
        response = self.client.post(library_url, library_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # 3. Student views available practice questions
        self.client.force_authenticate(user=self.student)
        list_url = reverse('practice-questions-list')
        
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Sum Two Numbers')
        
        # 4. Student views library
        library_url = reverse('practice-questions-library')
        response = self.client.get(library_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(len(response.data['data']), 1)
        
        # 5. Student gets question details
        detail_url = reverse('practice-questions-detail', kwargs={'pk': question_id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Sum Two Numbers')
        self.assertEqual(len(response.data['test_cases']), 2)
        
        # 6. Student submits solution
        submit_url = reverse('practice-questions-submit', kwargs={'pk': question_id})
        submission_data = {
            'source_code': 'def sum_two_numbers(a, b):\n    return a + b',
            'language': 'python'
        }
        
        response = self.client.post(submit_url, submission_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertIn('data', response.data)
        
        # 7. Student checks progress
        progress_url = reverse('practice-questions-progress')
        response = self.client.get(progress_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['summary']['total_attempted'], 1)
        
        # 8. Student views submission history
        submissions_url = reverse('practice-submissions-list')
        response = self.client.get(submissions_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
        # 9. Test filtering and search
        # Filter by difficulty
        response = self.client.get(list_url, {'difficulty': 'easy'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
        # Search by title
        response = self.client.get(list_url, {'search': 'Sum'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
        # 10. Test statistics endpoint
        stats_url = reverse('practice-questions-statistics')
        response = self.client.get(stats_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['data']['total_questions'], 1)
        self.assertEqual(response.data['data']['by_difficulty']['easy'], 1)
        
        # 11. Test categories endpoint
        categories_url = reverse('practice-questions-categories')
        response = self.client.get(categories_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertIn('Basic Math', response.data['data'])
    
    def test_permission_boundaries(self):
        """Test that permissions are properly enforced"""
        
        # Create a practice question as teacher
        self.client.force_authenticate(user=self.teacher)
        create_url = reverse('practice-questions-list')
        
        question_data = {
            'title': 'Test Question',
            'description': 'Test description',
            'difficulty': 'medium',
            'category': 'Test',
            'test_cases': [{'input': 'test', 'expected_output': 'result'}],
            'point_value': 200
        }
        
        response = self.client.post(create_url, question_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        question_id = response.data['id']
        
        # Switch to student
        self.client.force_authenticate(user=self.student)
        
        # Student should not be able to create questions
        response = self.client.post(create_url, question_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Student should not be able to update questions
        update_url = reverse('practice-questions-detail', kwargs={'pk': question_id})
        response = self.client.put(update_url, question_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Student should not be able to delete questions
        response = self.client.delete(update_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Student should be able to view questions
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Switch back to teacher
        self.client.force_authenticate(user=self.teacher)
        
        # Teacher should not be able to submit practice questions
        submit_url = reverse('practice-questions-submit', kwargs={'pk': question_id})
        submission_data = {
            'source_code': 'def test():\n    return "result"',
            'language': 'python'
        }
        
        response = self.client.post(submit_url, submission_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Teacher should not be able to view student progress
        progress_url = reverse('practice-questions-progress')
        response = self.client.get(progress_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_api_error_handling(self):
        """Test API error handling for invalid data"""
        
        self.client.force_authenticate(user=self.teacher)
        create_url = reverse('practice-questions-list')
        
        # Test invalid difficulty
        invalid_data = {
            'title': 'Test Question',
            'description': 'Test description',
            'difficulty': 'invalid_difficulty',
            'category': 'Test',
            'test_cases': [{'input': 'test', 'expected_output': 'result'}],
            'point_value': 100
        }
        
        response = self.client.post(create_url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Test invalid point value
        invalid_data['difficulty'] = 'easy'
        invalid_data['point_value'] = -10
        
        response = self.client.post(create_url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Test invalid test cases format
        invalid_data['point_value'] = 100
        invalid_data['test_cases'] = 'not_a_list'
        
        response = self.client.post(create_url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_filtering_and_search_functionality(self):
        """Test advanced filtering and search capabilities"""
        
        self.client.force_authenticate(user=self.teacher)
        create_url = reverse('practice-questions-list')
        
        # Create multiple questions with different attributes
        questions = [
            {
                'title': 'Easy Array Problem',
                'description': 'Work with arrays',
                'difficulty': 'easy',
                'category': 'Arrays',
                'test_cases': [{'input': '[1,2,3]', 'expected_output': '6'}],
                'point_value': 100
            },
            {
                'title': 'Hard String Problem',
                'description': 'Complex string manipulation',
                'difficulty': 'hard',
                'category': 'Strings',
                'test_cases': [{'input': 'hello', 'expected_output': 'olleh'}],
                'point_value': 300
            },
            {
                'title': 'Medium Math Problem',
                'description': 'Mathematical calculations',
                'difficulty': 'medium',
                'category': 'Math',
                'test_cases': [{'input': '5', 'expected_output': '120'}],
                'point_value': 200
            }
        ]
        
        for question_data in questions:
            response = self.client.post(create_url, question_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Switch to student for testing
        self.client.force_authenticate(user=self.student)
        list_url = reverse('practice-questions-list')
        
        # Test difficulty filtering
        response = self.client.get(list_url, {'difficulty': 'easy'})
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['difficulty'], 'easy')
        
        response = self.client.get(list_url, {'difficulty': 'hard'})
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['difficulty'], 'hard')
        
        # Test multiple difficulty filtering
        response = self.client.get(list_url, {'difficulty': 'easy,medium'})
        self.assertEqual(len(response.data['results']), 2)
        
        # Test category filtering
        response = self.client.get(list_url, {'category': 'Arrays'})
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['category'], 'Arrays')
        
        # Test search functionality
        response = self.client.get(list_url, {'search': 'Array'})
        self.assertEqual(len(response.data['results']), 1)
        
        response = self.client.get(list_url, {'search': 'Problem'})
        self.assertEqual(len(response.data['results']), 3)  # All have "Problem" in title
        
        # Test ordering
        response = self.client.get(list_url, {'ordering': 'difficulty'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response = self.client.get(list_url, {'ordering': '-point_value'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should be ordered by point_value descending (300, 200, 100)
        self.assertEqual(response.data['results'][0]['point_value'], 300)