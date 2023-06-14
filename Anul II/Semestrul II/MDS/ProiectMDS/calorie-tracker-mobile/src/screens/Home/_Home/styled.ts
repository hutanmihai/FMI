import styled from 'styled-components/native';
import { COLORS } from '../../../utils/styled/constants';

export const Components = {
  Container: styled.View`
    flex: 1;
    background-color: ${COLORS.black};
    justify-content: flex-end;
    padding: 16px;
    padding-bottom: 64px;
  `,

  WelcomeText: styled.Text`
    font-size: 36px;
    color: ${COLORS.gold};
    font-weight: bold;
    text-align: center;
  `,

  TargetText: styled.Text`
    font-size: 20px;
    color: ${COLORS.gold};
    text-align: center;
    margin-vertical: 12px;
  `,

  PieChartWrapper: styled.View`
    flex: 1;
    align-items: center;
    position: relative;
    padding-top: 24px;
    margin-top: 64px;
  `,

  CaloriesText: styled.Text<{ offset?: string }>`
    position: absolute;
    font-size: 24px;
    color: ${COLORS.gold};
    font-weight: bold;
    z-index: 1;
    ${({ offset }) => offset && `top: ${offset}`};
  `,

  ButtonsWrapper: styled.View`
    justify-content: center;
    flex-direction: row;
    flex-wrap: wrap;
    width: 100%;
  `,

  Text: styled.Text`
    font-size: 30px;
    color: ${COLORS.green};
    font-weight: bold;
  `,

  Button: styled.TouchableOpacity`
    width: 40%;
    height: 50px;
    flex-direction: row;
    background-color: ${COLORS.green};
    justify-content: center;
    align-items: center;
    border-radius: 8px;
    margin: 0 12px 24px 12px;
  `,

  ButtonLabel: styled.Text`
    font-size: 20px;
    font-weight: bold;
  `,

  AdditionalInfo: styled.Text<{ color: string; offset: string }>`
    position: absolute;
    font-size: 20px;
    font-weight: bold;
    ${({ color }) => color && `color: ${color}`};
    ${({ offset }) => offset && `top: ${offset}`};
  `,

  TextContainer: styled.View`
    height: 150px;
    justify-content: flex-start;
    align-items: center;
  `,
};
