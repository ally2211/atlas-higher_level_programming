#!/usr/bin/node
const request = require('request');
const charID = 18;
//const url = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/people/${charID}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  try {
    const data = JSON.parse(body);
    // Convert the JSON response into an object
    const numberOfFilms = data.films.length;
    console.log(numberOfFilms);
    // console.log(data.films); // Print the title of the movie
  } catch (parseError) {
    console.error(parseError);
  }
});