import { paths } from '@/routes/paths'
import { useAuthContext } from '@/auth/hooks'
import { usePathname } from 'next/navigation'
import RouteButton from '@/components/buttons/route-button'
import LogoutButton from '@/components/buttons/logout-button'

import Stack from '@mui/material/Stack'

export default function NavRightSide() {
  const { user } = useAuthContext()
  const pathname = usePathname()

  const isOnAdminPage = pathname.includes(paths.admin.root)

  return (
    <Stack
      flexGrow={1}
      direction="row"
      alignItems="center"
      justifyContent="flex-end"
      spacing={{ xs: 0.5, sm: 1 }}
    >
      {user && (
        <>
          {!isOnAdminPage ? (
            <RouteButton text="Admin" href={paths.admin.root} icon="ri:admin-fill" />
          ) : (
            <RouteButton text="Home" href={paths.home} icon="bx:home" />
          )}

          <LogoutButton />
        </>
      )}
    </Stack>
  )
}
