import Image from 'next/image'
import { varFade } from '@/components/animate'
import { useResponsive } from '@/hooks/use-responsive'
import SectionContainer from '@/app/components/section-container'

import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import {
  Timeline,
  TimelineDot,
  TimelineItem,
  TimelineContent,
  TimelineConnector,
  TimelineSeparator,
  TimelineOppositeContent,
} from '@mui/lab'

const EXPERIENCES = [
  {
    title: 'Software Engineer',
    company: 'iBac',
    location: 'Remote',
    date: 'May 2022 - Present',
    icon: '/assets/landing-page/experience/ibac.webp',
    descriptions: [
      'Proud member of the iBac team, a startup team consisting of 3 developers, which aims to help the young scholars from Romania to get the best restults at their Baccalaureate exam.',
      'I am responsible of the frontend web development part, and using React and Next.js I managed to create a beautiful and responsive admin dashboard.',
      'Contributed to arhitectural decisions and feature brainstorming sessions, ensuring the delivery of a high quality product.',
    ],
    image: '/assets/landing-page/experience/ibac.webp',
  },
  {
    title: 'Junior Software Engineer',
    company: 'Capgemini Engineering',
    location: 'Remote',
    date: 'July 2022 - May 2023',
    icon: '/assets/landing-page/experience/capgemini.webp',
    descriptions: [
      'Began my journey at Capgemini Engineering as an Intern and after two months I was promoted to the position of a Junior.',
      'Initiated and executed projects from inception, leveraging Docker for efficient containerization and establishing robust CI/CD Pipelines for both deployment and testing.',
      'Developed, documented and tested RESTful APIs to facilitate seamless collaboration with the frontend team.',
      'Proficiently processed and filtered substantial volumes of data received from data engineering teams, ensuring the delivery of comprehensible and industry-standard APIs.',
      'Contributed to projects utilizing a technology stack comprising Docker, FastAPI, Django, SQLAlchemy, Alembic, PostgreSQL, Poetry and Pytest.',
    ],
    image: '/assets/landing-page/experience/capgemini.webp',
  },
]

export default function HomeExperience() {
  const mdUp = useResponsive('up', 'md')

  return (
    <SectionContainer id="experience" variants={varFade().inLeft} title="Experience">
      <Timeline position="left">
        {EXPERIENCES.map((experience, index) => (
          <TimelineItem key={index}>
            {mdUp ? (
              <TimelineOppositeContent
                sx={{
                  flex: 0.5,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                }}
              >
                <Image
                  src={experience.image}
                  alt="hero"
                  width={500}
                  height={300}
                  style={{
                    marginRight: 20,
                    borderRadius: 10,
                  }}
                />
              </TimelineOppositeContent>
            ) : (
              <TimelineOppositeContent
                sx={{
                  flex: 0,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                }}
              />
            )}
            <TimelineSeparator>
              <TimelineDot
                variant="outlined"
                sx={{
                  backgroundImage: `url(${experience.icon})`,
                  backgroundSize: 'cover',
                  width: 30,
                  height: 30,
                  borderRadius: '50%',
                }}
              />
              <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent>
              <Box
                sx={{
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between',
                }}
              >
                <Typography variant="h4" gutterBottom>
                  {experience.title}
                </Typography>

                <Typography variant="body1" gutterBottom>
                  {experience.company}, {experience.location}, {experience.date}
                </Typography>

                {experience.descriptions.map((description, index) => (
                  <Typography key={index} variant="body2" gutterBottom>
                    {description}
                  </Typography>
                ))}
              </Box>
            </TimelineContent>
          </TimelineItem>
        ))}
      </Timeline>
    </SectionContainer>
  )
}
