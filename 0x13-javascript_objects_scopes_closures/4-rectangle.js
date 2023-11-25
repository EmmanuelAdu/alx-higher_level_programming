#!/usr/bin/node
/**
 * Adding two new instance methods to class Rectangle
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

   // New Method
  rotate() {
    let a = 0;
    a = this.width;
    this.width = this.height;
    this.height = a;
   }

  // Second New Method
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
