#!/usr/bin/node
$(document).ready(function() {
    // Use the fetch API to retrieve greeting data
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json()) // Parse the JSON from the response
        .then(data => {
            // Use jQuery to set the text of div#hello to the greeting
            $('#hello').text(data.hello);
        })
        .catch(error => console.error('Error fetching data:', error)); // Log any errors to the console
});
