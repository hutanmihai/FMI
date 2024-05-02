import React from 'react'
import { TouchableOpacity, Dimensions } from 'react-native'

import { palette } from '@/theme'
import { TBox } from '@/types/game'

type TGridBoxProps = {
  status: TBox
  onPress: () => void
}

const colorMap = {
  clear: palette.blue,
  ship: palette.green,
  destroyed: palette.red,
  'not-allowed': palette.yellow,
}

const { width } = Dimensions.get('window')
const BOX_SIZE = Math.floor(width / 11)

function GridBox({ status, onPress }: TGridBoxProps) {
  return (
    <TouchableOpacity
      onPress={onPress}
      style={{
        width: BOX_SIZE,
        height: BOX_SIZE,
        borderWidth: 1,
        borderColor: palette.darkBlue,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: colorMap[status],
      }}
    />
  )
}

export default GridBox
