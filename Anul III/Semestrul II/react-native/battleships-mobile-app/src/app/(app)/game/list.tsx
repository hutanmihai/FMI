import { useRouter } from 'expo-router'
import { SafeAreaView, StyleSheet, View } from 'react-native'

import FloatingBar from '@/components/home/floating-bar'
import GamesList from '@/components/home/games-list'
import Button from '@/components/ui/button'
import { useAuth } from '@/context/auth'
import { useCreateGame } from '@/hooks/game'
import { palette } from '@/theme'

function HomeScreen() {
  const { logout } = useAuth()
  const router = useRouter()
  const { refetch } = useCreateGame()

  const handleCreateGame = async () => {
    const { data: createdGame } = await refetch()
    if (createdGame) {
      router.push(`/game/${createdGame.id}`)
    }
  }

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: palette.white }}>
      <View style={styles.container}>
        <Button onPress={handleCreateGame} title="Create Game" style={{ borderRadius: 0 }} />
        <GamesList />
        <FloatingBar
          onHomePress={() => {
            router.replace('/game/list')
          }}
          onProfilePress={() => {
            router.push('/user/me')
          }}
          onLogoutPress={logout}
        />
      </View>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: palette.white,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100%',
  },
})

export default HomeScreen
