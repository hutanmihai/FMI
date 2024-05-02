import { MaterialIcons, MaterialCommunityIcons } from '@expo/vector-icons'
import { Tabs } from 'expo-router'

import { palette } from '@/theme'

function AuthLayout() {
  return (
    <Tabs>
      <Tabs.Screen
        name="login"
        options={{
          title: 'Login',
          tabBarIcon: () => <MaterialIcons name="login" size={22} color={palette.green} />,
          tabBarStyle: { backgroundColor: palette.blue },
          tabBarLabelStyle: { color: palette.white, fontSize: 12 },
          headerStyle: { backgroundColor: palette.blue },
          headerTitleStyle: { color: palette.white },
        }}
      />
      <Tabs.Screen
        name="register"
        options={{
          title: 'Register',
          tabBarIcon: () => (
            <MaterialCommunityIcons name="account-plus" size={22} color={palette.green} />
          ),
          tabBarStyle: { backgroundColor: palette.blue },
          tabBarLabelStyle: { color: palette.white, fontSize: 12 },
          headerStyle: { backgroundColor: palette.blue },
          headerTitleStyle: { color: palette.white },
        }}
      />
    </Tabs>
  )
}

export default AuthLayout
