import { useContext, useEffect, useState } from 'react';
import { TextField, Button, Card, Typography, Snackbar } from '@mui/material';
import { Alert } from '@mui/material';
import { LocalComponents } from './styled';
import { AuthContext } from '../../providers/AuthProvider/context.ts';
import { setProfile, setSubscribed } from '../../api/profile';
import { useSearchParams } from 'react-router-dom';

const Account = () => {
  const { user, currentProfile, setCurrentProfile } = useContext(AuthContext);
  const [searchParams] = useSearchParams();

  const [firstName, setFirstName] = useState(currentProfile?.firstName ?? '');
  const [lastName, setLastName] = useState(currentProfile?.lastName ?? '');
  const [username, setUsername] = useState(currentProfile?.username ?? '');
  const [errors, setErrors] = useState({ firstName: '', lastName: '' });
  const [open, setOpen] = useState(false);

  useEffect(() => {
    if (searchParams.values().next().value && user) {
      setSubscribed(user?.email ?? user?.uid, searchParams.values().next().value).then();
      setCurrentProfile({ ...currentProfile, isSubscribed: searchParams.values().next().value });
    }
  }, []);

  const handleInputChange = (event: any) => {
    const { name, value } = event.target;

    const _errors = { ...errors };

    switch (name) {
      case 'firstName':
        _errors.firstName = value.length < 2 ? 'First Name must be at least 2 characters long!' : '';
        setFirstName(value);
        break;
      case 'lastName':
        _errors.lastName = value.length < 2 ? 'Last Name must be at least 2 characters long!' : '';
        setLastName(value);
        break;
      case 'username':
        setUsername(value);
        break;
      default:
        break;
    }

    setErrors(errors);
  };

  const handleSubmit = async (event: any) => {
    event.preventDefault();

    if (validateForm()) {
      if (!username) {
        setUsername(firstName + lastName);
      }

      console.log(
        `First Name: ${firstName}, Last Name: ${lastName}, Username: ${!username ? firstName + lastName : username}`,
      );
      if (user) {
        await setProfile(user?.email ?? user?.uid, {
          firstName,
          lastName,
          username: !username ? firstName + lastName : username,
        });
        setOpen(true);
      }
    } else {
      console.error('Invalid Form');
    }
  };

  const validateForm = () => {
    let valid = true;
    Object.values(errors).forEach((val) => val.length > 0 && (valid = false));
    return valid;
  };

  const handleClose = (event: any, reason: any) => {
    if (reason === 'clickaway') {
      return;
    }

    setOpen(false);
  };

  return (
    <LocalComponents.Container>
      <Card sx={{ padding: '20px', margin: '20px', width: '300px', borderRadius: 8 }}>
        <Typography variant='h4' align='center'>
          Account
        </Typography>
        <Typography variant='h6' align='center'>
          {user?.email}
        </Typography>
        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <TextField
            name='firstName'
            label='First Name'
            value={firstName}
            onChange={handleInputChange}
            margin='normal'
            required
            error={!!errors.firstName}
            helperText={errors.firstName}
          />
          <TextField
            name='lastName'
            label='Last Name'
            value={lastName}
            onChange={handleInputChange}
            margin='normal'
            required
            error={!!errors.lastName}
            helperText={errors.lastName}
          />
          <TextField name='username' label='Username' value={username} onChange={handleInputChange} margin='normal' />
          {currentProfile?.isSubscribed && (
            <Typography variant='body1' align='center'>
              You are subscribed to Vision Canvas Pro!
            </Typography>
          )}
          <Button type='submit' variant='contained' color='primary' sx={{ mt: 2 }}>
            Save
          </Button>
        </form>
        <Snackbar open={open} autoHideDuration={3000} onClose={handleClose}>
          <Alert onClose={handleClose} severity='success' sx={{ width: '100%' }}>
            Profile saved successfully!
          </Alert>
        </Snackbar>
      </Card>
    </LocalComponents.Container>
  );
};

export default Account;
