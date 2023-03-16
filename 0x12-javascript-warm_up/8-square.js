#!/usr/bin/node
const [firstArg] = process.argv.slice(2);
let num = parseInt(firstArg);

if (parseInt(firstArg)){
    for (let width = num; width > 0; width--){
        let row = '';
        for (let height = num; height > 0; height--){
            row += 'x';
        }
        console.log(row);
    }
} else {
    console.log('Missing number of occurences');
}
