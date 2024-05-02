import { useLocalSearchParams, useRouter } from 'expo-router'
import { Pressable, StyleSheet, Text, View } from 'react-native'

import Grid from '@/components/game/grid'
import Button from '@/components/ui/button'
import Chip from '@/components/ui/chip'
import { useSendMap } from '@/hooks/game'
import { useGrid } from '@/hooks/useGrid'
import { palette } from '@/theme'
import { EShipPosition } from '@/types/game'

function MapConfigScreen() {
  const { id } = useLocalSearchParams<{ id: string }>()
  // @ts-ignore
  const { mutateAsync: sendMap } = useSendMap(id)
  const router = useRouter()

  const {
    grid,
    shipsCoord,
    shipsNum,
    areAllShipsPlaced,
    selectedShip,
    selectedShipPosition,
    setSelectedShip,
    setSelectedShipPosition,
    placeShipOnGrid,
    handleRevert,
  } = useGrid()

  const handleSendMap = async () => {
    try {
      await sendMap({ ships: shipsCoord })
      router.back()
      // eslint-disable-next-line @typescript-eslint/no-unused-vars
    } catch (_) {}
  }

  return (
    <View style={styles.container}>
      <Grid grid={grid} onPress={placeShipOnGrid} />
      <View style={styles.chipsContainer}>
        <Pressable onPress={() => setSelectedShip('s')} disabled={areAllShipsPlaced.s}>
          <Chip size="S" number={shipsNum.s} />
        </Pressable>
        <Pressable onPress={() => setSelectedShip('m')} disabled={areAllShipsPlaced.m}>
          <Chip size="M" number={shipsNum.m} />
        </Pressable>
        <Pressable onPress={() => setSelectedShip('l')} disabled={areAllShipsPlaced.l}>
          <Chip size="L" number={shipsNum.l} />
        </Pressable>
        <Pressable onPress={() => setSelectedShip('xl')} disabled={areAllShipsPlaced.xl}>
          <Chip size="XL" number={shipsNum.xl} />
        </Pressable>
      </View>

      <View style={styles.positionContainer}>
        <Button
          onPress={() => setSelectedShipPosition(EShipPosition.HORIZONTAL)}
          title="Horizontal"
          style={{ width: 150 }}
        />
        <Button
          onPress={() => setSelectedShipPosition(EShipPosition.VERTICAL)}
          title="Vertical"
          style={{ width: 150 }}
        />
      </View>
      <Button title="Revert" onPress={handleRevert} style={{ width: 300 }} />
      {areAllShipsPlaced.s &&
        areAllShipsPlaced.m &&
        areAllShipsPlaced.l &&
        areAllShipsPlaced.xl && (
          <Button title="Send Map" onPress={handleSendMap} style={{ width: 300, marginTop: 20 }} />
        )}
      <View style={styles.selectedShipContainer}>
        <Text style={styles.selectedShipTitle}>Selected Ship</Text>
        <Text>{selectedShip?.toUpperCase()}</Text>
        <Text>{selectedShipPosition}</Text>
      </View>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'column',
    alignItems: 'center',
    backgroundColor: palette.white,
    height: '100%',
    marginTop: '10%',
  },
  chipsContainer: {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'space-around',
    width: '100%',
    marginVertical: 20,
  },
  positionContainer: {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    width: '80%',
    marginBottom: 20,
  },
  selectedShipContainer: {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
  },
  selectedShipTitle: {
    color: palette.blue,
    fontWeight: 'bold',
    fontSize: 20,
    marginTop: 10,
    marginBottom: 5,
  },
})

export default MapConfigScreen
