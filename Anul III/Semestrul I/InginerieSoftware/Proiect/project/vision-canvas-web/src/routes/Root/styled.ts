import styled from 'styled-components';
import { COLORS } from '../../utils/colors.ts';

export const LocalComponents = {
  Wrapper: styled.div`
    width: 100vw;
    height: 100vh;
    background-color: ${COLORS.black};
    overflow: hidden;
  `,

  Container: styled.div`
    width: 100%;
    height: 100%;
  `,
};
