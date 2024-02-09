import styled from 'styled-components';
import { COLORS } from '../../utils/colors.ts';

export const LocalComponents = {
  Container: styled.div`
    padding: 16px;
  `,

  Button: styled.label`
    font:
      16px 'Roboto',
      sans-serif;
    width: 100px;
    height: 50px;
    background-color: ${COLORS.orange};
    color: ${COLORS.black};
    border-radius: 4px;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    text-align: center;
  `,
};
