#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2]; // The API URL is provided as a command-line argument

if (!apiUrl) {
  console.log('Please provide the Star Wars API URL as an argument.');
  process.exit(1);
}

// Function to fetch data from the provided URL
function fetchData(url, callback) {
  request(url, function (error, response, body) {
    if (!error && response.statusCode == 200) {
      const data = JSON.parse(body);
      callback(data);
    } else {
      console.error('Failed to fetch data:', error);
    }
  });
}

// Fetch the list of films
fetchData(apiUrl, function (data) {
  let count = 0; // Counter for films including Wedge Antilles

  // Iterate over each film
  const films = data.results;
  let completedRequests = 0;
  for (let i = 0; i < films.length; i++) {
    const film = films[i];
    
    // Check each character URL in the film
    film.characters.forEach((characterUrl) => {
      fetchData(characterUrl, function (characterData) {
        completedRequests++;
        
        // If the character is Wedge Antilles (ID 18)
        if (characterData.url.includes('/18/')) {
          count++;
        }

        // Ensure all requests are completed before printing the count
        if (completedRequests === films.reduce((acc, film) => acc + film.characters.length, 0)) {
          console.log(count);
        }
      });
    });
  }
});

