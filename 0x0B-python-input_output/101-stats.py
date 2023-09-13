#!/usr/bin/python3
"""
Code Script for Computing Metrics"""
import sys


"""Initialize variables"""
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

try:
    # Read stdin line by line
    for line in sys.stdin:
        # Parse the line
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update total file size
        total_file_size += file_size

        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Increment line count
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    """ Print final statistics on keyboard interruption"""
    print("Total file size:", total_file_size)
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
