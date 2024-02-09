import { useRouteError } from 'react-router-dom';
import { useEffect } from 'react';
import { LocalComponents } from './styled.ts';

export default function Error() {
  const error = useRouteError();
  const errorMessage =
    typeof error === 'object' &&
    error &&
    ('message' in error
      ? typeof error.message === 'string' && error.message
      : 'statusText' in error
        ? typeof error.statusText === 'string' && error.statusText
        : undefined);

  useEffect(() => {
    console.log(error);
  }, []);

  return (
    <LocalComponents.Container>
      <h1>Oops!</h1>
      <p>Sorry, an unexpected error has occurred.</p>
      <p>
        <i>{errorMessage}</i>
      </p>
    </LocalComponents.Container>
  );
}
