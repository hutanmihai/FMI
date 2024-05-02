import { Text, View, StyleSheet } from 'react-native'

import { useMe } from '@/hooks/user'
import { palette } from '@/theme'

function MeScreen() {
  const { data: me } = useMe()

  return (
    <View style={styles.container}>
      <Text style={styles.title}>User Info</Text>
      <View style={styles.card}>
        <Text style={styles.cardText}>ID: {me?.user.id}</Text>
      </View>
      <View style={styles.card}>
        <Text style={styles.cardText}>Email: {me?.user.email}</Text>
      </View>
      <View style={styles.card}>
        <Text style={styles.cardText}>Games Played: {me?.gamesPlayed}</Text>
      </View>
      <View style={styles.card}>
        <Text style={styles.cardText}>Games Won: {me?.gamesWon}</Text>
      </View>
      <View style={styles.card}>
        <Text style={styles.cardText}>Games Lost: {me?.gamesLost}</Text>
      </View>
      <View style={styles.card}>
        <Text style={styles.cardText}>Currently Playing: {me?.currentlyGamesPlaying}</Text>
      </View>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    color: palette.blue,
  },
  card: {
    width: '100%',
    backgroundColor: palette.blue,
    padding: 15,
    borderRadius: 10,
    marginTop: 10,
    shadowColor: palette.darkBlue,
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.23,
    shadowRadius: 2.62,
    elevation: 2,
  },
  cardText: {
    fontSize: 16,
    color: palette.white,
  },
})
export default MeScreen
