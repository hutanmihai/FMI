import AuthForm from '@/components/auth/auth-form'
import { useAuth } from '@/context/auth'

function LoginScreen() {
  const { login, isLoading } = useAuth()

  return <AuthForm onClick={login} isLoading={isLoading} buttonText="Login" />
}

export default LoginScreen
