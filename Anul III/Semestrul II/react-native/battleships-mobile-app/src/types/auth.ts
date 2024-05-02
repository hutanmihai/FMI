export type TLoginRequest = {
  email: string
  password: string
}

export type TRegisterRequest = {
  email: string
  password: string
}

export type TTokens = {
  accessToken: string
  refreshToken: string
}
