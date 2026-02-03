from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import PracticeQuestion, PracticeQuestionLibrary

User = get_user_model()


class AdminInterfaceTest(TestCase):
    def setUp(self):
        # Create a superuser for admin access
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        
        # Create a regular user
        self.regular_user = User.objects.create_user(
            username='teacher',
            email='teacher@example.com',
            password='teacherpass123'
        )
        
        # Create a practice question
        self.practice_question = PracticeQuestion.objects.create(
            title='Admin Test Question',
            description='A question for testing admin interface',
            difficulty='medium',
            category='Testing',
            test_cases=[{'input': 'test', 'expected_output': 'test'}],
            starter_code='# Write your code here',
            point_value=150,
            created_by=self.regular_user
        )
        
        self.client = Client()
    
    def test_admin_practice_question_list_view(self):
        """Test that admin can view practice questions list"""
        self.client.login(username='admin', password='adminpass123')
        
        url = reverse('admin:gamification_practicequestion_changelist')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Test Question')
        self.assertContains(response, 'medium')
        self.assertContains(response, 'Testing')
    
    def test_admin_practice_question_detail_view(self):
        """Test that admin can view practice question details"""
        self.client.login(username='admin', password='adminpass123')
        
        url = reverse('admin:gamification_practicequestion_change', args=[self.practice_question.pk])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Test Question')
        self.assertContains(response, 'A question for testing admin interface')
        self.assertContains(response, 'medium')
        self.assertContains(response, 'Testing')
        self.assertContains(response, '150')  # point_value
    
    def test_admin_practice_question_library_integration(self):
        """Test that practice question library works in admin"""
        self.client.login(username='admin', password='adminpass123')
        
        # Create a library entry
        library_entry = PracticeQuestionLibrary.objects.create(
            question=self.practice_question,
            is_public=True,
            tags=['admin-test', 'integration']
        )
        
        # Check library list view
        url = reverse('admin:gamification_practicequestionlibrary_changelist')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Test Question')
        
        # Check library detail view
        url = reverse('admin:gamification_practicequestionlibrary_change', args=[library_entry.pk])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Test Question')
    
    def test_admin_filtering_and_search(self):
        """Test admin filtering and search functionality"""
        self.client.login(username='admin', password='adminpass123')
        
        # Create additional questions for testing filters
        PracticeQuestion.objects.create(
            title='Easy Question',
            description='An easy question',
            difficulty='easy',
            category='Basics',
            test_cases=[],
            point_value=100,
            created_by=self.regular_user
        )
        
        PracticeQuestion.objects.create(
            title='Hard Question',
            description='A hard question',
            difficulty='hard',
            category='Advanced',
            test_cases=[],
            point_value=200,
            created_by=self.regular_user
        )
        
        # Test difficulty filter
        url = reverse('admin:gamification_practicequestion_changelist')
        response = self.client.get(url + '?difficulty=medium')
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Test Question')
        self.assertNotContains(response, 'Easy Question')
        self.assertNotContains(response, 'Hard Question')
        
        # Test category filter
        response = self.client.get(url + '?category=Testing')
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Test Question')
        self.assertNotContains(response, 'Easy Question')
        
        # Test search functionality
        response = self.client.get(url + '?q=Admin')
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Test Question')