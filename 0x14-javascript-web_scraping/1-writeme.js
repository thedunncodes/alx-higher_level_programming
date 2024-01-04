#!/usr/bin/node
// Read contents in a file

const path = process.argv[2];
const data = process.argv[3];

const fs = require('fs');

fs.writeFile(path, data, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
  console.log('Success!');
});
