#!/usr/bin/node
// script that prints the addition of 2 integers

require('process');

function add (a, b) {
  console.log(a + b);
}

const data = process.argv;
const val1 = parseInt(data[2]);
const val2 = parseInt(data[3]);

add(val1, val2);
