#!/usr/bin/python3

"""
This Py script takes in a URL and an email address, sends a POST request
to the URL with the email as a parameter then displays the body of
the response
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
