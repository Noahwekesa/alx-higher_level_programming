#!/usr/bin/python3
for first_digit in range(0, 8):
	for second_number in (first_digit+1, 10):
		print(("{:d}, {:d}".format(first_digit, second_number), end=", ")
