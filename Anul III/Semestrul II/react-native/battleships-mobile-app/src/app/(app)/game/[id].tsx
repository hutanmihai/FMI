import { useLocalSearchParams } from 'expo-router'
import React from 'react'
import { StyleSheet, Text, View } from 'react-native'

import Button from '@/components/ui/button'
import Label from '@/components/ui/label'
import LinkButton from '@/components/ui/link-button'
import { useGetGame, useJoinGame } from '@/hooks/game'
import useCanPlayGame from '@/hooks/useCanPlayGame'
import useCanStartMapConfig from '@/hooks/useCanStartMapConfig'
import useIsGameJoinable from '@/hooks/useIsGameJoinable'
import useIsWaitingForEnemyMapConfig from '@/hooks/useIsWaitingForEnemyMapConfig'
import useWinner from '@/hooks/useWinner'
import { palette } from '@/theme'

function GameScreen() {
  const { id } = useLocalSearchParams<{ id: string }>()
  // @ts-ignore
  const { data: game, isLoading } = useGetGame(id, true)
  // @ts-ignore
  const { mutate: joinGame } = useJoinGame(id)

  const { isGameJoinable } = useIsGameJoinable(game)
  const { canStartMapConfig } = useCanStartMapConfig(game)
  const { canPlayGame } = useCanPlayGame(game)
  const { isWaitingForEnemyMapConfig } = useIsWaitingForEnemyMapConfig(game)
  const { isGameFinished, amWinner, winMessage, lossMessage } = useWinner(game)

  if (isLoading) {
    return (
      <View style={styles.screenContainer}>
        <Text>Loading...</Text>
      </View>
    )
  }

  return (
    <View style={styles.screenContainer}>
      <Text style={styles.text}>{game?.id}</Text>
      <Label status={game?.status} />
      {isGameFinished &&
        (amWinner ? (
          <Text style={{ color: palette.green, fontWeight: 'bold', fontSize: 14 }}>
            {winMessage}
          </Text>
        ) : (
          <Text style={{ color: palette.red, fontWeight: 'bold', fontSize: 14 }}>
            {lossMessage}
          </Text>
        ))}
      <Text>{game?.player1.email}</Text>
      <Text>{game?.player2?.email}</Text>
      {isGameJoinable && (
        <Button title="Join game" onPress={() => joinGame()} style={styles.button} />
      )}

      {canStartMapConfig && (
        <LinkButton
          route={`/game/map/${game?.id}`}
          title="Start Map Config"
          style={styles.button}
        />
      )}
      {canPlayGame && (
        <LinkButton
          route={`/game/play/${game?.id}`}
          title={game?.moves.length === 0 ? 'Start Game' : 'Continue Game'}
          style={styles.button}
        />
      )}
      {isWaitingForEnemyMapConfig && (
        <Text style={{ color: palette.green, fontSize: 16, marginTop: 10 }}>
          Waiting for enemy to configure map...
        </Text>
      )}
    </View>
  )
}

const styles = StyleSheet.create({
  screenContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: palette.white,
  },
  button: {
    width: 300,
    marginVertical: 10,
  },
  text: {
    color: palette.blue,
    fontWeight: 'bold',
    fontSize: 20,
    marginBottom: 5,
  },
})

export default GameScreen
