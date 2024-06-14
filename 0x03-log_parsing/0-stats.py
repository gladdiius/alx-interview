#!/usr/bin/python3
"""
Script that reads stdin line by line, parses log data, and computes metrics.

Input format expected:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_file_size = 0 
line_count = 0

def parse_line(line):
    """
    Parse a line of log data and update status code counts.

    Args:
        line (str): A line of log data in the expected format.

    Returns:
        int: File size parsed from the log line, or 0 if the line is invalid.
    """
    try:
        _, _, _, _, _, status_code, file_size = line.split()
        status_code = status_code.strip('"')
        file_size = int(file_size)

        if status_code in status_codes:
            status_codes[status_code] += 1

        return file_size
    except ValueError:
        return 0


def print_stats():
    """
    Print accumulated statistics in ascending order of status codes.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        file_size = parse_line(line)
        total_file_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
