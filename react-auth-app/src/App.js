import React, { useState, useEffect } from 'react';
import './App.css';
import Register from './components/Register';
import Login from './components/Login';
import Protected from './components/Protected';

function App() {
  const [token, setToken] = useState(null);
  const [view, setView] = useState('login'); // 'login', 'register', 'protected'

  // Load token from localStorage on component mount
  useEffect(() => {
    const savedToken = localStorage.getItem('authToken');
    if (savedToken) {
      setToken(savedToken);
      setView('protected');
    }
  }, []);

  // Save token to localStorage when it changes
  useEffect(() => {
    if (token) {
      localStorage.setItem('authToken', token);
    } else {
      localStorage.removeItem('authToken');
    }
  }, [token]);

  const handleLoginSuccess = (accessToken) => {
    setToken(accessToken);
    setView('protected');
  };

  const handleRegisterSuccess = () => {
    setView('login');
  };

  const handleLogout = () => {
    setToken(null);
    setView('login');
  };

  return (
    <div className="App">
      <div className="container">
        <h1 className="app-title">🔐 React Auth App</h1>
        <p className="app-subtitle">FastAPI JWT Authentication Demo</p>

        {view === 'login' && (
          <Login 
            onLoginSuccess={handleLoginSuccess}
            onSwitchToRegister={() => setView('register')}
          />
        )}

        {view === 'register' && (
          <Register 
            onRegisterSuccess={handleRegisterSuccess}
            onSwitchToLogin={() => setView('login')}
          />
        )}

        {view === 'protected' && token && (
          <Protected 
            token={token}
            onLogout={handleLogout}
          />
        )}
      </div>
    </div>
  );
}

export default App;

