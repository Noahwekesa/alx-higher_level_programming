#!/usr/bin/python3
"""
Python Function to Append a String to a Text File and Return the Number of Characters Added
"""


def append_write(filename="", text=""):
    """function implementation"""
    with open(filename, "a", encoding="utf8") as file:
            file.write(text)
            return len(text)
    