import styled from 'styled-components/native';
import { COLORS } from '../../../utils/styled/constants';

export const Components = {
  Container: styled.View`
    flex: 1;
    background-color: ${COLORS.black};
    align-items: center;
  `,

  Label: styled.Text`
    color: ${COLORS.green};
    font-weight: bold;
    font-size: 24px;
  `,

  ItemCell: styled.View`
    width: 100%;
    min-width: 90%;
    border: 1px solid ${COLORS.gold};
    margin-vertical: 16px;
    border-radius: 8px;
    padding: 16px;
  `,

  ItemCellDetails: styled.View`
    flex-direction: row;
  `,

  ItemCellFieldTitle: styled.Text`
    color: ${COLORS.black};
    font-size: 24px;
    font-weight: bold;
    text-transform: capitalize;
  `,

  ItemCellFieldDescription: styled.Text<{ color?: string }>`
    color: ${(props) => props.color || COLORS.black};
    font-size: 20px;
    margin-top: 8px;
  `,

  ButtonsWrapper: styled.View<{ hasMinwidth?: boolean }>`
    margin-top: 16px;
    ${(props) => props.hasMinwidth && 'min-width: 60%;'}
    max-width: 100%;
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

  CreateDiaryText: styled.Text`
    font-size: 24px;
    color: ${COLORS.gold};
    text-align: center;
    margin-top: 16px;
  `,
};
