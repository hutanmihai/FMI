import { Stack } from 'expo-router'

import { palette } from '@/theme'

function AppLayout() {
  return (
    <Stack>
      <Stack.Screen
        name="user/me"
        options={{
          presentation: 'modal',
          title: 'Me',
          headerStyle: { backgroundColor: palette.blue },
          headerTitleStyle: { color: palette.white },
          headerTintColor: palette.yellow,
        }}
      />
      <Stack.Screen
        name="game/map/[id]"
        options={{
          title: 'Map Config',
          headerStyle: { backgroundColor: palette.blue },
          headerTitleStyle: { color: palette.white },
          headerTintColor: palette.yellow,
        }}
      />
      <Stack.Screen
        name="game/play/[id]"
        options={{
          title: 'Play Game',
          headerStyle: { backgroundColor: palette.blue },
          headerTitleStyle: { color: palette.white },
          headerTintColor: palette.yellow,
        }}
      />
      <Stack.Screen
        name="game/[id]"
        options={{
          title: 'Game Overview',
          headerStyle: { backgroundColor: palette.blue },
          headerTitleStyle: { color: palette.white },
          headerTintColor: palette.yellow,
        }}
      />
      <Stack.Screen
        name="game/list"
        options={{
          title: 'Battleships',
          headerStyle: { backgroundColor: palette.blue },
          headerTitleStyle: { color: palette.white },
          headerTintColor: palette.yellow,
        }}
      />
    </Stack>
  )
}

export default AppLayout
