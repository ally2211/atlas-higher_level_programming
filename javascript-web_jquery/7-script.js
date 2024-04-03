#!/usr/bin/node
$(document).ready(function() {
    // Use the fetch API to retrieve character data
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
        .then(response => response.json()) // Parse the JSON from the response
        .then(data => {
            // Use jQuery to set the text of div#character to the character's name
            $('#character').text(data.name);
        })
        .catch(error => console.error('Error fetching data:', error)); // Log any errors to the console
});
