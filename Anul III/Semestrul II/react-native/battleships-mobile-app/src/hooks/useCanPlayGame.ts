import { useMemo } from 'react'

import { useAuth } from '@/context/auth'
import { EGameStatus, TGame } from '@/types/game'

function useCanPlayGame(game: TGame | undefined) {
  const { user } = useAuth()
  const userId = user?.id

  const canPlayGame = useMemo(() => {
    if (!game || !userId) {
      return false
    }
    return (
      game.status === EGameStatus.ACTIVE && (game.player1Id === userId || game.player2Id === userId)
    )
  }, [game, userId])

  return { canPlayGame }
}

export default useCanPlayGame
