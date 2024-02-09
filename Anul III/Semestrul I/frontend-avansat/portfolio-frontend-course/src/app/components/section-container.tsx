import { ReactNode } from 'react'
import { bgGradient } from '@/theme/css'
import { m, Variants } from 'framer-motion'
import { MotionViewport } from '@/components/animate'

import Box from '@mui/material/Box'
import { Container } from '@mui/material'
import Typography from '@mui/material/Typography'
import { alpha, useTheme } from '@mui/material/styles'

type Props = {
  id: string
  useBgGradient?: boolean
  children: ReactNode
  variants: Variants
  title?: string
}

export default function SectionContainer({ children, useBgGradient, id, variants, title }: Props) {
  const theme = useTheme()

  return (
    <Box
      id={id}
      component="section"
      sx={{
        pt: { xs: 8, md: 10 },
        pb: { xs: 8, md: 10 },
        py: 10,
        position: 'relative',
        ...(useBgGradient && {
          ...bgGradient({
            startColor: alpha(theme.palette.background.default, 0.5),
            endColor: alpha(theme.palette.primary.main, 0.05),
          }),
        }),
      }}
    >
      <Container maxWidth="lg" component={MotionViewport}>
        <m.div variants={variants}>
          {title && (
            <Typography variant="h2" align="center" sx={{ mb: 5 }}>
              {title}
            </Typography>
          )}
          {children}
        </m.div>
      </Container>
    </Box>
  )
}
