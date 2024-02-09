// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-nocheck
import ImageEditor from '@toast-ui/react-image-editor';
import 'tui-image-editor/dist/tui-image-editor.css';
import { LocalComponents } from './styled.ts';
import { useState, useRef, useContext } from 'react';
import { ImageContext } from '../../providers/ImageProvider/context.ts';
import './index.css';
import { AuthContext } from '../../providers/AuthProvider/context.ts';
import { saveProfileImage } from '../../api/profile';
import { unstable_usePrompt } from 'react-router-dom';

const Editor = () => {
  const { imageBase64, setImage } = useContext(ImageContext);
  const { user, currentProfile } = useContext(AuthContext);

  const imageEditorRef = useRef(null);

  const [refreshKey, setRefreshKey] = useState(0);
  const [blurValue, setBlurValue] = useState(0);

  const screenHeight = window.innerHeight;
  const screenWidth = window.innerWidth;

  unstable_usePrompt({
    message: 'Are you sure? Unsaved changes will be lost.',
    when: true,
  });

  const refreshComponent = () => {
    setRefreshKey((prevKey) => prevKey + 1);
  };

  const handleBackgroundRemoval = async () => {
    console.log('Removing background');
    const response = await fetch(`${import.meta.env.VITE_REACT_APP_API_URL}/background-removal`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ image: imageEditorRef.current.getInstance().toDataURL() + '=' }),
    });

    if (!response.ok) {
      alert('Error removing background');
      return;
    } else {
      alert('Background removed');
    }

    const data = await response.json();
    setImage(data.image);
    refreshComponent();
  };

  const handleBlur = async () => {
    console.log('Blurring with value', blurValue);
    const response = await fetch(`${import.meta.env.VITE_REACT_APP_API_URL}/blur`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        image: imageEditorRef.current.getInstance().toDataURL() + '=',
        value: blurValue,
        type: 'gaussian',
      }),
    });

    if (!response.ok) {
      alert('Error blurring');
      return;
    } else {
      alert('Blurred');
    }

    const data = await response.json();
    setImage(data.image);
    refreshComponent();
  };

  const handleObjectRemoval = async () => {
    if (imageEditorRef.current) {
      console.log('Getting selection dimensions');
      const coords = imageEditorRef.current.getInstance().getCropzoneRect();

      const response = await fetch(`${import.meta.env.VITE_REACT_APP_API_URL}/object-removal`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          image: imageEditorRef.current.getInstance().toDataURL() + '=',
          x0: coords.left,
          y0: coords.top,
          width: coords.width,
          height: coords.height,
        }),
      });

      if (!response.ok) {
        alert('Error removing object');
        return;
      } else {
        alert('Object removed');
      }

      const data = await response.json();
      setImage(data.image);
      refreshComponent();
    }
  };

  const handleDownload = () => {
    if (imageEditorRef.current) {
      const imageEditorInstance = imageEditorRef.current.getInstance();
      const dataURL = imageEditorInstance.toDataURL();
      const link = document.createElement('a');
      link.download = 'image.png';
      link.href = dataURL;
      link.click();
    }
  };

  const saveImage = async () => {
    if (imageEditorRef.current && user) {
      const imageEditorInstance = imageEditorRef.current.getInstance();
      const imageBase64 = imageEditorInstance.toDataURL();
      await saveProfileImage(user.email ?? user.uid, imageBase64);
    }
  };

  return (
    <LocalComponents.Container key={refreshKey}>
      <ImageEditor
        ref={imageEditorRef}
        includeUI={{
          loadImage: {
            path: imageBase64,
            name: 'image',
          },
        }}
        cssMaxHeight={screenHeight * 0.7}
        cssMaxWidth={screenWidth * 0.7}
        selectionStyle={{ cornerSize: 20, rotatingPointOffset: 70 }}
        usageStatistics={false}
      />
      <button
        onClick={handleDownload}
        style={{
          position: 'absolute',
          top: '84px',
          right: '16px',
          zIndex: 100,
          backgroundColor: '#fff',
          color: '#000',
          border: 'none',
          padding: '8px',
          borderRadius: '8px',
          cursor: 'pointer',
        }}>
        Download
      </button>
      {currentProfile?.isSubscribed && (
        <>
          <button
            style={{
              position: 'absolute',
              top: '124px',
              right: '16px',
              zIndex: 100,
              backgroundColor: '#fff',
              color: '#000',
              border: 'none',
              padding: '8px',
              borderRadius: '8px',
              cursor: 'pointer',
            }}
            onClick={saveImage}>
            Save Image
          </button>

          <button
            onClick={handleBackgroundRemoval}
            style={{
              position: 'absolute',
              top: '184px',
              right: '16px',
              zIndex: 100,
              backgroundColor: '#fff',
              color: '#000',
              border: 'none',
              padding: '8px',
              borderRadius: '8px',
              cursor: 'pointer',
            }}>
            Remove Background
          </button>
          <button
            onClick={handleBlur}
            style={{
              position: 'absolute',
              top: '244px',
              right: '16px',
              zIndex: 100,
              backgroundColor: '#fff',
              color: '#000',
              border: 'none',
              padding: '8px',
              borderRadius: '8px',
              cursor: 'pointer',
            }}>
            Blur
          </button>
          <input
            type='range'
            min='0'
            max='100'
            value={blurValue}
            onChange={(e) => setBlurValue(e.target.value)}
            style={{
              position: 'absolute',
              top: '284px',
              right: '16px',
              zIndex: 100,
              cursor: 'pointer',
            }}
          />
          <button
            onClick={handleBackgroundRemoval}
            style={{
              position: 'absolute',
              top: '344px',
              right: '16px',
              zIndex: 100,
              backgroundColor: '#fff',
              color: '#000',
              border: 'none',
              padding: '8px',
              borderRadius: '8px',
              cursor: 'pointer',
            }}>
            Remove object
          </button>
          <button
            onClick={handleObjectRemoval}
            style={{
              position: 'absolute',
              top: '404px',
              right: '16px',
              zIndex: 100,
              backgroundColor: '#fff',
              color: '#000',
              border: 'none',
              padding: '8px',
              borderRadius: '8px',
              cursor: 'pointer',
            }}>
            Remove selected object
          </button>
        </>
      )}
    </LocalComponents.Container>
  );
};

export default Editor;
