#!/usr/bin/node
// script that computes and prints a factorial

require('process');

const data = process.argv;
const value = parseInt(data[2]);

function myRecursive (value) {
  if (isNaN(value) || value === 1 || value === 0) {
    return (1);
  }

  return (value * myRecursive(value - 1));
}
console.log(myRecursive(value));
