#!/usr/bin/node
$(document).ready(function() {
    // Add click event listener to div#red_header
    $('#red_header').click(function() {
        // Add the 'red' class to the <header> element
        $('header').addClass('red');
    });
});
