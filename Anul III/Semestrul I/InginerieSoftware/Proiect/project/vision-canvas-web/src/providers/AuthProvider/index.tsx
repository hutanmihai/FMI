import { ReactNode, useCallback, useEffect, useMemo, useState } from 'react';
import { AuthContext } from './context.ts';
import {
  User,
  GoogleAuthProvider,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signInWithPopup,
  signOut,
  onAuthStateChanged,
  sendPasswordResetEmail,
} from 'firebase/auth';
import { auth } from '../../utils/firebase.ts';
import { getProfile, setProfile } from '../../api/profile';
import { Profile } from '../../api/profile/types.ts';

const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<User | undefined | null>(null);
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
  const [currentProfile, setCurrentProfile] = useState<Profile | undefined | null>(null);

  useEffect(() => {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        logInUser(user).then();
        console.log('[AUTH STATE CHANGED] Logged in user detected');
      } else {
        logOutUser().then();
        console.log('[AUTH STATE CHANGED] No logged in user detected');
      }
    });
  }, []);

  const logInUser = async (user: User) => {
    setUser(user);
    setIsLoggedIn(true);

    const _profile = await getProfile(user.email ?? user.uid);
    setCurrentProfile(_profile);

    console.log('[LOGGED IN USER]', user.email);
  };

  const logOutUser = async () => {
    setUser(undefined);
    setIsLoggedIn(false);

    setCurrentProfile(undefined);

    console.log('[LOGGED OUT USER]');
  };

  const signUpUserWithEmailAndPassword = useCallback(async (email: string, password: string) => {
    try {
      const userCredentials = await createUserWithEmailAndPassword(auth, email, password);

      const user = userCredentials.user;
      await logInUser(user);

      await setProfile(user.email ?? user.uid, {} as Profile);

      console.log('[SIGNED UP USER]', user.email);
      return true;
    } catch (error) {
      console.log(error);
      alert('Error signing up. Please try again.');
      return false;
    }
  }, []);

  const signInUserWithEmailAndPassword = useCallback(async (email: string, password: string) => {
    try {
      const userCredentials = await signInWithEmailAndPassword(auth, email, password);

      const user = userCredentials.user;
      await logInUser(user);

      console.log('[SIGNED IN USER]', user.email);
      return true;
    } catch (error) {
      console.log(error);
      alert('Invalid email or password.');
      return false;
    }
  }, []);

  const signInUserWithGoogle = useCallback(async () => {
    try {
      const provider = new GoogleAuthProvider();
      const userCredentials = await signInWithPopup(auth, provider);

      const user = userCredentials.user;
      await logInUser(user);

      await setProfile(user.email ?? user.uid, { firstName: user.displayName } as Profile);

      console.log('[SIGNED IN USER WITH GOOGLE]', user.email);
      return true;
    } catch (error) {
      console.log(error);
      alert('Error signing in with Google. Please try again.');
      return false;
    }
  }, []);

  const signOutUser = useCallback(async () => {
    try {
      await signOut(auth);

      await logOutUser();

      console.log('[SIGNED OUT USER]');
      return true;
    } catch (error) {
      console.log(error);
      alert('Error signing out. Please try again.');
      return false;
    }
  }, []);

  const sendUserPasswordResetEmail = async (email: string) => {
    try {
      await sendPasswordResetEmail(auth, email);
      console.log('[SENT PASSWORD RESET EMAIL]');
      alert('Password reset email sent. Please check your inbox.');
    } catch (error) {
      console.log(error);
      alert('Error sending password reset email. Please try again.');
    }
  };

  const value = useMemo(
    () => ({
      user,
      currentProfile,
      setCurrentProfile,
      isLoggedIn,
      signUpUserWithEmailAndPassword,
      signInUserWithEmailAndPassword,
      signInUserWithGoogle,
      signOutUser,
      sendUserPasswordResetEmail,
    }),
    [
      user,
      currentProfile,
      setCurrentProfile,
      isLoggedIn,
      signUpUserWithEmailAndPassword,
      signInUserWithEmailAndPassword,
      signInUserWithGoogle,
      signOutUser,
      sendUserPasswordResetEmail,
    ],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export default AuthProvider;
