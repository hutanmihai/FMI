import React, { useContext, useEffect, useState } from 'react';

import { Components } from './styled';
import InputComponent from '../../../components/InputComponent';
import { UserHeightMetric, UserWeightMetric } from '../../../api/types/user';
import { AuthContext } from '../../../providers/AuthProvider/context';
import { apiFetch } from '../../../api';
import { useNavigation } from '@react-navigation/native';
import { FontAwesomeIcon } from '@fortawesome/react-native-fontawesome';
import { faGoogle } from '@fortawesome/free-brands-svg-icons';
import { COLORS } from '../../../utils/styled/constants';

const Account = () => {
  // Navigation hooks
  const navigation = useNavigation();

  // Context hooks
  const { user, setUser, logout } = useContext(AuthContext);

  // User input hooks
  const [name, setName] = useState<string | undefined>();
  const [height, setHeight] = useState<string | undefined>();
  const [weight, setWeight] = useState<string | undefined>();
  const [targetWeight, setTargetWeight] = useState<string | undefined>();
  const [targetCalories, setTargetCalories] = useState<string | undefined>();

  // Set user input values on mount
  useEffect(() => {
    if (!user) {
      return;
    }

    setName(user.name);
    setHeight(user.height?.toString());
    setWeight(user.weight?.toString());
    setTargetWeight(user.target_weight?.toString());
    setTargetCalories(user.target_calories?.toString());
  }, []);

  const _onSave = async () => {
    if (!user) {
      return;
    }

    // Convert strings to numbers
    const heightNumber = height ? Number(height) : undefined;
    const weightNumber = weight ? Number(weight) : undefined;
    const targetWeightNumber = targetWeight ? Number(targetWeight) : undefined;
    const targetCaloriesNumber = targetCalories ? Number(targetCalories) : undefined;

    // Update user
    await apiFetch({
      path: '/user/me',
      method: 'PUT',
      body: {
        name,
        pref_height_metric: 'cm',
        height: heightNumber,
        pref_weight_metric: 'kg',
        weight: weightNumber,
        target_weight: targetWeightNumber,
        target_calories: targetCaloriesNumber,
      },
    }).then((data) => {
      // If successful, update user context and navigate back
      setUser(data);
      navigation.goBack();
    });
  };

  return (
    <Components.Container contentContainerStyle={{ alignItems: 'center' }}>
      <InputComponent label={'Name'} placeholder={'Name...'} value={name} setValue={setName} />
      <InputComponent label={'Height'} placeholder={'Height...'} value={height} setValue={setHeight} />
      <InputComponent label={'Weight'} placeholder={'Weight...'} value={weight} setValue={setWeight} />
      <InputComponent
        label={'Target Weight'}
        placeholder={'Target Weight...'}
        value={targetWeight}
        setValue={setTargetWeight}
      />
      <InputComponent
        label={'Target Calories'}
        placeholder={'Target Calories...'}
        value={targetCalories}
        setValue={setTargetCalories}
      />
      <Components.ButtonContainer>
        <Components.Button onPress={_onSave}>
          <Components.ButtonLabel>Save</Components.ButtonLabel>
        </Components.Button>
        <Components.Button onPress={logout}>
          <FontAwesomeIcon icon={faGoogle} color={COLORS.black} />
          <Components.ButtonLabel>{'Logout'}</Components.ButtonLabel>
        </Components.Button>
      </Components.ButtonContainer>
    </Components.Container>
  );
};

export default Account;
