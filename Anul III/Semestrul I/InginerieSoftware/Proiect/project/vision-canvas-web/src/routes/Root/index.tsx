import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import { PhotoLibrary } from '@mui/icons-material';
import React, { useContext, useEffect, useState } from 'react';
import { COLORS } from '../../utils/colors.ts';
import { LocalComponents } from './styled.ts';
import { Outlet, useNavigate } from 'react-router-dom';
import { AuthContext } from '../../providers/AuthProvider/context.ts';
import { Link } from 'react-router-dom';
import { convertFileToBase64 } from '../../utils';
import { setProfile } from '../../api/profile';

const pages = ['dashboard', 'login', 'register'];

const Root = () => {
  const { user, isLoggedIn, signOutUser, currentProfile, setCurrentProfile } = useContext(AuthContext);

  const navigate = useNavigate();

  const [anchorElNav, setAnchorElNav] = useState<null | HTMLElement>(null);
  const [anchorElUser, setAnchorElUser] = useState<null | HTMLElement>(null);
  const [displayedPages, setDisplayedPages] = useState<string[]>(pages);

  useEffect(() => {
    if (isLoggedIn) {
      setDisplayedPages(pages.filter((page) => page !== 'login' && page !== 'register'));
    } else {
      setDisplayedPages(pages);
    }
  }, [isLoggedIn]);

  const handleOpenNavMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElNav(event.currentTarget);
  };

  const handleOpenUserMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const onLogout = async () => {
    handleCloseUserMenu();
    const res = await signOutUser();
    if (res) {
      navigate('/');
    }
  };

  const onAccountClick = () => {
    handleCloseUserMenu();
    navigate('/account');
  };

  const onSubscriptionClick = () => {
    handleCloseUserMenu();
    navigate('/subscription');
  };

  const onChangeAvatarClick = () => {
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';
    fileInput.onchange = async (event) => {
      const file = event?.target?.files[0];
      const imageBase64 = await convertFileToBase64(file);
      if (user) {
        await setProfile(user.email ?? user.uid, { avatar: imageBase64 });
        alert('Avatar updated.');
        setCurrentProfile({ ...currentProfile, avatar: imageBase64 });
      }
    };
    fileInput.click();
  };

  return (
    <LocalComponents.Wrapper>
      <AppBar
        position='static'
        style={{
          backgroundColor: COLORS.orange,
        }}>
        <Container maxWidth='xl'>
          <Toolbar disableGutters>
            <PhotoLibrary sx={{ display: { xs: 'none', md: 'flex' }, mr: 1 }} />
            <Link
              to={'/'}
              style={{
                textDecoration: 'none',
                color: COLORS.white,
              }}>
              <Typography
                variant='h6'
                noWrap
                component='div'
                sx={{
                  mr: 2,
                  display: { xs: 'none', md: 'flex' },
                  fontFamily: 'monospace',
                  fontWeight: 700,
                  letterSpacing: '.3rem',
                  color: 'inherit',
                  textDecoration: 'none',
                }}>
                Vision Canvas
              </Typography>
            </Link>

            <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
              <IconButton
                size='large'
                aria-label='account of current user'
                aria-controls='menu-appbar'
                aria-haspopup='true'
                onClick={handleOpenNavMenu}
                color='inherit'>
                <MenuIcon />
              </IconButton>
              <Menu
                id='menu-appbar'
                anchorEl={anchorElNav}
                anchorOrigin={{
                  vertical: 'bottom',
                  horizontal: 'left',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'left',
                }}
                open={Boolean(anchorElNav)}
                onClose={handleCloseNavMenu}
                sx={{
                  display: { xs: 'block', md: 'none' },
                }}>
                {displayedPages.map((page) => (
                  <Link
                    key={page}
                    to={`/${page}`}
                    style={{
                      color: COLORS.black,
                      textDecoration: 'none',
                      textTransform: 'uppercase',
                    }}>
                    <MenuItem onClick={handleCloseNavMenu}>
                      <Typography textAlign='center'>{page}</Typography>
                    </MenuItem>
                  </Link>
                ))}
              </Menu>
            </Box>
            <PhotoLibrary sx={{ display: { xs: 'flex', md: 'none' }, mr: 1 }} />
            <Typography
              variant='h5'
              noWrap
              component='a'
              href='#app-bar-with-responsive-menu'
              sx={{
                mr: 2,
                display: { xs: 'flex', md: 'none' },
                flexGrow: 1,
                fontFamily: 'monospace',
                fontWeight: 700,
                letterSpacing: '.3rem',
                color: 'inherit',
                textDecoration: 'none',
              }}>
              Vision Canvas
            </Typography>
            <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
              {displayedPages.map((page) => (
                <Link key={page} to={`/${page}`} style={{ color: 'inherit', textDecoration: 'none' }}>
                  <Button onClick={handleCloseNavMenu} sx={{ my: 2, color: 'white', display: 'block' }}>
                    {page}
                  </Button>
                </Link>
              ))}
            </Box>

            <Box sx={{ flexGrow: 0 }}>
              {isLoggedIn ? (
                <Tooltip title='Open settings'>
                  <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                    <Avatar
                      alt={user?.displayName ?? 'User'}
                      src={currentProfile?.avatar ? currentProfile.avatar : user?.photoURL ?? ''}
                    />
                  </IconButton>
                </Tooltip>
              ) : null}
              <Menu
                sx={{ mt: '45px' }}
                id='menu-appbar'
                anchorEl={anchorElUser}
                anchorOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                open={Boolean(anchorElUser)}
                onClose={handleCloseUserMenu}>
                <MenuItem onClick={onAccountClick}>
                  <Typography textAlign='center'>{'Account'}</Typography>
                </MenuItem>
                <MenuItem onClick={onSubscriptionClick}>
                  <Typography textAlign='center'>{'Subscription'}</Typography>
                </MenuItem>
                <MenuItem onClick={onChangeAvatarClick}>
                  <Typography textAlign='center'>{'Change avatar'}</Typography>
                </MenuItem>
                <MenuItem onClick={onLogout}>
                  <Typography textAlign='center' color='error'>
                    {'Log out'}
                  </Typography>
                </MenuItem>
              </Menu>
            </Box>
          </Toolbar>
        </Container>
      </AppBar>
      <LocalComponents.Container>
        <Outlet />
      </LocalComponents.Container>
    </LocalComponents.Wrapper>
  );
};

export default Root;
