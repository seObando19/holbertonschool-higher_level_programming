#!/usr/bin/node

const fs = require('fs');
const procees = require('process');
const request = require('request');

const url = procees.argv[2];
const file = procees.argv[3];

request(url, function (error, response, body) {
  if (error) console.log('Error:', error);
  fs.writeFile(file, body, 'utf-8', function (err) {
    if (err) return console.log(err);
  });
});
