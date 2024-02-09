import { forwardRef } from 'react'
import Iconify from '@/components/iconify'
import { RouterLink } from '@/routes/components'

import Box from '@mui/material/Box'
import Link from '@mui/material/Link'
import { styled } from '@mui/material/styles'
import ListItemButton from '@mui/material/ListItemButton'

import { NavItemProps } from '../types'

// eslint-disable-next-line react/display-name
export const NavItem = forwardRef<HTMLDivElement, NavItemProps>(
  ({ title, path, icon, ...other }, ref) => {
    const renderContent = (
      <StyledNavItem ref={ref} {...other}>
        <Box component="span" sx={{ mr: 2, display: 'inline-flex' }}>
          <Iconify icon={icon!} width={20} height={20} />
        </Box>

        <Box component="span" sx={{ flexGrow: 1 }}>
          {title}
        </Box>
      </StyledNavItem>
    )

    return (
      <Link component={RouterLink} href={path} color="inherit" underline="none">
        {renderContent}
      </Link>
    )
  }
)

const StyledNavItem = styled(ListItemButton)(({ theme }) => {
  return {
    ...theme.typography.body2,
    color: theme.palette.text.secondary,
    fontWeight: theme.typography.fontWeightMedium,
    height: 48,
  }
})
