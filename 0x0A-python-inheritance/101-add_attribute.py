#!/usr/bin/python3
"""
 a function that adds a new attribute to an object if its possible:
"""


def add_attribute(obj, attr_name, attr_value):
    """
    function to implement adds a new attr
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
