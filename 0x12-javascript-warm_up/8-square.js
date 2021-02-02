#!/usr/bin/node
// script that prints a square

require('process');
const cantPrint = parseInt(process.argv[2]);

if (Number.isInteger(cantPrint)) {
  for (let i = 0; i < cantPrint; i++) {
    console.log('X'.repeat(cantPrint));
  }
} else {
  console.log('Missing size');
}
