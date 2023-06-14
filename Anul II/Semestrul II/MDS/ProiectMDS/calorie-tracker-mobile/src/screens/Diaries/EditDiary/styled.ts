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
    text-transform: capitalize;
  `,

  ItemCell: styled.View`
    width: 100%;
    border: 1px solid ${COLORS.gold};
    min-width: 85%;
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

  ButtonsWrapper: styled.View<{ hasMinWidth?: boolean }>`
    margin-top: 16px;
    ${(props) => props.hasMinWidth && 'min-width: 60%;'}
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
};
