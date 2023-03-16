#!/usr/bin/node
const [firstArg, secondArg] = process.argv.slice(2);
const num1 = parseInt(firstArg);
const num2 = parseInt(secondArg);

function add (num1, num2) {
  const result = num1 + num2;
  return result;
}
console.log(add(num1, num2));
