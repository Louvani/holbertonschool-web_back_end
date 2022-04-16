export default function groceriesList() {
  const list = [
    ['Apples', 10], ['Tomatoes', 10], ['Pasta', 1], ['Rice', 1], ['Banana', 5]
  ];
  const grocery = new Map(list);
  return grocery;
}
