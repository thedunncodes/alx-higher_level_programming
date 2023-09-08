#!/usr/bin/python3

"""This takes your Github credentials
and uses the Github API to display your id"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = argv[1]
    password = argv[2]
    response = requests.get(url, auth=(user, password))
    print(response.json().get('id'))
