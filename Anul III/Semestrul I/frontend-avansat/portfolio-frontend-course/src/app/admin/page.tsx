'use client'

import Iconify from '@/components/iconify'
import { useState, useEffect } from 'react'
import { Project, Projects } from '@/types/project.type'
import { ConfirmDialog } from '@/components/custom-dialog'
import { doc, getDocs, deleteDoc } from 'firebase/firestore'
import ProjectsItem from '@/components/projects/projects-item'
import AddProjectModal from '@/app/components/add-project-modal'
import { DB, projectsRef } from '@/auth/context/firebase/auth-provider'

import Box from '@mui/material/Box'
import Stack from '@mui/material/Stack'
import Grid from '@mui/material/Unstable_Grid2'
import { Button, Container } from '@mui/material'
import Typography from '@mui/material/Typography'
import LoadingButton from '@mui/lab/LoadingButton'

export default function AdminHome() {
  const [projects, setProjects] = useState<Projects>([])
  const [isDialogOpen, setIsDialogOpen] = useState(false)
  const [isDeleteDialogOpen, setIsDeleteDialogOpen] = useState(false)
  const [isDeleteLoading, setIsDeleteLoading] = useState(false)
  const [selectedProject, setSelectedProject] = useState<Project | null>(null)

  useEffect(() => {
    const getProjectsList = async () => {
      try {
        const data = await getDocs(projectsRef)
        const filteredData = data.docs.map((doc) => {
          return {
            id: doc.id,
            ...doc.data(),
          }
        })
        setProjects(filteredData as Projects)
        console.log(filteredData)
      } catch (error) {
        console.log(error)
      }
    }
    getProjectsList()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isDialogOpen])

  const handleDelete = async () => {
    if (!selectedProject) {
      // Handle the case when no project is selected
      return
    }
    setIsDeleteLoading(true)
    try {
      const projectDocRef = doc(DB, 'projects', selectedProject.id)
      await deleteDoc(projectDocRef)
      setProjects((prevProjects) =>
        prevProjects.filter((project) => project.id !== selectedProject.id)
      )
    } catch (error) {
      console.log(error)
    }
    setIsDeleteLoading(false)
  }

  return (
    <Container maxWidth="lg" sx={{ my: 15 }}>
      <Stack direction="row" alignItems="space-between" justifyContent="spcae-between">
        <Box sx={{ flexGrow: 1 }}>
          <Typography variant="h3" gutterBottom>
            Projects
          </Typography>
        </Box>
        <Box sx={{ flexShrink: 0 }}>
          <Button
            variant="contained"
            color="primary"
            startIcon={<Iconify icon="mingcute:add-line" />}
            onClick={() => {
              setIsDialogOpen(true)
            }}
          >
            Add Project
          </Button>
        </Box>
      </Stack>
      <Grid container spacing={2}>
        <Grid xs={12} md={12}>
          {projects.map((project, index) => (
            <Stack key={index}>
              <ProjectsItem project={project} key={project.id} />
              <Button
                fullWidth
                color="error"
                variant="outlined"
                startIcon={<Iconify icon="mdi:delete" />}
                sx={{ mt: 1, mb: 10 }}
                onClick={() => {
                  setIsDeleteDialogOpen(true)
                  setSelectedProject(project)
                }}
              >
                Delete
              </Button>
            </Stack>
          ))}
        </Grid>
      </Grid>
      {isDialogOpen && <AddProjectModal isOpen={isDialogOpen} setIsOpen={setIsDialogOpen} />}
      <ConfirmDialog
        open={isDeleteDialogOpen}
        onClose={() => setIsDeleteDialogOpen(false)}
        title="Delete Project"
        content={
          <Typography variant="body1" gutterBottom>
            Are you sure you want to delete this project?
          </Typography>
        }
        action={
          <LoadingButton
            loading={isDeleteLoading}
            variant="contained"
            color="error"
            onClick={async () => {
              await handleDelete()
              setIsDeleteDialogOpen(false)
            }}
          >
            Șterge
          </LoadingButton>
        }
      />
    </Container>
  )
}
