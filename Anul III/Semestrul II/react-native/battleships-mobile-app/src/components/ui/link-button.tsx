import { useRouter } from 'expo-router'
import { ReactNode } from 'react'
import { TouchableOpacity, Text, StyleSheet, ActivityIndicator } from 'react-native'

import { palette } from '@/theme'

type TLinkButtonProps = {
  route: string
  title: string
  iconLeft?: ReactNode
  iconRight?: ReactNode
  style?: any
  textStyle?: any
  disabled?: boolean
  loading?: boolean
}

function LinkButton({
  route,
  title,
  iconLeft,
  iconRight,
  style,
  textStyle,
  disabled,
  loading,
}: TLinkButtonProps) {
  const router = useRouter()
  return (
    <TouchableOpacity
      onPress={() => router.push(route)}
      disabled={disabled}
      style={[disabled ? styles.disabledButton : styles.button, style]}
    >
      {iconLeft}
      {loading ? (
        <ActivityIndicator color="white" />
      ) : (
        <Text style={[styles.buttonText, textStyle]}>{title}</Text>
      )}
      {iconRight}
    </TouchableOpacity>
  )
}

const styles = StyleSheet.create({
  button: {
    backgroundColor: palette.green,
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 5,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    width: '100%',
  },
  disabledButton: {
    backgroundColor: 'grey',
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 5,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    width: '100%',
  },
  buttonText: {
    color: palette.white,
    fontSize: 16,
  },
})

export default LinkButton
