#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  get size () {
    return this.width;
  }

  set size (value) {
    this.width = value;
    this.height = value;
  }
}

module.exports = Square;
