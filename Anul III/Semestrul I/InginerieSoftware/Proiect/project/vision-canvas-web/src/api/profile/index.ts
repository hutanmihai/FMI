import { doc, getDoc, setDoc, updateDoc, arrayUnion, arrayRemove } from 'firebase/firestore';
import { db } from '../../utils/firebase';
import { Profile } from './types';

export const getProfile = async (key: string): Promise<Profile | null> => {
  const docRef = doc(db, 'profile', key);
  const docSnap = await getDoc(docRef);

  if (docSnap.exists()) {
    console.log('Document data:', docSnap.data());
    return docSnap.data() as Profile;
  } else {
    console.log('No such document!');
    return null;
  }
};

export const setProfile = async (key: string, profile: Profile): Promise<void> => {
  const docRef = doc(db, 'profile', key);
  await setDoc(docRef, profile, { merge: true });
};

export const setSubscribed = async (key: string, isSubscribed: boolean): Promise<void> => {
  const docRef = doc(db, 'profile', key);
  await setDoc(docRef, { isSubscribed }, { merge: true });
};

export const saveProfileImage = async (key: string, imageBase64: string): Promise<void> => {
  try {
    const docRef = doc(db, 'profile', key);
    await updateDoc(docRef, { images: arrayUnion(imageBase64) });
    alert('Image saved.');
  } catch (e) {
    console.log(e);
    alert('Error saving image.');
  }
};

export const getProfileImages = async (key: string): Promise<string[]> => {
  const docRef = doc(db, 'profile', key);
  const docSnap = await getDoc(docRef);

  if (docSnap.exists()) {
    const profile = docSnap.data() as Profile;
    return profile.images ?? [];
  } else {
    return [];
  }
};

export const deleteProfileImage = async (key: string, imageBase64: string): Promise<void> => {
  const docRef = doc(db, 'profile', key);
  await updateDoc(docRef, { images: arrayRemove(imageBase64) });
};
