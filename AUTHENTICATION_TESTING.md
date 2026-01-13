# Authentication Integration Testing Guide

## Overview

This guide helps you test the complete authentication integration between the React frontend and Django backend.

## Setup Instructions

### 1. Start the Backend

```bash
cd Autograder/backend

# Install dependencies (if not already done)
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create test users
python manage.py create_test_users

# Start the server
python manage.py runserver
```

### 2. Start the Frontend

```bash
cd Autograder

# Install dependencies (if not already done)
npm install

# Start the development server
npm run dev
```

## Test Users

The `create_test_users` command creates these test accounts:

| Username | Password | Role | Email |
|----------|----------|------|-------|
| testteacher | testpass123 | teacher | teacher@test.com |
| teststudent | testpass123 | student | student@test.com |
| testadmin | testpass123 | admin | admin@test.com |

## Testing Checklist

### 1. Basic API Connection

- [ ] Visit `http://localhost:5173`
- [ ] Click "Test API Connection"
- [ ] Should see successful response with API endpoints

### 2. User Registration

- [ ] Click "Sign Up" from landing page
- [ ] Fill out registration form with new user details
- [ ] Select role (Student/Teacher/TA)
- [ ] Submit form
- [ ] Should redirect to appropriate dashboard
- [ ] Check that JWT tokens are stored in localStorage

### 3. User Login

- [ ] Click "Sign In" from landing page
- [ ] Use test credentials (e.g., testteacher/testpass123)
- [ ] Should redirect to appropriate dashboard based on role
- [ ] Check that user info is displayed correctly

### 4. Authentication State

- [ ] Visit `/auth-test` page
- [ ] Check authentication status shows "Authenticated: Yes"
- [ ] Verify user information is displayed correctly
- [ ] Check that JWT tokens are present in localStorage

### 5. Protected Routes

- [ ] Try accessing `/teacher/dashboard` without login
- [ ] Should redirect to login page
- [ ] Login as teacher, should access teacher routes
- [ ] Login as student, should be redirected away from teacher routes

### 6. Token Management

- [ ] Login successfully
- [ ] Check localStorage for tokens (use browser dev tools)
- [ ] Refresh the page - should remain logged in
- [ ] Clear localStorage and refresh - should redirect to login

### 7. Logout Functionality

- [ ] Login successfully
- [ ] Click logout button
- [ ] Should redirect to login page
- [ ] Check that tokens are cleared from localStorage
- [ ] Try accessing protected routes - should redirect to login

### 8. Error Handling

- [ ] Try login with invalid credentials
- [ ] Should show error message
- [ ] Try registration with existing username
- [ ] Should show validation errors
- [ ] Try accessing API when backend is down
- [ ] Should show appropriate error messages

## Debug Tools

### Authentication Status Component

Visit `/auth-test` to see:
- Current authentication state
- User information
- JWT token details
- localStorage contents
- Test buttons for various auth functions

### Browser Developer Tools

Check these in your browser's dev tools:

1. **Application/Storage Tab**:
   - localStorage should contain `autograder_access_token` and `autograder_refresh_token`

2. **Network Tab**:
   - API requests should include `Authorization: Bearer <token>` headers
   - Login/register requests should return tokens

3. **Console**:
   - Enable API debug mode in `.env` to see request/response logs

## Common Issues & Solutions

### 1. CORS Errors

**Problem**: Browser blocks requests to Django backend

**Solution**: 
- Ensure Django CORS settings allow `http://localhost:5173`
- Check `CORS_ALLOWED_ORIGINS` in Django settings

### 2. 401 Unauthorized Errors

**Problem**: API returns 401 even with valid token

**Solutions**:
- Check JWT token format and expiration
- Verify Django JWT settings
- Ensure token is being sent in Authorization header

### 3. Token Refresh Issues

**Problem**: Access token expires and refresh fails

**Solutions**:
- Check refresh token validity
- Verify Django JWT refresh endpoint
- Check token refresh logic in API client

### 4. Registration Validation Errors

**Problem**: Registration fails with validation errors

**Solutions**:
- Check password requirements (minimum 8 characters)
- Ensure all required fields are filled
- Check for unique username/email constraints

### 5. Route Protection Not Working

**Problem**: Can access protected routes without authentication

**Solutions**:
- Verify ProtectedRoute component is wrapping routes
- Check AuthContext initialization
- Ensure token validation is working

## API Endpoints Testing

You can test these endpoints directly:

### Authentication Endpoints

```bash
# Register new user
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "newuser@test.com",
    "password": "testpass123",
    "password2": "testpass123",
    "first_name": "New",
    "last_name": "User",
    "role": "student"
  }'

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testteacher",
    "password": "testpass123"
  }'

# Get current user (requires token)
curl -X GET http://localhost:8000/api/users/me/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Next Steps

Once authentication is working:

1. **Update existing components** to use real API data instead of mocks
2. **Add loading states** to all components
3. **Implement proper error handling** in UI
4. **Add user profile management** features
5. **Create role-based navigation** components

## Troubleshooting Commands

```bash
# Check Django logs
cd Autograder/backend
python manage.py runserver --verbosity=2

# Check if users exist
python manage.py shell
>>> from django.contrib.auth import get_user_model
>>> User = get_user_model()
>>> User.objects.all()

# Reset database (if needed)
python manage.py flush
python manage.py migrate
python manage.py create_test_users

# Check frontend console
# Open browser dev tools and check for JavaScript errors
```

## Success Criteria

Authentication integration is successful when:

- ✅ Users can register and login through the UI
- ✅ JWT tokens are properly stored and managed
- ✅ Protected routes redirect unauthenticated users
- ✅ Role-based access control works correctly
- ✅ Token refresh happens automatically
- ✅ Logout clears tokens and redirects properly
- ✅ Error messages are displayed appropriately
- ✅ Authentication state persists across page refreshes