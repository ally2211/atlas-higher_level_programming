#!/usr/bin/node
//  print() that prints the rectangle using the character X
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (sideLength) {
    // A square is a rectangle with equal width and height
    super(sideLength, sideLength);
  }

  print () {
    if (this.width === 0 || this.height === 0) {
      console.log('Missing size');
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = ''; // Start with an empty string for the row
        for (let j = 0; j < this.width; j++) {
          row += 'X'; // Add 'X' to the row string for each column
        }
        console.log(row);
      }
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

// Exporting the class if you're using Node.js
// and want it to be accessible from other files
module.exports = Square;
