import { useState, useEffect } from 'react'
import { getDocs } from 'firebase/firestore'
import { varFade } from '@/components/animate'
import { Projects } from '@/types/project.type'
import { LoadingScreen } from '@/components/loading-screen'
import ProjectsItem from '@/components/projects/projects-item'
import SectionContainer from '@/app/components/section-container'
import { projectsRef } from '@/auth/context/firebase/auth-provider'

import Box from '@mui/material/Box'

export default function HomeProjects() {
  const [isLoading, setIsLoading] = useState<boolean>(true)
  const [projects, setProjects] = useState<Projects>([])

  useEffect(() => {
    setIsLoading(true)
    const getProjectsList = async () => {
      try {
        const data = await getDocs(projectsRef)
        const filteredData = data.docs.map((doc) => doc.data())
        setProjects(filteredData as Projects)
        console.log(filteredData)
      } catch (error) {
        console.log(error)
      }
    }
    getProjectsList()
    setIsLoading(false)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  if (isLoading) {
    return <LoadingScreen />
  }

  return (
    <SectionContainer id="projects" variants={varFade().in} title="Projects">
      <Box
        gap={{ xs: 3, lg: 10 }}
        display="grid"
        alignItems="center"
        gridTemplateColumns={{
          xs: 'repeat(1, 1fr)',
          md: 'repeat(2, 1fr)',
        }}
      >
        {projects.map((project) => (
          <ProjectsItem project={project} key={project.id} />
        ))}
      </Box>
    </SectionContainer>
  )
}
