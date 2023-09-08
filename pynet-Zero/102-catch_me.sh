#!/bin/bash
# send a request to a specified URL
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
