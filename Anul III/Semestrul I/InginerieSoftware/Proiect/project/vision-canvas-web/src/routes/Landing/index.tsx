import { LocalComponents } from './styled';
import ReactCompareImage from 'react-compare-image';
import BaseImage from '../../assets/images/base.png';
import ComparisonImage from '../../assets/images/comparison.png';

const Landing = () => {
  return (
    <LocalComponents.Container>
      <LocalComponents.Title>Vision Canvas</LocalComponents.Title>
      <LocalComponents.ComparisonWrapper>
        <ReactCompareImage leftImage={BaseImage} rightImage={ComparisonImage} sliderLineColor='#000' />
      </LocalComponents.ComparisonWrapper>
    </LocalComponents.Container>
  );
};

export default Landing;
