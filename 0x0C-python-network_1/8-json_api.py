#!/usr/bin/python3
"""
takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''
    try:
        url = 'http://0.0.0.0:5000/search_user'
        info = {'q': q}
        giveme = requests.post(url, info).json()
        if {'id', 'name'} <= giveme.keys():
            print('[{id}] {name}'.format(id=giveme.get('id'), name=giveme.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
