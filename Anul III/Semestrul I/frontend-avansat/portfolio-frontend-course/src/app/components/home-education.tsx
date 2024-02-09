import Image from 'next/image'
import { varFade } from '@/components/animate'
import { useResponsive } from '@/hooks/use-responsive'
import SectionContainer from '@/app/components/section-container'

import Box from '@mui/material/Box'
import { useTheme } from '@mui/material/styles'
import Typography from '@mui/material/Typography'
import {
  Timeline,
  TimelineDot,
  TimelineItem,
  TimelineContent,
  TimelineSeparator,
  TimelineConnector,
  TimelineOppositeContent,
} from '@mui/lab'

const EDUCATIONS = [
  {
    institution: 'University of Bucharest',
    degree: 'Bachelor of Science in Computer Science',
    date: '2021 - 2024',
    gpa: '8/10',
    icon: '/assets/landing-page/education/unibuc.webp',
    descriptions: [
      'I am a member of the performance group, benefiting from a full scholarship throughout my university journey.',
      "During my Bachelor's degree, I took part in a lot of interesting subjects that broadened my knowledge. Some of them include Data Structures, Advanced Algorithms, Object- Oriented Programming, Operating Systems, Artificial Intelligence and Advanced Databases.",
    ],
    image: '/assets/landing-page/education/unibuc.webp',
  },
  {
    institution: 'National College "Gheorghe Lazar"',
    degree: 'High School Diploma in Mathematics and Computer Science',
    date: '2017 - 2021',
    gpa: '9.5/10',
    icon: '/assets/landing-page/education/lazar.webp',
    descriptions: ['Baccalaureate exam: 10 Computer Science, 9,75 Mathematics'],
    image: '/assets/landing-page/education/lazar.webp',
  },
]

export default function HomeEducation() {
  const theme = useTheme()

  const mdUp = useResponsive('up', 'md')

  return (
    <SectionContainer id="education" useBgGradient variants={varFade().inRight} title="Education">
      <Timeline position="right">
        {EDUCATIONS.map((education, index) => (
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
                  src={education.image}
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
                  backgroundImage: `url(${education.icon})`,
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
                  {education.institution}
                </Typography>

                <Typography variant="body1" gutterBottom>
                  {education.degree}, {education.date}, {education.gpa}
                </Typography>

                {education.descriptions.map((description, index) => (
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
