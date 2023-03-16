#!/usr/bin/node
const [firstArg] = process.argv.slice(2);

function factorial(n) {
  if (isNaN(n)) {
    return 1;
  } else if (n < 0) {
    return NaN;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(firstArg));
