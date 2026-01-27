from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .models import (
    PracticeQuestion, UserPoints, Achievement, UserAchievement,
    PracticeSubmission, PracticeProgress, StudentAnalytics, 
    LeaderboardEntry, PracticeQuestionLibrary
)

User = get_user_model()


class PracticeQuestionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_practice_question_creation(self):
        """Test creating a practice question with valid data"""
        question = PracticeQuestion.objects.create(
            title='Test Array Problem',
            description='Find the maximum element in an array',
            difficulty='easy',
            category='Arrays',
            test_cases=[
                {'input': '[1, 2, 3]', 'expected': '3'},
                {'input': '[5, 1, 9]', 'expected': '9'}
            ],
            starter_code='def find_max(arr):\n    pass',
            point_value=100,
            created_by=self.user
        )
        
        self.assertEqual(question.title, 'Test Array Problem')
        self.assertEqual(question.difficulty, 'easy')
        self.assertEqual(question.point_value, 100)
        self.assertEqual(question.created_by, self.user)
        self.assertTrue(question.is_active)

    def test_practice_question_str_representation(self):
        """Test string representation of practice question"""
        question = PracticeQuestion.objects.create(
            title='Test Problem',
            description='Test description',
            difficulty='medium',
            category='Strings',
            test_cases=[],
            point_value=150,
            created_by=self.user
        )
        
        self.assertEqual(str(question), 'Test Problem (medium)')

    def test_practice_question_ordering(self):
        """Test that practice questions are ordered by difficulty and title"""
        easy_question = PracticeQuestion.objects.create(
            title='B Problem',
            description='Easy problem',
            difficulty='easy',
            category='Arrays',
            test_cases=[],
            point_value=100,
            created_by=self.user
        )
        
        hard_question = PracticeQuestion.objects.create(
            title='A Problem',
            description='Hard problem',
            difficulty='hard',
            category='Algorithms',
            test_cases=[],
            point_value=300,
            created_by=self.user
        )
        
        medium_question = PracticeQuestion.objects.create(
            title='A Problem',
            description='Medium problem',
            difficulty='medium',
            category='Strings',
            test_cases=[],
            point_value=200,
            created_by=self.user
        )
        
        questions = list(PracticeQuestion.objects.all())
        self.assertEqual(questions[0], easy_question)  # easy comes first
        self.assertEqual(questions[1], medium_question)  # medium comes second
        self.assertEqual(questions[2], hard_question)  # hard comes last


class UserPointsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_points_creation(self):
        """Test creating user points with default values"""
        points = UserPoints.objects.create(user=self.user)
        
        self.assertEqual(points.total_points, 0)
        self.assertEqual(points.practice_points, 0)
        self.assertEqual(points.assignment_points, 0)
        self.assertEqual(points.user, self.user)

    def test_user_points_str_representation(self):
        """Test string representation of user points"""
        points = UserPoints.objects.create(
            user=self.user,
            total_points=250,
            practice_points=150,
            assignment_points=100
        )
        
        self.assertEqual(str(points), 'testuser: 250 points')

    def test_user_points_ordering(self):
        """Test that user points are ordered by total points descending"""
        user2 = User.objects.create_user(
            username='user2',
            email='user2@example.com',
            password='testpass123'
        )
        
        points1 = UserPoints.objects.create(user=self.user, total_points=100)
        points2 = UserPoints.objects.create(user=user2, total_points=200)
        
        points_list = list(UserPoints.objects.all())
        self.assertEqual(points_list[0], points2)  # Higher points first
        self.assertEqual(points_list[1], points1)

    def test_user_points_one_to_one_constraint(self):
        """Test that each user can only have one UserPoints record"""
        UserPoints.objects.create(user=self.user, total_points=100)
        
        with self.assertRaises(IntegrityError):
            UserPoints.objects.create(user=self.user, total_points=200)


