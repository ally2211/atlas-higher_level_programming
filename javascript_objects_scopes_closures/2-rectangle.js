#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } 
  }
}
// Exporting the class if you're using Node.js
// and want it to be accessible from other files
module.exports = Rectangle;
