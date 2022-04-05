#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print (char = 'X') {
    for (let j = 0; j < this.height; j++) {
      let k = 0;
      for (; k < this.width; k++) {
        process.stdout.write(char);
      }
      if (k === this.width) {
        console.log('');
      }
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
