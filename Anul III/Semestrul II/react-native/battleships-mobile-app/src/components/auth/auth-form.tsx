import { useState } from 'react'
import { StyleSheet, Text, TextInput, View } from 'react-native'

import Button from '@/components/ui/button'
import { palette } from '@/theme'

type TAuthFormProps = {
  onClick: ({ email, password }: { email: string; password: string }) => void
  isLoading: boolean
  buttonText: string
}

function AuthForm({ onClick, isLoading, buttonText }: TAuthFormProps) {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  return (
    <View style={styles.container}>
      <Text style={styles.label}>Email:</Text>
      <TextInput
        style={styles.input}
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      <Text style={styles.label}>Password:</Text>
      <TextInput style={styles.input} value={password} onChangeText={setPassword} secureTextEntry />
      <Button
        title={buttonText}
        onPress={() => onClick({ email, password })}
        disabled={isLoading}
        style={{ width: 300 }}
        loading={isLoading}
      />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 20,
    backgroundColor: palette.white,
  },
  label: {
    fontSize: 14,
    marginBottom: 5,
    color: palette.blue,
  },
  input: {
    width: 300,
    height: 40,
    borderWidth: 1,
    borderColor: palette.blue,
    borderRadius: 5,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
})

export default AuthForm
