#!/usr/bin/python3
"""
A program function that prints a square with the character #.
"""


def print_square(size):
    """
    size(size of the length)(int)
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print("#" * size)
