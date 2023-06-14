import AsyncStorage from '@react-native-async-storage/async-storage';
import { ADMIN_JWT, BACKEND_URL } from '../env';

// Custom API fetch function
export const apiFetch = async ({
  method = 'GET',
  path,
  body,
  isAdmin = false,
}: {
  method?: 'GET' | 'POST' | 'PUT' | 'DELETE';
  path: string;
  body?: unknown;
  isAdmin?: boolean;
}) => {
  // Check if there is a JWT in storage
  const userJWT = await AsyncStorage.getItem('userJWT');

  // If there is no JWT and the path is not /login, return
  if (!userJWT && path !== '/login') {
    console.log('[API] No JWT found');
    return;
  }

  // Set the default headers
  const defaultHeaders = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  };

  // Set the authorization headers
  const authHeaders = {
    Authorization: `Bearer ${isAdmin ? ADMIN_JWT : userJWT}`,
  };

  // If the method is GET and there is a body, return
  if (method === 'GET' && body) {
    console.log('[API] GET request with body');
    return;
  }

  let data;
  try {
    // If the path is /login, send a POST request with the token as a query parameter
    if (path === '/login') {
      console.log('[API] Login request');
      console.log(BACKEND_URL + path, `?token=${(body as any).token}`);
      const response = await fetch(BACKEND_URL + path + `?token=${(body as any).token}`, {
        method,
        headers: {
          ...defaultHeaders,
        },
      });
      data = await response.json();

      // Return the JWT
      return data.token;
    }

    // If the path is not /login, send a request with the JWT in the Authorization header
    console.log('[API] Request', method, path);
    const response = await fetch(BACKEND_URL + path, {
      method,
      body: body ? JSON.stringify(body) : undefined,
      headers: {
        ...defaultHeaders,
        ...authHeaders,
      },
    });

    data = await response.json();
  } catch (error) {
    console.log(`[API] ${path} Error`, error);
  }

  // Return the data
  return data;
};
