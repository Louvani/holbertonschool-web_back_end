export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  set size(newSize) {
    if (typeof newSize !== 'number') {
      throw TypeError('Size must be a number');
    }
    this._size = newSize;
  }

  set location(newLocation) {
    if (typeof newLocation !== 'string') {
      throw TypeError('Location must be a string');
    }
    this._location = newLocation;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'number') {
      return this._size;
    }
    return this._location;
  }
}
