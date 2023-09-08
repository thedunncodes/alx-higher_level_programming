#!/bin/bash
# Displays status code of the response of the URL passed in as argument
curl -s -o /dev/null -w "%{http_code}" "$1"
