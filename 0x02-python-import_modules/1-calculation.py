#!/usr/bin/python3
#Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.
if __name__ == '__main__':
    from calculator_1 import *
    a = 10 
    b = 5
    print('{a} + {a} = {}'.format(add(a, b)))
    print('{a} - {b} = {}'.format(sub(a, b)))
    print('{a} * {b} = {}'.format(mul(a, b)))
    print('{a} / {b} = {}'.format(div(a, b)))

