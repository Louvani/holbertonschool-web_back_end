import promptSync from 'prompt-sync';

const prompt = promptSync();

const name = prompt('Welcome to Holberton School, what is your name?\n');
console.log('Your name is: ', name);

process.on('exit', () => {
  process.stdout.write('This important software is now closing\n');
});
