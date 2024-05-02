import { useMemo } from 'react'

import { useAuth } from '@/context/auth'
import { EGameStatus, TGame } from '@/types/game'

function useIsGameJoinable(game: TGame | undefined) {
  const { user } = useAuth()
  const userId = user?.id

  const isGameJoinable = useMemo(() => {
    if (!game || !userId) {
      return false
    }
    return !(
      game.status === EGameStatus.FINISHED ||
      (game.player1Id && game.player2Id) ||
      [game.player1Id, game.player2Id].includes(userId)
    )
  }, [game, userId])

  return { isGameJoinable }
}

export default useIsGameJoinable
