#!/usr/bin/node
const fs = require('fs');
const path = require('path');
const { argv } = require('node:process');

const len = argv.length;
if (len <= 2) {
  console.log(`Usage: ${path.basename(argv[1])} <file path>`);
} else {
  const file = path.resolve(argv[2]);
  fs.readFile(file, 'utf8', (err, data) => {
    if (err) console.log('Error', err);
    else console.log(data);
  });
}
