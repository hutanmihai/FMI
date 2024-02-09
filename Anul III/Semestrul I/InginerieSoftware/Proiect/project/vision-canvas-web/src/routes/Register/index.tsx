import { Box, Container, CssBaseline, Grid, TextField, Typography } from '@mui/material';
import { LocalComponents } from './styled.ts';
import Button from '@mui/material/Button';
import { COLORS } from '../../utils/colors.ts';
import { FormEvent, useContext } from 'react';
import { AuthContext } from '../../providers/AuthProvider/context.ts';
import { Link, useNavigate } from 'react-router-dom';
import GoogleButton from 'react-google-button';

const Register = () => {
  const { signUpUserWithEmailAndPassword, signInUserWithGoogle } = useContext(AuthContext);

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

    if (userData.email.length < 4) {
      alert('Please enter an email address.');
      return;
    }

    if (userData.password.length < 6 || userData.password.length > 30) {
      alert('Please enter a password between 6 and 30 characters.');
      return;
    }

    console.log(userData);

    const res = await signUpUserWithEmailAndPassword(userData.email, userData.password);
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
            Register
          </Typography>
          <Box component='form' noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  autoComplete='given-name'
                  name='firstName'
                  required
                  fullWidth
                  id='firstName'
                  label='First Name'
                  autoFocus
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  required
                  fullWidth
                  id='lastName'
                  label='Last Name'
                  name='lastName'
                  autoComplete='family-name'
                />
              </Grid>
              <Grid item xs={12}>
                <TextField required fullWidth id='email' label='Email Address' name='email' autoComplete='email' />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name='password'
                  label='Password'
                  type='password'
                  id='password'
                  autoComplete='new-password'
                />
              </Grid>
            </Grid>
            <Button type='submit' fullWidth variant='contained' sx={{ mt: 3, mb: 2 }} style={{ height: 50 }}>
              Register
            </Button>
            <GoogleButton style={{ width: '100%', marginBottom: 8 }} onClick={onGoogleSignIn} />
            <Grid container justifyContent='flex-end'>
              <Grid item>
                <Link
                  to={'/login'}
                  style={{
                    color: '#1976d2',
                  }}>
                  Already have an account? Log in
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>
    </LocalComponents.Container>
  );
};

export default Register;
