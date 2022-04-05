#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }
  
  print () {
    for (let j = 0; j < this.height; j++) {
      let k = 0;
      for (; k < this.width; k++) {
        process.stdout.write('X');
      }
      if (k === this.width) {
        console.log('');
      }
    }
  }
};
