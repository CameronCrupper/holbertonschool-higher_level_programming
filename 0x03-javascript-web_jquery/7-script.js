#!/usr/bin/node
const uri = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const $character = $('div#character');
$.ajax({
  url: uri,
  dataType: 'json'
}).done((data) => {
  $character.text(data.name);
});
