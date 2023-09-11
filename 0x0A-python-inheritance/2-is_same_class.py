#!/usr/bin/python3
"""
function that returns True of the obj is exacly an instance of the,
specified class
"""


def is_same_class(obj, a_class):
    """ function with 2 parameters"""
    return type(obj) is a_class
