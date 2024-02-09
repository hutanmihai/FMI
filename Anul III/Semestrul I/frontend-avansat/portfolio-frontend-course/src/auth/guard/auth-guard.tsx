import { paths } from '@/routes/paths'
import { useRouter } from 'next/navigation'
import { useAuthContext } from '@/auth/hooks'
import { SplashScreen } from '@/components/loading-screen'
import { useState, useEffect, ReactNode, useCallback } from 'react'

type Props = {
  children: ReactNode
}

export default function AuthGuard({ children }: Props) {
  const { loading } = useAuthContext()

  return <>{loading ? <SplashScreen /> : <Container>{children}</Container>}</>
}

function Container({ children }: Props) {
  const router = useRouter()

  const { authenticated } = useAuthContext()

  const [checked, setChecked] = useState(false)

  const check = useCallback(() => {
    if (!authenticated) {
      const searchParams = new URLSearchParams({
        returnTo: window.location.pathname,
      }).toString()

      const loginPath = paths.auth.login

      const href = `${loginPath}?${searchParams}`

      router.replace(href)
    } else {
      setChecked(true)
    }
  }, [authenticated, router])

  useEffect(() => {
    check()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  if (!checked) {
    return null
  }

  return <>{children}</>
}
