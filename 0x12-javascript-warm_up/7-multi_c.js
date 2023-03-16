#!/usr/bin/node
const [firstArg] = process.argv.slice(2);
let num = parseInt(firstArg);

if (parseInt(firstArg)) {
  while (num > 0) {
    console.log('C is fun');
    num = num - 1;
  }
} else {
  console.log('Missing number of occurrences');
}
