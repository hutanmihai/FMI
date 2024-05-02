import { useCallback, useEffect, useState } from 'react'

import { EShipPosition, TBox, TShip } from '@/types/game'
import { generateEmptyGrid, mapShipSizeToLength } from '@/utils/grid'
import { EToastType, showNotification } from '@/utils/toast'

export type TShipsNum = {
  s: number
  m: number
  l: number
  xl: number
}

export type TAreAllShipsPlaced = {
  s: boolean
  m: boolean
  l: boolean
  xl: boolean
}

type TStateHistory = {
  grid: TBox[][]
  shipsCoord: TShip[]
  shipsNum: TShipsNum
  areAllShipsPlaced: TAreAllShipsPlaced
}

export const useGrid = () => {
  const [grid, setGrid] = useState<TBox[][]>(generateEmptyGrid)
  const [shipsCoord, setShipsCoord] = useState<TShip[]>([])
  const [shipsNum, setShipsNum] = useState({
    s: 4,
    m: 3,
    l: 2,
    xl: 1,
  })
  const [areAllShipsPlaced, setAreAllShipsPlaced] = useState({
    s: false,
    m: false,
    l: false,
    xl: false,
  })
  const [stateHistory, setStateHistory] = useState<TStateHistory[]>([
    {
      grid: [...grid],
      shipsCoord: [...shipsCoord],
      shipsNum: { ...shipsNum },
      areAllShipsPlaced: { ...areAllShipsPlaced },
    },
  ])

  const [selectedShip, setSelectedShip] = useState<'s' | 'm' | 'l' | 'xl' | null>(null)
  const [selectedShipPosition, setSelectedShipPosition] = useState<EShipPosition>(
    EShipPosition.HORIZONTAL
  )

  useEffect(() => {
    if (shipsNum.s === 0) {
      setAreAllShipsPlaced((prev) => ({ ...prev, s: true }))
    }
    if (shipsNum.m === 0) {
      setAreAllShipsPlaced((prev) => ({ ...prev, m: true }))
    }
    if (shipsNum.l === 0) {
      setAreAllShipsPlaced((prev) => ({ ...prev, l: true }))
    }
    if (shipsNum.xl === 0) {
      setAreAllShipsPlaced((prev) => ({ ...prev, xl: true }))
    }
  }, [shipsNum])

  const updateGridBox = useCallback((grid: TBox[][], x: string, y: number, status: TBox) => {
    const newGrid = [...grid]
    newGrid[y - 1][x.charCodeAt(0) - 'A'.charCodeAt(0)] = status
    setGrid(() => newGrid)
  }, [])

  const placeShipOnGrid = useCallback(
    (rowIndex: number, colIndex: number) => {
      if (!selectedShip || selectedShipPosition === null) return

      const shipLength = mapShipSizeToLength(selectedShip)

      let isValidPlacement = true
      const newGrid = JSON.parse(JSON.stringify(grid)) // Deep copy to modify

      // Check if the ship can be placed
      for (let i = 0; i < shipLength; i++) {
        const currentRow =
          selectedShipPosition === EShipPosition.HORIZONTAL ? rowIndex : rowIndex + i
        const currentCol =
          selectedShipPosition === EShipPosition.HORIZONTAL ? colIndex + i : colIndex
        if (currentRow >= 10 || currentCol >= 10 || newGrid[currentRow][currentCol] !== 'clear') {
          isValidPlacement = false
          break
        }
      }

      // Place the ship if valid and mark the surrounding cells as 'not-allowed'
      if (isValidPlacement) {
        for (let i = 0; i < shipLength; i++) {
          const currentRow =
            selectedShipPosition === EShipPosition.HORIZONTAL ? rowIndex : rowIndex + i
          const currentCol =
            selectedShipPosition === EShipPosition.HORIZONTAL ? colIndex + i : colIndex

          newGrid[currentRow][currentCol] = 'ship' // Mark the ship's position

          // Mark the surrounding cells as 'not-allowed'
          for (let x = -1; x <= 1; x++) {
            for (let y = -1; y <= 1; y++) {
              if (
                currentRow + x >= 0 &&
                currentRow + x < 10 &&
                currentCol + y >= 0 &&
                currentCol + y < 10
              )
                newGrid[currentRow + x][currentCol + y] = 'not-allowed'
            }
          }
        }

        // Additional step to clean 'not-allowed' markings for the ship's cells
        for (let i = 0; i < shipLength; i++) {
          const currentRow =
            selectedShipPosition === EShipPosition.HORIZONTAL ? rowIndex : rowIndex + i
          const currentCol =
            selectedShipPosition === EShipPosition.HORIZONTAL ? colIndex + i : colIndex
          newGrid[currentRow][currentCol] = 'ship'
        }

        const newShipCoord = {
          x: String.fromCharCode(65 + colIndex),
          y: rowIndex + 1,
          size: shipLength,
          direction: selectedShipPosition,
        }

        setGrid(() => newGrid)
        setShipsCoord((prev) => [...prev, newShipCoord])
        setShipsNum((prev) => ({ ...prev, [selectedShip]: prev[selectedShip] - 1 }))
        setSelectedShip(() => null)

        setStateHistory((prev) => [
          ...prev,
          {
            grid: [...grid],
            shipsCoord: [...shipsCoord],
            shipsNum: { ...shipsNum },
            areAllShipsPlaced: { ...areAllShipsPlaced },
          },
        ])
      } else {
        showNotification(EToastType.ERROR, 'Invalid placement, please try again.')
      }
    },
    [grid, selectedShip, selectedShipPosition, shipsCoord, shipsNum, areAllShipsPlaced]
  )

  const handleRevert = useCallback(() => {
    if (stateHistory.length > 1) {
      const lastState = stateHistory[stateHistory.length - 1]
      setGrid(lastState.grid)
      setShipsCoord(lastState.shipsCoord)
      setShipsNum(lastState.shipsNum)
      setAreAllShipsPlaced(lastState.areAllShipsPlaced)
      setStateHistory((prev) => prev.slice(0, prev.length - 1))
    }
  }, [stateHistory])

  return {
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
    updateGridBox,
  }
}
