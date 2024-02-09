import { m } from 'framer-motion'
import SvgColor from '@/components/svg-color'
import { useSettingsContext } from '@/components/settings'

import IconButton from '@mui/material/IconButton'

export const varHover = (hover = 1.09, tap = 0.97) => ({
  hover: { scale: hover },
  tap: { scale: tap },
})

export default function ThemeModeButton() {
  const settings = useSettingsContext()

  return settings.themeMode === 'light' ? (
    <IconButton
      component={m.button}
      whileTap="tap"
      whileHover="hover"
      variants={varHover(1.05)}
      aria-label="dark mode"
      key="dark"
      onClick={() => settings.onUpdate('themeMode', 'dark')}
      sx={{
        width: 40,
        height: 40,
        '& .svg-color': {
          background: (theme) =>
            `linear-gradient(135deg, ${theme.palette.primary.dark} 0%, ${theme.palette.primary.darker} 100%)`,
        },
      }}
    >
      <SvgColor src="/assets/setting/ic_moon.svg" width={24} height={24} />
    </IconButton>
  ) : (
    <IconButton
      component={m.button}
      whileTap="tap"
      whileHover="hover"
      variants={varHover(1.05)}
      aria-label="light mode"
      key="light"
      onClick={() => settings.onUpdate('themeMode', 'light')}
      sx={{
        width: 40,
        height: 40,
        '& .svg-color': {
          background: (theme) =>
            `linear-gradient(135deg, ${theme.palette.warning.light} 0%, ${theme.palette.warning.main} 100%)`,
        },
      }}
    >
      <SvgColor src="/assets/setting/ic_sun.svg" width={24} height={24} />
    </IconButton>
  )
}
