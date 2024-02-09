import { LocalComponents } from './styled';
import { Box, Container, CssBaseline, Grid, TextField, Typography } from '@mui/material';
import Button from '@mui/material/Button';
import { FormEvent, useContext } from 'react';
import { AuthContext } from '../../providers/AuthProvider/context.ts';
import { COLORS } from '../../utils/colors.ts';
import { Link, useNavigate } from 'react-router-dom';
import GoogleButton from 'react-google-button';

const Login = () => {
  const { signInUserWithEmailAndPassword, signInUserWithGoogle } = useContext(AuthContext);

  const navigate = useNavigate();

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const data = new FormData(event.currentTarget);
    const userData = {
      email: data.get('email'),
      password: data.get('password'),
    };

    if (typeof userData.email !== 'string' || typeof userData.password !== 'string') {
      return;
    }

    if (!userData.email.length) {
      alert('Please enter an email address.');
      return;
    }

    if (!userData.password.length) {
      alert('Please enter a password.');
      return;
    }

    console.log(userData);

    const res = await signInUserWithEmailAndPassword(userData.email, userData.password);
    if (res) {
      navigate('/dashboard');
    }
  };

  const onGoogleSignIn = async () => {
    const res = await signInUserWithGoogle();

    if (res) {
      navigate('/dashboard');
    }
  };

  return (
    <LocalComponents.Container>
      <Container
        component='main'
        maxWidth='xs'
        style={{
          backgroundColor: COLORS.white,
          borderRadius: 8,
        }}>
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}>
          <Typography component='h1' variant='h5'>
            Log in
          </Typography>
          <Box component='form' onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <TextField
              margin='normal'
              required
              fullWidth
              id='email'
              label='Email Address'
              name='email'
              autoComplete='email'
              autoFocus
            />
            <TextField
              margin='normal'
              required
              fullWidth
              name='password'
              label='Password'
              type='password'
              id='password'
              autoComplete='current-password'
            />
            <Button type='submit' fullWidth variant='contained' sx={{ mt: 3, mb: 2 }} style={{ height: 50 }}>
              Log In
            </Button>
            <GoogleButton style={{ width: '100%', marginBottom: 8 }} onClick={onGoogleSignIn} />
            <Grid container>
              <Grid item xs>
                <Link
                  to={'/forgot-password'}
                  style={{
                    color: '#1976d2',
                  }}>
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link
                  to={'/register'}
                  style={{
                    color: '#1976d2',
                  }}>
                  {"Don't have an account? Register"}
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>
    </LocalComponents.Container>
  );
};

export default Login;
