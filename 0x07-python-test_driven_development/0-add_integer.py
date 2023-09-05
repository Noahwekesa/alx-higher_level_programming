#!/usr/bin/python3
"""
program that adds 2 integers
"""


def add_integer(a, b=98):
    """
add a and b
they should be (int) or (float)
Return an integer: the addition of a and b
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
