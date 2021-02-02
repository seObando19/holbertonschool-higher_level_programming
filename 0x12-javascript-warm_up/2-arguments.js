#!/usr/bin/node
// script that prints a message depending of the number of arguments passed

const pross = require('process');
const cant = pross.argv;

console.log(cant.length === 2 ? 'No argument' : 'Argument found');
