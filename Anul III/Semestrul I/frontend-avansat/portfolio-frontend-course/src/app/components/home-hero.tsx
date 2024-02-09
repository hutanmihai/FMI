import Iconify from '@/components/iconify'
import { m, useScroll } from 'framer-motion'
import { HEADER } from '@/layouts/nav/config-layout'
import { useResponsive } from '@/hooks/use-responsive'
import { bgBlur, bgGradient, textGradient } from '@/theme/css'
import { varFade, MotionContainer } from '@/components/animate'
import { useRef, useState, useEffect, useCallback } from 'react'

import Box from '@mui/material/Box'
import Stack from '@mui/material/Stack'
import Container from '@mui/material/Container'
import Grid from '@mui/material/Unstable_Grid2'
import Typography from '@mui/material/Typography'
import { alpha, styled } from '@mui/material/styles'

const StyledRoot = styled('div')(({ theme }) => ({
  ...bgGradient({
    color: alpha(theme.palette.background.default, theme.palette.mode === 'light' ? 0.9 : 0.94),
    imgUrl: '/assets/landing-page/hero.webp',
  }),
  width: '100%',
  height: '100vh',
  position: 'relative',
  [theme.breakpoints.up('md')]: {
    top: 0,
    left: 0,
    position: 'fixed',
  },
}))

const StyledWrapper = styled('div')(({ theme }) => ({
  height: '100%',
  overflow: 'hidden',
  position: 'relative',
  [theme.breakpoints.up('md')]: {
    marginTop: HEADER.H_DESKTOP_OFFSET,
  },
}))

const StyledTextGradient = styled(m.h1)(({ theme }) => ({
  ...textGradient(
    `300deg, ${theme.palette.primary.main} 0%, ${theme.palette.warning.main} 25%, ${theme.palette.primary.main} 50%, ${theme.palette.warning.main} 75%, ${theme.palette.primary.main} 100%`
  ),
  padding: 0,
  marginTop: 8,
  lineHeight: 1,
  fontWeight: 900,
  marginBottom: 24,
  letterSpacing: 8,
  textAlign: 'center',
  backgroundSize: '400%',
  fontSize: `${64 / 16}rem`,
  fontFamily: theme.typography.fontSecondaryFamily,
  [theme.breakpoints.up('md')]: {
    fontSize: `${96 / 16}rem`,
  },
}))

type StyledPolygonProps = {
  opacity?: number
  anchor?: 'left' | 'right'
}

const StyledPolygon = styled('div')<StyledPolygonProps>(
  ({ opacity = 1, anchor = 'left', theme }) => ({
    ...bgBlur({
      opacity,
      color: theme.palette.background.default,
    }),
    zIndex: 9,
    bottom: 0,
    height: 80,
    width: '50%',
    position: 'absolute',
    clipPath: 'polygon(0% 0%, 100% 100%, 0% 100%)',
    ...(anchor === 'left' && {
      left: 0,
      ...(theme.direction === 'rtl' && {
        transform: 'scale(-1, 1)',
      }),
    }),
    ...(anchor === 'right' && {
      right: 0,
      transform: 'scaleX(-1)',
      ...(theme.direction === 'rtl' && {
        transform: 'scaleX(1)',
      }),
    }),
  })
)

export default function HomeHero() {
  const mdUp = useResponsive('up', 'md')

  const heroRef = useRef<HTMLDivElement | null>(null)

  const { scrollY } = useScroll()

  const [percent, setPercent] = useState(0)

  const getScroll = useCallback(() => {
    let heroHeight = 0

    if (heroRef.current) {
      heroHeight = heroRef.current.offsetHeight
    }

    scrollY.on('change', (scrollHeight) => {
      const scrollPercent = (scrollHeight * 100) / heroHeight

      setPercent(Math.floor(scrollPercent))
    })
  }, [scrollY])

  useEffect(() => {
    getScroll()
  }, [getScroll])

  const opacity = 1 - percent / 100

  const hide = percent > 120

  const renderDescription = (
    <Stack
      alignItems="center"
      justifyContent="center"
      sx={{
        height: 1,
        mx: 'auto',
        maxWidth: 480,
        opacity: opacity > 0 ? opacity : 0,
        mt: {
          md: `-${HEADER.H_DESKTOP + percent * 2.5}px`,
        },
      }}
    >
      <m.div variants={varFade().in}>
        <Typography
          variant="h2"
          sx={{
            textAlign: 'center',
          }}
        >
          Software engineer
        </Typography>
      </m.div>

      <m.div variants={varFade().in}>
        <StyledTextGradient
          animate={{ backgroundPosition: '200% center' }}
          transition={{
            repeatType: 'reverse',
            ease: 'linear',
            duration: 20,
            repeat: Infinity,
          }}
        >
          Mihai Hutan
        </StyledTextGradient>
      </m.div>

      <m.div variants={varFade().in}>
        <Typography variant="body2" sx={{ textAlign: 'center' }}>
          I am a dedicated final-year computer science student at the University of Bucharest,
          Romania, with a passion for programming and a keen interest in machine learning and web
          development.
        </Typography>
      </m.div>

      <Stack spacing={3} sx={{ textAlign: 'center', mt: 3 }}>
        <m.div variants={varFade().in}>
          <Typography variant="h4" sx={{ opacity: 0.48 }}>
            Socials
          </Typography>
        </m.div>

        <Stack spacing={5} direction="row" justifyContent="center">
          <m.div variants={varFade().in}>
            <a
              href="https://linkedin.com/in/hutanmihai/"
              aria-label="Check out my LinkedIn Account"
            >
              <Iconify icon="logos:linkedin-icon" width={40} height={40} />
            </a>
          </m.div>
          <m.div variants={varFade().in}>
            <a href="https://github.com/hutanmihai" aria-label="Check out my Github Account">
              <Iconify icon="icon-park:github" width={40} height={40} />
            </a>
          </m.div>
          <m.div variants={varFade().in}>
            <a href="mailto:hutanmihai29@gmail.com" aria-label="Contact me on email">
              <Iconify icon="logos:google-gmail" width={40} height={40} />
            </a>
          </m.div>
        </Stack>
      </Stack>
    </Stack>
  )

  const renderPolygons = (
    <>
      <StyledPolygon />
      <StyledPolygon anchor="right" opacity={0.48} />
      <StyledPolygon anchor="right" opacity={0.48} sx={{ height: 48, zIndex: 10 }} />
      <StyledPolygon anchor="right" sx={{ zIndex: 11, height: 24 }} />
    </>
  )

  return (
    <>
      <StyledRoot
        ref={heroRef}
        sx={{
          ...(hide && {
            opacity: 0,
          }),
        }}
      >
        <StyledWrapper>
          <Container component={MotionContainer} sx={{ height: 1 }}>
            <Grid container columnSpacing={{ md: 10 }} sx={{ height: 1 }}>
              <Grid xs={12} md={6}>
                {renderDescription}
              </Grid>
            </Grid>
          </Container>
        </StyledWrapper>
      </StyledRoot>

      {mdUp && renderPolygons}

      <Box sx={{ height: { md: '100vh' } }} />
    </>
  )
}
