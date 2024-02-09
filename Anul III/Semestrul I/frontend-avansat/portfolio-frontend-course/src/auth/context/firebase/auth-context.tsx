'use client'

import { createContext } from 'react'
import { FirebaseContextType } from '@/auth/types'

export const AuthContext = createContext({} as FirebaseContextType)
