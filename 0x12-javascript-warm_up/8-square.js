#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let num = parseInt(process.argv[2]); num > 0; num--) {
    let output = '';
    for (let num = parseInt(process.argv[2]); num > 0; num--) {
      output += 'x';
    }
    console.log(output);
  }
}
