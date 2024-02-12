#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  for (let row = 0; row < size; row++) {
    let output = '';
    for (let col = 0; col < size; col++) {
      output += 'X';
    }
    console.log(output);
  }
}
