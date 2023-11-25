#!/usr/bin/node
/**
 * Printing the Rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      for (let j = 0; j < this.width; j++) {
	myVar += 'X';
      }
      console.log(myVar);
    }
  }
}

module.exports = Rectangle;
