import React, { useContext } from 'react';
import { Components } from './styled';
import { FontAwesomeIcon } from '@fortawesome/react-native-fontawesome';
import { faGoogle } from '@fortawesome/free-brands-svg-icons';
import { COLORS } from '../../../utils/styled/constants';
import { AuthContext } from '../../../providers/AuthProvider/context';

const Login = () => {
  // Variables from the authentication context
  const { login } = useContext(AuthContext);

  return (
    <Components.Container>
      <Components.Text>You need to be logged in to use our app!</Components.Text>
      <Components.Button onPress={login}>
        <FontAwesomeIcon icon={faGoogle} color={COLORS.black} />
        <Components.ButtonLabel>{'Login'}</Components.ButtonLabel>
      </Components.Button>
    </Components.Container>
  );
};

export default Login;
