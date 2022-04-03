import { signUpUser } from './4-user-promise.js';
import { uploadPhoto } from './5-photo-reject.js';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const user = await signUpUser(firstName, lastName);
  let photo;
  try {
    photo = await uploadPhoto(fileName);
  } catch (error) {
    photo = error.toString();
  }
  return [
    { value: user, status: 'fulfilled' },
    { value: photo, status: 'rejected' },
  ];
}
