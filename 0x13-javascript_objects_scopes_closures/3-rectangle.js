#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let cont = 1;
    while (cont <= (this.height)) {
      cont++;
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
