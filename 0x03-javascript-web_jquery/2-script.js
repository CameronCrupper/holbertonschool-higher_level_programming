#!/usr/bin/node
const $head = $('header');
const $redhead = $('div#red_header');
$redhead.on('click', function () {
    $head.css('color', '#FF0000');
});
