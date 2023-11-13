#!/usr/bin/node
// Prints first arg
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
