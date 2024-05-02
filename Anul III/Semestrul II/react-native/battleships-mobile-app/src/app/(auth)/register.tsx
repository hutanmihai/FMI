import AuthForm from '@/components/auth/auth-form'
import { useAuth } from '@/context/auth'

function RegisterScreen() {
  const { register, isLoading } = useAuth()

  return <AuthForm onClick={register} isLoading={isLoading} buttonText="Register" />
}

export default RegisterScreen