class AchievementModelTest(TestCase):
    def test_achievement_creation(self):
        """Test creating an achievement with valid data"""
        achievement = Achievement.objects.create(
            name='First Steps',
            description='Complete your first practice question',
            icon='🎯',
            badge_type='first_completion',
            criteria={'type': 'first_completion', 'count': 1},
            rarity='common'
        )
        
        self.assertEqual(achievement.name, 'First Steps')
        self.assertEqual(achievement.badge_type, 'first_completion')
        self.assertEqual(achievement.rarity, 'common')
        self.assertTrue(achievement.is_active)

    def test_achievement_str_representation(self):
        """Test string representation of achievement"""
        achievement = Achievement.objects.create(
            name='Speed Demon',
            description='Complete a problem in under 30 seconds',
            icon='⚡',
            badge_type='speed',
            criteria={'type': 'speed', 'time_limit': 30},
            rarity='rare'
        )
        
        self.assertEqual(str(achievement), 'Speed Demon (rare)')


class UserAchievementModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.achievement = Achievement.objects.create(
            name='First Steps',
            description='Complete your first practice question',
            icon='🎯',
            badge_type='first_completion',
            criteria={'type': 'first_completion'},
            rarity='common'
        )

    def test_user_achievement_creation(self):
        """Test creating a user achievement"""
        user_achievement = UserAchievement.objects.create(
            user=self.user,
            achievement=self.achievement
        )
        
        self.assertEqual(user_achievement.user, self.user)
        self.assertEqual(user_achievement.achievement, self.achievement)

    def test_user_achievement_str_representation(self):
        """Test string representation of user achievement"""
        user_achievement = UserAchievement.objects.create(
            user=self.user,
            achievement=self.achievement
        )
        
        self.assertEqual(str(user_achievement), 'testuser - First Steps')

    def test_user_achievement_unique_constraint(self):
        """Test that a user can't earn the same achievement twice"""
        UserAchievement.objects.create(
            user=self.user,
            achievement=self.achievement
        )
        
        with self.assertRaises(IntegrityError):
            UserAchievement.objects.create(
                user=self.user,
                achievement=self.achievement
            )


class PracticeSubmissionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.question = PracticeQuestion.objects.create(
            title='Test Problem',
            description='Test description',
            difficulty='easy',
            category='Arrays',
            test_cases=[],
            point_value=100,
            created_by=self.user
        )

    def test_practice_submission_creation(self):
        """Test creating a practice submission"""
        submission = PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.question,
            source_code='def solution(): return True',
            status='success',
            test_results=[{'test': 1, 'passed': True}],
            points_earned=100,
            attempt_number=1
        )
        
        self.assertEqual(submission.student, self.user)
        self.assertEqual(submission.practice_question, self.question)
        self.assertEqual(submission.status, 'success')
        self.assertEqual(submission.points_earned, 100)
        self.assertEqual(submission.attempt_number, 1)

    def test_practice_submission_str_representation(self):
        """Test string representation of practice submission"""
        submission = PracticeSubmission.objects.create(
            student=self.user,
            practice_question=self.question,
            source_code='def solution(): return True',
            status='success',
            attempt_number=2
        )
        
        expected_str = 'testuser - Test Problem (Attempt 2)'
        self.assertEqual(str(submission), expected_str)


class PracticeProgressModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.question = PracticeQuestion.objects.create(
            title='Test Problem',
            description='Test description',
            difficulty='easy',
            category='Arrays',
            test_cases=[],
            point_value=100,
            created_by=self.user
        )

    def test_practice_progress_creation(self):
        """Test creating practice progress"""
        progress = PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.question,
            is_completed=True,
            attempts_count=3,
            best_score=85.5,
            time_spent=300
        )
        
        self.assertEqual(progress.student, self.user)
        self.assertEqual(progress.practice_question, self.question)
        self.assertTrue(progress.is_completed)
        self.assertEqual(progress.attempts_count, 3)
        self.assertEqual(progress.best_score, 85.5)
        self.assertEqual(progress.time_spent, 300)

    def test_practice_progress_str_representation(self):
        """Test string representation of practice progress"""
        progress = PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.question,
            is_completed=True
        )
        
        expected_str = 'testuser - Test Problem (Completed)'
        self.assertEqual(str(progress), expected_str)

    def test_practice_progress_unique_constraint(self):
        """Test that each student can only have one progress record per question"""
        PracticeProgress.objects.create(
            student=self.user,
            practice_question=self.question
        )
        
        with self.assertRaises(IntegrityError):
            PracticeProgress.objects.create(
                student=self.user,
                practice_question=self.question
            )


class StudentAnalyticsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_student_analytics_creation(self):
        """Test creating student analytics with default values"""
        analytics = StudentAnalytics.objects.create(student=self.user)
        
        self.assertEqual(analytics.student, self.user)
        self.assertEqual(analytics.total_practice_completed, 0)
        self.assertEqual(analytics.total_assignments_completed, 0)
        self.assertEqual(analytics.average_score, 0.0)
        self.assertEqual(analytics.current_streak, 0)
        self.assertEqual(analytics.longest_streak, 0)
        self.assertEqual(analytics.total_time_spent, 0)
        self.assertEqual(analytics.performance_trend, [])
        self.assertEqual(analytics.concept_mastery, {})

    def test_student_analytics_str_representation(self):
        """Test string representation of student analytics"""
        analytics = StudentAnalytics.objects.create(student=self.user)
        
        self.assertEqual(str(analytics), 'testuser Analytics')


class LeaderboardEntryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_leaderboard_entry_creation(self):
        """Test creating a leaderboard entry"""
        entry = LeaderboardEntry.objects.create(
            user=self.user,
            rank=1,
            total_points=500,
            completed_problems=10,
            leaderboard_type='global'
        )
        
        self.assertEqual(entry.user, self.user)
        self.assertEqual(entry.rank, 1)
        self.assertEqual(entry.total_points, 500)
        self.assertEqual(entry.completed_problems, 10)
        self.assertEqual(entry.leaderboard_type, 'global')

    def test_leaderboard_entry_str_representation(self):
        """Test string representation of leaderboard entry"""
        entry = LeaderboardEntry.objects.create(
            user=self.user,
            rank=5,
            total_points=300,
            completed_problems=6,
            leaderboard_type='class'
        )
        
        self.assertEqual(str(entry), '#5 testuser (class)')

    def test_leaderboard_entry_ordering(self):
        """Test that leaderboard entries are ordered by rank"""
        user2 = User.objects.create_user(
            username='user2',
            email='user2@example.com',
            password='testpass123'
        )
        
        entry1 = LeaderboardEntry.objects.create(
            user=self.user,
            rank=2,
            total_points=300,
            completed_problems=6,
            leaderboard_type='global'
        )
        
        entry2 = LeaderboardEntry.objects.create(
            user=user2,
            rank=1,
            total_points=500,
            completed_problems=10,
            leaderboard_type='global'
        )
        
        entries = list(LeaderboardEntry.objects.all())
        self.assertEqual(entries[0], entry2)  # Rank 1 first
        self.assertEqual(entries[1], entry1)  # Rank 2 second


class PracticeQuestionLibraryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.question = PracticeQuestion.objects.create(
            title='Library Question',
            description='A question from the library',
            difficulty='medium',
            category='Algorithms',
            test_cases=[],
            point_value=200,
            created_by=self.user
        )

    def test_practice_question_library_creation(self):
        """Test creating a practice question library entry"""
        library_entry = PracticeQuestionLibrary.objects.create(
            question=self.question,
            is_public=True,
            tags=['algorithms', 'sorting', 'beginner']
        )
        
        self.assertEqual(library_entry.question, self.question)
        self.assertTrue(library_entry.is_public)
        self.assertEqual(library_entry.tags, ['algorithms', 'sorting', 'beginner'])