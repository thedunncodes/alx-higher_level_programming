#!/usr/bin/node
// Searches by ID in an api data

const id = process.argv[2];
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const targetstr = `https://swapi-api.alx-tools.com/api/people/${id}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;
    for (const cast of data.results) {
      for (const actor in cast) {
        if (actor === 'characters') {
          for (let i = 0; i < cast[actor].length; i++) {
            if (cast[actor][i] === targetstr) {
              count += 1;
            }
          }
        }
      }
    }
    console.log(count);
  }
});
