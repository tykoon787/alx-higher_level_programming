#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const path = require('path');

const len = argv.length;
if (len <= 2) {
  console.log(`Usage ${path.basename(argv[0])} <url>`);
} else {
  const completedTasks = {};
  const url = argv[2];
  // Get Request
  request.get(url, (err, response, body) => {
    if (err) console.log(err);
    else {
      // Parse into JS object
      const todos = JSON.parse(body);
      // Loop through each todo
      todos.forEach((task) => {
        // check if task is completed
        if (task.completed) {
          // check whether completedTasks object has a property, if so, add 1
          if (completedTasks[task.userId]) {
            completedTasks[task.userId] += 1;
            // Else, it means that we are meeting this userId for the first time, so value is 1
          } else {
            completedTasks[task.userId] = 1;
          }
        }
      });
      console.log(completedTasks);
    }
  });
}
