import React, { SetStateAction } from 'react';
import { Components } from './styled';
import { COLORS } from '../../utils/styled/constants';

const InputComponent = ({
  label,
  placeholder,
  value,
  setValue,
}: {
  label: string;
  placeholder: string;
  value?: string;
  setValue: (text: string) => void;
}) => {
  return (
    <Components.Container>
      <Components.Label>{label}</Components.Label>
      <Components.Input
        placeholder={placeholder}
        placeholderTextColor={COLORS.black}
        value={value}
        onChangeText={setValue}
      />
    </Components.Container>
  );
};

export default InputComponent;
