import { ReactNode, useContext } from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { LocalComponents } from './styled.ts';
import { CircularProgress } from '@mui/material';
import { AuthContext } from '../../providers/AuthProvider/context.ts';

const ProtectedRoute = ({ children, redirectPath }: { children: ReactNode; redirectPath: string }) => {
  const { user, currentProfile } = useContext(AuthContext);

  return (
    <>
      {user !== null && currentProfile !== null ? (
        user ? (
          children ? (
            children
          ) : (
            <Outlet />
          )
        ) : (
          <Navigate to={redirectPath} replace />
        )
      ) : (
        <LocalComponents.Container>
          <CircularProgress />
        </LocalComponents.Container>
      )}
    </>
  );
};

export default ProtectedRoute;
