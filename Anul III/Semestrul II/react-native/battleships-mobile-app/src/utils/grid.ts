import { TBox } from '@/types/game'

export const generateEmptyGrid = (): TBox[][] => {
  return Array.from({ length: 10 }, () => Array.from({ length: 10 }, () => 'clear'))
}

export const mapShipSizeToLength = (ship: 's' | 'm' | 'l' | 'xl') => {
  switch (ship) {
    case 's':
      return 2
    case 'm':
      return 3
    case 'l':
      return 4
    case 'xl':
      return 6
  }
}
