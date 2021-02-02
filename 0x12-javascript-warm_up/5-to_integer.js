#!/usr/bin/node
// script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer

require('process');
const myArr = process.argv;

const dato = parseInt(myArr[2]);
if (Number.isInteger(dato)) {
  console.log('My number: ' + dato);
} else {
  console.log('Not a number');
}
