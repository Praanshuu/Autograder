from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import PracticeQuestion, PracticeQuestionLibrary, PracticeSubmission, PracticeProgress

User = get_user_model()


class PracticeQuestionAPITestCase(TestCase):
    """Test cases for Practice Question API endpoints"""
    
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
        
        # Create test practice question
        self.practice_question = PracticeQuestion.objects.create(
            title='Test Array Problem',
            description='Find the maximum element in an array',
            difficulty='easy',
            category='Arrays',
            test_cases=[
                {
                    'input': '[1, 2, 3, 4, 5]',
                    'expected_output': '5'
                },
                {
                    'input': '[10, 20, 5]',
                    'expected_output': '20'
                }
            ],
            starter_code='def find_max(arr):\n    # Your code here\n    pass',
            point_value=100,
            created_by=self.teacher
        )
    
    def test_list_practice_questions_as_student(self):
        """Test that students can list practice questions"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-questions-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Array Problem')
    
    def test_list_practice_questions_as_teacher(self):
        """Test that teachers can list practice questions"""
        self.client.force_authenticate(user=self.teacher)
        url = reverse('practice-questions-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_create_practice_question_as_teacher(self):
        """Test that teachers can create practice questions"""
        self.client.force_authenticate(user=self.teacher)
        url = reverse('practice-questions-list')
        
        data = {
            'title': 'New Practice Question',
            'description': 'Test description',
            'difficulty': 'medium',
            'category': 'Strings',
            'test_cases': [
                {
                    'input': 'hello',
                    'expected_output': 'HELLO'
                }
            ],
            'starter_code': 'def uppercase(s):\n    pass',
            'point_value': 150
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Practice Question')
        self.assertEqual(response.data['created_by'], self.teacher.id)
    
    def test_create_practice_question_as_student_forbidden(self):
        """Test that students cannot create practice questions"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-questions-list')
        
        data = {
            'title': 'Student Question',
            'description': 'Should not be allowed',
            'difficulty': 'easy',
            'category': 'Test',
            'test_cases': [],
            'point_value': 100
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_filter_by_difficulty(self):
        """Test filtering practice questions by difficulty"""
        # Create additional questions with different difficulties
        PracticeQuestion.objects.create(
            title='Hard Problem',
            description='A difficult problem',
            difficulty='hard',
            category='Algorithms',
            test_cases=[{'input': 'test', 'expected_output': 'result'}],
            point_value=300,
            created_by=self.teacher
        )
        
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-questions-list')
        
        # Filter for easy questions
        response = self.client.get(url, {'difficulty': 'easy'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['difficulty'], 'easy')
        
        # Filter for hard questions
        response = self.client.get(url, {'difficulty': 'hard'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['difficulty'], 'hard')
    
    def test_filter_by_category(self):
        """Test filtering practice questions by category"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-questions-list')
        
        response = self.client.get(url, {'category': 'Arrays'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['category'], 'Arrays')
    
    def test_search_practice_questions(self):
        """Test searching practice questions by title and description"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-questions-list')
        
        response = self.client.get(url, {'search': 'Array'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_get_practice_question_detail(self):
        """Test retrieving a specific practice question"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-questions-detail', kwargs={'pk': self.practice_question.id})
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Array Problem')
        self.assertEqual(len(response.data['test_cases']), 2)
    
    def test_library_endpoint(self):
        """Test the library endpoint for browsing available questions"""
        # Add question to library
        PracticeQuestionLibrary.objects.create(
            question=self.practice_question,
            is_public=True,
            tags=['beginner', 'arrays']
        )
        
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-questions-library')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(len(response.data['data']), 1)
    
    def test_categories_endpoint(self):
        """Test the categories endpoint"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-questions-categories')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertIn('Arrays', response.data['data'])
    
    def test_statistics_endpoint(self):
        """Test the statistics endpoint"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-questions-statistics')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['data']['total_questions'], 1)
        self.assertEqual(response.data['data']['by_difficulty']['easy'], 1)
    
    def test_submit_practice_question_as_student(self):
        """Test submitting code for a practice question"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-questions-submit', kwargs={'pk': self.practice_question.id})
        
        data = {
            'source_code': 'def find_max(arr):\n    return max(arr)',
            'language': 'python'
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertIn('data', response.data)
    
    def test_submit_practice_question_as_teacher_forbidden(self):
        """Test that teachers cannot submit practice questions"""
        self.client.force_authenticate(user=self.teacher)
        url = reverse('practice-questions-submit', kwargs={'pk': self.practice_question.id})
        
        data = {
            'source_code': 'def find_max(arr):\n    return max(arr)',
            'language': 'python'
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_progress_endpoint_as_student(self):
        """Test the progress endpoint for students"""
        # Create some progress data
        PracticeProgress.objects.create(
            student=self.student,
            practice_question=self.practice_question,
            is_completed=True,
            attempts_count=3,
            best_score=85.0
        )
        
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-questions-progress')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(len(response.data['data']), 1)
        self.assertEqual(response.data['summary']['total_completed'], 1)
    
    def test_progress_endpoint_as_teacher_forbidden(self):
        """Test that teachers cannot access student progress endpoint"""
        self.client.force_authenticate(user=self.teacher)
        url = reverse('practice-questions-progress')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_unauthenticated_access_forbidden(self):
        """Test that unauthenticated users cannot access the API"""
        url = reverse('practice-questions-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PracticeSubmissionAPITestCase(TestCase):
    """Test cases for Practice Submission API endpoints"""
    
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
        
        # Create test practice question
        self.practice_question = PracticeQuestion.objects.create(
            title='Test Problem',
            description='Test description',
            difficulty='easy',
            category='Test',
            test_cases=[{'input': 'test', 'expected_output': 'result'}],
            point_value=100,
            created_by=self.teacher
        )
        
        # Create test submission
        self.submission = PracticeSubmission.objects.create(
            student=self.student,
            practice_question=self.practice_question,
            source_code='def test():\n    return "result"',
            language='python',
            status='success',
            test_results=[{'status': 'pass'}],
            points_earned=100,
            attempt_number=1
        )
    
    def test_list_submissions_as_student(self):
        """Test that students can list their own submissions"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-submissions-list')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['student'], self.student.id)
    
    def test_list_submissions_as_teacher(self):
        """Test that teachers can list submissions for their questions"""
        self.client.force_authenticate(user=self.teacher)
        url = reverse('practice-submissions-list')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_filter_submissions_by_status(self):
        """Test filtering submissions by status"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-submissions-list')
        
        response = self.client.get(url, {'status': 'success'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_get_submission_detail(self):
        """Test retrieving a specific submission"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-submissions-detail', kwargs={'pk': self.submission.id})
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['points_earned'], 100)


class PracticeQuestionLibraryAPITestCase(TestCase):
    """Test cases for Practice Question Library API endpoints"""
    
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
        
        # Create test practice question
        self.practice_question = PracticeQuestion.objects.create(
            title='Library Question',
            description='A question in the library',
            difficulty='medium',
            category='Library',
            test_cases=[{'input': 'test', 'expected_output': 'result'}],
            point_value=200,
            created_by=self.teacher
        )
        
        # Create library entry
        self.library_entry = PracticeQuestionLibrary.objects.create(
            question=self.practice_question,
            is_public=True,
            tags=['test', 'library']
        )
    
    def test_list_library_as_student(self):
        """Test that students can list public library questions"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-library-list')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_list_library_as_teacher(self):
        """Test that teachers can list all library questions"""
        self.client.force_authenticate(user=self.teacher)
        url = reverse('practice-library-list')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_create_library_entry_as_teacher(self):
        """Test that teachers can add questions to the library"""
        # Create another question
        question2 = PracticeQuestion.objects.create(
            title='Another Question',
            description='Another test question',
            difficulty='hard',
            category='Test',
            test_cases=[{'input': 'test', 'expected_output': 'result'}],
            point_value=300,
            created_by=self.teacher
        )
        
        self.client.force_authenticate(user=self.teacher)
        url = reverse('practice-library-list')
        
        data = {
            'question_id': str(question2.id),
            'is_public': True,
            'tags': ['new', 'test']
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['question']['title'], 'Another Question')
    
    def test_create_library_entry_as_student_forbidden(self):
        """Test that students cannot add questions to the library"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-library-list')
        
        data = {
            'question_id': str(self.practice_question.id),
            'is_public': True,
            'tags': ['test']
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_search_library(self):
        """Test searching the library"""
        self.client.force_authenticate(user=self.student)
        url = reverse('practice-library-list')
        
        response = self.client.get(url, {'search': 'Library'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_filter_library_by_public(self):
        """Test filtering library by public status"""
        self.client.force_authenticate(user=self.teacher)
        url = reverse('practice-library-list')
        
        response = self.client.get(url, {'is_public': 'true'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)