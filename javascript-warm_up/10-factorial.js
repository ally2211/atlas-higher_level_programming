#!/usr/bin/node
//  script that computes and prints a factorial

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1; // Base case: factorial of 0 or 1 is 1
  } else {
    return n * factorial(n - 1); // Recursive case: n! = n * (n-1)!
  }
}

const number = parseInt(process.argv[2], 10);

if (isNaN(number)) {
  console.log(`${factorial(0)}`);
}

console.log(`${factorial(number)}`);
