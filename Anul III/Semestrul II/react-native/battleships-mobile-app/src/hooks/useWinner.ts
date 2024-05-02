import { useMemo } from 'react'

import { useAuth } from '@/context/auth'
import { EGameStatus, TGame } from '@/types/game'

function useWinner(game: TGame | undefined) {
  const { user } = useAuth()
  const userId = user?.id

  const winMessage = 'Well fought soldier! You won!'
  const lossMessage = 'Better luck next time!'

  const isGameFinished = game?.status === EGameStatus.FINISHED

  const amWinner = useMemo(() => {
    if (isGameFinished) {
      const hitsPlayer1 = game.moves.filter(
        (move) => move.playerId === game.player1Id && move.result
      ).length
      const hitsPlayer2 = game.moves.filter(
        (move) => move.playerId === game.player2Id && move.result
      ).length
      if (game.player1Id === userId) {
        return hitsPlayer1 > hitsPlayer2
      } else {
        return hitsPlayer2 > hitsPlayer1
      }
    }
  }, [game, user])

  return { winMessage, lossMessage, isGameFinished, amWinner }
}

export default useWinner
