import { ListItemButtonProps } from '@mui/material/ListItemButton'

export type NavItemBaseProps = {
  title: string
  path: string
  icon?: string
}

export type NavItemProps = ListItemButtonProps & NavItemBaseProps

export type NavListProps = {
  data: NavItemBaseProps
}

export type NavProps = {
  data: NavItemBaseProps[]
}
