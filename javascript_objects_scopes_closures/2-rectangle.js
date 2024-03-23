#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
          this.width = w;
          this.height = h;
        } else {
          // If w or h is not a positive integer, create an empty object.
          // This step is technically redundant in JavaScript because
          // an object of Rectangle without width and height is essentially empty,
          // but it's here to explicitly follow the requirement.
          return {}; // This attempt won't affect the instantiation of the class in standard JavaScript.
        }
  }
  
  // Exporting the class if you're using Node.js
  // and want it to be accessible from other files
  module.exports = Rectangle;
  