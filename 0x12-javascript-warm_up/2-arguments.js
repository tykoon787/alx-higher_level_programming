#!/usr/bin/node
const { argv } = require('process');
const len = argv.length;
if (len <= 2) {
  console.log('No argument');
} else if (len === 3) {
  console.log('Argument found');
} else if (len > 2) {
  console.log('Arguments found');
}