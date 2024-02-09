export type ActionMapType<M extends { [index: string]: any }> = {
  [Key in keyof M]: M[Key] extends undefined
    ? {
        type: Key
      }
    : {
        type: Key
        payload: M[Key]
      }
}

export type AuthUserType = null | Record<string, any>

export type AuthStateType = {
  status?: string
  loading: boolean
  user: AuthUserType
}

export type FirebaseContextType = {
  user: AuthUserType
  loading: boolean
  authenticated: boolean
  unauthenticated: boolean
  logout: () => Promise<void>
  loginWithGoogle: () => Promise<void>
  login: (email: string, password: string) => Promise<void>
}
