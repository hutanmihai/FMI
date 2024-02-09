'use client'

import Iconify from '@/components/iconify'

import { Button } from '@mui/material'

export default function ResumeButton() {
  const handleDownload = () => {
    window.open('/assets/resume.pdf', '_blank')
  }

  return (
    <Button
      variant="outlined"
      color="primary"
      endIcon={<Iconify icon="lucide:download" />}
      onClick={handleDownload}
    >
      Resume
    </Button>
  )
}
