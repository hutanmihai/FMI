import { apiConfig } from '@/config.global'
import { TMeResponse } from '@/types/user'
import axiosInstance from '@/utils/axios'

export const me = async () => {
  const response = await axiosInstance.get(apiConfig.user.me)
  return response.data as TMeResponse
}
