#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

// Exporting the class if you're using Node.js
// and want it to be accessible from other files
module.exports = Rectangle;
