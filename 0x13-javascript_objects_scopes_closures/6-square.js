#!/usr/bin/node
const square = require('./4-rectangle');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      let cont = 1;
      while (cont <= (this.height)) {
        cont++;
        console.log('X'.repeat(this.width));
      }
    } else {
      let cont2 = 1;
      while (cont2 <= (this.height)) {
        cont2++;
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
