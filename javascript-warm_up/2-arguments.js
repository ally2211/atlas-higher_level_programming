#!/usr/bin/node
// Subtracting the first two elements 
// which are the path and file

let numberOfArguments = process.argv.length - 2;

if (numberOfArguments === 1) {
    console.log("Argument found");
} else if (numberOfArguments > 1) {
    console.log("Arguments found");
} else {
    console.log("No argument");
}