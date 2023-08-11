#!/usr/bin/python3
#a program that prints the number of and the list of its arguments.
if __name__ == '__main__':

    import sys
    arguments = sys.argv[1:]
    num_arg = len(arguments)
    print('0 arguments.')
    if num_arg == 0:
        print(".")
    else:
        for num_arg, arg in enumerate(arguments, start=1):
            print(f"{num_arg}: {arg}")
