#!/usr/bin/python3
"""
takes in a URL
send a request to the URL and displays the body
of the response(decoded in utf-8)
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError


if __name__ == "__main__":
    giveme = Request(argv[1])
    try:
        with urlopen(giveme) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as ex:
        print('Error code:', ex.code)
