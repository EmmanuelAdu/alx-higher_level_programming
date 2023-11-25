#!/usr/bin/node
/**
 * Inherits from previous Square
 */
const prevSquare = require('./5-square');

class Square extends prevSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;

    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      for (let j = 0; j < this.width; j++) {
        myVar += myChar;
      }
      console.log(myVar);
    }
  }
}

module.exports = Square;
