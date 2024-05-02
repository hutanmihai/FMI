import { AxiosError } from 'axios'
import { useMutation } from 'react-query'

import { login, register } from '@/requests/auth'
import { TLoginRequest, TRegisterRequest } from '@/types/auth'
import { EToastType, showNotification } from '@/utils/toast'

export const useLogin = () => {
  return useMutation('login', async (payload: TLoginRequest) => await login(payload), {
    onSuccess: async () => {
      showNotification(EToastType.SUCCESS, 'Login successful')
    },
    onError: (error: AxiosError) => {
      showNotification(EToastType.ERROR, error.message)
    },
  })
}

export const useRegister = () => {
  return useMutation('register', async (payload: TRegisterRequest) => await register(payload), {
    onSuccess: async () => {
      showNotification(EToastType.SUCCESS, 'Registration successful')
    },
    onError: (error: AxiosError) => {
      showNotification(EToastType.ERROR, error.message)
    },
  })
}
