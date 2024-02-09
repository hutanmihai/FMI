import { LocalComponents } from './styled';
import { Box, Container, CssBaseline, TextField, Typography } from '@mui/material';
import Button from '@mui/material/Button';
import { FormEvent, useContext } from 'react';
import { AuthContext } from '../../providers/AuthProvider/context.ts';
import { COLORS } from '../../utils/colors.ts';
import { useNavigate } from 'react-router-dom';

const ForgotPassword = () => {
  const { sendUserPasswordResetEmail } = useContext(AuthContext);

  const navigate = useNavigate();

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const data = new FormData(event.currentTarget);
    const userData = {
      email: data.get('email'),
    };

    if (typeof userData.email !== 'string') {
      return;
    }

    if (!userData.email.length) {
      alert('Please enter an email address.');
      return;
    }

    console.log(userData);

    await sendUserPasswordResetEmail(userData.email);
    navigate('/login');
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
            Forgot password
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
            <Button type='submit' fullWidth variant='contained' sx={{ mt: 3, mb: 2 }} style={{ height: 50 }}>
              Reset password
            </Button>
          </Box>
        </Box>
      </Container>
    </LocalComponents.Container>
  );
};

export default ForgotPassword;
