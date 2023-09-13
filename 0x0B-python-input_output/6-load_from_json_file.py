#!/usr/bin/python3
"""
Function to Create an Object from a JSON File
"""
import json


def load_from_json_file(filename):
    """function implementation"""
    with open(filename)as file:
        return json.load(file)
