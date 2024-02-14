#!/usr/bin/node
const Squarex = require('./5-square');

class Square extends Squarex {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 1; i <= this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
