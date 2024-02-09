import { ReactElement } from 'react'

import { BoxProps } from '@mui/material/Box'

export type LabelColor =
  | 'default'
  | 'primary'
  | 'secondary'
  | 'info'
  | 'success'
  | 'warning'
  | 'error'

export type LabelVariant = 'filled' | 'outlined' | 'soft'

export interface LabelProps extends BoxProps {
  startIcon?: ReactElement | null
  endIcon?: ReactElement | null
  color?: LabelColor
  variant?: LabelVariant
}
