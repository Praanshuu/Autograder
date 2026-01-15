# Registration Debugging Guide

## Current Status

The registration endpoint is **working correctly** on the backend. Testing with curl shows successful registration:

```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser123",
    "email": "test@example.com",
    "password": "TestPass123!",
    "password2": "TestPass123!",
    "first_name": "Test",
    "last_name": "User",
    "role": "student"
  }'
```

Response: `201 Created` with user data and JWT tokens.

## Changes Made

### 1. Fixed API Error Handling (`src/services/apiClient.js`)
- Updated `handleApiError` to properly extract Django REST Framework validation errors
- Django returns errors directly in response.data, not nested under an `errors` key
- Added enhanced debug logging for registration requests and errors

### 2. Added Debug Logging
- Frontend now logs registration request details (URL, method, data, headers)
- Backend already has debug logging in `users/views.py` for registration attempts
- Enhanced error logging shows status, message, errors, and full response data

## Testing Steps

1. **Open Browser Console** (F12 or Cmd+Option+I)
   - Go to the Console tab to see frontend logs

2. **Open Backend Terminal**
   - Watch for backend logs showing registration attempts

3. **Try to Register a New User**
   - Go to http://localhost:5173/register
   - Fill in the form:
     - First Name: Test
     - Last Name: User
     - Username: newstudent123
     - Email: newstudent@example.com
     - Password: TestPass123!
     - Confirm Password: TestPass123!
     - Role: Student
   - Click "Create Account"

4. **Check Logs**
   - **Frontend Console**: Look for "=== REGISTRATION REQUEST ===" and "=== API ERROR ===" logs
   - **Backend Terminal**: Look for "=== REGISTRATION ATTEMPT ===" and validation errors

## Expected Behavior

### If Registration Succeeds:
- Status: 201 Created
- User is logged in automatically
- Redirected to dashboard based on role

### If Registration Fails:
- Frontend console will show:
  - The exact data being sent
  - The error status code
  - Validation errors for each field
- Backend terminal will show:
  - Request data received
  - Validation errors (if any)

## Common Issues

### Password Validation
Django has strict password validation:
- Minimum 8 characters
- Cannot be too similar to username/email
- Cannot be entirely numeric
- Cannot be a common password

### Required Fields
All fields are required:
- username
- email
- password
- password2 (must match password)
- first_name
- last_name
- role

### Username/Email Already Exists
If you see a 400 error about username or email already existing, try a different username/email.

## Next Steps

After testing registration:
1. Check the console logs to see what data is being sent
2. Check the backend logs to see what validation errors occur
3. Share the logs so we can identify the exact issue
