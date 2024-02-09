import { createContext } from 'react';

export interface ImageContextProps {
  imageBase64: string | null;
  setImage: (image: string | null) => void;
}

export const ImageContext = createContext<ImageContextProps>({
  imageBase64: null,
  setImage: () => {},
});
