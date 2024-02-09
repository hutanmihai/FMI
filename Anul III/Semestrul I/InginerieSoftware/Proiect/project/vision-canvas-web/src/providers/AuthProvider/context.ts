import { createContext } from 'react';
import { User } from 'firebase/auth';
import { Profile } from '../../api/profile/types.ts';

export interface AuthContextProps {
  user?: User | null;
  currentProfile?: Profile | null;
  setCurrentProfile: (profile: Profile) => void;
  isLoggedIn: boolean;
  signUpUserWithEmailAndPassword: (email: string, password: string) => Promise<boolean>;
  signInUserWithEmailAndPassword: (email: string, password: string) => Promise<boolean>;
  signInUserWithGoogle: () => Promise<boolean>;
  signOutUser: () => Promise<boolean>;
  sendUserPasswordResetEmail: (email: string) => Promise<void>;
}

export const AuthContext = createContext<AuthContextProps>({
  user: null,
  currentProfile: null,
  setCurrentProfile: () => {},
  isLoggedIn: false,
  signUpUserWithEmailAndPassword: async () => false,
  signInUserWithEmailAndPassword: async () => false,
  signInUserWithGoogle: async () => false,
  signOutUser: async () => false,
  sendUserPasswordResetEmail: async () => {},
});
