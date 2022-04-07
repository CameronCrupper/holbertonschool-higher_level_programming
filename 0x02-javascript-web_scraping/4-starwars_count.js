#!/usr/bin/node
const request = require('request');
const uri = process.argv[2];
let time = 0;
request(uri, function (_err, _res, body) {
  body = JSON.parse(body).results;
  for (let j = 0; j < body.length; j++) {
    const characters = body[j].characters;
    for (let k = 0; k < characters.length; k++) {
      const actor = characters[k];
      const Id = actor.split('/')[5];
      if (Id === '18') {
        time += 1;
      }
    }
  }
  console.log(time);
});
