#!/bin/bash
# Displays the body of the response of a JSON POST request
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
