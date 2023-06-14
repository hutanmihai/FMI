import { GoogleSignin } from '@react-native-google-signin/google-signin';

// Custom hook for Google login
const useGoogleLogin = () => {
  // Login with Google
  const login = async () => {
    // Configure Google Signin with client IDs
    GoogleSignin.configure({
      webClientId: '629397680151-ddanmmurphd401a47956hd5efi039s07.apps.googleusercontent.com',
      iosClientId: '629397680151-07imd6m10o7nm8f3cqii26hpdamj6sd1.apps.googleusercontent.com',
    });

    // Check if Google Play Services are available, otherwise return undefined
    try {
      await GoogleSignin.hasPlayServices();
    } catch (error) {
      console.log('[GOOGLE PLAY SERVICE]', error);
      return undefined;
    }

    // Try to log in with Google and return the user, otherwise return undefined
    try {
      return await GoogleSignin.signIn();
    } catch (error) {
      console.log('[GOOGLE SIGNIN]', error);
      return undefined;
    }
  };

  // Logout from Google
  const logout = async () => {
    // Revoke access and sign out from Google, otherwise log the error
    try {
      await GoogleSignin.revokeAccess();
      await GoogleSignin.signOut();
    } catch {
      console.log('[GOOGLE SIGNOUT]');
    }
  };

  // Return the login and logout functions
  return { login, logout };
};

export default useGoogleLogin;
