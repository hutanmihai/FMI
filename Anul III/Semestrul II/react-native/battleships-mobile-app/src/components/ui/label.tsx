import { StyleSheet, Text } from 'react-native'

import { palette } from '@/theme'
import { EGameStatus } from '@/types/game'

type TLabel = {
  status: EGameStatus | undefined
}

function Label({ status }: TLabel) {
  const getStatusStyles = () => {
    switch (status) {
      case EGameStatus.FINISHED:
        return {
          borderColor: palette.green, // Example color
          backgroundColor: palette.red, // Example color
          color: palette.white,
        }
      case EGameStatus.CREATED:
        return {
          borderColor: palette.red, // Example color
          backgroundColor: palette.yellow, // Example color
          color: palette.darkBlue,
        }
      case EGameStatus.ACTIVE:
        return {
          borderColor: palette.blue, // Example color
          backgroundColor: palette.green, // Example color
          color: palette.darkBlue,
        }
      // Add more cases as needed
      default:
        return {
          borderColor: palette.yellow,
          backgroundColor: palette.blue,
          color: palette.white,
        }
    }
  }

  return <Text style={[styles.label, getStatusStyles()]}>{status}</Text>
}

const styles = StyleSheet.create({
  label: {
    fontWeight: 'bold',
    fontSize: 16,
    textAlign: 'center',
    marginBottom: 4,
    paddingHorizontal: 1,
    borderWidth: 1,
    borderStyle: 'solid',
  },
})

export default Label
