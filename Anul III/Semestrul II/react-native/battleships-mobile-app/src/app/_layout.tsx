import { Slot } from 'expo-router'
import React from 'react'
import { RootSiblingParent } from 'react-native-root-siblings'
import { QueryClient, QueryClientProvider } from 'react-query'

import { AuthProvider } from '@/context/auth'

const queryClient = new QueryClient()

function RootLayout() {
  return (
    <RootSiblingParent>
      <QueryClientProvider client={queryClient}>
        <AuthProvider>
          <Slot />
        </AuthProvider>
      </QueryClientProvider>
    </RootSiblingParent>
  )
}

export default RootLayout
