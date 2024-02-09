import { ReactNode } from 'react'

import { DialogProps } from '@mui/material/Dialog'

export type ConfirmDialogProps = Omit<DialogProps, 'title' | 'content'> & {
  title: ReactNode
  content?: ReactNode
  action: ReactNode
  onClose: VoidFunction
}
