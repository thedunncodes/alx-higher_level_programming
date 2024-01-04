#!/usr/bin/node
// Read contents in a file

const path = process.argv[2];

const fs = require('fs');

fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
