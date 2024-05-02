import { apiConfig } from '@/config.global'
import { TGamesListResponse, TShip, TStrike, TGame } from '@/types/game'
import axiosInstance from '@/utils/axios'

export const listGames = async () => {
  const response = await axiosInstance.get(apiConfig.game.list)
  return response.data as TGamesListResponse
}

export const createGame = async () => {
  const response = await axiosInstance.post(apiConfig.game.create)
  return response.data as TGame
}

export const getGame = async (id: string) => {
  const response = await axiosInstance.get(apiConfig.game.get(id))
  return response.data as TGame
}

export const joinGame = async (id: string) => {
  await axiosInstance.post(apiConfig.game.join(id))
}

export const sendMap = async (id: string, payload: { ships: TShip[] }) => {
  await axiosInstance.patch(apiConfig.game.sendMap(id), payload)
}

export const strike = async (id: string, payload: TStrike) => {
  await axiosInstance.post(apiConfig.game.strike(id), payload)
}
