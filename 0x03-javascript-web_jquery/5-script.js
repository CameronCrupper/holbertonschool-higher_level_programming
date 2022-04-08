#!/usr/bin/node
const $element = $('ul.my_list');
const $NewElement = $('div#add_item');
$NewElement.on('click', () => {
  $element.append('<li>Item</li>');
});
