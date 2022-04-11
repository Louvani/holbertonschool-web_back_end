const fs = require('fs');

function countStudents(path) {
  try {
    const rawData = fs.readFileSync(path, { encoding: 'utf8' });
    const data = rawData.split('\n');
    const filtered = data.filter((items) => items !== '').map((item) => item.split(',')).shift();
    console.log('Number of students: ', filtered.length);
    const db = {};
    for (const student of filtered) {
      const keys = Object.keys(db);
      if (keys.includes(student[3])) {
        db[student[3]].push(student[0]);
      } else {
        db[student[3]] = [student[0]];
      }
    }
    const keysFinal = Object.keys(db);
    keysFinal.forEach((field) => {
      console.log(`Number of students in ${field}: ${db[field].length}. List: ${db[field].join(', ')}`);
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
