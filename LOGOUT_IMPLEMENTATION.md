# Logout/Sign Out Implementation

## Changes Made

### 1. StudentLayout.jsx
- Added `useAuth` hook import
- Added `useNavigate` hook import
- Created `handleLogout` function that calls `logout()` and navigates to `/login`
- Connected sidebar "Sign Out" button to `handleLogout`
- Connected dropdown menu "Logout" item to `handleLogout`
- Updated user avatar to show actual user initials from `user.first_name` and `user.last_name`
- Updated user name display to show actual user name

### 2. TeacherLayout.jsx
- Added `useAuth` hook import
- Added `useNavigate` hook import
- Created `handleLogout` function that calls `logout()` and navigates to `/login`
- Connected sidebar "Sign Out" button to `handleLogout`
- Connected dropdown menu "Logout" item to `handleLogout`
- Updated user avatar to show actual user initials from `user.first_name` and `user.last_name`
- Updated user name display to show actual user name

## How It Works

### Logout Flow:
1. User clicks "Sign Out" button (sidebar) or "Logout" (dropdown menu)
2. `handleLogout()` is called
3. `logout()` from AuthContext is executed:
   - Calls `authService.logout()`
   - Clears JWT tokens from localStorage
   - Updates auth state (user = null, isAuthenticated = false)
4. User is redirected to `/login` page

### Token Management:
- Access token and refresh token are stored in localStorage
- Keys: `autograder_access_token` and `autograder_refresh_token`
- On logout, both tokens are removed
- User must log in again to get new tokens

## Testing

### Test Logout Functionality:

1. **Login as Student**
   - Go to http://localhost:5173/login
   - Login with: `student_315` / `password`
   - You should see the student dashboard

2. **Test Sidebar Logout**
   - Click the "Sign Out" button at the bottom of the sidebar
   - You should be redirected to the login page
   - Try accessing `/student/dashboard` - you should be redirected to login

3. **Login as Teacher**
   - Login with: `teacher` / `password` or `Sharingan` / `testpass123`
   - You should see the teacher dashboard

4. **Test Dropdown Logout**
   - Click on your profile avatar/name in the top right
   - Click "Logout" in the dropdown menu
   - You should be redirected to the login page
   - Try accessing `/teacher/dashboard` - you should be redirected to login

5. **Verify Token Clearing**
   - Open browser DevTools (F12)
   - Go to Application > Local Storage > http://localhost:5173
   - After logout, verify that `autograder_access_token` and `autograder_refresh_token` are removed

## Additional Features

### User Display:
- Both layouts now show the actual logged-in user's name and initials
- Student layout: Shows first and last name in dropdown
- Teacher layout: Shows first and last name in dropdown
- Avatar shows user initials (first letter of first name + first letter of last name)

### Logout Locations:
1. **Sidebar** - "Sign Out" button at the bottom (visible on desktop)
2. **Dropdown Menu** - "Logout" option in user profile dropdown (visible on all screen sizes)

## Files Modified

1. `src/components/layout/StudentLayout.jsx`
2. `src/components/layout/TeacherLayout.jsx`

## Files Already Implemented (No Changes Needed)

1. `src/contexts/AuthContext.jsx` - Already has logout function
2. `src/services/authService.js` - Already has logout implementation
3. `src/utils/tokenManager.js` - Already has clearTokens function
4. `src/components/auth/LogoutButton.jsx` - Standalone logout button component (can be used elsewhere)
