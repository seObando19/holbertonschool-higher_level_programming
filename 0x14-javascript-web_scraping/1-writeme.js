#!/usr/bin/node

const fs = require('fs');
const procees = require('process');

const file = procees.argv[2];
const text = procees.argv[3];

fs.writeFile(file, text, 'utf-8', function (err) {
  if (err) return console.log(err);
});
