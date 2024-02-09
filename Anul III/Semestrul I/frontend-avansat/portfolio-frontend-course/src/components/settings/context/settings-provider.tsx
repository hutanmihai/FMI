'use client'

import { useMemo, ReactNode } from 'react'
import { useLocalStorage } from '@/hooks/use-local-storage'

import { SettingsValueProps } from '../types'
import { SettingsContext } from './settings-context'

const STORAGE_KEY = 'settings'

type SettingsProviderProps = {
  children: ReactNode
  defaultSettings: SettingsValueProps
}

export function SettingsProvider({ children, defaultSettings }: SettingsProviderProps) {
  const { state, update } = useLocalStorage(STORAGE_KEY, defaultSettings)

  const memoizedValue = useMemo(
    () => ({
      ...state,
      onUpdate: update,
    }),
    [update, state]
  )

  return <SettingsContext.Provider value={memoizedValue}>{children}</SettingsContext.Provider>
}
