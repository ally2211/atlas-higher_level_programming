#!/usr/bin/node
//  print() that prints the rectangle using the character X
const Square1 = require('./5-square');
class Square extends Square1 {
  charPrint (x) {
    if (this.width === 0 || this.height === 0) {
      console.log('Missing size');
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = ''; // Start with an empty string for the row
        for (let j = 0; j < this.width; j++) {
          if (x === undefined) {
            row += 'X';
            // Add 'X' to the row string for each column
          } else {
            row += x;
          }
        }
        console.log(row);
      }
    }
  }
}

// Exporting the class if you're using Node.js
// and want it to be accessible from other files
module.exports = Square;
