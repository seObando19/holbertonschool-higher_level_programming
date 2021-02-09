#!/usr/bin/node

const fs = require('fs');
const procees = require('process');

const file = procees.argv[2];
fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
