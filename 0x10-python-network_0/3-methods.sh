#!/bin/bash
# To get all the methods of a server
curl -sI "$1" | grep -i '^Allow:' | awk '{$1=""; gsub(/^[ \t]+/, ""); print $0}'
