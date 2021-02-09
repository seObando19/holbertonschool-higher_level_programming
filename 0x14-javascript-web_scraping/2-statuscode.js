#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) console.log('Error:', error);
  console.log('code:', response.statusCode);
});
