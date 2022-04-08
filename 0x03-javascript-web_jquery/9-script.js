#!/usr/bin/node
$(document).ready(function () {
  const uri = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const $hello = $('div#hello');
  function fetch () {
    return $.get({
      url: uri,
      dataType: 'json'
    });
  }
  fetch().then((res) => {
    $hello.text(res.hello);
  });
});
