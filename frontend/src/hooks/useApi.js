import { useState, useEffect, useCallback } from 'react';

// Custom hook for API calls with loading states
export const useApi = (apiFunction, dependencies = [], options = {}) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const { 
    immediate = true, // Whether to call API immediately
    onSuccess = null, // Success callback
    onError = null,   // Error callback
  } = options;

  const execute = useCallback(async (...args) => {
    try {
      setLoading(true);
      setError(null);
      
      const response = await apiFunction(...args);
      
      if (response.success) {
        setData(response.data);
        if (onSuccess) onSuccess(response.data);
        return response;
      } else {
        const errorMessage = response.message || 'An error occurred';
        setError(errorMessage);
        if (onError) onError(errorMessage);
        return response;
      }
    } catch (err) {
      const errorMessage = err.message || 'An unexpected error occurred';
      setError(errorMessage);
      if (onError) onError(errorMessage);
      return { success: false, error: errorMessage };
    } finally {
      setLoading(false);
    }
  }, [apiFunction, onSuccess, onError]);

  useEffect(() => {
    if (immediate && apiFunction) {
      execute();
    }
  }, dependencies);

  const refetch = useCallback(() => {
    return execute();
  }, [execute]);

  return {
    data,
    loading,
    error,
    execute,
    refetch,
  };
};

// Hook for manual API calls (not automatic)
export const useApiCall = (apiFunction, options = {}) => {
  return useApi(apiFunction, [], { ...options, immediate: false });
};

// Hook for paginated API calls
export const usePaginatedApi = (apiFunction, dependencies = [], options = {}) => {
  const [allData, setAllData] = useState([]);
  const [hasMore, setHasMore] = useState(true);
  const [page, setPage] = useState(1);

  const { data, loading, error, execute } = useApi(
    (...args) => apiFunction(...args, { page }),
    [...dependencies, page],
    options
  );

  useEffect(() => {
    if (data) {
      if (page === 1) {
        setAllData(data.results || data);
      } else {
        setAllData(prev => [...prev, ...(data.results || data)]);
      }
      
      // Check if there's more data (adjust based on your API response structure)
      setHasMore(data.next ? true : false);
    }
  }, [data, page]);

  const loadMore = useCallback(() => {
    if (hasMore && !loading) {
      setPage(prev => prev + 1);
    }
  }, [hasMore, loading]);

  const reset = useCallback(() => {
    setPage(1);
    setAllData([]);
    setHasMore(true);
  }, []);

  return {
    data: allData,
    loading,
    error,
    hasMore,
    loadMore,
    reset,
    refetch: () => {
      reset();
      execute();
    },
  };
};