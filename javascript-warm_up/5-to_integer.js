#!/usr/bin/node
//  a script that prints My number: <first argument converted in integer>
const arg = process.argv[2];
const number = parseInt(arg, 10);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
