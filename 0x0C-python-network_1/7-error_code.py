#!/usr/bin/python3
"""
takes in a URL
send a request to the URL and displays
the body of the response
"""

from sys import argv
import requests


if __name__ == "__main__":
    giveme = requests.get(argv[1])

    if giveme.status_code >= 400:
        print('Error code:', giveme.status_code)
    else:
        print(giveme.text)
