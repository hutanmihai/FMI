import styled from 'styled-components/native';
import { COLORS } from '../../../utils/styled/constants';

export const Components = {
  Container: styled.ScrollView`
    flex: 1;
    background-color: ${COLORS.black};
    padding-top: 80px;
  `,

  Button: styled.TouchableOpacity`
    width: 45%;
    height: 48px;
    flex-direction: row;
    gap: 4px;
    background-color: ${COLORS.green};
    justify-content: center;
    align-items: center;
    border-radius: 8px;
    margin-top: 24px;
  `,

  ButtonContainer: styled.View`
    flex-direction: row;
    flex: 1;
    align-items: flex-end;
    justify-content: space-between;
    width: 100%;
    padding: 0 19px;
  `,

  ButtonLabel: styled.Text`
    font-size: 20px;
    font-weight: bold;
  `,
};
