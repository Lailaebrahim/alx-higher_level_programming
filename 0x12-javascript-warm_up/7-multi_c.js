#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let num = parseInt(process.argv[2]); num > 0; num--) {
    console.log('C is fun');
  }
}
