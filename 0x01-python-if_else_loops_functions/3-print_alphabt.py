#!/usr/bin/python3
for alph in range(97, 123):
    if chr(alph) not in ["q", 'e']:
        print('Character: {:c}' .format(chr(alph)))

