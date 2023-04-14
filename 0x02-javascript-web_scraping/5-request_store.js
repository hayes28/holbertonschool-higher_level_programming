#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.
// The first argument is the URL to request.
// The second argument the file path to store the body response.
// The file must be UTF-8 encoded.
// You must use the module request.

const request = require('request');
const fs = require('fs');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
    if (err) throw err;
    console.log(`File saved to ${process.argv[3]}`); // backticks
  });
});
