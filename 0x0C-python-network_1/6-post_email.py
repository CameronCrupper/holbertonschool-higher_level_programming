#!/usr/bin/python3
"""
takes in a URL and an email
sends a POST request to the URL
with the email as parameter
displays body of the response
"""

from sys import argv
import requests


if __name__ == "__main__":
    info = {'email': argv[2]}
    giveme = requests.post(argv[1], data=info)

    print(giveme.text)
