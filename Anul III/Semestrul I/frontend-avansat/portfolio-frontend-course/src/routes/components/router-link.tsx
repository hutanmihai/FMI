import { forwardRef } from 'react'
import Link, { LinkProps } from 'next/link'

// eslint-disable-next-line react/display-name
const RouterLink = forwardRef<HTMLAnchorElement, LinkProps>(({ ...other }, ref) => (
  <Link ref={ref} {...other} />
))

export default RouterLink
