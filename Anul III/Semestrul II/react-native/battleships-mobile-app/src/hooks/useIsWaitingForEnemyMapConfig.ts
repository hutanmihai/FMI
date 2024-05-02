import { useMemo } from 'react'

import { useAuth } from '@/context/auth'
import { TGame } from '@/types/game'

function useIsWaitingForEnemyMapConfig(game: TGame | undefined) {
  const { user } = useAuth()
  const userId = user?.id

  const isWaitingForEnemyMapConfig = useMemo(() => {
    if (!game || !userId) {
      return false
    }
    return (
      game.status === 'MAP_CONFIG' &&
      (game.player1Id === userId || game.player2Id === userId) &&
      // @ts-ignore
      game.shipsCoord.filter((ship) => ship.playerId === userId).length > 0
    )
  }, [game, userId])

  return { isWaitingForEnemyMapConfig }
}

export default useIsWaitingForEnemyMapConfig
