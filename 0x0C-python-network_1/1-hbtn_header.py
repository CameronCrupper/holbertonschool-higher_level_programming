#!/usr/bin/python3
"""
takes in a URL
sends a request to the URL and
displays the value of the x-request-id
variable found in the header response
"""
from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    giveme = Request(argv[1])
    with urlopen(giveme) as res:
        headers = res.info()
        print(headers.get('X-Request-Id'))
