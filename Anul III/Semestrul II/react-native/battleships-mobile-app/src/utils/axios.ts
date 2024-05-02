import axios from 'axios'

import { BACKEND_URL } from '@/config.global'
import { TErrorResponse } from '@/types/error'
import { getAccessToken } from '@/utils/session'

const axiosInstance = axios.create({ baseURL: BACKEND_URL })

axiosInstance.interceptors.request.use(
  async (config) => {
    const token = await getAccessToken()
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

axiosInstance.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    if (
      error.response &&
      error.response.status === 401 &&
      error.response.data === typeof 'string'
    ) {
      console.log('UNAUTHORIZED')
      throw new Error('Unauthorized')
    }
    if (error.response && error.response.data) {
      const errorObject: TErrorResponse = error.response.data
      console.error('ERROR', errorObject)
      throw new Error(errorObject.message)
    }
    return Promise.reject(error)
  }
)

export default axiosInstance
