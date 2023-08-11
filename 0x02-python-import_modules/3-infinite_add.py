#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    result = 0
    for argument in sys.argv[1:]:
        result += int(argument)
        print('{}'.format(result))
