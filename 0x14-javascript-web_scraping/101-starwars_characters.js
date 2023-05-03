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
      const promises = []; // create an array to store the promises returned by requests
      // For each character, perform a request and store the promise in the array
      characters.forEach((person) => {
        const promise = new Promise((resolve, reject) => {
          request.get(person, (personErr, personRes, personBody) => {
            if (personErr) reject(personErr);
            else {
              // Get name of person
              const name = JSON.parse(personBody).name;
              resolve(name); // resolve the promise with the person's name
            }
          });
        });
        promises.push(promise); // push the promise into the array
      });

      Promise.all(promises) // wait for all promises to resolve
        .then((names) => {
          // names is an array of all the resolved promises
          names.forEach((char) => {
            console.log(char);
          });
        })
        .catch((err) => {
          console.log(err);
        });
    }
  });
}
