import React from 'react';
import AuthProvider from './AuthProvider';

const Providers = ({ children }: { children?: React.ReactNode }) => {
  return <AuthProvider>{children}</AuthProvider>;
};

export default Providers;
