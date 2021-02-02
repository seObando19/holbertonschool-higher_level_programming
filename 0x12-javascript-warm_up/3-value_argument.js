#!/usr/bin/node
// script that prints a message depending of the number of arguments passed

const pross = require('process');
const myArr = pross.argv;

if (!myArr[2]) {
  console.log('Argument found');
} else {
  console.log(myArr[2]);
}
