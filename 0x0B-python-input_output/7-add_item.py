#!/usr/bin/python3
"""Script to add arguments to a Python List and Save to a File"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


arguments = []

"""for Iterate through the arguments and append them to the list"""
for arg in sys.argv[1:]:
    arguments.append(arg)

"""Save the list as a JSON representation in a file named add_item.json"""
save_to_json_file(arguments, "add_item.json")
