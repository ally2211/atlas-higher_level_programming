#!/usr/bin/node
// Subtracting the first two elements
// which are the path and file

let counter = 0;


if (process.argv[2]) {
  console.log(process.argv[2]);
} else if (!process.argv[2]) {
  console.log('No Argument');
}
