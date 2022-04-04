#!/usr/bin/node
const square = parseInt(process.argv[2]);
if (square) {
  for (let i = 0; i < square; i++) {
    let j = 0;
    for (; j < square; j++) {
      process.stdout.write('X');
    }
    if (j === square) {
      console.log('');
    }
  }
} else {
  console.log('Missing size');
}
