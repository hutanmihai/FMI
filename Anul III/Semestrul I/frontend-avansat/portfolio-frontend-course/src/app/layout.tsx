import { ReactNode } from 'react'
import ThemeProvider from '@/theme'
import { primaryFont } from '@/theme/typography'
import { AuthProvider } from '@/auth/context/firebase'
import { SettingsProvider } from '@/components/settings'
import { MotionLazy } from '@/components/animate/motion-lazy'

export const metadata = {
  title: 'Mihai Hutan',
  description:
    'A showcase of my projects, skills, and passion for programming. Dive into my world of frontend & backend development, and machine learning explorations.',
  keywords:
    'developer, portfolio, projects, skills, frontend, backend, machine learning, programming, web development, software engineer, full stack, react, nextjs, nodejs, typescript, javascript, python, tensorflow, pytorch, machine learning, deep learning, data preprocessing, data augmentation, data',
  manifest: '/manifest.json',
  icons: [
    { rel: 'icon', url: '/favicon/favicon.ico' },
    { rel: 'icon', type: 'image/png', sizes: '16x16', url: '/favicon/favicon-16x16.png' },
    { rel: 'icon', type: 'image/png', sizes: '32x32', url: '/favicon/favicon-32x32.png' },
    { rel: 'apple-touch-icon', sizes: '180x180', url: '/favicon/apple-touch-icon.png' },
  ],
}

export const viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  themeColor: '#000000',
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" className={primaryFont.className}>
      <body>
        <AuthProvider>
          <SettingsProvider defaultSettings={{ themeMode: 'dark' }}>
            <ThemeProvider>
              <MotionLazy>{children}</MotionLazy>
            </ThemeProvider>
          </SettingsProvider>
        </AuthProvider>
      </body>
    </html>
  )
}
