// Token Management Utilities
const TOKEN_KEYS = {
  ACCESS: 'autograder_access_token',
  REFRESH: 'autograder_refresh_token',
};

export const tokenManager = {
  // Get tokens from localStorage
  getAccessToken: () => {
    return localStorage.getItem(TOKEN_KEYS.ACCESS);
  },

  getRefreshToken: () => {
    return localStorage.getItem(TOKEN_KEYS.REFRESH);
  },

  // Set tokens in localStorage
  setTokens: (accessToken, refreshToken) => {
    if (accessToken) {
      localStorage.setItem(TOKEN_KEYS.ACCESS, accessToken);
    }
    if (refreshToken) {
      localStorage.setItem(TOKEN_KEYS.REFRESH, refreshToken);
    }
  },

  // Clear tokens from localStorage
  clearTokens: () => {
    localStorage.removeItem(TOKEN_KEYS.ACCESS);
    localStorage.removeItem(TOKEN_KEYS.REFRESH);
  },

  // Check if user is authenticated
  isAuthenticated: () => {
    const token = tokenManager.getAccessToken();
    if (!token) return false;

    try {
      // Check if token is expired (JWT tokens have exp claim)
      const payload = JSON.parse(atob(token.split('.')[1]));
      const currentTime = Date.now() / 1000;
      return payload.exp > currentTime;
    } catch (error) {
      console.error('Error parsing token:', error);
      return false;
    }
  },

  // Get user info from token
  getUserFromToken: () => {
    const token = tokenManager.getAccessToken();
    if (!token) return null;

    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      return {
        userId: payload.user_id,
        username: payload.username,
        exp: payload.exp,
      };
    } catch (error) {
      console.error('Error parsing token:', error);
      return null;
    }
  },
};