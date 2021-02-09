#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) console.log('Error:', error);
  const taskCompleted = {};
  const res = JSON.parse(body);
  for (const i in res) {
    const task = res[i];
    const user = res[i].userId;
    if (task.completed === true) {
      if (taskCompleted[user] === undefined) {
        taskCompleted[user] = 1;
      } else {
        taskCompleted[user] += 1;
      }
    }
  }
  console.log(taskCompleted);
});
