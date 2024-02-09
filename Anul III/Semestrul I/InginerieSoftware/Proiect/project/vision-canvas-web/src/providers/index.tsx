import { ReactNode } from 'react';
import AuthProvider from './AuthProvider';
import ImageProvider from './ImageProvider';

const Providers = ({ children }: { children?: ReactNode }) => {
  return (
    <AuthProvider>
      <ImageProvider>{children}</ImageProvider>
    </AuthProvider>
  );
};

export default Providers;
