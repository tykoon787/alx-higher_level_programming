#!/usr/bin/node
const path = require('path');
const fs = require('fs');
const { argv } = require('process');

const len = argv.length;
if (len <= 3) {
  console.log(`Usage: ${path.basename(argv[0])} <file_path> <string>`);
} else {
  const file = path.resolve(argv[2]);
  const data = argv[3];
  fs.writeFile(file, data, 'utf8', (err) => {
    if (err) console.log(err);
  });
}
