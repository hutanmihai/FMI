import { LocalComponents } from './styled';
import { useContext, useEffect, useState } from 'react';
import { convertFileToBase64 } from '../../utils';
import { useNavigate } from 'react-router-dom';
import { ImageContext } from '../../providers/ImageProvider/context.ts';
import { deleteProfileImage, getProfileImages } from '../../api/profile';
import { AuthContext } from '../../providers/AuthProvider/context.ts';
import './index.css';

const Dashboard = () => {
  const navigate = useNavigate();

  const { setImage } = useContext(ImageContext);
  const { user } = useContext(AuthContext);

  const [profileImages, setProfileImages] = useState<string[]>([]);

  useEffect(() => {
    if (user) {
      getProfileImages(user.email ?? user.uid).then(setProfileImages);
    }
  }, [user]);

  const handleImageClick = (imageBase64: string) => {
    setImage(imageBase64);
    navigate('/editor');
  };

  const handleDownloadClick = (imageBase64: string) => {
    const link = document.createElement('a');
    link.href = imageBase64;
    link.download = 'image.png';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const handleDeleteClick = async (imageBase64: string) => {
    if (user) {
      await deleteProfileImage(user.email ?? user.uid, imageBase64);
      setProfileImages(profileImages.filter((image) => image !== imageBase64));
    }
  };

  const handleUpload = async (e: any) => {
    e.preventDefault();
    const file = e.target.files[0];

    if (file.size > 5 * 1024 * 1024) {
      alert('The uploaded image is too big. Please upload an image smaller than 5MB.');
      return;
    }
    const fileAsBase64 = await convertFileToBase64(file);

    setImage(fileAsBase64);
    navigate('/editor');
  };

  return (
    <LocalComponents.Container>
      <LocalComponents.Button onChange={handleUpload} htmlFor='file'>
        Upload photo
        <input type='file' id='file' hidden />
      </LocalComponents.Button>
      <div className={'dashboard-images-wrapper'}>
        {profileImages.map((image, index) => (
          <div key={index} className='dashboard-image-container'>
            <img
              src={image}
              alt={`profile ${index}`}
              className='dashboard-image'
              onClick={() => handleImageClick(image)}
            />
            <button className='dashboard-image-download' onClick={() => handleDownloadClick(image)}>
              Download
            </button>
            <button className='dashboard-image-delete' onClick={() => handleDeleteClick(image)}>
              Delete
            </button>
          </div>
        ))}
      </div>
    </LocalComponents.Container>
  );
};

export default Dashboard;
