#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) console.log('Error:', error);

  const res = JSON.parse(body).results;
  let cant = 0;
  for (const index in res) {
    const character = res[index].characters;
    for (const i in character) {
      if (character[i].includes('18')) {
        cant++;
      }
    }
  }
  console.log(cant);
});
