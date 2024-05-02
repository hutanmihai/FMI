import { useRouter, useSegments } from 'expo-router'
import { createContext, useContext, useState, useEffect, useCallback, ReactNode } from 'react'

import { useLogin, useRegister } from '@/hooks/auth'
import { me } from '@/requests/user'
import { TLoginRequest, TRegisterRequest } from '@/types/auth'
import { TUser } from '@/types/user'
import { deleteTokens, storeTokens } from '@/utils/session'

type AuthContextType = {
  user: TUser | null
  isLoading: boolean
  login: (payload: TLoginRequest) => Promise<void>
  register: (payload: TRegisterRequest) => Promise<void>
  logout: () => Promise<void>
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<TUser | null>(null)
  const [isLoading, setIsLoading] = useState(false)

  const segment = useSegments()[0]
  const router = useRouter()

  const { mutate: loginMutation } = useLogin()
  const { mutate: registerMutation } = useRegister()

  useEffect(() => {
    if (!user && segment !== '(auth)') {
      router.replace('(auth)/login')
    } else if (user && segment === '(auth)') {
      router.replace('(app)/game/list')
    }
  }, [user, segment])

  const login = useCallback(
    async (payload: TLoginRequest) => {
      setIsLoading(true)
      loginMutation(payload, {
        onSuccess: async (tokens) => {
          try {
            await storeTokens(tokens)
            const { user } = await me()
            setUser(user)
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
          } catch (error) {
            await deleteTokens()
            setUser(null)
          }
        },
        onError: () => {
          setUser(null)
        },
      })
      setIsLoading(false)
    },
    [loginMutation]
  )

  const register = useCallback(
    async (payload: TRegisterRequest) => {
      setIsLoading(true)
      registerMutation(payload, {
        onSuccess: async () => {
          router.push('(auth)/login')
        },
      })
      setIsLoading(false)
    },
    [registerMutation]
  )

  const logout = useCallback(async () => {
    await deleteTokens()
    setUser(null)
  }, [])

  const value = { user, isLoading, login, register, logout }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}
