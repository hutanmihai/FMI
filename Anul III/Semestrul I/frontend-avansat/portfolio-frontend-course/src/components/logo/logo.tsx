import { forwardRef, ElementType } from 'react'
import { RouterLink } from '@/routes/components'

import Link from '@mui/material/Link'
import Box, { BoxProps } from '@mui/material/Box'

export interface LogoProps extends BoxProps {
  disabledLink?: boolean
}

interface BoxOptions {
  alt?: string
}

const MuiBox = <C extends ElementType>(props: BoxProps<C, { component?: C }> & BoxOptions) => {
  return <Box {...props}>{props.children}</Box>
}

// eslint-disable-next-line react/display-name
const Logo = forwardRef<HTMLDivElement, LogoProps>(
  ({ disabledLink = false, sx, ...other }, ref) => {
    const logo = (
      <MuiBox
        component="img"
        src="/logo/logo_single.svg"
        sx={{ width: 40, height: 40, cursor: 'pointer', ...sx }}
        alt="logo"
      />
    )

    if (disabledLink) {
      return logo
    }

    return (
      <Link component={RouterLink} href="/" sx={{ display: 'contents' }}>
        {logo}
      </Link>
    )
  }
)

export default Logo
