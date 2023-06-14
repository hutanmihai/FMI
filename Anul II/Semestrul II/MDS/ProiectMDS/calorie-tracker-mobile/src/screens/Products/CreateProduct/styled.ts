import styled from 'styled-components/native';
import { COLORS } from '../../../utils/styled/constants';

export const Components = {
  Container: styled.View`
    flex: 1;
    background-color: ${COLORS.black};
    align-items: center;
  `,

  ButtonsWrapper: styled.View`
    margin-top: 16px;
    width: 100%;
    height: 48px;
    flex-direction: row;
    justify-content: space-around;
  `,

  Button: styled.TouchableOpacity<{ color: string }>`
    width: 40%;
    background-color: ${(props) => props.color};
    align-items: center;
    justify-content: center;
    padding-vertical: 8px;
    border-radius: 8px;
  `,

  ButtonLabel: styled.Text`
    color: ${COLORS.black};
    font-size: 20px;
    font-weight: bold;
  `,
};
