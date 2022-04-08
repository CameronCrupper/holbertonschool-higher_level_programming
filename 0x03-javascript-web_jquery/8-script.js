#!/usr/bin/node
const uri = 'https://swapi-api.hbtn.io/api/films/?format=json';
const $movies = $('ul#list_movies');
$.ajax({
  url: uri,
  dataType: 'json'
}).done((data) => {
  const movie = data.results;
  for (let j = 0; j < movie.length; j++) {
    const title = movie[j].title;
    const element = `<li>${title}`;
    $movies.append(element);
  }
});
