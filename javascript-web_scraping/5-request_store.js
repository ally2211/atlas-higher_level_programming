#!/usr/bin/node
const http = require('http');
const fs = require('fs');
const webpage = process.argv[2];
const filewrite = process.argv[3];

if (!filewrite) {
  // console.log('Please provide a file path as an argument.');
  process.exit(1);
}
if (!webpage) {
  console.log('Please provide a webpage URL as the first argument.');
  process.exit(1);
}

http.get(webpage, (response) => {
  let data = '';
  // A chunk of data has been received.
  response.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  response.on('end', () => {
    console.log(data);
    fs.writeFile(filewrite, data, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
      // console.log('File has been written successfully');
    });
  });
}).on('error', (err) => {
  console.log('Error: ' + err.message);
});
