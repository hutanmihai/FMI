import { LocalComponents } from './styled';
import { useContext } from 'react';
import { AuthContext } from '../../providers/AuthProvider/context.ts';

const checkoutLink = 'https://buy.stripe.com/test_5kA15V7lH8mq4ak5kk';

const Subscription = () => {
  const { currentProfile } = useContext(AuthContext);

  return (
    <LocalComponents.Container>
      <div className='subscription-card'>
        <h2 className='subscription-title'>Vision Canvas Premium</h2>
        <p className='subscription-price'>€9.99</p>
        <ul className='subscription-features'>
          <li>Save photos</li>
          <li>Access to 3 image editing algorithms</li>
        </ul>
        {!currentProfile?.isSubscribed ? (
          <>
            <p className='subscription-type'>One-time purchase</p>
            <button
              className='subscription-button'
              onClick={() => {
                window.location.href = checkoutLink;
              }}>
              Checkout
            </button>
          </>
        ) : (
          <p className='subscription-type'>You are subscribed</p>
        )}
      </div>
    </LocalComponents.Container>
  );
};

export default Subscription;
