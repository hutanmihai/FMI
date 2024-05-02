import { AxiosError } from 'axios'
import { useRouter } from 'expo-router'
import { useMutation, useQuery, useQueryClient } from 'react-query'

import { createGame, getGame, joinGame, listGames, sendMap, strike } from '@/requests/game'
import { TShip, TStrike } from '@/types/game'
import { EToastType, showNotification } from '@/utils/toast'

export const useListGames = () => {
  return useQuery('listGames', listGames, {
    onError: (error: AxiosError) => {
      showNotification(EToastType.ERROR, error.message)
    },
    refetchInterval: 5000,
  })
}

export const useCreateGame = () => {
  const queryClient = useQueryClient()

  return useQuery('createGame', createGame, {
    onSuccess: async () => {
      showNotification(EToastType.SUCCESS, 'Game created')
      await queryClient.invalidateQueries('listGames')
    },
    onError: (error: AxiosError) => {
      showNotification(EToastType.ERROR, error.message)
    },
    enabled: false,
  })
}

export const useGetGame = (id: string, refetchInterval: boolean) => {
  return useQuery(['getGame', id], () => getGame(id), {
    onError: (error: AxiosError) => {
      showNotification(EToastType.ERROR, error.message)
    },
    refetchInterval: refetchInterval ? 2000 : false,
  })
}

export const useJoinGame = (id: string) => {
  const queryClient = useQueryClient()
  return useMutation(['joinGame', id], () => joinGame(id), {
    onSuccess: async () => {
      showNotification(EToastType.SUCCESS, 'Game joined')
      await queryClient.invalidateQueries('listGames')
      await queryClient.invalidateQueries(['getGame', id])
    },
    onError: (error: AxiosError) => {
      showNotification(EToastType.ERROR, error.message)
    },
  })
}

export const useSendMap = (id: string) => {
  const router = useRouter()
  const queryClient = useQueryClient()
  return useMutation(['sendMap', id], (payload: { ships: TShip[] }) => sendMap(id, payload), {
    onSuccess: async () => {
      showNotification(EToastType.SUCCESS, 'Map sent successfully')
      router.replace(`(app)/game/${id}`)
      await queryClient.invalidateQueries(['getGame', id])
    },
    onError: (error: AxiosError) => {
      showNotification(EToastType.ERROR, error.message)
    },
  })
}

export const useStrike = (id: string) => {
  return useMutation(['strike', id], (payload: TStrike) => strike(id, payload), {
    onSuccess: () => {
      showNotification(EToastType.SUCCESS, 'Strike sent successfully')
    },
    onError: (error: AxiosError) => {
      showNotification(EToastType.ERROR, error.message)
    },
  })
}
