import React, { useEffect, useMemo, useRef, useState } from 'react';
import useGoogleLogin from './useGoogleLogin';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { AuthContext } from './context';
import { apiFetch } from '../../api';
import { User } from '../../api/types/user';

// Provider for authentication
const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const { login: googleLogin, logout: googleLogout } = useGoogleLogin();

  // States for authentication
  const [user, setUser] = useState<User | undefined>();
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
  const [userJWT, setUserJWT] = useState<string | undefined>();
  const [isLoading, setIsLoading] = useState<boolean>(true);

  // Check if user is logged in on app start
  useEffect(() => {
    console.log('[AUTH] Checking if user is logged in');
    // Search for userJWT in AsyncStorage
    AsyncStorage.getItem('userJWT').then((userJWT) => {
      setIsLoading(false);
      // If userJWT is found, set userJWT, user and isLoggedIn
      if (userJWT) {
        setUserJWT(userJWT);

        // Fetch user data
        apiFetch({
          path: '/user/me',
        }).then((data) => {
          if (data) {
            setUser(data);
            return;
          }

          // If no user is found, logout
          console.log('[AUTH] No user found');
          logout().then();
        });

        // Log user in with JWT
        console.log('[AUTH] Logged in with JWT', userJWT);
        setIsLoggedIn(true);
        return;
      }

      // If no userJWT is found, logout
      console.log('[AUTH] No JWT found');
      setIsLoggedIn(false);
      setUserJWT(undefined);
    });
  }, []);

  // Console log user data when userJWT, user or isLoggedIn changes
  useEffect(() => {
    if (!userJWT) {
      console.log('[AUTH] No JWT found');
      return;
    }

    console.log('----------------');
    console.log('[AUTH] Logged in with JWT', userJWT);
    console.log('[AUTH] Logged in', isLoggedIn);
    console.log('[AUTH] Is loading', isLoading);
    console.log('[AUTH] User', user);
    console.log('----------------');
  }, [userJWT, user, isLoggedIn, isLoading]);

  // Login function
  const login = async () => {
    // Logout first
    await logout();

    // Login with Google
    const user = await googleLogin();

    // If no user or no user.idToken is found, return
    if (!user || !user.idToken) {
      return;
    }

    // Get the JWT token from the API
    const userJWT = await apiFetch({
      method: 'POST',
      path: '/login',
      body: {
        token: user.idToken,
      },
    });

    // If no userJWT is found, return
    if (!userJWT) {
      return;
    }

    // Set userJWT, user
    setUserJWT(userJWT);
    setIsLoggedIn(true);
    await AsyncStorage.setItem('userJWT', userJWT);

    // Fetch user data
    apiFetch({
      path: '/user/me',
    }).then((data) => {
      if (data) {
        setUser(data);
        setIsLoggedIn(true);
        return;
      }

      console.log('[AUTH] No user found');
      logout().then();
    });
  };

  // Logout function
  const logout = async () => {
    // Logout from Google
    await googleLogout();

    // Remove userJWT, user
    await AsyncStorage.removeItem('userJWT');
    setUserJWT(undefined);
    setIsLoggedIn(false);
    setUser(undefined);
  };

  // Create value object for context
  const value = useMemo(
    () => ({ login, logout, isLoggedIn, user, setUser, userJWT, isLoading }),
    [login, logout, user, setUser, isLoggedIn, userJWT, isLoading],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export default AuthProvider;
