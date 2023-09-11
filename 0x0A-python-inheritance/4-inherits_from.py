#!/usr/bin/python3
"""
function to check inheritance
"""


def inherits_from(obj, a_class):
    """function to that implements logic"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
         return issubclass(type(obj), a_class)
    return False
