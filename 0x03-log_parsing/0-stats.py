#!/usr/bin/python3
"""
Script that reads stdin line by line, parses log data, and computes metrics.

Input format expected:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys

# Dictionary to count occurrences of specific status codes
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_file_size = 0  # Accumulated total file size
line_count = 0  # Counter for the number of lines processed


def parse_log_line(line):
    """
    Parse a line of log data and update status code counts.

    Args:
        line (str): A line of log data in the expected format.

    Returns:
        int: File size parsed from the log line, or 0 if the line is invalid.
    """
    try:
        # Split the line into components
        parts = line.split()
        if len(parts) < 7:
            return 0
        
        status_code = parts[-2].strip('"')
        file_size = int(parts[-1])

        # Update status code count if it's a valid code
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        return file_size
    except (ValueError, IndexError):
        # Skip invalid lines
        return 0


def print_statistics():
    """
    Print accumulated statistics in ascending order of status codes.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")


def main():
    """
    Main function to read stdin, parse log lines, and print statistics.
    """
    global total_file_size, line_count
    
    try:
        for line in sys.stdin:
            # Parse the line and update total file size
            file_size = parse_log_line(line)
            total_file_size += file_size
            line_count += 1

            # Print stats every 10 lines or on keyboard interruption
            if line_count % 10 == 0:
                print_statistics()

    except KeyboardInterrupt:
        # Handle keyboard interruption gracefully by printing current stats
        print_statistics()
        raise


if __name__ == "__main__":
    main()
