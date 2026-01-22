# API Client Setup Documentation

## Overview

This document describes the API client setup for connecting the React frontend to the Django backend. The setup includes axios configuration, JWT token handling, and service modules for each API domain.

## Architecture

```
src/
├── config/
│   └── api.js              # API configuration and endpoints
├── utils/
│   └── tokenManager.js     # JWT token management utilities
├── services/
│   ├── apiClient.js        # Main axios client with interceptors
│   ├── authService.js      # Authentication API calls
│   ├── classService.js     # Class management API calls
│   ├── assignmentService.js # Assignment API calls
│   ├── submissionService.js # Submission and grading API calls
│   ├── notificationService.js # Notification API calls
│   └── index.js           # Main services export
├── contexts/
│   └── AuthContext.jsx    # React context for authentication state
├── hooks/
│   └── useApi.js          # Custom hooks for API calls
└── components/
    └── auth/
        ├── ProtectedRoute.jsx # Route protection component
        └── LoginForm.jsx      # Login form component
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
VITE_API_BASE_URL=http://localhost:8000/api
VITE_NODE_ENV=development
VITE_API_DEBUG=true
```

### API Configuration

The API configuration is centralized in `src/config/api.js`:

```javascript
export const API_CONFIG = {
  BASE_URL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api',
  TIMEOUT: 10000,
  ENDPOINTS: {
    // All API endpoints are defined here
  }
};
```

## Usage Examples

### 1. Authentication

```javascript
import { authService } from '../services';

// Login
const handleLogin = async (credentials) => {
  const result = await authService.login(credentials);
  if (result.success) {
    console.log('User logged in:', result.data.user);
  } else {
    console.error('Login failed:', result.message);
  }
};

// Register
const handleRegister = async (userData) => {
  const result = await authService.register(userData);
  if (result.success) {
    console.log('User registered:', result.data.user);
  }
};

// Get current user
const getCurrentUser = async () => {
  const result = await authService.getCurrentUser();
  if (result.success) {
    console.log('Current user:', result.data.user);
  }
};
```

### 2. Using the Auth Context

```javascript
import { useAuth } from '../contexts/AuthContext';

const MyComponent = () => {
  const { user, isAuthenticated, login, logout, isLoading } = useAuth();

  if (isLoading) return <div>Loading...</div>;

  return (
    <div>
      {isAuthenticated ? (
        <div>
          <p>Welcome, {user.username}!</p>
          <button onClick={logout}>Logout</button>
        </div>
      ) : (
        <div>Please log in</div>
      )}
    </div>
  );
};
```

### 3. Protected Routes

```javascript
import ProtectedRoute from '../components/auth/ProtectedRoute';

// Protect a route for teachers only
<Route path="/teacher/dashboard" element={
  <ProtectedRoute requiredRole="teacher">
    <TeacherDashboard />
  </ProtectedRoute>
} />

// Protect a route for any authenticated user
<Route path="/dashboard" element={
  <ProtectedRoute>
    <Dashboard />
  </ProtectedRoute>
} />
```

### 4. Using API Hooks

```javascript
import { useApi, useApiCall } from '../hooks/useApi';
import { classService } from '../services';

const ClassList = () => {
  // Automatic API call on component mount
  const { data: classes, loading, error, refetch } = useApi(
    classService.getClasses,
    [], // dependencies
    {
      onSuccess: (data) => console.log('Classes loaded:', data),
      onError: (error) => console.error('Failed to load classes:', error)
    }
  );

  // Manual API call
  const { execute: createClass, loading: creating } = useApiCall(
    classService.createClass
  );

  const handleCreateClass = async (classData) => {
    const result = await createClass(classData);
    if (result.success) {
      refetch(); // Refresh the class list
    }
  };

  if (loading) return <div>Loading classes...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      {classes?.map(cls => (
        <div key={cls.id}>{cls.name}</div>
      ))}
      <button 
        onClick={() => handleCreateClass({ name: 'New Class' })}
        disabled={creating}
      >
        {creating ? 'Creating...' : 'Create Class'}
      </button>
    </div>
  );
};
```

