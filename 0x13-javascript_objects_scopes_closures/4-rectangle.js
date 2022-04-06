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

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  } 

  double () {
    this.height = (this.height * 2);
    this.width = (this.width * 2);
  }
}
module.exports = Rectangle;
