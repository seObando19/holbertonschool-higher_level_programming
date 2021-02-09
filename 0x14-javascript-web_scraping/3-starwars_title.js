#!/usr/bin/node

const request = require('request');
const process = require('process');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
const dataSearch = `${url}${id}`;
request(dataSearch, function (error, response, body) {
  if (error) console.log('Error:', error);
  console.log(JSON.parse(body).title);
});
