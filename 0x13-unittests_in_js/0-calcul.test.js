const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

desccribe('calculate Number', () => {
  it('check output when parameters are okay'), () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(3.7, 1), 5);
    assert.strictEqual(calculateNumber(1.7, 3), 5);
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(-1, -2), -3);
  }
  it('return NaN if arguments are incorrects'), () => {
    assert.strictEqual(isNaN(calculateNumber()), true);
    assert.strictEqual(isNaN(calculateNumber(1)), true);
  }
});
