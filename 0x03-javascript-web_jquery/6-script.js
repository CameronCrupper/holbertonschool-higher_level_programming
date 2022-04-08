#!/usr/bin/node
const $head = $('header');
const $new = $('div#update_header');
$new.on('click', () => {
  $head.text('New Header!!!');
});
