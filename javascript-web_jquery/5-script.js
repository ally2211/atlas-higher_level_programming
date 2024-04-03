#!/usr/bin/node
$(document).ready(function() {
    // Add click event listener to div#add_item
    $('#add_item').click(function() {
        // Append a new <li> element with the content "Item" to <ul class="my_list">
        $('ul.my_list').append('<li>Item</li>');
    });
});
