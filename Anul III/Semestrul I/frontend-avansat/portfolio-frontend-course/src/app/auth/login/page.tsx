'use client'

import { z } from 'zod'
import React, { useState } from 'react'
import { useForm } from 'react-hook-form'
import Iconify from '@/components/iconify'
import { useAuthContext } from '@/auth/hooks'
import { useBoolean } from '@/hooks/use-boolean'
import { PATH_AFTER_LOGIN } from '@/config-global'
import { zodResolver } from '@hookform/resolvers/zod'
import { useRouter, useSearchParams } from 'next/navigation'
import FormProvider, { RHFTextField } from '@/components/hook-form'

import { Button } from '@mui/material'
import Alert from '@mui/material/Alert'
import Stack from '@mui/material/Stack'
import Divider from '@mui/material/Divider'
import IconButton from '@mui/material/IconButton'
import Typography from '@mui/material/Typography'
import LoadingButton from '@mui/lab/LoadingButton'
import InputAdornment from '@mui/material/InputAdornment'

export default function Login() {
  const { login, loginWithGoogle } = useAuthContext()

  const router = useRouter()

  const [errorMsg, setErrorMsg] = useState('')

  const searchParams = useSearchParams()

  const returnTo = searchParams.get('returnTo')

  const password = useBoolean()

  const LoginSchema = z.object({
    email: z.string().email('Email must be a valid email address').min(1, 'Email is required'),
    password: z.string().min(1, 'Password is required'),
  })

  const defaultValues = {
    email: '',
    password: '',
  }

  const methods = useForm({
    resolver: zodResolver(LoginSchema),
    defaultValues,
  })

  const {
    reset,
    handleSubmit,
    formState: { isSubmitting },
  } = methods

  const onSubmit = handleSubmit(async (data) => {
    try {
      await login?.(data.email, data.password)

      router.push(returnTo || PATH_AFTER_LOGIN)
    } catch (error) {
      console.error(error)
      reset()
      // @ts-ignore
      setErrorMsg(typeof error === 'string' ? error : error.message)
    }
  })

  const handleGoogleLogin = async () => {
    try {
      await loginWithGoogle()

      router.push(returnTo || PATH_AFTER_LOGIN)
    } catch (error) {
      console.error(error)
      reset()
      // @ts-ignore
      setErrorMsg(typeof error === 'string' ? error : error.message)
    }
  }

  const renderHead = (
    <Stack spacing={2} sx={{ mb: 5 }}>
      <Typography variant="h4">Sign in to Admin Panel</Typography>
    </Stack>
  )

  const renderForm = (
    <Stack spacing={2.5}>
      {!!errorMsg && <Alert severity="error">{errorMsg}</Alert>}

      <RHFTextField name="email" label="Email address" />

      <RHFTextField
        name="password"
        label="Password"
        type={password.value ? 'text' : 'password'}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <IconButton onClick={password.onToggle} edge="end">
                <Iconify icon={password.value ? 'solar:eye-bold' : 'solar:eye-closed-bold'} />
              </IconButton>
            </InputAdornment>
          ),
        }}
      />

      <LoadingButton
        fullWidth
        color="inherit"
        size="large"
        type="submit"
        variant="contained"
        loading={isSubmitting}
      >
        Login
      </LoadingButton>
    </Stack>
  )

  const renderLoginOption = (
    <div>
      <Divider
        sx={{
          my: 2.5,
          typography: 'overline',
          color: 'text.disabled',
          '&:before, :after': {
            borderTopStyle: 'dashed',
          },
        }}
      >
        OR
      </Divider>

      <Stack direction="row" justifyContent="center" spacing={2}>
        <Button
          fullWidth
          variant="outlined"
          onClick={handleGoogleLogin}
          startIcon={<Iconify icon="eva:google-fill" color="#00A76F" />}
          sx={{
            height: 44,
          }}
        >
          Login with Google
        </Button>
      </Stack>
    </div>
  )

  return (
    <FormProvider methods={methods} onSubmit={onSubmit}>
      {renderHead}
      {renderForm}
      {renderLoginOption}
    </FormProvider>
  )
}
