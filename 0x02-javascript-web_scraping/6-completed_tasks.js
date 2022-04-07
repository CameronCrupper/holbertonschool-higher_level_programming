#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (_err, _res, body) {
  if (_err) {
    console.log(_err);
  } else {
    const tasks = {};
    body = JSON.parse(body);
    for (let j = 0; j < body.length; j++) {
      const userId = body[j].userId;
      const completed = body[j].completed;
      if (completed && !tasks[userId]) {
        tasks[userId] = 0;
      }
      if (completed) ++tasks[userId];
    }
    console.log(tasks);
  }
});
