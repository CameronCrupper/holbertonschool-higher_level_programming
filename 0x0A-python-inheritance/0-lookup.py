#!/usr/bin/python3

"""
function that returns a list of available attributes
and methids of an object
python3 -c 'print(__import__("my_module").__doc__)'
"""

def lookup(obj):

    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    return (vars(obj))
