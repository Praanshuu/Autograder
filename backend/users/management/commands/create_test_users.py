from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create test users for development'

    def handle(self, *args, **options):
        test_users = [
            {
                'username': 'testteacher',
                'email': 'teacher@test.com',
                'password': 'testpass123',
                'first_name': 'Test',
                'last_name': 'Teacher',
                'role': 'teacher'
            },
            {
                'username': 'teststudent',
                'email': 'student@test.com',
                'password': 'testpass123',
                'first_name': 'Test',
                'last_name': 'Student',
                'role': 'student'
            },
            {
                'username': 'testadmin',
                'email': 'admin@test.com',
                'password': 'testpass123',
                'first_name': 'Test',
                'last_name': 'Admin',
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True
            }
        ]

        for user_data in test_users:
            username = user_data['username']
            
            if User.objects.filter(username=username).exists():
                self.stdout.write(
                    self.style.WARNING(f'User {username} already exists, skipping...')
                )
                continue
            
            password = user_data.pop('password')
            user = User.objects.create_user(**user_data)
            user.set_password(password)
            user.save()
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created user: {username} ({user.role})')
            )

        self.stdout.write(
            self.style.SUCCESS('\nTest users created! You can now use these credentials:')
        )
        self.stdout.write('Teacher: testteacher / testpass123')
        self.stdout.write('Student: teststudent / testpass123')
        self.stdout.write('Admin: testadmin / testpass123')