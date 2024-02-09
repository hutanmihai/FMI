import { ReactNode, useMemo, useState } from 'react';
import { ImageContext } from './context.ts';

const ImageProvider = ({ children }: { children: ReactNode }) => {
  const [imageBase64, setImageBase64] = useState<string | null>(null);

  const setImage = (image: string | null) => {
    setImageBase64(image);
    console.log('image set');
  };

  const value = useMemo(() => ({ imageBase64, setImage }), [imageBase64, setImage]);

  return <ImageContext.Provider value={value}>{children}</ImageContext.Provider>;
};

export default ImageProvider;
