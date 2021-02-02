#!/usr/bin/node
// script that prints a message depending of the number of arguments passed

require('process');
const cant = process.argv;

if (cant.length === 2) {
  console.log('No argument');
} else if (cant.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
