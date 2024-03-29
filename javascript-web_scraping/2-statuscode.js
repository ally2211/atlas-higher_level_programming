#!/usr/bin/node
const request = require('request');
const urlpath = process.argv[2];

if (!urlpath) {
  // console.log('Please provide a URL path as an argument.');
  process.exit(1);
}

request(urlpath, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response && response.statusCode);
});
