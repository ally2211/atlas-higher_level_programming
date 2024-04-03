#!/usr/bin/node
$(document).ready(function() {
    // Use the fetch API to retrieve title data
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
        .then(response => response.json()) // Parse the JSON from the response
        .then(data => {
            data.results.forEach(function(movie) {
                // Use jQuery to append each movie title to UL#list_movies
                $('ul#list_movies').append('<li>' + movie.title + '</li>');
            });
        })
        .catch(error => console.error('Error fetching data:', error)); // Log any errors to the console
});