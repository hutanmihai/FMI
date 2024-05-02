import { StyleSheet, Text, View } from 'react-native'

import { palette } from '@/theme'

type TChipProps = {
  size: 'S' | 'M' | 'L' | 'XL'
  number: number
}

function Chip({ size, number }: TChipProps) {
  return (
    <View style={styles.chip}>
      <Text style={styles.text}>{size}</Text>
      <Text style={styles.text}>{number}</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  chip: {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    borderStyle: 'solid',
    borderWidth: 1,
    borderColor: palette.yellow,
    backgroundColor: palette.blue,
    width: 50,
    borderRadius: 100,
  },
  text: {
    color: palette.white,
  },
})

export default Chip
