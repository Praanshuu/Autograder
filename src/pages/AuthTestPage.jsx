import React, { useState } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { useAuthUser } from '../hooks/useAuthUser';
import { authService } from '../services/authService';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import UserProfile from '../components/auth/UserProfile';
import AuthStatus from '../components/debug/AuthStatus';
import LogoutButton from '../components/auth/LogoutButton';

const AuthTestPage = () => {
  const auth = useAuth();
  const authUser = useAuthUser();
  const [testResults, setTestResults] = useState([]);
  const [testing, setTesting] = useState(false);

  const addTestResult = (test, success, message) => {
    setTestResults(prev => [...prev, { test, success, message, timestamp: new Date() }]);
  };

  const runAuthTests = async () => {
    setTesting(true);
    setTestResults([]);

    // Test 1: Check if tokens exist
    try {
      const hasTokens = authService.isAuthenticated();
      addTestResult('Token Check', hasTokens, hasTokens ? 'Tokens found in localStorage' : 'No valid tokens found');
    } catch (error) {
      addTestResult('Token Check', false, `Error: ${error.message}`);
    }

    // Test 2: Get current user
    try {
      const response = await authService.getCurrentUser();
      addTestResult('Get Current User', response.success, response.success ? 'User data retrieved' : response.message);
    } catch (error) {
      addTestResult('Get Current User', false, `Error: ${error.message}`);
    }

    // Test 3: Test token from localStorage
    try {
      const tokenUser = authService.getUserFromToken();
      addTestResult('Token Parsing', !!tokenUser, tokenUser ? 'Token parsed successfully' : 'Failed to parse token');
    } catch (error) {
      addTestResult('Token Parsing', false, `Error: ${error.message}`);
    }

    setTesting(false);
  };

  const testLogin = async () => {
    const testCredentials = {
      username: 'testuser',
      password: 'testpass123'
    };

    setTesting(true);
    const result = await auth.login(testCredentials);
    addTestResult('Test Login', result.success, result.success ? 'Login successful' : result.error);
    setTesting(false);
  };

  return (
    <div className="container mx-auto p-8 space-y-8">
      <div className="text-center">
        <h1 className="text-3xl font-bold mb-4">Authentication Test Page</h1>
        <p className="text-gray-600">Test and debug authentication functionality</p>
      </div>

      {/* Quick Actions */}
      <Card>
        <CardHeader>
          <CardTitle>Quick Actions</CardTitle>
        </CardHeader>
        <CardContent className="flex gap-4 flex-wrap">
          <Button onClick={runAuthTests} disabled={testing}>
            {testing ? 'Running Tests...' : 'Run Auth Tests'}
          </Button>
          <Button onClick={testLogin} disabled={testing} variant="outline">
            Test Login (testuser/testpass123)
          </Button>
          <LogoutButton />
          <Button 
            variant="outline" 
            onClick={() => window.location.href = '/login'}
          >
            Go to Login
          </Button>
          <Button 
            variant="outline" 
            onClick={() => window.location.href = '/register'}
          >
            Go to Register
          </Button>
        </CardContent>
      </Card>

      {/* Auth State Summary */}
      <Card>
        <CardHeader>
          <CardTitle>Authentication State Summary</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
            <div className={`p-4 rounded-lg ${authUser.isAuthenticated ? 'bg-green-100' : 'bg-red-100'}`}>
              <p className="font-semibold">Authenticated</p>
              <p className={authUser.isAuthenticated ? 'text-green-600' : 'text-red-600'}>
                {authUser.isAuthenticated ? 'Yes' : 'No'}
              </p>
            </div>
            <div className="p-4 rounded-lg bg-blue-100">
              <p className="font-semibold">Role</p>
              <p className="text-blue-600">{authUser.user?.role || 'None'}</p>
            </div>
            <div className="p-4 rounded-lg bg-purple-100">
              <p className="font-semibold">Username</p>
              <p className="text-purple-600">{authUser.user?.username || 'None'}</p>
            </div>
            <div className="p-4 rounded-lg bg-orange-100">
              <p className="font-semibold">Loading</p>
              <p className="text-orange-600">{authUser.isLoading ? 'Yes' : 'No'}</p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Test Results */}
      {testResults.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle>Test Results</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              {testResults.map((result, index) => (
                <div
                  key={index}
                  className={`p-3 rounded-md border ${
                    result.success ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'
                  }`}
                >
                  <div className="flex justify-between items-start">
                    <div>
                      <p className="font-semibold">{result.test}</p>
                      <p className="text-sm text-gray-600">{result.message}</p>
                    </div>
                    <span className={`px-2 py-1 text-xs rounded ${
                      result.success ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                    }`}>
                      {result.success ? 'PASS' : 'FAIL'}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* User Profile */}
      {authUser.isAuthenticated && (
        <div>
          <h2 className="text-2xl font-bold mb-4">User Profile</h2>
          <UserProfile />
        </div>
      )}

      {/* Debug Information */}
      <div>
        <h2 className="text-2xl font-bold mb-4">Debug Information</h2>
        <AuthStatus />
      </div>
    </div>
  );
};

export default AuthTestPage;