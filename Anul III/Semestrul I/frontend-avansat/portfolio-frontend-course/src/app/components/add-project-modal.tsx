import { z } from 'zod'
import { useForm } from 'react-hook-form'
import { addDoc } from '@firebase/firestore'
import { Project } from '@/types/project.type'
import { zodResolver } from '@hookform/resolvers/zod'
import { ConfirmDialog } from '@/components/custom-dialog'
import FormProvider, { RHFTextField } from '@/components/hook-form'
import { projectsRef } from '@/auth/context/firebase/auth-provider'
import RHFTechnologiesFields from '@/components/hook-form/rhf-technologies-fields'
import TextFieldsContainer from '@/components/form-containers/text-fields-container'

import Box from '@mui/material/Box'
import Grid from '@mui/material/Unstable_Grid2'
import LoadingButton from '@mui/lab/LoadingButton'

type Props = {
  isOpen: boolean
  setIsOpen: Function
}

export default function AddProjectModal({ isOpen, setIsOpen }: Props) {
  const ProjectSchema = z.object({
    title: z.string().min(3).max(50),
    description: z.string().min(3).max(500),
    technologies: z.array(z.string().min(1).max(30)),
    github_link: z.string().url().nullable(),
    live_demo_link: z.string().url().nullable(),
    youtube_link: z.string().url().nullable(),
  })

  const defaultValues = {
    title: '',
    description: '',
    technologies: [''],
    github_link: null,
    live_demo_link: null,
    youtube_link: null,
  }

  const methods = useForm<Project>({
    resolver: zodResolver(ProjectSchema),
    defaultValues,
  })

  const {
    reset,
    handleSubmit,
    formState: { isSubmitting },
  } = methods

  const onSubmit = async (formData: Project) => {
    try {
      await addDoc(projectsRef, formData)
    } catch (error) {
      console.log(error)
    }
    setIsOpen(false)
    reset()
  }

  const formContent = (
    <FormProvider methods={methods} onSubmit={handleSubmit(onSubmit)}>
      <Grid container spacing={3}>
        <Grid xs={12} md={12} mt={2}>
          <Box rowGap={3} columnGap={2} display="grid">
            <TextFieldsContainer>
              <RHFTextField name="title" label="Title" />
              <RHFTextField name="description" label="Description" />
              <RHFTextField name="github_link" label="Github Link" />
              <RHFTextField name="live_demo_link" label="Live Demo Link" />
              <RHFTextField name="youtube_link" label="Youtube Link" />
            </TextFieldsContainer>
            <RHFTechnologiesFields />
          </Box>
        </Grid>
      </Grid>
    </FormProvider>
  )

  return (
    <ConfirmDialog
      open={isOpen}
      onClose={() => {
        reset()
        setIsOpen(false)
      }}
      title="Add Project"
      content={formContent}
      action={
        <LoadingButton
          loading={isSubmitting}
          variant="contained"
          color="primary"
          onClick={handleSubmit(onSubmit)}
        >
          Add
        </LoadingButton>
      }
    />
  )
}
