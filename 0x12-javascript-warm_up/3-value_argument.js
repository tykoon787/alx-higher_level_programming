#!/usr/bin/node
const [firstArg, ...restArgs] = process.argv.slice(2);

if (firstArg !== undefined) {
    console.log(firstArg);
} else {
    console.log('No argument');
}
