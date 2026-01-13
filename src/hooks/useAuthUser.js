import { useAuth } from '../contexts/AuthContext';

// Convenience hook for accessing user information
export const useAuthUser = () => {
  const { user, isAuthenticated, isLoading } = useAuth();

  return {
    user,
    isAuthenticated,
    isLoading,
    isTeacher: user?.role === 'teacher',
    isStudent: user?.role === 'student',
    isTA: user?.role === 'ta',
    isAdmin: user?.role === 'admin',
    fullName: user ? `${user.first_name} ${user.last_name}` : '',
    initials: user ? `${user.first_name?.[0] || ''}${user.last_name?.[0] || ''}` : '',
  };
};