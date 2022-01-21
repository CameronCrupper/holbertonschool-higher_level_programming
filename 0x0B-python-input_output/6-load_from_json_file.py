#!/usr/bin/python3

"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

import json


def load_from_json_file(filename):
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
