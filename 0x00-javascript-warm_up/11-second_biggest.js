#!/usr/bin/node
const len = process.argv.length;
const num = process.argv.slice(2).map(function (i) {
  return parseInt(i);
});
const max = Math.max.apply(Math, num);
const min = Math.min.apply(Math, num);
if (len > 3) {
  let j = 0;
  let i = 0;
  let secBig = min;
  for (; i < len; i++) {
    j = num[i];
    if (j > secBig && j < max) {
      secBig = j;
    }
  }
  console.log(secBig);
} else {
  console.log(0);
}
