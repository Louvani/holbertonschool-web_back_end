export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    const value = idx;
    /* eslint-disable-next-line no-param-reassign */
    array[array.indexOf(idx)] = appendString + value;
  }

  return array;
}
