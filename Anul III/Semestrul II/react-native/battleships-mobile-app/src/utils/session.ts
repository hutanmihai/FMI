import * as SecureStore from 'expo-secure-store'

import { TTokens } from '@/types/auth'

export const storeTokens = async (tokens: TTokens) => {
  try {
    await SecureStore.setItemAsync('accessToken', tokens.accessToken)
    await SecureStore.setItemAsync('refreshToken', tokens.refreshToken)
  } catch (error) {
    console.error('Error storing tokens:', error)
  }
}

export const getAccessToken = async () => {
  try {
    return await SecureStore.getItemAsync('accessToken')
  } catch (error) {
    console.error('Error getting access token:', error)
  }
}

export const getRefreshToken = async () => {
  try {
    return await SecureStore.getItemAsync('refreshToken')
  } catch (error) {
    console.error('Error getting refresh token:', error)
  }
}

export const deleteTokens = async () => {
  try {
    await SecureStore.deleteItemAsync('accessToken')
    await SecureStore.deleteItemAsync('refreshToken')
  } catch (error) {
    console.error('Error deleting tokens:', error)
  }
}
