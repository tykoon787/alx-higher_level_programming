#!/usr/bin/node
const { argv } = require('process');
const path = require('path');
const request = require('request');

// Variables
const len = argv.length;
let count = 0;

// Check Length
if (len <= 2) {
  console.log(`Usage: ${path.basename(argv[0])} <url>`);
} else {
  const url = argv[2];
  // Make request
  request(url, (err, responose, body) => {
    if (err) console.log(err);
    else {
      // Parse body into results, returns a result object
      const results = JSON.parse(body).results;
      // Loop through eaech result to get characters
      for (let i = 0; i < results.length; i++) {
        const resultObject = results[i];
        const charObj = resultObject.characters;
        // Loop through each characters to check if the value contains '18'
        for (let j = 0; j < charObj.length; j++) {
          if (charObj[j].includes('18')) {
            count = count + 1;
          }
        }
      }
      console.log(count);
    }
  });
}
