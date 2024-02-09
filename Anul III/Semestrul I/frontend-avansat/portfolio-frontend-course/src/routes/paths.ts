const ROOTS = {
  AUTH: '/auth',
  HOME: '/',
  ADMIN: '/admin',
}

export const paths = {
  // ROOT
  home: ROOTS.HOME,
  // AUTH
  auth: {
    login: `${ROOTS.AUTH}/login`,
  },
  // ADMIN
  admin: {
    root: ROOTS.ADMIN,
  },
}
