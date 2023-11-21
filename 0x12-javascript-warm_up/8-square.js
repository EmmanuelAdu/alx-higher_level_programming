#!/usr/bin/node
const a = process.argv[2];

if (!parseInt(a)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < a; i++) {
    let y = 0;
    let newString = '';

    while (y < a) {
      newString = newString + 'X';
      y++;
    }
    console.log(newString);
  }
}
