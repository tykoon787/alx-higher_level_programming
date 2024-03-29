#!/usr/bin/node
const SquareClass = require('./5-square');

class Square extends SquareClass {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
