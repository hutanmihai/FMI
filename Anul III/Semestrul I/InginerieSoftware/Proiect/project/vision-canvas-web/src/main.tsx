import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Root from './routes/Root';
import Error from './routes/Error';
import Login from './routes/Login';
import Register from './routes/Register';
import Providers from './providers';
import ProtectedRoute from './routes/ProtectedRoute';
import Dashboard from './routes/Dashboard';
import ProtectedInvertedRoute from './routes/ProtectedInvertedRoute';
import Account from './routes/Account';
import Landing from './routes/Landing';
import Subscription from './routes/Subscription';
import Editor from './routes/Editor';
import ForgotPassword from './routes/ForgotPassword';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    errorElement: <Error />,
    children: [
      {
        path: '/',
        element: <Landing />,
      },
      {
        path: '/register',
        element: (
          <ProtectedInvertedRoute redirectPath={'/dashboard'}>
            <Register />
          </ProtectedInvertedRoute>
        ),
      },
      {
        path: '/login',
        element: (
          <ProtectedInvertedRoute redirectPath={'/dashboard'}>
            <Login />
          </ProtectedInvertedRoute>
        ),
      },
      {
        path: '/forgot-password',
        element: (
          <ProtectedInvertedRoute redirectPath={'/forgot-password'}>
            <ForgotPassword />
          </ProtectedInvertedRoute>
        ),
      },
      {
        path: '/dashboard',
        element: (
          <ProtectedRoute redirectPath={'/register'}>
            <Dashboard />
          </ProtectedRoute>
        ),
      },
      {
        path: '/account',
        element: (
          <ProtectedRoute redirectPath={'/register'}>
            <Account />
          </ProtectedRoute>
        ),
      },
      {
        path: '/subscription',
        element: (
          <ProtectedRoute redirectPath={'/register'}>
            <Subscription />
          </ProtectedRoute>
        ),
      },
      {
        path: '/editor',
        element: (
          <ProtectedRoute redirectPath={'/register'}>
            <Editor />
          </ProtectedRoute>
        ),
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Providers>
      <RouterProvider router={router} />
    </Providers>
  </React.StrictMode>,
);
