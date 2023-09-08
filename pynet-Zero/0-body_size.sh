#!/bin/bash
# to get the size of a response
curl -sI $1 | grep -i '^Content-Length:' | awk '{print $2}'
