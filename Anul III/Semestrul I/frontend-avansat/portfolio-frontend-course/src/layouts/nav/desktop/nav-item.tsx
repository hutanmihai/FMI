import { forwardRef } from 'react'
import { RouterLink } from '@/routes/components'

import Link from '@mui/material/Link'
import { styled } from '@mui/material/styles'
import ListItemButton from '@mui/material/ListItemButton'

import { NavItemProps } from '../types'

// eslint-disable-next-line react/display-name
export const NavItem = forwardRef<HTMLDivElement, NavItemProps>(
  ({ title, path, ...other }, ref) => {
    const renderContent = (
      <StyledNavItem disableRipple disableTouchRipple ref={ref} {...other}>
        {title}
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
    padding: 0,
    height: '100%',
    fontWeight: theme.typography.fontWeightMedium,
    transition: theme.transitions.create(['all'], {
      duration: theme.transitions.duration.shorter,
    }),
    '&:hover': {
      opacity: 0.64,
      backgroundColor: 'transparent',
    },
  }
})
