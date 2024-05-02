import { Link } from 'expo-router'
import { useMemo } from 'react'
import { FlatList, StyleSheet, Text, TouchableOpacity, View } from 'react-native'

import Label from '@/components/ui/label'
import { useAuth } from '@/context/auth'
import { useListGames } from '@/hooks/game'
import { palette } from '@/theme'
import { EGameStatus, TGame } from '@/types/game'

function GamesList() {
  const { data: games, isLoading } = useListGames()
  const { user } = useAuth()
  const userId = user?.id

  const filteredGames = useMemo(() => {
    if (!games) {
      return []
    }
    return games.games.filter((game) => {
      const isPlayer = game.player1Id === userId || game.player2Id === userId
      if (game.status === EGameStatus.CREATED) {
        return true
      }
      return (
        [EGameStatus.MAP_CONFIG, EGameStatus.ACTIVE, EGameStatus.FINISHED].includes(game.status) &&
        isPlayer
      )
    })
  }, [games])

  const renderGameItem = ({ item: game }: { item: any }) => (
    <Link href={`/game/${game.id}`} asChild>
      <TouchableOpacity style={styles.gameItem}>
        <GameDetails game={game} />
      </TouchableOpacity>
    </Link>
  )

  if (isLoading) {
    return (
      <View style={styles.centered}>
        <Text style={styles.loadingText}>Loading...</Text>
      </View>
    )
  }

  return (
    <FlatList
      data={filteredGames}
      renderItem={renderGameItem}
      keyExtractor={(game) => game.id}
      contentContainerStyle={styles.listContainer}
      showsVerticalScrollIndicator={false}
    />
  )
}

const GameDetails = ({ game }: { game: TGame }) => (
  <View style={styles.gameDetailsContainer}>
    <Text style={styles.gameText}>{game.id}</Text>
    <Label status={game.status} />
    <Text style={{ color: palette.blue }}>Players:</Text>
    <Text style={styles.emailText}>{game.player1.email}</Text>
    <Text style={styles.emailText}>{game.player2?.email}</Text>
  </View>
)

const styles = StyleSheet.create({
  centered: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: palette.blue,
  },
  loadingText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: palette.red,
  },
  listContainer: {
    padding: 10,
    backgroundColor: palette.white,
  },
  gameItem: {
    padding: 20,
    marginVertical: 10,
    borderRadius: 10,
    shadowColor: palette.darkBlue,
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.23,
    shadowRadius: 2.62,
    elevation: 2,
  },
  gameText: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 5,
    color: palette.blue,
    textAlign: 'center',
  },
  emailText: {
    fontSize: 14,
  },
  moveText: {
    fontSize: 14,
    marginTop: 5,
  },
  gameDetailsContainer: {
    marginVertical: 10,
    borderStyle: 'solid',
    borderBottomWidth: 1,
    paddingBottom: 5,
    borderBottomColor: palette.blue,
  },
})

export default GamesList
