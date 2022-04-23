import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const get = promisify(client.get).bind(client);

(async () => {
  client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
  client.on('connect', () => console.log('Redis client connected to the server'));
})();

async function setNewSchool(schoolName, value) {
  await client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  try {
    const school = await get(schoolName);
    console.log(school);
  } catch (error) {
    console.log(error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
