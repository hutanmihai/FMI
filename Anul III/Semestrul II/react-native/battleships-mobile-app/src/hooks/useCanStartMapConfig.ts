import { useMemo } from 'react'

import { useAuth } from '@/context/auth'
import { EGameStatus, TGame } from '@/types/game'

function useCanStartMapConfig(game: TGame | undefined) {
  const { user } = useAuth()
  const userId = user?.id

  const canStartMapConfig = useMemo(() => {
    if (!game || !userId) {
      return false
    }
    return (
      game.status === EGameStatus.MAP_CONFIG &&
      (game.player1Id === userId || game.player2Id === userId) &&
      // @ts-ignore
      game.shipsCoord.filter((ship) => ship.playerId === userId).length === 0
    )
  }, [game, userId])

  return { canStartMapConfig }
}

export default useCanStartMapConfig
