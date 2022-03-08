#!/usr/bin/python3
"""
take in a URL and email
send a post request to the URL with email as parameter
and dispalys the body of the response(decoded in UTF-8)
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    data = urlencode({'email': argv[2]}).encode('ascii')
    giveme = Request(argv[1], data)
    with urlopen(giveme) as res:
        print(res.read().decode('utf-8'))
