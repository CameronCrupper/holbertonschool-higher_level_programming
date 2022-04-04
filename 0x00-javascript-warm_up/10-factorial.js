#!/usr/bin/node
function factorial (i) {
  if (i === 0 || isNaN(i)) {
    return 1;
  }
  return i * factorial(i - 1);
}
const i = parseInt(process.argv[2]);
console.log(factorial(i));
