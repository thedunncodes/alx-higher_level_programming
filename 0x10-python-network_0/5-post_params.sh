#!/bin/bash
# sends a POST request with some data/query string
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
