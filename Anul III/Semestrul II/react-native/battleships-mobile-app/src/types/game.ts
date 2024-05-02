import { TUser } from '@/types/user'

export enum EGameAxis {
  X = 'x',
  Y = 'y',
}

export enum EAxisRange {
  MIN = 0,
  MAX = 9,
}

export enum EGameStatus {
  CREATED = 'CREATED',
  MAP_CONFIG = 'MAP_CONFIG',
  ACTIVE = 'ACTIVE',
  FINISHED = 'FINISHED',
}

export enum EShipPosition {
  HORIZONTAL = 'HORIZONTAL',
  VERTICAL = 'VERTICAL',
}

export type TGame = {
  id: string
  status: EGameStatus
  playerToMoveId: string | null
  moves: TMove[]
  // TODO: Fix this type
  shipsCoord: TShip[]
  player1: TUser
  player2: TUser | null
  player1Id: string
  player2Id: string | null
}

export type TMove = {
  playerId: string
  result: boolean
  x: string
  y: number
}

export type TStrike = {
  x: string
  y: number
}

export type TShip = {
  x: string
  y: number
  size: number
  direction: EShipPosition
}

export type TGamesListResponse = {
  total: number
  games: {
    id: string
    status: EGameStatus
    playerToMoveId: string | null
    player1: TUser
    player2: TUser | null
    player1Id: string
    player2Id: string | null
  }[]
}

export type TBox = 'clear' | 'ship' | 'destroyed' | 'not-allowed'

export type TShipSize = 's' | 'm' | 'l' | 'xl'
