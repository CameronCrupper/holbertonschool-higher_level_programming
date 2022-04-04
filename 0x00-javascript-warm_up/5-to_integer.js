#!/usr/bin/node
const test = parseInt(process.argv[2])
if (test) {
  console.log('My number: ' + test);
} else {
    console.log('Not a number');
}
