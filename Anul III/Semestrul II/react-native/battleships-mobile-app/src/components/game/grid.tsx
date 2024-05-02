import { View } from 'react-native'

import GridBox from '@/components/game/box'
import { TBox } from '@/types/game'

type TGridProps = {
  grid: TBox[][]
  onPress?: (x: number, y: number) => void
}

function Grid({ grid, onPress }: TGridProps) {
  return (
    <View>
      {grid.map((row: TBox[], rowIndex) => (
        <View key={rowIndex} style={{ flexDirection: 'row' }}>
          {row.map((cell, colIndex) => (
            <GridBox
              key={`${rowIndex}-${colIndex}`}
              status={cell}
              onPress={() => onPress && onPress(rowIndex, colIndex)}
            />
          ))}
        </View>
      ))}
    </View>
  )
}

export default Grid
