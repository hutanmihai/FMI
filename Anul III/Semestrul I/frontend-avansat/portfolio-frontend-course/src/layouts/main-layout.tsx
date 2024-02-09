import { ReactNode } from 'react'
import Footer from '@/layouts/footer'
import Navbar from '@/layouts/nav/nav'
import { useScroll } from 'framer-motion'
import ScrollProgress from '@/components/scroll-progress/scroll-progress'

import Box from '@mui/material/Box'

export default function MainLayout({ children }: { children: ReactNode }) {
  const { scrollYProgress } = useScroll()

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', height: 1 }}>
      <ScrollProgress scrollYProgress={scrollYProgress} />
      <Navbar />

      <Box
        component="main"
        sx={{
          flexGrow: 1,
        }}
      >
        {children}
      </Box>

      <Footer />
    </Box>
  )
}
