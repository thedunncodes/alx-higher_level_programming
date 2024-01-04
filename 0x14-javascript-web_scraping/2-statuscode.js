#!/usr/bin/node
// gets status code of a web url

const url = process.argv[2];

const request = require('request');

request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
