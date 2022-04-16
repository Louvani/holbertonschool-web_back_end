export default function cleanSet(set, startString) {
  let clean = '';
  if (!startString || !startString.length) return clean;
  set.forEach((value) => {
    if (value && value.startsWith(startString)) clean += `${value.slice(startString.length)}-`;
  });
  return clean.slice(0, clean.length - 1);
}
