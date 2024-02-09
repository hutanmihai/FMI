import { bgBlur } from '@/theme/css'
import NavMobile from '@/layouts/nav/mobile'
import { usePathname } from 'next/navigation'
import NavDesktop from '@/layouts/nav/desktop'
import NavLeftSide from '@/layouts/nav/left-side'
import NavRightSide from '@/layouts/nav/right-side'
import { HEADER } from '@/layouts/nav/config-layout'
import { useOffSetTop } from '@/hooks/use-off-set-top'
import { useResponsive } from '@/hooks/use-responsive'
import { navConfig } from '@/layouts/nav/config-navigation'
import ResumeButton from '@/components/buttons/resume-button'
import ThemeModeButton from '@/components/buttons/theme-mode-button'

import Box from '@mui/material/Box'
import Stack from '@mui/material/Stack'
import AppBar from '@mui/material/AppBar'
import { Container } from '@mui/material'
import Toolbar from '@mui/material/Toolbar'
import { useTheme } from '@mui/material/styles'

export default function Navbar() {
  const theme = useTheme()

  const mdUp = useResponsive('up', 'md')

  const offsetTop = useOffSetTop(HEADER.H_DESKTOP)

  const isAdmin = usePathname().includes('/admin')

  return (
    <AppBar>
      <Toolbar
        disableGutters
        sx={{
          height: {
            xs: HEADER.H_MOBILE,
            md: HEADER.H_DESKTOP,
          },
          transition: theme.transitions.create(['height'], {
            easing: theme.transitions.easing.easeInOut,
            duration: theme.transitions.duration.shorter,
          }),
          ...(offsetTop && {
            ...bgBlur({
              color: theme.palette.background.default,
            }),
            height: {
              md: HEADER.H_DESKTOP_OFFSET,
            },
          }),
        }}
      >
        <Container sx={{ height: 1, display: 'flex', alignItems: 'center' }}>
          <NavLeftSide />
          <Box sx={{ flexGrow: 1 }} />
          {isAdmin && (
            <Stack alignItems="center" direction={{ xs: 'row-reverse' }}>
              <NavRightSide />
              <ThemeModeButton />
            </Stack>
          )}
          {mdUp && !isAdmin && <NavDesktop data={navConfig} />}
          <Stack
            alignItems="center"
            direction={{ xs: 'row', md: 'row-reverse' }}
            spacing={{ xs: 0, sm: 1 }}
          >
            {mdUp && !isAdmin && <NavRightSide />}
            {!isAdmin && <ResumeButton />}
            {!isAdmin && <ThemeModeButton />}
            {!mdUp && !isAdmin && <NavMobile data={navConfig} />}
          </Stack>
        </Container>
      </Toolbar>
    </AppBar>
  )
}
