'use client'

import { initializeApp } from 'firebase/app'
import { FIREBASE_API } from '@/config-global'
import { AuthContext } from '@/auth/context/firebase/auth-context'
import { AuthUserType, ActionMapType, AuthStateType } from '@/auth/types'
import { doc, getDoc, collection, getFirestore } from 'firebase/firestore'
import { useMemo, useEffect, ReactNode, useReducer, useCallback } from 'react'
import {
  getAuth,
  signOut,
  signInWithPopup,
  onAuthStateChanged,
  GoogleAuthProvider,
  signInWithEmailAndPassword,
} from 'firebase/auth'

const firebaseApp = initializeApp(FIREBASE_API)

export const AUTH = getAuth(firebaseApp)

export const DB = getFirestore(firebaseApp)

export const projectsRef = collection(DB, 'projects')

enum Types {
  INITIAL = 'INITIAL',
}

type Payload = {
  [Types.INITIAL]: {
    user: AuthUserType
  }
}

type Action = ActionMapType<Payload>[keyof ActionMapType<Payload>]

const initialState: AuthStateType = {
  user: null,
  loading: true,
}

const reducer = (state: AuthStateType, action: Action) => {
  if (action.type === Types.INITIAL) {
    return {
      loading: false,
      user: action.payload.user,
    }
  }
  return state
}

type Props = {
  children: ReactNode
}

export function AuthProvider({ children }: Props) {
  const [state, dispatch] = useReducer(reducer, initialState)

  const initialize = useCallback(() => {
    try {
      onAuthStateChanged(AUTH, async (user) => {
        if (user) {
          const userProfile = doc(DB, 'users', user.uid)

          const docSnap = await getDoc(userProfile)

          const profile = docSnap.data()

          dispatch({
            type: Types.INITIAL,
            payload: {
              user: {
                ...user,
                ...profile,
                id: user.uid,
              },
            },
          })
        } else {
          dispatch({
            type: Types.INITIAL,
            payload: {
              user: null,
            },
          })
        }
      })
    } catch (error) {
      console.error(error)
      dispatch({
        type: Types.INITIAL,
        payload: {
          user: null,
        },
      })
    }
  }, [])

  useEffect(() => {
    initialize()
  }, [initialize])

  // LOGIN
  const login = useCallback(async (email: string, password: string) => {
    await signInWithEmailAndPassword(AUTH, email, password)
  }, [])

  const loginWithGoogle = useCallback(async () => {
    const provider = new GoogleAuthProvider()

    await signInWithPopup(AUTH, provider)
  }, [])

  // LOGOUT
  const logout = useCallback(async () => {
    await signOut(AUTH)
  }, [])

  const checkAuthenticated = state.user ? 'authenticated' : 'unauthenticated'

  const status = state.loading ? 'loading' : checkAuthenticated

  const memoizedValue = useMemo(
    () => ({
      user: state.user,
      loading: status === 'loading',
      authenticated: status === 'authenticated',
      unauthenticated: status === 'unauthenticated',
      login,
      logout,
      loginWithGoogle,
    }),
    [status, state.user, login, logout, loginWithGoogle]
  )

  return <AuthContext.Provider value={memoizedValue}>{children}</AuthContext.Provider>
}
