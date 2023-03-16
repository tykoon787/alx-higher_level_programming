#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      Object.assign(this, {});
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width || !this.height) {
      console.log('');
      return;
    }
    let rectangleStr = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rectangleStr += 'X';
        if (j < this.width - 1) {
          rectangleStr += '';
        }
      }
      if (i < this.height - 1) {
        rectangleStr += '\n';
      }
    }
    console.log(rectangleStr);
  }

  rotate () {
    if (!this.width || !this.height) {
      console.log('');
      return;
    }
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    if (!this.width || !this.height) {
      console.log('');
      return;
    }
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
