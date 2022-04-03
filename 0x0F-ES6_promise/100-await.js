import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  const obj = {};
  try {
    Object.assign(obj, { photo: uploadPhoto(), user: createUser() });
  } catch (error) {
    Object.assign(obj, { photo: null, user: null });
  }
  return obj;
}
