#!/usr/bin/node
const request = require('request');
const path = require('path');
const { argv } = require('process');

const len = argv.length;
if (len <= 2) {
  console.log(`Usage: ${path.basename(argv[0])} <url>`);
} else {
  const url = argv[2];
  request.get(url, (err, res, body) => {
    if (err) console.log(err);
    else {
      console.log(`code: ${res.statusCode}`);
    }
  });
}
