import { ReactNode } from 'react'

import { Box } from '@mui/material'

export default function TextFieldsContainer({ children }: { children: ReactNode }) {
  return (
    <Box
      rowGap={3}
      columnGap={2}
      display="grid"
      gridTemplateColumns={{
        xs: 'repeat(1, 1fr)',
        sm: 'repeat(2, 1fr)',
      }}
    >
      {children}
    </Box>
  )
}
