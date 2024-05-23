#!/usr/bin/node
# get characters from api

get_movie_data() {
  movie_id=$1
  response=$(curl -s "https://swapi.dev/api/films/$movie_id/")
  if [[ $(echo "$response" | jq -r '.detail') == "Not found" ]]; then
    echo "Error: Movie ID $movie_id not found."
    exit 1
  else
    echo "$response"
  fi
}

get_character_name() {
  character_url=$1
  response=$(curl -s "$character_url")
  character_name=$(echo "$response" | jq -r '.name')
  echo "$character_name"
}

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <Movie ID>"
  exit 1
fi

movie_id=$1
movie_data=$(get_movie_data "$movie_id")
character_urls=$(echo "$movie_data" | jq -r '.characters[]')

for url in $character_urls; do
  get_character_name "$url"
done
