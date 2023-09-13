#!/usr/bin/python3
"""
function to append text to a file aftr a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ function implementation"""
    with open(filename, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
