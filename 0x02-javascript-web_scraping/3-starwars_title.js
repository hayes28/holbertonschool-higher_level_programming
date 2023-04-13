#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.
// The first argument is the movie ID
// You must use the Star wars API with the endpoint http://swapi.co/api/films/:id
// You must use the module request
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (err, response, body) {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
