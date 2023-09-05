#!/usr/bin/python3

"""Same as Task 3"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    r = requests.post(url, data=values)
    print(r.text)
