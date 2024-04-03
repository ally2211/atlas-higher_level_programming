#!/usr/bin/node
$(document).ready(function() {
    // Add click event listener to div#add_item
    $('#update_header').click(function() {
        // change text of header
        $('header').text('New Header!!!');
    });
});
