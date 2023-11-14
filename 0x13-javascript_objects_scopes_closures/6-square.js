#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        if (c !== undefined) {
          const Char = c;
          row += Char;
        } else {
          const Char = 'X';
          row += Char;
        }
      }
      console.log(row);
    }
  }
}

module.exports = Square;
