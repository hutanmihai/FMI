import { paths } from '@/routes/paths'
import { useEffect, ReactNode, useCallback } from 'react'
import { SplashScreen } from '@/components/loading-screen'
import { useRouter, useSearchParams } from 'next/navigation'

import { useAuthContext } from '../hooks'

type Props = {
  children: ReactNode
}

export default function GuestGuard({ children }: Props) {
  const { loading } = useAuthContext()

  return <>{loading ? <SplashScreen /> : <Container>{children}</Container>}</>
}

function Container({ children }: Props) {
  const router = useRouter()

  const searchParams = useSearchParams()

  const returnTo = searchParams.get('returnTo') || paths.home

  const { authenticated } = useAuthContext()

  const check = useCallback(() => {
    if (authenticated) {
      router.replace(returnTo)
    }
  }, [authenticated, returnTo, router])

  useEffect(() => {
    check()
  }, [check])

  return <>{children}</>
}
