import React, { useState } from 'react';
import { api } from '../../services/apiClient';
import { Button } from '../ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../ui/card';

const ApiTest = () => {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const testApiConnection = async () => {
    setLoading(true);
    try {
      // Test the API root endpoint
      const response = await api.get('/');
      setResult({
        success: true,
        data: response.data,
        status: response.status,
      });
    } catch (error) {
      setResult({
        success: false,
        error: error.message,
        status: error.response?.status || 'Network Error',
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="w-full max-w-2xl mx-auto mt-8">
      <CardHeader>
        <CardTitle>API Connection Test</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <Button
          onClick={testApiConnection}
          disabled={loading}
          className="w-full"
        >
          {loading ? 'Testing...' : 'Test API Connection'}
        </Button>

        {result && (
          <div className="mt-4">
            <h3 className="font-semibold mb-2">Result:</h3>
            <div className={`p-4 rounded-md ${result.success ? 'bg-green-50 border border-green-200' : 'bg-red-50 border border-red-200'}`}>
              <div className="text-sm">
                <p><strong>Status:</strong> {result.status}</p>
                <p><strong>Success:</strong> {result.success ? 'Yes' : 'No'}</p>
                {result.success ? (
                  <div>
                    <p><strong>API Response:</strong></p>
                    <pre className="mt-2 text-xs bg-gray-100 p-2 rounded overflow-auto">
                      {JSON.stringify(result.data, null, 2)}
                    </pre>
                  </div>
                ) : (
                  <p><strong>Error:</strong> {result.error}</p>
                )}
              </div>
            </div>
          </div>
        )}

        <div className="text-sm text-gray-600">
          <p><strong>Expected Backend URL:</strong> http://localhost:8000/api</p>
          <p><strong>Test Endpoint:</strong> GET /api/</p>
          <p className="mt-2">
            Make sure your Django backend is running on port 8000 before testing.
          </p>
        </div>
      </CardContent>
    </Card>
  );
};

export default ApiTest;