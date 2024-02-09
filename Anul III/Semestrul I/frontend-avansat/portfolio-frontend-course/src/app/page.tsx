'use client'

import MainLayout from '@/layouts/main-layout'
import HomeHero from '@/app/components/home-hero'
import HomeSkills from '@/app/components/home-skills'
import HomeAboutMe from '@/app/components/home-about-me'
import HomeProjects from '@/app/components/home-projects'
import HomeEducation from '@/app/components/home-education'
import HomeExperience from '@/app/components/home-experience'

import Box from '@mui/material/Box'
import { useTheme } from '@mui/material/styles'

export default function Home() {
  const theme = useTheme()
  return (
    <MainLayout>
      <section id="home">
        <HomeHero />
      </section>
      <Box
        sx={{
          overflow: 'hidden',
          position: 'relative',
          bgcolor: 'background.default',
        }}
      >
        <HomeAboutMe />
        <HomeProjects />
        <section id="skills">
          <HomeSkills />
        </section>
        <HomeExperience />
        <HomeEducation />
      </Box>
    </MainLayout>
  )
}
