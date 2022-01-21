#!/usr/bin/python3

"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

import json


def save_to_json_file(my_obj, filename):
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
