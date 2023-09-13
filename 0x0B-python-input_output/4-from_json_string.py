#!/usr/bin/python3
"""
Function to Convert JSON String to Python Object
"""
import json


def from_json_string(my_str):
    """function implementation"""
    return json.loads(my_str)
