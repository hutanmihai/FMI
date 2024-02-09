import Iconify from '@/components/iconify'
import { RouterLink } from '@/routes/components'

import { Button } from '@mui/material'

type Props = {
  text: string
  href: string
  icon: string
}

export default function RouteButton({ text, href, icon }: Props) {
  return (
    <Button
      component={RouterLink}
      href={href}
      variant="outlined"
      color="primary"
      endIcon={<Iconify icon={icon} width={20} height={20} />}
    >
      {text}
    </Button>
  )
}
