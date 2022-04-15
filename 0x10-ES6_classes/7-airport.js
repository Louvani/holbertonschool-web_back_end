export default class Airport {
  constructor(name, code) {
    this.name = name;
    this.code = code;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw TypeError('Name must bue a string');
    }
    this._name = newName;
  }

  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw TypeError('Code must bue a string');
    }
    this._code = newCode;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
