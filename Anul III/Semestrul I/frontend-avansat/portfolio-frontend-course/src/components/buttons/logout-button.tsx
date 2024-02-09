import Iconify from '@/components/iconify'
import { useRouter } from 'next/navigation'
import { useAuthContext } from '@/auth/hooks'

import { Button } from '@mui/material'

export default function LogoutButton() {
  const { user, logout } = useAuthContext()
  const router = useRouter()

  const handleLogout = async () => {
    try {
      await logout()
      router.replace('/')
    } catch (error) {
      console.error(error)
    }
  }
  return (
    <Button
      variant="outlined"
      color="error"
      onClick={handleLogout}
      sx={{ fontWeight: 'fontWeightBold', color: 'error.main' }}
      endIcon={<Iconify icon="mdi:logout" width={20} height={20} />}
    >
      Logout
    </Button>
  )
}