### 5. Direct API Calls

```javascript
import { classService, assignmentService } from '../services';

// Get classes
const classes = await classService.getClasses();

// Get assignments for a specific class
const assignments = await assignmentService.getClassAssignments('class-id');

// Create new assignment
const newAssignment = await assignmentService.createAssignment({
  title: 'New Assignment',
  class_obj: 'class-id',
  due_date: '2024-12-31T23:59:59Z'
});

// Submit code
const submission = await submissionService.submitCode({
  assignment: 'assignment-id',
  question: 'question-id',
  code_content: 'print("Hello World")',
  language: 'python'
});
```

## API Services

### AuthService
- `register(userData)` - User registration
- `login(credentials)` - User login
- `logout()` - User logout
- `getCurrentUser()` - Get current user info
- `updateCurrentUser(userData)` - Update user profile
- `updateSettings(settings)` - Update user settings

### ClassService
- `getClasses(params)` - Get user's classes
- `getArchivedClasses()` - Get archived classes
- `getClass(classId)` - Get class details
- `createClass(classData)` - Create new class
- `updateClass(classId, classData)` - Update class
- `joinClass(classId, joinCode)` - Join class with code
- `archiveClass(classId)` - Archive/unarchive class
- `getClassPeople(classId)` - Get class roster

### AssignmentService
- `getAssignments(params)` - Get assignments
- `getClassAssignments(classId)` - Get class assignments
- `getAssignment(assignmentId)` - Get assignment details
- `createAssignment(assignmentData)` - Create assignment
- `updateAssignment(assignmentId, assignmentData)` - Update assignment
- `publishAssignment(assignmentId)` - Publish assignment
- `closeAssignment(assignmentId)` - Close assignment

### SubmissionService
- `getSubmissions(params)` - Get submissions
- `getAssignmentSubmissions(assignmentId)` - Get assignment submissions
- `submitCode(submissionData)` - Submit code
- `runCode(codeData)` - Test code without submitting
- `gradeSubmission(submissionId, gradeData)` - Grade submission
- `publishGrade(submissionId)` - Publish grade
- `runAutograder(assignmentId)` - Run autograder

### NotificationService
- `getNotifications(params)` - Get notifications
- `getUnreadNotifications()` - Get unread notifications
- `markAsRead(notificationId)` - Mark notification as read
- `markAllAsRead()` - Mark all notifications as read

## Token Management

JWT tokens are automatically handled by the API client:

- **Storage**: Tokens are stored in localStorage
- **Auto-refresh**: Access tokens are automatically refreshed when expired
- **Auto-logout**: Users are redirected to login when refresh fails
- **Request headers**: Authorization headers are automatically added

## Error Handling

The API client provides consistent error handling:

```javascript
const result = await someApiCall();

if (result.success) {
  // Handle success
  console.log('Data:', result.data);
} else {
  // Handle error
  console.error('Error:', result.message);
  console.error('Field errors:', result.errors);
}
```

## Testing the Connection

1. Start your Django backend: `python manage.py runserver`
2. Start your React frontend: `npm run dev`
3. Visit `http://localhost:5173` and click "Test API Connection"
4. You should see a successful response from the Django API

## Backend Requirements

Make sure your Django backend has:

1. **CORS configured** for `http://localhost:5173`
2. **JWT authentication** enabled
3. **All API endpoints** working as documented
4. **Database migrations** applied

## Next Steps

1. **Replace mock data** in existing components with API calls
2. **Add loading states** to all components
3. **Implement error handling** in UI components
4. **Add form validation** for user inputs
5. **Create registration form** component
6. **Add real-time features** (WebSocket integration)

## Troubleshooting

### Common Issues

1. **CORS errors**: Check Django CORS settings
2. **401 Unauthorized**: Check JWT token configuration
3. **Network errors**: Ensure backend is running on port 8000
4. **Token refresh fails**: Check JWT settings in Django

### Debug Mode

Enable debug mode in `.env`:
```env
VITE_API_DEBUG=true
```

This will log all API requests and responses to the console.