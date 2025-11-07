import React, { useState, useEffect } from 'react';
import { getCurrentUser, getProtectedTest, getUserProfile, getDashboard } from '../services/api';

function Protected({ token, onLogout }) {
  const [userInfo, setUserInfo] = useState(null);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  // Load user info on component mount
  useEffect(() => {
    loadUserInfo();
  }, []);

  const loadUserInfo = async () => {
    try {
      const userData = await getCurrentUser(token);
      setUserInfo(userData);
    } catch (err) {
      setError('Failed to load user information');
    }
  };

  const handleProtectedTest = async () => {
    setError('');
    setLoading(true);
    try {
      const data = await getProtectedTest(token);
      setResponse({ endpoint: 'Protected Test', data });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleUserProfile = async () => {
    setError('');
    setLoading(true);
    try {
      const data = await getUserProfile(token);
      setResponse({ endpoint: 'User Profile', data });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDashboard = async () => {
    setError('');
    setLoading(true);
    try {
      const data = await getDashboard(token);
      setResponse({ endpoint: 'Dashboard', data });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="protected-container">
      <h2 className="form-title">🎉 Welcome to Protected Area!</h2>

      {error && <div className="error-message">{error}</div>}

      {userInfo && (
        <div className="user-info">
          <h3>👤 User Information</h3>
          <p><strong>Username:</strong> {userInfo.username}</p>
          <p><strong>Email:</strong> {userInfo.email}</p>
          <p><strong>User ID:</strong> {userInfo.id}</p>
          <p><strong>Status:</strong> {userInfo.is_active ? '✅ Active' : '❌ Inactive'}</p>
          <p><strong>Created At:</strong> {new Date(userInfo.created_at).toLocaleString()}</p>
        </div>
      )}

      <div className="info-message">
        <strong>🔒 Protected Endpoints</strong>
        <p>Click the buttons below to test different protected endpoints. All requests include your JWT token.</p>
      </div>

      <div className="buttons-container">
        <button 
          className="btn btn-info" 
          onClick={handleProtectedTest}
          disabled={loading}
        >
          🧪 Test Endpoint
        </button>
        <button 
          className="btn btn-info" 
          onClick={handleUserProfile}
          disabled={loading}
        >
          👤 User Profile
        </button>
        <button 
          className="btn btn-info" 
          onClick={handleDashboard}
          disabled={loading}
        >
          📊 Dashboard
        </button>
      </div>

      {loading && (
        <div className="info-message">
          <strong>Loading...</strong>
        </div>
      )}

      {response && (
        <div className="response-container">
          <h3>📡 Response from: {response.endpoint}</h3>
          <div className="response-content">
            <pre>{JSON.stringify(response.data, null, 2)}</pre>
          </div>
        </div>
      )}

      <div className="logout-container">
        <button 
          className="btn btn-danger" 
          onClick={onLogout}
        >
          🚪 Logout
        </button>
      </div>

      <div className="info-message" style={{ marginTop: '20px' }}>
        <strong>ℹ️ Token Info</strong>
        <p style={{ wordBreak: 'break-all', fontSize: '0.85rem' }}>
          Your JWT token is stored in the component state and localStorage.
        </p>
      </div>
    </div>
  );
}

export default Protected;

