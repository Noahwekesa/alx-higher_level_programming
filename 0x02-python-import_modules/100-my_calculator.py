#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    from calculator_1 import add,sub,mul,div
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = {"+": add, "-": sub, "*": mul, "/": div}
    arg = len(sys.argv) - 1
    if arg != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit

        if sys.argv[2] not in list(operator.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
        sys.exit

        if operator == '+':
            print('{} + {} = {}'.format(a, b, add(a, b)))
        elif operator == '-':
            print('{} - {} = {}'.format(a, b, sub(a, b)))
        elif operator == '*':
            print('{} * {} = {}'.format(a, b, mul(a, b)))
        elif operator == '/':
            print('{} + {} = {}'.format(a, b, add(a, b)))
            