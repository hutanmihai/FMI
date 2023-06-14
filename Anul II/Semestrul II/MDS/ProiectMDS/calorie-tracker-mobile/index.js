import { registerRootComponent } from 'expo';

import App from './App';
import Providers from './src/providers';

const AppWrapper = () => {
  return (
    <Providers>
      <App />
    </Providers>
  );
};

registerRootComponent(AppWrapper);
