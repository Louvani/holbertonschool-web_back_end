export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw Error('Cannot process');
  for (const idx of map) if (idx[1] === 1) map.set(idx[0], 100);
  return map;
}
