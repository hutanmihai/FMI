import styled from 'styled-components/native';
import { COLORS } from '../../../utils/styled/constants';

export const Components = {
  Container: styled.View`
    flex: 1;
    align-items: center;
    justify-content: center;
    background-color: ${COLORS.black};
    padding-bottom: 48px;
  `,

  Button: styled.TouchableOpacity`
    width: 50%;
    height: 40px;
    flex-direction: row;
    gap: 4px;
    background-color: ${COLORS.green};
    justify-content: center;
    align-items: center;
    border-radius: 8px;
  `,

  ButtonLabel: styled.Text`
    font-size: 20px;
    font-weight: bold;
  `,

  Text: styled.Text`
    font-size: 36px;
    text-align: center;
    color: ${COLORS.green};
    padding-horizontal: 32px;
    align-self: center;
    margin-bottom: 100px;
  `,
};
