'use client'

import { ReactNode } from 'react'
import { AuthGuard } from '@/auth/guard'
import MainLayout from '@/layouts/main-layout'

export default function AdminRootLayout({ children }: { children: ReactNode }) {
  return (
    <AuthGuard>
      <MainLayout>{children}</MainLayout>
    </AuthGuard>
  )
}
