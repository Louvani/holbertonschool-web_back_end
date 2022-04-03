import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  const obj = {};
  try {
    obj.photo = uploadPhoto();
    obj.user = createUser();
  } catch (error) {
    obj.photo = null;
    obj.user = null;
  }
  return obj;
}
