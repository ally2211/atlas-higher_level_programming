#!/usr/bin/node
$(document).ready(function() {
    // Use jQuery to add click event listener to the div#red_header
    $('#red_header').click(function() {
        // When div#red_header is clicked, change the text color of the <header> to red
        $('header').css('color', '#FF0000');
    });
});
