#!/usr/bin/python3

def uppercase(str):
    for char in str:
        upper_char = char.upper() if 'a' <= char <= 'z' else char
        print("{:s}" .format(upper_char), end='')
        print("\n", end='')
