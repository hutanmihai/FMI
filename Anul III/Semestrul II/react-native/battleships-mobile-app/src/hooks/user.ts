import { AxiosError } from 'axios'
import { useQuery } from 'react-query'

import { me } from '@/requests/user'
import { EToastType, showNotification } from '@/utils/toast'

export const useMe = () => {
  return useQuery('me', () => me(), {
    onError: (error: AxiosError) => {
      showNotification(EToastType.ERROR, error.message)
    },
  })
}
