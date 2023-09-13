#!/usr/bin/python3
"""
Function to Write an Object to a Text File using JSON Representation
"""
import json


def save_to_json_file(my_obj, filename):
    """function implementation"""
    with open(filename, 'w')as file:
        json.dump(my_obj, file)
