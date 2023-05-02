#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const fs = require('fs');
const path = require('path');

const len = argv.length;
if (len <= 3) {
  console.log(`Usage: ${path.basename(argv[0])} <url> <file>`);
} else {
  const url = argv[2];
  const file = argv[3];

  request.get(url, (err, response, body) => {
    if (err) console.log(err);
    else {
      fs.writeFile(file, body, 'utf8', (err) => {
        if (err) console.log(err);
      });
    }
  });
}
