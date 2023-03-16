#!/usr/bin/node
const [firstArg] = process.argv.slice(2);

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n < 0) {
    return NaN;
  } else {
    let result = 1;
    for (let i = n; i > 0; i--) {
      result *= i;
    }
    return result;
  }
}
console.log(factorial(firstArg));
