import Iconify from '@/components/iconify'
import { Project } from '@/types/project.type'

import Card from '@mui/material/Card'
import Stack from '@mui/material/Stack'
import Button from '@mui/material/Button'
import { alpha } from '@mui/material/styles'
import Typography from '@mui/material/Typography'

export default function ProjectsItem({ project }: { project: Project }) {
  return (
    <Card
      title={project.title}
      sx={{
        textAlign: 'center',
        bgcolor: 'background.default',
        p: (theme) => theme.spacing(10, 5),
        ...{
          boxShadow: (theme) => ({
            md: `-40px 40px 80px ${
              theme.palette.mode === 'light'
                ? alpha(theme.palette.grey[500], 0.16)
                : alpha(theme.palette.common.black, 0.4)
            }`,
          }),
        },
      }}
    >
      <Stack spacing={2}>
        <Typography variant="h4" mb={2}>
          {project.title}
        </Typography>
        <Typography sx={{ color: 'text.secondary' }}>{project.description}</Typography>
        <Stack direction="row" spacing={2} justifyContent="center" alignItems="center" mb={4}>
          {project.github_link && (
            <Button
              color="inherit"
              size="medium"
              variant="contained"
              endIcon={<Iconify icon="icon-park:github" />}
              target="_blank"
              rel="noopener"
              href={project.github_link}
            >
              Github
            </Button>
          )}
          {project.youtube_link && (
            <Button
              color="error"
              size="medium"
              variant="outlined"
              endIcon={<Iconify icon="openmoji:youtube" />}
              target="_blank"
              rel="noopener"
              href={project.youtube_link}
            >
              Youtube
            </Button>
          )}
          {project.live_demo_link && (
            <Button
              color="primary"
              size="medium"
              variant="contained"
              endIcon={<Iconify icon="carbon:demo" />}
              target="_blank"
              rel="noopener"
              href={project.live_demo_link}
            >
              Live Demo
            </Button>
          )}
        </Stack>
        {project.technologies.length > 0 && (
          <Stack
            direction="row"
            spacing={2}
            justifyContent="center"
            alignItems="center"
            flexWrap="wrap"
          >
            {project.technologies.map((technology) => (
              <Iconify
                key={technology}
                icon={`devicon:${technology}`}
                width={40}
                height={40}
                sx={{ mx: 'auto' }}
              />
            ))}
          </Stack>
        )}
      </Stack>
    </Card>
  )
}
