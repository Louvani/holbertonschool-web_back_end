export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  // Getters
  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  // Setters
  set name(newName) {
    if (typeof newName !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = newName;
  }

  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw TypeError('Code must be a string');
    }
    this._code = newCode;
  }

  // return the attributes in the following format name (code).
  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
