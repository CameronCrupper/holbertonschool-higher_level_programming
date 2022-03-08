#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    giveme = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(giveme.text)))
    print('\t- content: {_content}'.format(_content=giveme.text))
