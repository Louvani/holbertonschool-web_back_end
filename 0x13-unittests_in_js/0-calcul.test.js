const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('check output when parameters are okay', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(3.7, 1), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(3.7, 1.2), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(-1, -2), -3);
  });
  it('return NaN if arguments are incorrects', () => {
    assert.strictEqual(isNaN(calculateNumber()), true);
    assert.strictEqual(isNaN(calculateNumber(5)), true);
    assert.strictEqual(isNaN(calculateNumber('5', 'abc')), true);
    assert.strictEqual(isNaN(calculateNumber('5abc', '3')), true);
  });
});
