#!/usr/bin/node
// script that searches the second
// biggest integer in the list of arguments.

const numberOfArguments = process.argv.length - 2;

if (numberOfArguments === 0 || numberOfArguments === 1) {
  console.log(0);
} else {
  let myArray = [];
  for (let i = 0; i < numberOfArguments; i++) {
    myArray[i] = process.argv[i + 2];
    console.log(myArray[i]);
}
// Sort the array in ascending order and then reverse it to make it descending
myArray.sort((a, b) => a - b).reverse();

// Check if there are at least two unique elements
const uniqueElements = [...new Set(myArray)];
console.log(uniqueElements[1]);
// Print the second highest element
}
