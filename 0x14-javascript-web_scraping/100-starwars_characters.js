#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let all = JSON.parse(body).characters;
    for (let cha of all) {
      request(cha, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
