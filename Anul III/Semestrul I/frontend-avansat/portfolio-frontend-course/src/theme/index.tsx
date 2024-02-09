'use client'

import { useMemo, ReactNode } from 'react'
import { useSettingsContext } from '@/components/settings'

import CssBaseline from '@mui/material/CssBaseline'
import { createTheme, ThemeOptions, ThemeProvider as MuiThemeProvider } from '@mui/material/styles'

import { palette } from './palette'
import { shadows } from './shadows'
import { typography } from './typography'
import { customShadows } from './custom-shadows'
import { componentsOverrides } from './overrides'
import NextAppDirEmotionCacheProvider from './next-emotion-cache'

type Props = {
  children: ReactNode
}

export default function ThemeProvider({ children }: Props) {
  const settings = useSettingsContext()

  const memoizedValue = useMemo(
    () => ({
      palette: {
        ...palette(settings.themeMode),
      },
      customShadows: {
        ...customShadows(settings.themeMode),
      },
      shadows: shadows(settings.themeMode),
      shape: { borderRadius: 8 },
      typography,
    }),
    [settings.themeMode]
  )

  const theme = createTheme(memoizedValue as ThemeOptions)

  theme.components = componentsOverrides(theme)

  return (
    <NextAppDirEmotionCacheProvider options={{ key: 'css' }}>
      <MuiThemeProvider theme={theme}>
        <CssBaseline />
        {children}
      </MuiThemeProvider>
    </NextAppDirEmotionCacheProvider>
  )
}
