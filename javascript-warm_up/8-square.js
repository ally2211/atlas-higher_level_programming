#!/usr/bin/node
//  Write a script that prints 3 lines:

const number = parseInt(process.argv[2]);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let row = ''; // Start with an empty string for the row
    for (let j = 0; j < number; j++) {
      row += 'X'; // Add 'X' to the row string for each column
    }
    console.log(row);
  }
}
