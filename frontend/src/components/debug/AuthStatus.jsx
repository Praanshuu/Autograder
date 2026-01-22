import React from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { tokenManager } from '../../utils/tokenManager';
import { Card, CardContent, CardHeader, CardTitle } from '../ui/card';
import { Button } from '../ui/button';

const AuthStatus = () => {
  const { user, isAuthenticated, isLoading, error } = useAuth();
  
  const accessToken = tokenManager.getAccessToken();
  const refreshToken = tokenManager.getRefreshToken();
  const tokenUser = tokenManager.getUserFromToken();

  const clearTokens = () => {
    tokenManager.clearTokens();
    window.location.reload();
  };

  return (
    <Card className="w-full max-w-4xl mx-auto mt-8">
      <CardHeader>
        <CardTitle>Authentication Status (Debug)</CardTitle>
      </CardHeader>
      <CardContent className="space-y-6">
        {/* Auth Context State */}
        <div>
          <h3 className="font-semibold mb-2">Auth Context State</h3>
          <div className="bg-gray-50 p-4 rounded-md text-sm">
            <div className="grid grid-cols-2 gap-4">
              <div>
                <p><strong>Is Authenticated:</strong> {isAuthenticated ? 'Yes' : 'No'}</p>
                <p><strong>Is Loading:</strong> {isLoading ? 'Yes' : 'No'}</p>
                <p><strong>Has Error:</strong> {error ? 'Yes' : 'No'}</p>
                {error && <p><strong>Error:</strong> {error}</p>}
              </div>
              <div>
                <p><strong>User ID:</strong> {user?.id || 'None'}</p>
                <p><strong>Username:</strong> {user?.username || 'None'}</p>
                <p><strong>Role:</strong> {user?.role || 'None'}</p>
                <p><strong>Email:</strong> {user?.email || 'None'}</p>
              </div>
            </div>
          </div>
        </div>

        {/* Token Information */}
        <div>
          <h3 className="font-semibold mb-2">Token Information</h3>
          <div className="bg-gray-50 p-4 rounded-md text-sm">
            <div className="space-y-2">
              <p><strong>Has Access Token:</strong> {accessToken ? 'Yes' : 'No'}</p>
              <p><strong>Has Refresh Token:</strong> {refreshToken ? 'Yes' : 'No'}</p>
              
              {accessToken && (
                <div className="mt-4">
                  <p><strong>Access Token (first 50 chars):</strong></p>
                  <code className="block bg-white p-2 rounded border text-xs break-all">
                    {accessToken.substring(0, 50)}...
                  </code>
                </div>
              )}
              
              {tokenUser && (
                <div className="mt-4">
                  <p><strong>Token User Info:</strong></p>
                  <pre className="bg-white p-2 rounded border text-xs">
                    {JSON.stringify(tokenUser, null, 2)}
                  </pre>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Full User Object */}
        {user && (
          <div>
            <h3 className="font-semibold mb-2">Full User Object</h3>
            <div className="bg-gray-50 p-4 rounded-md">
              <pre className="text-xs overflow-auto">
                {JSON.stringify(user, null, 2)}
              </pre>
            </div>
          </div>
        )}

        {/* Actions */}
        <div>
          <h3 className="font-semibold mb-2">Debug Actions</h3>
          <div className="flex gap-2">
            <Button
              variant="outline"
              size="sm"
              onClick={clearTokens}
            >
              Clear Tokens & Reload
            </Button>
            <Button
              variant="outline"
              size="sm"
              onClick={() => console.log('Auth State:', { user, isAuthenticated, isLoading, error })}
            >
              Log Auth State
            </Button>
          </div>
        </div>

        {/* Local Storage Contents */}
        <div>
          <h3 className="font-semibold mb-2">Local Storage (Auth Keys)</h3>
          <div className="bg-gray-50 p-4 rounded-md text-sm">
            <div className="space-y-1">
              {Object.keys(localStorage).filter(key => key.includes('autograder')).map(key => (
                <div key={key} className="flex justify-between">
                  <span className="font-mono">{key}:</span>
                  <span className="text-gray-600 truncate ml-2 max-w-xs">
                    {localStorage.getItem(key)?.substring(0, 30)}...
                  </span>
                </div>
              ))}
              {Object.keys(localStorage).filter(key => key.includes('autograder')).length === 0 && (
                <p className="text-gray-500">No autograder keys found in localStorage</p>
              )}
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default AuthStatus;