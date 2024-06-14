#!/usr/bin/python3
"""Parses log data from standard input, calculates metrics, and prints them
every 10 lines or on keyboard interrupt.

This script expects log lines in the following format:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Lines that don't match this format are skipped.

The script calculates the following metrics:

* Total file size: Sum of all file sizes encountered.
* Number of lines by status code: Counts occurrences of each unique status code.

The script prints these metrics every 10 lines read from standard input or
upon receiving a keyboard interrupt (CTRL+C).
"""

from collections import Counter
import sys


def main():
    """Main function that parses log data and prints metrics."""
    total_size = 0
    status_counts = Counter()
    line_count = 0

    def print_stats():
        """Prints the calculated metrics."""
        global total_size, status_counts
        print(f"Total file size: {total_size}")
        for code, count in sorted(status_counts.items()):
            print(f"{code}: {count}")

    try:
        for line in sys.stdin:
            line_count += 1
            # Check if the line matches the expected format
            if not line.strip():
                continue  # Skip empty lines
            parts = line.split()
            if len(parts) < 7 or not parts[2].startswith("GET") or not parts[5].isdigit() or not parts[6].isdigit():
                continue  # Skip lines with invalid format

            # Extract file size
            file_size = int(parts[6])
            total_size += file_size
            status_counts[int(parts[4])] += 1  # Increment count for status code

            # Print stats every 10 lines or on keyboard interrupt
            if line_count % 10 == 0 or line_count == 1:
                print_stats()
                line_count = 0  # Reset line count
                status_counts = Counter()  # Reset status counts

    except KeyboardInterrupt:
        print_stats()
        print("\nExiting due to keyboard interrupt.")


if __name__ == "__main__":
    main()
