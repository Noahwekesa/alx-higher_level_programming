#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char)-32)
            print("{:s}".format(upper_char), end='')
        else:
            upper_char = char
            print("{:s}".format(upper_char), end='')
