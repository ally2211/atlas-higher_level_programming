#!/usr/bin/node
$(document).ready(function() {
    // Add click event listener to div#toggle_header
    $('#toggle_header').click(function() {
        // Toggle between 'red' and 'green' classes on the <header>
        $('header').toggleClass('red green');
    });
});
