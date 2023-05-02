#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const path = require('path');

const len = argv.length;
if (len <= 2) {
  console.log(`Usage: ${path.basename(argv[0])} <id>`);
} else {
  const id = argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  request.get(url, (err, response, body) => {
    if (err) console.log(err);
    else {
      const data = JSON.parse(body);
      console.log(data.title);
    }
  });
}
