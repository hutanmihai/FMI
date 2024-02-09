import Logo from '@/components/logo'
import { bgGradient } from '@/theme/css'

import Box from '@mui/material/Box'
import Link from '@mui/material/Link'
import { Container } from '@mui/material'
import Typography from '@mui/material/Typography'
import { alpha, useTheme } from '@mui/material/styles'

export default function Footer() {
  const theme = useTheme()

  return (
    <Box
      component="footer"
      sx={{
        py: 5,
        textAlign: 'center',
        position: 'relative',
        bgcolor: 'background.default',
        ...bgGradient({
          startColor: alpha(theme.palette.primary.main, 0.05),
          endColor: alpha(theme.palette.background.default, 0.5),
        }),
      }}
    >
      <Container>
        <Logo sx={{ mb: 1, mx: 'auto' }} />

        <Typography variant="caption" component="div">
          © All rights reserved
          <br /> made by
          <Link href="https://mihaihutan.ro"> mihaihutan.ro </Link>
        </Typography>
      </Container>
    </Box>
  )
}
