#!/usr/bin/python3
const request = require('request');
let url = 'https://swapi-api.hbtn.io/api/films/' + ProcessingInstruction.argv[2];
request(url, function(error, response, body) {
  console.log(error || JSON.parse(body).title);
});