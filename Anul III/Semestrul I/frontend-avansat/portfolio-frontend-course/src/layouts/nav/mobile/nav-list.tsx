import { NavItem } from './nav-item'
import { NavListProps } from '../types'

export default function NavList({ data }: NavListProps) {
  return <NavItem title={data.title} path={data.path} icon={data.icon} />
}
