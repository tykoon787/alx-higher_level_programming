#!/usr/bin/node
const { argv } = require('process');
const path = require('path');
const request = require('request');

const len = argv.length;

// Check args
if (len <= 2) {
  console.log(`Usage: ${path.basename(argv[0])} <movie_Id>`);
} else {
  // Variables
  const filmId = argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
  // Make Request
  request.get(url, (err, respnse, body) => {
    if (err) console.log(err);
    else {
      // Retrieve characters (urls)
      const characters = JSON.parse(body).characters;
      // For each character, perfom request
      characters.forEach((person) => {
        request.get(person, (personErr, personRes, personBody) => {
          if (err) console.log(personErr);
          else {
            // Get name of person
            const name = JSON.parse(personBody).name;
            console.log(name);
          }
        });
      });
    }
  });
}
