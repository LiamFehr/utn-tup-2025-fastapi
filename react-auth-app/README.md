# React Auth App - FastAPI Integration

A React application that demonstrates authentication with a FastAPI backend using JWT tokens.

## Features

- 🔐 User Registration
- 🔑 User Login with JWT Authentication
- 🛡️ Protected Routes/Endpoints
- 💾 Token Storage (localStorage + React State)
- 🎨 Modern, Responsive UI
- 📱 Mobile-Friendly Design

## Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- FastAPI backend running on `http://localhost:8000`

## Installation

1. Navigate to the react app directory:
```bash
cd react-auth-app
```

2. Install dependencies:
```bash
npm install
```

## Configuration

The API base URL is configured in `src/services/api.js`. By default, it's set to `http://localhost:8000`.

If your FastAPI backend is running on a different port, update the `API_BASE_URL` constant:

```javascript
const API_BASE_URL = 'http://localhost:YOUR_PORT';
```

## Running the Application

1. Make sure your FastAPI backend is running:
```bash
# In your FastAPI project directory
uvicorn main:app --reload
```

2. Start the React development server:
```bash
npm start
```

The application will open automatically in your browser at `http://localhost:3000`.

## Usage

### Registration
1. Click on "Create Account" or "Register here"
2. Fill in username, email, and password
3. Click "Register"
4. You'll be automatically redirected to the login page after successful registration

### Login
1. Enter your username and password
2. Click "Login"
3. Upon successful authentication, you'll be redirected to the protected area

### Protected Area
Once logged in, you can:
- View your user information
- Test protected endpoints:
  - **Test Endpoint**: Basic protected endpoint test
  - **User Profile**: Get your user profile
  - **Dashboard**: Access your personalized dashboard
- Logout from your account

## Project Structure

```
react-auth-app/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Login.js          # Login component
│   │   ├── Register.js       # Registration component
│   │   └── Protected.js      # Protected area component
│   ├── services/
│   │   └── api.js           # API service functions
│   ├── App.js               # Main application component
│   ├── App.css              # Application styles
│   ├── index.js             # Entry point
│   └── index.css            # Global styles
├── package.json
└── README.md
```

## API Endpoints Used

### Authentication Endpoints
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get JWT token
- `GET /auth/me` - Get current user information

### Protected Endpoints
- `GET /protected/test` - Test protected endpoint
- `GET /protected/user-profile` - Get user profile
- `GET /protected/dashboard` - Get user dashboard

## Token Management

The JWT token is stored in two places:
1. **React State**: For immediate access during the current session
2. **localStorage**: For persistence across page refreshes

The token is automatically included in the `Authorization` header for all protected endpoint requests.

## Features Explained

### State Management
- Uses React `useState` for managing token, user info, and UI state
- Uses React `useEffect` for loading user data and persisting token

### Error Handling
- All API calls include proper error handling
- User-friendly error messages are displayed
- Loading states for better UX

### Responsive Design
- Mobile-first approach
- Beautiful gradient backgrounds
- Smooth animations and transitions
- Modern card-based layout

## Building for Production

To create a production build:

```bash
npm run build
```

This creates an optimized build in the `build/` directory.

## Troubleshooting

### CORS Issues
Make sure your FastAPI backend has CORS middleware configured to allow requests from `http://localhost:3000`.

### API Connection Issues
1. Verify the FastAPI server is running on `http://localhost:8000`
2. Check the `API_BASE_URL` in `src/services/api.js`
3. Ensure CORS is properly configured on the backend

### Token Issues
If you encounter authentication issues:
1. Clear localStorage: `localStorage.clear()` in browser console
2. Refresh the page
3. Try logging in again

## Technologies Used

- **React 18.2** - UI Library
- **JavaScript (ES6+)** - Programming Language
- **Fetch API** - HTTP Requests
- **localStorage** - Token Persistence
- **CSS3** - Styling with modern features

## License

This project is for educational purposes.

