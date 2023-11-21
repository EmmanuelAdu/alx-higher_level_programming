#!/usr/bin/node
const a = process.argv[2];

if (!parseInt(a)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < a; i++) {
    console.log('C is fun');
  }
}
