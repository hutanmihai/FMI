import styled from 'styled-components/native';
import { COLORS } from '../../../utils/styled/constants';

export const Components = {
  Container: styled.View`
    flex: 1;
    background-color: ${COLORS.black};
    align-items: center;
  `,

  Label: styled.Text`
    color: ${COLORS.gold};
    font-weight: bold;
    font-size: 24px;
    text-transform: capitalize;
    margin-bottom: 8px;
  `,

  ItemCell: styled.View`
    width: 100%;
    border: 1px solid ${COLORS.gold};
    max-width: 95%;
    min-width: 85%;
    margin-vertical: 16px;
    border-radius: 8px;
    padding: 16px;
    margin-horizontal: 8px;
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
    margin-bottom: 8px;
  `,

  ButtonsWrapper: styled.View`
    max-width: 100%;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  `,

  Button: styled.TouchableOpacity`
    align-items: center;
    justify-content: center;
    margin-bottom: 8px;
    margin-left: 16px;
  `,

  CreateButton: styled.TouchableOpacity`
    margin-top: 16px;
    margin-bottom: 8px;
    border-radius: 8px;
    width: 40%;
    height: 48px;
    background-color: ${COLORS.green};
    align-items: center;
    justify-content: center;
  `,

  ButtonLabel: styled.Text`
    color: ${COLORS.black};
    font-size: 20px;
    font-weight: bold;
  `,
};
