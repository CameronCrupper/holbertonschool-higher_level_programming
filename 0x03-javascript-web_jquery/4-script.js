#!/usr/bin/node
const $head = $('header');
const $togglehead = $('DIV#toggle_header');
$togglehead.on('click', () => {
  const current = $head.attr('class');
  if (current === 'green') {
    $head.toggleClass(`${current} red`);
  }
  if (current === 'red') {
    $head.toggleClass(`${current} green`);
  }
});
