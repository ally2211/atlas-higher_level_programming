#!/usr/bin/node
//  print() that prints the rectangle using the character X
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
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
}

// Exporting the class if you're using Node.js
// and want it to be accessible from other files
module.exports = Rectangle;
