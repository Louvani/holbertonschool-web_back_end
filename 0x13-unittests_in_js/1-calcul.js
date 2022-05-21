const calculateNumber = (type, a, b) => {

  const operations ={
    'SUM': (a, b)  => Math.round(a) + Math.round(b),
    'SUBTRACT': (a, b)  => Math.round(a) + Math.round(b),
    'DIVIDE': (a, b)  => {
      if (b === 0) {
        return "Error";
      }
      return Math.round(a) / Math.round(b);
    },
  }
};

module.exports = calculateNumber;
