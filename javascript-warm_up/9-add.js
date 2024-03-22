#!/usr/bin/node
//  Write a script that prints 3 lines:

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  if (!isNaN(a) & !isNaN(b)) {
    console.log(a + b);
  }
  else if (!isNaN(a)) {
    console.log(a);
  }
  else {
    console.log(a);
  }
}
add(a, b);
