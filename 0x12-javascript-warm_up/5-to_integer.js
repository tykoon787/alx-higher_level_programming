#!/usr/bin/node
const [firstArg] = process.argv.slice(2);

if (parseInt(firstArg)) {
    console.log(`My Number: ${parseInt(firstArg)}`);
} else {
    console.log('Not a number');
}
