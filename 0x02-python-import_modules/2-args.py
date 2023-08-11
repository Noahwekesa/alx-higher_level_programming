#!/usr/bin/python3
#a program that prints the number of and the list of its arguments.
if __name__ == '__main__':

    import sys
    num_arg = len(sys.argv) - 1
    print('{} arguments.'.format(num_arg))
    if num_arg == 0:
        print("")
    else:
        for num_arg, arg in enumerate(num_arg, start=1):
            print("{}: {}".format(num_arg, arg))
