#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const webpage = process.argv[2];
const filePath = process.argv[3];

if (!webpage || !filePath) {
  console.log('Usage: <script> <URL> <file path>');
  process.exit(1);
}

request(webpage, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response && response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        //Failed to write file:
        console.error(err);
      }
    });
  } else {
    console.log('Request failed with status:', response && response.statusCode);
  }
});
