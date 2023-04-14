#!/usr/bin/node
// Script that computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// Only print users with completed task
// You must use the module request

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) throw err;
  const tasks = JSON.parse(body);
  const dict = {};
  for (const task of tasks) {
    if (task.completed) {
      if (dict[task.userId]) {
        dict[task.userId] += 1;
      } else {
        dict[task.userId] = 1;
      }
    }
  }
  console.log(dict);
});
