#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{}".format())
        return True
    except (ValueError, TypeError, IndexError):
        return False
