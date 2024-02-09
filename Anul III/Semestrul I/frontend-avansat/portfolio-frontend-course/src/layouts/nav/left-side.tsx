import Logo from '@/components/logo'
import { paths } from '@/routes/paths'
import { RouterLink } from '@/routes/components'

import Link from '@mui/material/Link'
import Stack from '@mui/material/Stack'
import Typography from '@mui/material/Typography'

export default function NavLeftSide() {
  return (
    <Stack
      direction="row"
      alignItems="center"
      justifyContent="flex-start"
      spacing={{ xs: 0.5, sm: 1 }}
    >
      <Logo />
      <Link component={RouterLink} href={paths.home} color="inherit" underline="none">
        <Typography variant="h4">mihaihutan</Typography>
      </Link>
    </Stack>
  )
}
