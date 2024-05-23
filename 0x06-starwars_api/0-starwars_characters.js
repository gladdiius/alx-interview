#!/usr/bin/node

#!/usr/bin/node
// 0-starwars_characters.js
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character data:', charError);
        } else if (charResponse.statusCode !== 200) {
          console.error('Error fetching character data. Status Code:', charResponse.statusCode);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
