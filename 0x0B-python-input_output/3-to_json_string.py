#!/usr/bin/python3

"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

import json


def to_json_string(my_obj):

    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """
    return json.dumps(my_obj)
