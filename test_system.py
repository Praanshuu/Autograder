#!/usr/bin/env python3
"""
Test script for Autograder System
Tests the backend API without requiring Docker
"""

import requests
import json
import time
import sys
import os

# Add backend to Python path
sys.path.append('backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

def test_django_setup():
    """Test Django setup and database"""
    try:
        import django
        django.setup()
        
        from django.contrib.auth import get_user_model
        from assignments.models import Assignment, Question, TestCase
        from submissions.models import Submission
        
        print("✅ Django setup successful")
        
        # Check if we have test data
        User = get_user_model()
        users_count = User.objects.count()
        print(f"📊 Users in database: {users_count}")
        
        return True
    except Exception as e:
        print(f"❌ Django setup failed: {e}")
        return False

def test_subprocess_execution():
    """Test code execution using subprocess (fallback method)"""
    try:
        from backend.submissions.services import execute_code
        
        # Test Python code execution
        test_cases = [
            {'input': '', 'expected_output': 'Hello, World!'}
        ]
        
        code = 'print("Hello, World!")'
        results = execute_code(code, 'python', test_cases)
        
        if results and len(results) > 0:
            result = results[0]
            if result.get('status') == 'pass':
                print("✅ Subprocess code execution working")
                return True
            else:
                print(f"⚠️  Code execution returned: {result}")
                return False
        else:
            print("❌ No results from code execution")
            return False
            
    except Exception as e:
        print(f"❌ Subprocess execution failed: {e}")
        return False

def test_api_endpoints():
    """Test API endpoints"""
    try:
        # Start Django development server in background would be complex
        # Instead, let's test the service functions directly
        from backend.submissions.views import get_sample_questions
        from django.test import RequestFactory
        from django.contrib.auth import get_user_model
        
        # Create a mock request
        factory = RequestFactory()
        request = factory.get('/api/submissions/sample-questions/')
        
        # Create a test user
        User = get_user_model()
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={'email': 'test@example.com', 'role': 'student'}
        )
        request.user = user
        
        # Test the view
        response = get_sample_questions(request)
        
        if response.status_code == 200:
            data = json.loads(response.content)
            if data.get('success') and len(data.get('data', [])) > 0:
                print(f"✅ Sample questions API working ({len(data['data'])} questions)")
                return True
        
        print(f"⚠️  API response: {response.status_code}")
        return False
        
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

def test_frontend_build():
    """Test if frontend can be built"""
    try:
        import subprocess
        
        # Check if node_modules exists
        if not os.path.exists('node_modules'):
            print("📦 Installing Node.js dependencies...")
            result = subprocess.run(['npm', 'install'], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"❌ npm install failed: {result.stderr}")
                return False
        
        print("✅ Node.js dependencies available")
        
        # Test if we can import the main components
        if os.path.exists('src/components/features/CodeRunner.jsx'):
            print("✅ CodeRunner component exists")
            return True
        else:
            print("❌ CodeRunner component not found")
            return False
            
    except Exception as e:
        print(f"❌ Frontend test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Autograder System Components")
    print("=" * 50)
    
    tests = [
        ("Django Setup", test_django_setup),
        ("Code Execution (Subprocess)", test_subprocess_execution),
        ("API Endpoints", test_api_endpoints),
        ("Frontend Components", test_frontend_build),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        try:
            if test_func():
                passed += 1
            else:
                print(f"❌ {test_name} failed")
        except Exception as e:
            print(f"❌ {test_name} error: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed! System is ready.")
        print("\n🚀 Next steps:")
        print("1. Start Docker Desktop")
        print("2. Run: cd backend/code_executor && ./build_docker.sh")
        print("3. Run: python manage.py runserver (in backend/)")
        print("4. Run: npm run dev (in root directory)")
        print("5. Visit: http://localhost:3000")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
        
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)