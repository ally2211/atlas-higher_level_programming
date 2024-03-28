#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
const txtwrite = process.argv[3];

if (!path) {
  // console.log('Please provide a file path as an argument.');
  process.exit(1);
}

fs.writeFile(path, txtwrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
  // console.log('File has been written successfully');
});
