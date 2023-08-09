#!/usr/bin/python3
for first_digit in range(0, 8):
	for second_number in (1, 10):
		if first_digit == 8  and second_number == 10:
			print("{:d}{:d}".format(first_digit, second_number), end=", ")
	else:
		print("{:d}{:d}".format(first_digit, second_number))