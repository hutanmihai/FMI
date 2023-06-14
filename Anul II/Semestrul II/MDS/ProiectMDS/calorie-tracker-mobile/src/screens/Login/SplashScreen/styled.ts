import styled from 'styled-components/native';
import { COLORS } from '../../../utils/styled/constants';

export const Components = {
  Container: styled.View`
    flex: 1;
    background-color: ${COLORS.black};
    justify-content: center;
    align-items: center;
  `,

  SplashText: styled.Text`
    font-size: 30px;
    color: ${COLORS.green};
    font-weight: bold;
  `,
};
