import Iconify from '@/components/iconify'
import { varFade } from '@/components/animate'
import SectionContainer from '@/app/components/section-container'

import Box from '@mui/material/Box'
import Card from '@mui/material/Card'
import { alpha } from '@mui/material/styles'
import Typography from '@mui/material/Typography'

const CARDS = [
  {
    icon: 'cib:about-me',
    title: 'About Me',
    description:
      "Throughout my academic journey, I've honed my skills in various facets of computer science, positioning myself to excel in the dynamic world of technology. I am driven by the ambition to continually evolve and become one of the best programmers I can be. I eagerly anticipate opportunities to contribute to innovative projects and collaborate with like-minded professionals in the field.",
  },
  {
    icon: 'tabler:play-handball',
    title: 'Extra Activities',
    description:
      'Having played handball for nine years on a high-performing team, I understand the value of teamwork, communication, and determination in achieving collective goals.',
  },
]

export default function HomeAboutMe() {
  return (
    <SectionContainer id={'about-me'} variants={varFade().inUp}>
      <Box
        gap={{ xs: 3, lg: 10 }}
        display="grid"
        alignItems="center"
        gridTemplateColumns={{
          xs: 'repeat(1, 1fr)',
          md: 'repeat(2, 1fr)',
        }}
      >
        {CARDS.map((card, index) => (
          <Card
            key={index}
            sx={{
              textAlign: 'center',
              boxShadow: { md: 'none' },
              bgcolor: 'background.default',
              p: (theme) => theme.spacing(10, 5),
              ...(index === 0 && {
                boxShadow: (theme) => ({
                  md: `-40px 40px 80px ${
                    theme.palette.mode === 'light'
                      ? alpha(theme.palette.grey[500], 0.16)
                      : alpha(theme.palette.common.black, 0.4)
                  }`,
                }),
              }),
            }}
          >
            <Iconify
              icon={card.icon}
              width={50}
              height={50}
              sx={{
                mx: 'auto',
                ...(index === 0 && {
                  color: (theme) => theme.palette.primary.main,
                }),
                ...(index === 1 && {
                  color: (theme) => theme.palette.primary.dark,
                }),
              }}
            />

            <Typography variant="h5" sx={{ mt: 6, mb: 2 }}>
              {card.title}
            </Typography>

            <Typography sx={{ color: 'text.secondary' }}>{card.description}</Typography>
          </Card>
        ))}
      </Box>
    </SectionContainer>
  )
}
