#!/usr/bin/node
// Searches by ID in an api data

const url = process.argv[2];
const request = require('request');

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
            if (cast[actor][i].includes(18)) {
              count += 1;
            }
          }
        }
      }
    }
    console.log(count);
  }
});
