#!/usr/bin/node
// script that prints x times “C is fun”

require('process');
const cantPrint = parseInt(process.argv[2]);

if (Number.isInteger(cantPrint)) {
  for (let i = 0; i < cantPrint; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
