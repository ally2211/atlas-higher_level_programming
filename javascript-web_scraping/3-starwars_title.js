#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];

if (!movieID) {
  console.log('Please provide a movie ID as an argument.');
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${movieID}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  try {
    const data = JSON.parse(body); // Convert the JSON response into an object
    console.log(data.title); // Print the title of the movie
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
