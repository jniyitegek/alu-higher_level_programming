#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const films = JSON.parse(body).results;
    const wedgeAntillesId = '18';
    const count = films.filter(film =>
      film.characters.some(character => character.includes(wedgeAntillesId))
    ).length;

    console.log(count);
  } catch (err) {
    console.error('Error parsing JSON:', err);
  }
});
