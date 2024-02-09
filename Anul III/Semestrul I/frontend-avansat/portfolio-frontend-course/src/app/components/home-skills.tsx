import { m } from 'framer-motion'
import Iconify from '@/components/iconify'
import { useResponsive } from '@/hooks/use-responsive'
import { bgGradient, textGradient } from '@/theme/css'
import { varFade, MotionViewport } from '@/components/animate'

import Box from '@mui/material/Box'
import Button from '@mui/material/Button'
import Container from '@mui/material/Container'
import Grid from '@mui/material/Unstable_Grid2'
import Typography from '@mui/material/Typography'
import { alpha, styled, useTheme } from '@mui/material/styles'

type StyledPolygonProps = {
  anchor?: 'top' | 'bottom'
}

const StyledPolygon = styled('div')<StyledPolygonProps>(({ anchor = 'top', theme }) => ({
  left: 0,
  zIndex: 9,
  height: 80,
  width: '100%',
  position: 'absolute',
  clipPath: 'polygon(0% 0%, 100% 100%, 0% 100%)',
  backgroundColor: theme.palette.background.default,
  display: 'block',
  lineHeight: 0,
  ...(anchor === 'top' && {
    top: -1,
    transform: 'scale(-1, -1)',
  }),
  ...(anchor === 'bottom' && {
    bottom: -1,
    backgroundColor: theme.palette.background.default,
  }),
}))

export default function HomeSkills() {
  const theme = useTheme()

  const mdUp = useResponsive('up', 'md')

  const renderDescription = (
    <Box sx={{ textAlign: { xs: 'center', md: 'unset' }, mt: { xs: 10, md: 20 } }}>
      <m.div variants={varFade().inUp}>
        <Typography
          variant="h2"
          sx={{
            mt: 3,
            mb: 1,
            ...(mdUp && {
              mr: 7,
            }),
            ...textGradient(
              `300deg, ${theme.palette.primary.main} 0%, ${theme.palette.warning.main} 100%`
            ),
          }}
        >
          Skills and Technologies
        </Typography>
      </m.div>

      <m.div variants={varFade().in}>
        <Typography
          variant="body2"
          color="text.secondary"
          sx={{
            mb: 5,
            ...(mdUp && {
              mr: 15,
            }),
          }}
        >
          More detailed information about my skills and technologies can be found on my github
          profile.
        </Typography>
      </m.div>

      <m.div variants={varFade().inUp}>
        <Button
          color="inherit"
          size="large"
          variant="contained"
          endIcon={<Iconify icon="icon-park:github" />}
          target="_blank"
          rel="noopener"
          href="https://github.com/hutanmihai"
        >
          Go to Github
        </Button>
      </m.div>
    </Box>
  )

  const renderImg = (
    <Box
      component={m.img}
      src="/assets/landing-page/skills.svg"
      variants={varFade().in}
      sx={{
        height: 1,
        width: 0.5,
        objectFit: 'cover',
        position: 'absolute',
        boxShadow: `-80px 80px 80px ${
          theme.palette.mode === 'light'
            ? alpha(theme.palette.grey[500], 0.48)
            : alpha(theme.palette.common.black, 0.24)
        }`,
      }}
    />
  )

  return (
    <Box sx={{ position: 'relative' }}>
      <StyledPolygon />
      <Box
        sx={{
          minHeight: 600,
          overflow: 'hidden',
          position: 'relative',
          ...bgGradient({
            startColor: `${theme.palette.grey[900]} 25%`,
            endColor: alpha(theme.palette.grey[900], 0),
            imgUrl: '/assets/landing-page/skills.svg',
          }),
          ...(mdUp && {
            ...bgGradient({
              color: alpha(theme.palette.background.default, 0.8),
              imgUrl: '/assets/landing-page/overlay_skills.webp',
            }),
          }),
          my: 15,
        }}
      >
        <Container component={MotionViewport}>
          <Grid container>
            <Grid xs={12} md={6}>
              {renderDescription}
            </Grid>

            {mdUp && <Grid md={6}>{renderImg}</Grid>}
          </Grid>
        </Container>
      </Box>
      <StyledPolygon anchor="bottom" />
    </Box>
  )
}
