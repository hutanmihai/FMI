import { useLocalSearchParams, useRouter } from 'expo-router'
import { useEffect, useState } from 'react'
import { StyleSheet, Text, View } from 'react-native'

import GridBox from '@/components/game/box'
import Grid from '@/components/game/grid'
import { useAuth } from '@/context/auth'
import { useGetGame, useStrike } from '@/hooks/game'
import { useGrid } from '@/hooks/useGrid'
import { palette } from '@/theme'
import { EGameStatus, TBox } from '@/types/game'

function PlayGameScreen() {
  const { id } = useLocalSearchParams<{ id: string }>()
  const { user } = useAuth()
  const userId = user?.id
  // @ts-ignore
  const { mutate: strike } = useStrike(id)
  const { grid: myGrid, updateGridBox: updateMyGridBox } = useGrid()
  const { grid: enemyGrid, updateGridBox: updateEnemyGridBox } = useGrid()

  const [isMyTurn, setIsMyTurn] = useState(false)

  // @ts-ignore
  const { data: game } = useGetGame(id, !isMyTurn)
  const router = useRouter()

  useEffect(() => {
    if (game) {
      if (game.status === EGameStatus.FINISHED) {
        router.back()
      }
      if (game?.playerToMoveId === userId) {
        setIsMyTurn(true)
      }
      for (const ship of game?.shipsCoord) {
        // @ts-ignore
        updateMyGridBox([...myGrid], ship.x, ship.y, ship.hit ? 'destroyed' : 'ship')
      }
      for (const move of game?.moves.filter((move) => move.playerId === userId)) {
        // @ts-ignore
        updateEnemyGridBox(
          [...enemyGrid],
          move.x,
          move.y,
          move.result ? 'destroyed' : 'not-allowed'
        )
      }
    }
  }, [game])

  if (!game) {
    return null
  }

  return (
    <View style={styles.container}>
      <Grid grid={myGrid} />
      {isMyTurn ? (
        <Text style={styles.attack}>ATTACK!</Text>
      ) : (
        <Text style={styles.wait}>WAIT FOR ENEMY</Text>
      )}
      {enemyGrid.map((row: TBox[], rowIndex) => (
        <View key={rowIndex} style={{ flexDirection: 'row' }}>
          {row.map((cell, colIndex) => (
            <GridBox
              key={`${rowIndex}-${colIndex}`}
              status={cell}
              onPress={() => {
                if (!isMyTurn) return
                setIsMyTurn(false)
                strike(
                  { x: String.fromCharCode(65 + colIndex), y: rowIndex + 1 },
                  {
                    onSuccess: () => {
                      // TODO: update enemy grid
                    },
                  }
                )
              }}
            />
          ))}
        </View>
      ))}
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    flexDirection: 'column',
    backgroundColor: palette.white,
  },
  attack: {
    fontSize: 20,
    fontWeight: 'bold',
    color: palette.red,
  },
  wait: {
    fontSize: 20,
    fontWeight: 'bold',
    color: palette.blue,
  },
})

export default PlayGameScreen
