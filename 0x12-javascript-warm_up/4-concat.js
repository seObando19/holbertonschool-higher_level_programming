#!/usr/bin/node
//  script that prints two arguments passed to it, in the following format: “ is ”

require('process');
const myArry = process.argv;

const val1 = myArry[2];
const val2 = myArry[3];

console.log(val1 + ' is ' + val2);
