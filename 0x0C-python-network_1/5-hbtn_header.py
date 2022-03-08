#!/usr/bin/python3
"""
takes in a URL
sends a request to the URL and displays the
value of the variable x-request-ID in
the response header
"""
from sys import argv
import requests


if __name__ == "__main__":
    giveme = requests.get(argv[1])

    print(giveme.headers.get('X-Request-Id'))
