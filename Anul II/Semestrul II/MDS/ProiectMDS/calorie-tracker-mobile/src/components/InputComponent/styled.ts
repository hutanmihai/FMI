import styled from 'styled-components/native';
import { COLORS } from '../../utils/styled/constants';

export const Components = {
  Container: styled.View`
    width: 90%;
    height: 88px;
  `,

  Label: styled.Text`
    color: ${COLORS.green};
    font-weight: bold;
    font-size: 24px;
    margin-vertical: 8px;
  `,

  Input: styled.TextInput`
    background-color: ${COLORS.brown};
    flex: 1;
    border-radius: 8px;
    padding-left: 8px;
    height: 48px;
    color: ${COLORS.black};
    font-size: 16px;
    font-weight: bold;
  `,
};
