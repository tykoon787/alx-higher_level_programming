#!/usr/bin/node
const fs = require('fs');
const path = require('path');
const { argv } = require('process');

const len = argv.length;
if (len <= 2) {
  console.log(`Usage: ${path.basename(argv[1])} <file path>`);
} else {
  const file = path.resolve(argv[2]);
  fs.readFile(path.basename(file), 'utf8', (err, data) => {
    if (err) console.log(err);
    else console.log(data);
  });
}
