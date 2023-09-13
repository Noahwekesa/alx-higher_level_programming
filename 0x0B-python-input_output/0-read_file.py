#!/usr/bin/python3
"""
 function that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """implement function"""
    with open(filename, 'r', encoding='utf8')as file:
        print(file.read(), end='')
