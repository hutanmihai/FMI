import Toast from 'react-native-root-toast'

import { palette } from '@/theme'

export enum EToastType {
  ERROR = 'error',
  SUCCESS = 'success',
}

export const showNotification = (type: 'error' | 'success', message: string) => {
  let backgroundColor = palette.green
  if (type === 'error') {
    backgroundColor = palette.red
  }

  Toast.show(message, {
    duration: Toast.durations.SHORT,
    position: Toast.positions.TOP,
    shadow: true,
    animation: true,
    hideOnPress: true,
    delay: 0,
    opacity: 1,
    backgroundColor,
    textColor: palette.white,
    containerStyle: {
      padding: 10,
      borderRadius: 10,
      minWidth: 300,
      minHeight: 50,
    },
  })
}
