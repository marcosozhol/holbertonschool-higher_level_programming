#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + Process.argv[2];
request(url, function(error, response, body) {
  console.log(error || JSON.parse(body).title);
});
