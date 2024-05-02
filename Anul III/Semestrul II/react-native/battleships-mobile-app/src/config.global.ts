export const BACKEND_URL = 'http://163.172.177.98:8081'

export const apiConfig = {
  auth: {
    login: `${BACKEND_URL}/auth/login`,
    register: `${BACKEND_URL}/auth/register`,
  },
  user: {
    me: `${BACKEND_URL}/user/details/me`,
  },
  game: {
    list: `${BACKEND_URL}/game`,
    create: `${BACKEND_URL}/game`,
    get: (id: string) => `${BACKEND_URL}/game/${id}`,
    join: (id: string) => `${BACKEND_URL}/game/join/${id}`,
    strike: (id: string) => `${BACKEND_URL}/game/strike/${id}`,
    sendMap: (id: string) => `${BACKEND_URL}/game/${id}`,
  },
}
