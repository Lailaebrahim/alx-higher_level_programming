#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let max = Number.MIN_VALUE;
  let secondMax = Number.MIN_VALUE;
  for (let i = 0; i < process.argv.length; i++) {
    const element = process.argv[i];
    if (element > max) {
      secondMax = max;
      max = element;
    } else if (element < max && element > secondMax) {
      secondMax = element;
    }
  }
  console.log(secondMax);
}
