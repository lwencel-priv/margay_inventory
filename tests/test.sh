#!/bin/bash
curl --header "Content-Type: application/json" \
  --request POST \
  -d @types.json \
  http://127.0.0.1:5000/type 

curl --header "Content-Type: application/json" \
  --request POST \
  -d @units.json \
  http://127.0.0.1:5000/unit 

curl --header "Content-Type: application/json" \
  --request POST \
  -d @items.json \
  http://127.0.0.1:5000/item 