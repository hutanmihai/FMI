import { apiConfig } from '@/config.global'
import { TLoginRequest, TRegisterRequest, TTokens } from '@/types/auth'
import { TUser } from '@/types/user'
import axiosInstance from '@/utils/axios'

export const login = async (payload: TLoginRequest) => {
  const response = await axiosInstance.post(apiConfig.auth.login, payload)
  return response.data as TTokens
}

export const register = async (payload: TRegisterRequest) => {
  const response = await axiosInstance.post(apiConfig.auth.register, payload)
  return response.data as TUser
}
